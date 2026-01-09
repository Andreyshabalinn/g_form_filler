# Используем официальный Python образ
FROM python:3.12-slim

# Устанавливаем необходимые зависимости для Playwright
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    gnupg \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libx11-xcb1 \
    libxcb1 \
    libxshmfence1 \
    libasound2 \
    libxfixes3 \
    libxkbcommon0 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Создаём рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем Python-зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем браузеры для Playwright
RUN python -m playwright install

# Копируем скрипт в контейнер
COPY g_form_playwright.py .

# Команда по умолчанию
CMD ["python", "g_form_playwright.py"]
