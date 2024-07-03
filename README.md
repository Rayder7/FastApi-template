***Шаблон для приложения fastapi***


**Запуск приложения (папка src):**
uvicorn main:app --reload

**Запуск контейнера c БД:**
docker compose up -d

**Создаем .env в src с параметрами:**
APP_CONFIG__DB__URL=postgresql+asyncpg://postgres:postgres@localhost:5433/postgres
APP_CONFIG__ACCESS_TOKEN__RESET_PASSWORD_TOKEN_SECRET=password
APP_CONFIG__ACCESS_TOKEN__VERIFICATION_TOKEN_SECRET=password

**Инит алембик:**
alembic init -t async alembic

**Создать миграцю:**
alembic revision --autogenerate -m "init item"

**Применение миграций:**
alembic upgrade head
alembic downgrade -1
