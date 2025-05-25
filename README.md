# Time Bot

Простой чат-бот, который может отвечать на вопросы и сообщать текущее время.

## Установка

1. Создайте виртуальное окружение:
```bash
python -m venv .venv
```

2. Активируйте виртуальное окружение:
- Windows:
```bash
.venv\Scripts\activate
```
- Linux/Mac:
```bash
source .venv/bin/activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Создайте файл `.env` в корневой директории и добавьте ваш API ключ DeepSeek:
```
DEEPSEEK_API_KEY=your_deepseek_api_key_here
```

## Получение API-ключа DeepSeek

1. Перейдите на https://platform.deepseek.com/
2. Зарегистрируйтесь или войдите в аккаунт
3. В разделе "API Keys" создайте новый ключ и скопируйте его
4. Вставьте ключ в файл `.env` вместо `your_deepseek_api_key_here`

## Запуск

Запустите бота с помощью команды:
```bash
langgraph dev
```

## Использование

Бот отвечает на сообщения пользователя и может сообщить текущее время, если его об этом попросить. Пример запроса:
- "What time is it?"
- "Tell me the current time"
- "What's the time now?" 