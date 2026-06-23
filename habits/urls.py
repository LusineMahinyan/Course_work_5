from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (
    HabitCreateAPIView,
    HabitDeleteAPIView,
    HabitListAPIView,
    HabitUpdateAPIView,
    PublicHabitListAPIView,
)

app_name = HabitsConfig.name

urlpatterns = [
    path('', HabitListAPIView.as_view(), name='list'),
    path('create/', HabitCreateAPIView.as_view(), name='create'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='update'),
    path('delete/<int:pk>/', HabitDeleteAPIView.as_view(), name='delete'),
    path('public/', PublicHabitListAPIView.as_view(), name='public'),
]
