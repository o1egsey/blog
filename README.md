# Blog

Це веб-додаток блогу, побудований на Django та PostgreSQL для дисципліни "Автоматизація тестування програмного забезпечення"

## Основні функції
1. Користувач може реєструватися та авторизуватися.
2. При реєстрації потрібно підтвердити свій email
3. Можливість скидання паролю
4. На головній сторінці можна переглянути всі опубліковані пости, додати свій власний.
5. При натисканні на певний пост, його можна переглянути повністю. Якщо Ви є автором цього поста, то його можна відрегувати. Також під постом можна писати коментарі.
6. З меню головної сторінки можна перейти до свого Профайлу, де можна внести зміни у інформацію про себе(Ім'я, Прізвище, Вік тощо)

## Встановлення

Для встановлення додатку виконайте наступні кроки:

1. Склонуйте репозиторій

    ```bash
    git clone https://github.com/o1egsey/blog.git
    ```

2. Перейдіть у директорію проекту, створіть віртуальне середовище та активуйте його:

    ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Встановіть необхідні залежності:

    ```bash
    pip install -r requirements.txt
    ```
  
4. Застосуйте міграції:
   ```bash
   python manage.py migrate
   ```
   
5. Запустіть сервер:
   ```bash
   python manage.py runserver
   ```
   
SMTP сервер вже налаштований та працює.

## Автори

* Олег Аніщенко, Ін.м-22 - [GitHub](https://github.com/o1egsey)

