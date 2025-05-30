from rest_framework import generics, permissions, status
from .models import Event, EventException
from .serializers import EventSerializer, EventExceptionSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from datetime import datetime

class EventListCreateView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EventRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)

class CancelOccurrenceView(generics.CreateAPIView):
    serializer_class = EventExceptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        event_id = kwargs.get('event_id')
        occurrence_date_str = request.data.get('occurrence_date')

        if not occurrence_date_str:
            return Response({'error': 'occurrence_date is required'}, status=400)

        try:
            occurrence_date = datetime.strptime(occurrence_date_str, '%Y-%m-%d').date()
        except ValueError:
            return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=400)

        event = get_object_or_404(Event, id=event_id, user=request.user)

        exception, created = EventException.objects.get_or_create(
            event=event,
            occurrence_date=occurrence_date,
            defaults={'is_cancelled': True}
        )

        if not created and not exception.is_cancelled:
            exception.is_cancelled = True
            exception.save()

        serializer = self.get_serializer(exception)
        return Response(serializer.data, status=status.HTTP_201_CREATED)