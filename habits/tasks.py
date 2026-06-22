from django.utils import timezone
from habits.models import Habit
from users.services import send_telegram_message


def send_habit_reminders():
    """
    Отправка уведомлений о привычках по времени.
    Вызывается через Celery Beat.
    """

    now = timezone.now()

    habits = Habit.objects.filter(
        time__hour=now.hour,
        time__minute=now.minute,
    )

    for habit in habits:
        user = habit.user

        if not user.telegram_chat_id:
            continue

        # Формируем текст уведомления
        message = (
            f"⏰ Напоминание о привычке!\n\n"
            f"📝 Действие: {habit.action}\n"
            f"📍 Место: {habit.place}\n"
        )

        # если есть связанная приятная привычка
        if habit.related_habit:
            message += f"🎁 Награда: {habit.related_habit.action}\n"
        elif habit.reward:
            message += f"🎁 Награда: {habit.reward}\n"

        send_telegram_message(user.telegram_chat_id, message)


def test_task():
    print("Celery работает ✔")

