from django.test import TestCase
from rest_framework.serializers import ValidationError
from rest_framework.test import APIRequestFactory

from habits.models import Habit
from users.models import User
from habits.serializers import HabitSerializer


class HabitValidatorTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='test@test.com',
            username='test_user'
        )

        self.factory = APIRequestFactory()

    def test_execution_time_more_than_120_seconds(self):
        request = self.factory.post("/")
        request.user = self.user

        data = {
            "place": "Дом",
            "time": "10:00",
            "action": "Читать книгу",
            "duration": 130,
            "periodicity": 1,
            "is_pleasant": False,
        }

        serializer = HabitSerializer(
            data=data,
            context={"request": request}
        )

        self.assertFalse(serializer.is_valid())
        self.assertIn("duration", serializer.errors)
        self.assertEqual(
            serializer.errors["duration"][0],
            "Время выполнения должно быть не более 120 секунд."
        )


    def test_valid_duration(self):
        habit = Habit(
            user=self.user,
            place='Дом',
            action='Читать',
            time='10:00',
            duration=60
        )
        habit.full_clean()  # не должно падать
