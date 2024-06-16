# Docker-команда FROM вказує базовий образ контейнера
# Наш базовий образ - це Linux з попередньо встановленим python-3.10
FROM python:3.11-slim

# Встановимо змінну середовища
# ENV APP_HOME /app

# Встановимо робочу директорію всередині контейнера
WORKDIR /helper

# Скопіюємо інші файли в робочу директорію контейнера
COPY . /helper

# Встановимо залежності всередині контейнера
#RUN poetry export --without-hashes --format=requirements.txt > requirements.txt
RUN pip install -r requirements.txt

# Позначимо порт, де працює застосунок всередині контейнера
EXPOSE 5000

# Запустимо наш застосунок всередині контейнера
#ENTRYPOINT ["python", "__main__.py"]
