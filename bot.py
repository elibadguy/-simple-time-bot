import os
import requests
from dotenv import load_dotenv
from datetime import datetime

# Загружаем переменные из .env
load_dotenv()

# Получаем API-ключ из переменных окружения
api_key = os.getenv("OPENROUTER_API_KEY")
print("API KEY:", api_key)  # Для проверки, что ключ подхватился

# Ссылка для запросов к OpenRouter
url = "https://openrouter.ai/api/v1/chat/completions"

# Заголовки для запроса
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Функция, чтобы узнать текущее время в UTC
def get_current_time():
    now = datetime.utcnow()
    # Форматируем время как строку
    return {"utc": now.replace(microsecond=0).isoformat() + "Z"}

# Проверяем, спрашивает ли пользователь про время
def is_time_question(text):
    text = text.lower()
    # Список фраз, по которым определяем вопрос о времени
    time_words = [
        "what time is it", "current time", "now time",
        "сколько времени", "который час", "время сейчас"
    ]
    for word in time_words:
        if word in text:
            return True
    return False

# Функция для общения с OpenRouter
def ask_openrouter(text):
    data = {
        "model": "mistralai/devstral-small:free",  # Бесплатная модель
        "messages": [
            {"role": "user", "content": text}
        ]
    }
    # Отправляем запрос
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        try:
            # Пытаемся достать ответ из JSON
            return response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            return "Не удалось получить ответ от модели."
    else:
        return f"Ошибка: {response.status_code}\n{response.text}"

if __name__ == "__main__":
    # Спрашиваем пользователя, что он хочет узнать
    user_input = input("Введите ваш вопрос: ")
    if is_time_question(user_input):
        # Если вопрос про время — отвечаем сами
        print("Ответ:", get_current_time())
    else:
        # Иначе спрашиваем у OpenRouter
        print("Ответ:", ask_openrouter(user_input))
