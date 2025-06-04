from django.db import models
from django.conf import settings
from django.utils import timezone
from accounts.models import User

class Event(models.Model):
    """
    Represents a calendar event - either one-off or recurring.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    is_recurring = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Soft delete flag, optional
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.start_datetime})"


class RecurrenceRule(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name='recurrence_rule')

    FREQUENCY_CHOICES = [
        ('DAILY', 'Daily'),
        ('WEEKLY', 'Weekly'),
        ('MONTHLY', 'Monthly'),
        ('YEARLY', 'Yearly'),
    ]

    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES)
    interval = models.PositiveIntegerField(default=1)  # every n-th day/week/month/year
    
    # For WEEKLY recurrence (comma-separated weekdays)
    weekdays = models.CharField(max_length=20, blank=True, null=True)

    # Relative date pattern (e.g. 2nd Friday, last weekday)
    nth = models.IntegerField(blank=True, null=True)
    weekday_for_nth = models.CharField(max_length=2, blank=True, null=True)

    # For MONTHLY fixed day (e.g. 15th of every month)
    day_of_month = models.PositiveIntegerField(blank=True, null=True)

    # For YEARLY recurrence
    month = models.PositiveIntegerField(blank=True, null=True)
    day = models.PositiveIntegerField(blank=True, null=True)

    # Until date to stop recurrence (optional)
    until = models.DateField(blank=True, null=True)

    # Count of occurrences (optional, mutually exclusive with until)
    count = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"Recurs {self.frequency} every {self.interval} interval(s)"


class EventException(models.Model):
    """
    Stores exceptions to recurrence rules, such as deleted or modified instances.
    For example, deleting a single occurrence of a recurring event.
    """
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='exceptions')
    occurrence_date = models.DateField()  # date of the occurrence this exception applies to
    is_cancelled = models.BooleanField(default=False)  # if True, this occurrence is cancelled

    # If modified occurrence, can store override fields (optional - stretch)
    # For now, keep simple.

    class Meta:
        unique_together = ('event', 'occurrence_date')

    def __str__(self):
        status = "Cancelled" if self.is_cancelled else "Modified"
        return f"Exception on {self.occurrence_date} ({status})"
