from rest_framework.serializers import ValidationError


class HabitValidator:
    def __call__(self, attrs):
        reward = attrs.get('reward')
        related_habit = attrs.get('related_habit')
        is_pleasant = attrs.get('is_pleasant')
        duration = attrs.get('duration')
        periodicity = attrs.get('periodicity')

        if reward and related_habit:
            raise ValidationError(
                "Нельзя одновременно указывать вознаграждение и связанную привычку."
            )

        if duration and duration > 120:
            raise ValidationError(
                {"duration": "Время выполнения должно быть не более 120 секунд."}
            )

        if periodicity and periodicity > 7:
            raise ValidationError(
                "Нельзя выполнять привычку реже одного раза в 7 дней."
            )

        if is_pleasant and (reward or related_habit):
            raise ValidationError(
                "У приятной привычки не может быть вознаграждения или связанной привычки."
            )

        if related_habit and not related_habit.is_pleasant:
            raise ValidationError(
                "Связанная привычка должна быть приятной."
            )
