# Usamos una imagen oficial de Python como base
FROM python:3.9-slim

# Establecemos el directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos los archivos necesarios al contenedor
COPY . .

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponemos el puerto 5000 para la aplicación Flask
EXPOSE 5000

# Por defecto, el contenedor ejecutará la aplicación Flask
CMD ["python", "app.py"]
