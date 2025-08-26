# Imagem base do Python
FROM python:3.9-slim

# Diretório de trabalho no container
WORKDIR /app

# Copia e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY . .

# Expõe a porta que a aplicação usa
EXPOSE 5000

# Comando para iniciar o servidor
CMD ["python", "app.py"]