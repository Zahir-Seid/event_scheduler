from django.urls import path
from .views import (
    EventListCreateView,
    EventRetrieveUpdateDeleteView,
    CancelOccurrenceView,
)

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventRetrieveUpdateDeleteView.as_view(), name='event-detail'),
    path('events/<int:event_id>/cancel-occurrence/', CancelOccurrenceView.as_view(), name='cancel-occurrence'),
]
