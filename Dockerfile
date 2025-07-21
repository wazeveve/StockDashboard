FROM python:3.11-slim

WORKDIR /app

COPY . .

# Instala todas as dependencias necessárias para rodar o projeto
RUN pip install --no-cache-dir -r requirements.txt

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]