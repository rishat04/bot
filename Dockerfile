# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы
COPY . .

# Открываем порт
EXPOSE 5000

# Запускаем приложение (лучше использовать gunicorn для прода)
CMD ["python", "-u", "bot.py"]