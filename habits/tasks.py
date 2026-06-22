from celery import shared_task
from habits.models import Habit
from telegram_bot.services import send_telegram_message


@shared_task
def test_task():
    print('Celery работает 🚀')


@shared_task
def send_habit_reminders():
    habits = Habit.objects.all()

    for habit in habits:
        user = habit.user

        if user.telegram_chat_id:
            message = (
                f'⏰ Напоминание о привычке\n\n'
                f'📌 Привычка: {habit.action}\n'
                f'📍 Место: {habit.place}\n'
                f'🕘 Время: {habit.time}'
            )

            send_telegram_message(
                user.telegram_chat_id,
                message
            )
