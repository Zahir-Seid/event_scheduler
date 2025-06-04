from rest_framework import serializers
from .models import Event, RecurrenceRule, EventException


class RecurrenceRuleSerializer(serializers.ModelSerializer):
    weekdays = serializers.ListField(
        child=serializers.ChoiceField(choices=["MO", "TU", "WE", "TH", "FR", "SA", "SU"]),
        allow_empty=True,
        required=False,
        default=[]
    )
    
    until = serializers.DateField(required=False, allow_null=True)

    class Meta:
        model = RecurrenceRule
        fields = [
            'frequency', 'interval', 'weekdays', 'nth', 'weekday_for_nth', 'day_of_month',
            'month', 'day', 'until', 'count'
        ]

    def to_internal_value(self, data):
        # Convert empty string or None to None for 'until'
        until = data.get('until')
        if until in ('', None):
            data['until'] = None

        return super().to_internal_value(data)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        
        if instance.frequency == 'WEEKLY' and instance.weekdays:
            if isinstance(instance.weekdays, str):
                rep['weekdays'] = instance.weekdays.split(',')
            else:
                # Just in case, fallback:
                rep['weekdays'] = instance.weekdays if isinstance(instance.weekdays, list) else []
        else:
            rep['weekdays'] = []

        return rep

    def validate(self, data):
        count = data.get('count')
        until = data.get('until')
        frequency = data.get('frequency')

        # count and until are mutually exclusive
        if count and until:
            raise serializers.ValidationError("Only one of 'count' or 'until' should be set.")

        # Validate weekdays only if frequency is WEEKLY
        if frequency != 'WEEKLY' and data.get('weekdays'):
            raise serializers.ValidationError("Weekdays can only be set if frequency is 'WEEKLY'.")

        # Validate fields based on frequency
        if frequency == 'DAILY':
            # For daily, no weekdays, nth, weekday_for_nth, day_of_month, month, day
            forbidden_fields = ['weekdays', 'nth', 'weekday_for_nth', 'day_of_month', 'month', 'day']
            for field in forbidden_fields:
                if data.get(field):
                    raise serializers.ValidationError(f"Field '{field}' must be empty or null when frequency is DAILY.")

        elif frequency == 'WEEKLY':
            # weekdays required or empty list is okay
            # nth, weekday_for_nth, day_of_month, month, day not used generally
            forbidden_fields = ['day_of_month', 'month', 'day']
            for field in forbidden_fields:
                if data.get(field):
                    raise serializers.ValidationError(f"Field '{field}' must be empty or null when frequency is WEEKLY.")

        elif frequency == 'MONTHLY':
            # Must have either day_of_month OR nth+weekday_for_nth
            day_of_month = data.get('day_of_month')
            nth = data.get('nth')
            weekday_for_nth = data.get('weekday_for_nth')
            forbidden_fields = ['weekdays', 'month', 'day']

            if not day_of_month and not (nth and weekday_for_nth):
                raise serializers.ValidationError(
                    "For MONTHLY frequency, provide either 'day_of_month' or both 'nth' and 'weekday_for_nth'."
                )
            for field in forbidden_fields:
                if data.get(field):
                    raise serializers.ValidationError(f"Field '{field}' must be empty or null when frequency is MONTHLY.")

        elif frequency == 'YEARLY':
            # Must have month + (day OR nth+weekday_for_nth)
            month = data.get('month')
            day = data.get('day')
            nth = data.get('nth')
            weekday_for_nth = data.get('weekday_for_nth')
            forbidden_fields = ['weekdays', 'day_of_month']

            if not month:
                raise serializers.ValidationError("Field 'month' is required when frequency is YEARLY.")

            if not (day or (nth and weekday_for_nth)):
                raise serializers.ValidationError(
                    "For YEARLY frequency, provide 'day' or both 'nth' and 'weekday_for_nth'."
                )

            for field in forbidden_fields:
                if data.get(field):
                    raise serializers.ValidationError(f"Field '{field}' must be empty or null when frequency is YEARLY.")

        else:
            raise serializers.ValidationError(f"Unsupported frequency value: {frequency}")

        return data

    def create(self, validated_data):
        weekdays_list = validated_data.pop('weekdays', [])
        if validated_data.get('frequency') == 'WEEKLY':
            validated_data['weekdays'] = ",".join(weekdays_list)
        else:
            validated_data['weekdays'] = ''
        return super().create(validated_data)

    def update(self, instance, validated_data):
        weekdays_list = validated_data.pop('weekdays', [])
        if validated_data.get('frequency') == 'WEEKLY':
            validated_data['weekdays'] = ",".join(weekdays_list)
        else:
            validated_data['weekdays'] = ''
        return super().update(instance, validated_data)


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