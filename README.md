Шаблон для приложения fastapi


Запуск приложения (папка src):
uvicorn main:app --reload

Запуск контейнера c БД:
docker compose up -d

Создаем .env в src с параметрами:
APP_CONFIG__DB__URL=postgresql+asyncpg://postgres:postgres@localhost:5433/postgres

Инит алембик:
alembic init -t async alembic

Создать миграцю:
alembic revision --autogenerate -m "init item"

Применение миграций:
alembic upgrade head
alembic downgrade -1