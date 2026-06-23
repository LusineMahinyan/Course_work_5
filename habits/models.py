from django.db import models
from users.models import User


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    place = models.CharField(max_length=255)
    action = models.CharField(max_length=255)

    time = models.TimeField()

    is_pleasant = models.BooleanField(default=False)

    related_habit = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'is_pleasant': True},
        related_name='linked_habits'
    )

    reward = models.CharField(max_length=255, null=True, blank=True)

    periodicity = models.PositiveIntegerField(default=1)  # раз в N дней

    duration = models.PositiveIntegerField(help_text="в секундах")

    is_public = models.BooleanField(default=False)

    last_sent = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.action} ({self.user.username})"
