from rest_framework.serializers import ValidationError


class HabitValidator:

    def __call__(self, value):
        reward = value.get('reward')
        related_habit = value.get('related_habit')
        is_pleasant = value.get('is_pleasant')
        execution_time = value.get('execution_time')
        periodicity = value.get('periodicity')

        # Нельзя одновременно награду и связанную привычку
        if reward and related_habit:
            raise ValidationError(
                'Нельзя одновременно указывать вознаграждение и связанную привычку.'
            )

        # Время выполнения не более 120 секунд
        if execution_time > 120:
            raise ValidationError(
                'Время выполнения должно быть не более 120 секунд.'
            )

        # Периодичность не реже 1 раза в 7 дней
        if periodicity > 7:
            raise ValidationError(
                'Нельзя выполнять привычку реже одного раза в 7 дней.'
            )

        # Для приятной привычки нельзя награду и связанную привычку
        if is_pleasant and (reward or related_habit):
            raise ValidationError(
                'У приятной привычки не может быть вознаграждения или связанной привычки.'
            )

        # Связанная привычка должна быть приятной
        if related_habit and not related_habit.is_pleasant:
            raise ValidationError(
                'Связанная привычка должна быть приятной.'
            )
