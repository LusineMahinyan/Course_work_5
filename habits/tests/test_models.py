from django.test import TestCase
from habits.models import Habit
from users.models import User


class HabitModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='test@test.com',
            username='test_user'
        )

    def test_create_habit(self):
        habit = Habit.objects.create(
            user=self.user,
            place='Дом',
            time='10:00',
            action='Читать книгу',
            duration=60,
            is_public=True
        )

        self.assertEqual(habit.place, 'Дом')
        self.assertEqual(habit.action, 'Читать книгу')
        self.assertEqual(habit.duration, 60)
        self.assertEqual(habit.user, self.user)

    def test_valid_habit_creation(self):
        habit = Habit.objects.create(
            user=self.user,
            place='Дом',
            action='Читать',
            time='10:00',
            duration=60
        )

        self.assertEqual(habit.duration, 60)

    def test_str_method(self):
        habit = Habit.objects.create(
            user=self.user,
            place='Дом',
            action='Читать',
            time='10:00',
            duration=60
        )

        self.assertIn('Читать', str(habit))
