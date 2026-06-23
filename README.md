## 📘 Habit Tracker API

Проект трекера привычек на Django + DRF на основе книги “Атомные привычки”.

### 📌 Возможности
- регистрация и авторизация (JWT)
- создание привычек
- редактирование и удаление привычек
- публичные привычки
- напоминания в Telegram
- фоновая обработка задач (Celery + Beat)

### 🧠 Логика привычки

Формат:
```
Я буду [действие] в [время] в [место]
```

### ⚙️ Технологии
- Django
- Django REST Framework
- PostgreSQL
- Redis
- Celery
- Celery Beat
- Telegram Bot API

### 🔐 Авторизация
Получить токен:
```
POST /users/token/
```

Обновить токен:
```
POST /users/token/refresh/
```

### 👤 Пользователи
Регистрация:
```
POST /users/register/
```

### 📊 Привычки
CRUD:
```
GET /habits/
POST /habits/
PUT /habits/<id>/
DELETE /habits/<id>/
```

Публичные привычки:
```
GET /habits/public/
```

### 🔔 Уведомления

- Celery выполняет задачи в фоне
- Celery Beat запускает планировщик
- Redis хранит очередь задач
- Telegram отправляет уведомления пользователю

 ### 🚀 Запуск проекта
```
python manage.py migrate
python manage.py runserver
celery -A config worker -l info -P solo
celery -A config beat -l info
```

### 📬 Telegram

Создать .env:

```
TELEGRAM_BOT_TOKEN=your_token
```

### 📌 Swagger
```
/swagger/
/redoc/
```
