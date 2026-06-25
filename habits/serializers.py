from rest_framework import serializers
from django.core.exceptions import ValidationError
from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Habit
        fields = '__all__'

    def validate(self, attrs):
        reward = attrs.get('reward')
        related_habit = attrs.get('related_habit')
        is_pleasant = attrs.get('is_pleasant')
        duration = attrs.get('duration')
        periodicity = attrs.get('periodicity')

        if reward and related_habit:
            raise serializers.ValidationError(
                "Нельзя одновременно указывать награду и связанную привычку."
            )

        if duration is not None and duration > 120:
            raise serializers.ValidationError(
                {"duration": "Время выполнения должно быть не более 120 секунд."}
            )

        if periodicity is not None and periodicity > 7:
            raise serializers.ValidationError(
                "Нельзя выполнять привычку реже одного раза в 7 дней."
            )

        if is_pleasant and (reward or related_habit):
            raise serializers.ValidationError(
                "У приятной привычки не может быть награды или связанной привычки."
            )

        if related_habit and not related_habit.is_pleasant:
            raise serializers.ValidationError(
                "Связанная привычка должна быть приятной."
            )

        return attrs

