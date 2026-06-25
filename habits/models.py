from django.core.exceptions import ValidationError
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

    periodicity = models.PositiveIntegerField(default=1)

    duration = models.PositiveIntegerField()

    is_public = models.BooleanField(default=False)

    last_sent = models.DateTimeField(null=True, blank=True)

    def clean(self):
        if self.duration > 120:
            raise ValidationError({
                "duration": "Время выполнения должно быть не более 120 секунд."
            })

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.action} ({self.user.username})"