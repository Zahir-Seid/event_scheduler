from rest_framework import serializers
from .models import Event, RecurrenceRule, EventException


class RecurrenceRuleSerializer(serializers.ModelSerializer):
    weekdays = serializers.ListField(
        child=serializers.ChoiceField(choices=["MO", "TU", "WE", "TH", "FR", "SA", "SU"]),
        allow_empty=True,
        required=False
    )

    class Meta:
        model = RecurrenceRule
        fields = ['frequency', 'interval', 'weekdays', 'nth', 'weekday_for_nth', 'until', 'count']

    def to_internal_value(self, data):
        # Convert list to comma-separated string for weekdays
        if isinstance(data.get('weekdays'), list):
            data['weekdays'] = ",".join(data['weekdays'])
        return super().to_internal_value(data)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        # Convert stored comma-separated string back to list
        if instance.weekdays:
            rep['weekdays'] = instance.weekdays.split(',')
        else:
            rep['weekdays'] = []
        return rep
    def validate(self, data):
        if data.get('count') and data.get('until'):
            raise serializers.ValidationError("Only one of 'count' or 'until' should be set.")
        return data



class EventSerializer(serializers.ModelSerializer):
    recurrence_rule = RecurrenceRuleSerializer(required=False)

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'start_datetime', 'end_datetime', 'is_recurring', 'recurrence_rule']

    def create(self, validated_data):
        recurrence_data = validated_data.pop('recurrence_rule', None)
        event = Event.objects.create(**validated_data)
        if recurrence_data:
            RecurrenceRule.objects.create(event=event, **recurrence_data)
        return event

    def update(self, instance, validated_data):
        recurrence_data = validated_data.pop('recurrence_rule', None)

        # Update base event fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Handle recurrence
        if recurrence_data:
            if hasattr(instance, 'recurrence_rule'):
                for attr, value in recurrence_data.items():
                    setattr(instance.recurrence_rule, attr, value)
                instance.recurrence_rule.save()
            else:
                RecurrenceRule.objects.create(event=instance, **recurrence_data)
        else:
            # If recurrence removed, delete existing rule
            if hasattr(instance, 'recurrence_rule'):
                instance.recurrence_rule.delete()

        return instance

class EventExceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventException
        fields = ['id', 'event', 'occurrence_date', 'is_cancelled']

    def validate(self, data):
        if not data.get('is_cancelled', False):
            raise serializers.ValidationError("Currently only cancelled exceptions are supported.")
        return data