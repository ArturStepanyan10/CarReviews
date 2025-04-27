# CarReviews

## Установка и запуск

Что необходимо чтоб запустить проект:

- Git
- Docker
- VS Code или PyCharm 
- ЯП Python

### Запуск проекта

#### 1. Клонируйте репозиторий
```bash
git https://github.com/ArturStepanyan10/CarReviews
cd CarReviews
```

#### 2. Соберите и запустите контейнеры
```bash
docker-compose up --build
```

#### 3. Применить миграции
```bash
docker-compose exec web python manage.py migrate
```

#### 4. Для тестирования ограничение доступа к запросам создайте суперпользователя
```bash
docker-compose exec web python manage.py createsuperuser
```

#### 5. Теперь сгенерируйте токен
```bash
docker-compose exec web python manage.py drf_create_token <имя суперпользователя>
```

