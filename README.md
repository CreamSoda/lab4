Лабораторная работа 4. Вариант 12: Сайт афиша (кинотеатры, сеансы, фильмы) 
=====

Постановка задачи
-----------------

Нужно реализовать веб-приложение в соответствии с вариантом задания. Технологии, которые нужно использовать: 

- фреймворк Django
- ХД *mysql* или postgresql

Деплой приложения
-------

1. Загрузить проект из репозитория git:

  ```
  git clone https://github.com/CreamSoda/lab4.git
  ```
2. Перейти в директорию проекта:

  ```
  cd lab4
  ```
3. Создать базу данных для приложения:

  ```
  mysql -u root -p < db/create_db.sql
  ```

4. Создать в базе данных таблицы

  ```
  python manage.py syncdb
  ```

5. Поднять сервер:

  ```
  python manage.py runserver
  ```
6. Приложение доступно по адресу: 
  ```
  http://localhost:8000/myapp
  ```
   Админка 
   ```
   http://localhost:8000/admin
   ```
