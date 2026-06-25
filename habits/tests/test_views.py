from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from habits.models import Habit
from users.models import User


class HabitAPIViewTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email='test@test.com',
            username='test_user',
            password='12345'
        )

        refresh = RefreshToken.for_user(self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}'
        )

        self.habit = Habit.objects.create(
            user=self.user,
            place='Дом',
            time='10:00',
            action='Читать книгу',
            duration=60,
            is_public=True
        )

    def test_create_habit(self):
        data = {
            'place': 'Парк',
            'time': '12:00',
            'action': 'Бегать',
            'duration': 30,
            'is_public': False,
        }

        response = self.client.post('/habits/create/', data)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_list_habits(self):
        response = self.client.get('/habits/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_habit(self):
        data = {
            'place': 'Дом',
            'time': '11:00',
            'action': 'Читать книгу',
            'duration': 90,
            'is_public': True,
        }

        response = self.client.patch(
            f'/habits/update/{self.habit.pk}/',
            data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_habit(self):
        response = self.client.delete(
            f'/habits/delete/{self.habit.pk}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_public_habits(self):
        response = self.client.get('/habits/public/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_cannot_edit_foreign_habit(self):
        other_user = User.objects.create_user(
            email='other@test.com',
            username='other',
            password='12345'
        )

        self.client.force_authenticate(user=other_user)

        response = self.client.patch(
            f'/habits/update/{self.habit.pk}/',
            {'action': 'hack'}
        )

        self.assertIn(response.status_code, [403, 404])

    def test_cannot_delete_foreign_habit(self):
        other_user = User.objects.create_user(
            email='other2@test.com',
            username='other2',
            password='12345'
        )

        self.client.force_authenticate(user=other_user)

        response = self.client.delete(
            f'/habits/delete/{self.habit.pk}/'
        )

        self.assertIn(response.status_code, [403, 404])

    def test_public_only_returns_public(self):
        response = self.client.get('/habits/public/')

        self.assertEqual(response.status_code, 200)

        for item in response.data['results']:
            self.assertTrue(item['is_public'])

