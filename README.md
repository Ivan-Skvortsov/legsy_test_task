<div id="top"></div>
<div align="center">
<h1>Тестовое задание Legsy</h1>
</div>

## О проекте
Цель задания - сервис на FastAPI, который взаимодействует с сайтом https://wildberries.com.<br/>
Полное описание задания: https://drive.google.com/file/d/1niwAIM2MWZooI6flqhmgzCJBbm_8l7R2/view

<p align="right">(<a href="#top">наверх</a>)</p>

## Использованные технологии и пакеты
* [FastAPI](https://fastapi.tiangolo.com/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [Celery](https://docs.celeryq.dev/en/stable/)

<p align="right">(<a href="#top">наверх</a>)</p>

## Необходимый софт
Для развертывания проекта потребуется машина с предустановленным Docker и Docker-Compose, версии не ниже 19.03.0.<br/>
Инструкцию по установке можно найти на <a href="https://docs.docker.com/">официальном сайте</a>.

## Установка
Склонируйте проект на Ваш компьютер
   ```sh
   git clone https://github.com/Ivan-Skvortsov/legsy_test_task.git
   ```
Перейдите в папку с инструкциями docker-compose
   ```sh
   cd legsy_test_task
   ```
Создайте файл с переменными окружения
   ```sh
   touch .env
   ```
Наполните файл следующими переменными
   ```sh
    POSTGRES_DB= # имя базы данных 
    POSTGRES_USER= # имя пользователя БД
    POSTGRES_PASSWORD= # пароль БД
    DB_HOST= # хост, на котором развернута БД
    DB_PORT= # порт БД
    CELERY_BROKER_URL= # адрес брокера для Celery
   ```
   > **Note**:
   > Можно воспользоваться предзаполненным файлом с переменными окружения. Для этого просто переименуйте `.env.example` в `.env`
    
Запустите контейнеры
   ```sh
   sudo docker-compose up -d
   ```
Проект будет доступен по адресу `http://127.0.0.1:8000`<br/>
Сваггер доступен по адресу: `http://127.0.0.1:8000/docs`<br/>
Документация ReDoc доступна по адресу `http://127.0.0.1:8000/redoc`


## Об авторе
Автор: Иван Скворцов<br/><br />
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:pprofcheg@gmail.com)
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/Profcheg)
<p align="right">(<a href="#top">наверх</a>)</p>
