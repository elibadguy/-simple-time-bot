import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

# Для отладки: покажем, что Python видит ваш ключ
api_key = os.getenv("OPENROUTER_API_KEY")
print("API KEY:", api_key)

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

def get_current_time() -> dict:
    """Return the current UTC time in ISO‑8601 format."""
    current_time = datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    return {"utc": current_time}

def is_time_question(question: str) -> bool:
    # Простая проверка на вопрос о времени (можно доработать)
    time_phrases = [
        "what time is it", "current time", "now time", "сколько времени", "который час", "время сейчас"
    ]
    q = question.lower()
    return any(phrase in q for phrase in time_phrases)

def ask_openrouter(question: str):
    data = {
        "model": "mistralai/devstral-small:free",  # <-- правильный ID модели!
        "messages": [
            {"role": "user", "content": question}
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        # Извлекаем текст ответа
        try:
            return result["choices"][0]["message"]["content"]
        except Exception:
            return result
    else:
        return f"Ошибка: {response.status_code}\n{response.text}"

if __name__ == "__main__":
    question = input("Введите ваш вопрос: ")
    if is_time_question(question):
        print("Ответ:", get_current_time())
    else:
        answer = ask_openrouter(question)
        print("Ответ:", answer)