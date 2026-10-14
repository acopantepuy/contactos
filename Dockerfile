# 1. Imagen base oficial ligera
FROM python:3.12-slim

# 2. Variables de entorno para optimizar Python en contenedores
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Directorio de trabajo
WORKDIR /app

# 4. Instalar dependencias del sistema necesarias para PostgreSQL y compilación
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 5. Instalar requerimientos Python (aprovechando caché de capas de Docker)
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 6. Copiar el código fuente
COPY . /app/

# 7. Exponer el puerto
EXPOSE 8000

# 8. Comando de arranque por defecto
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]