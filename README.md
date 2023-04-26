# Blog

Це веб-додаток блогу, побудований на Django та PostgreSQL для дисципліни "Автоматизація тестування програмного забезпечення"

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
   

## Автори

* Олег Аніщенко, Ін.м-22 - [GitHub](https://github.com/o1egsey)

