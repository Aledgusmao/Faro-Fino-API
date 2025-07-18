# Usa uma imagem base oficial e segura do Python
FROM python:3.10-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia a lista de ingredientes para dentro do container
COPY requirements.txt .

# Instala todos os ingredientes
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o resto do nosso código (o main.py) para dentro do container
COPY . .

# Expõe a porta que o Render espera que um Web Service use.
# Isso resolve o problema de "porta não encontrada".
EXPOSE 10000

# O comando final para iniciar a API.
# Diz ao "fogão" (uvicorn) para rodar nosso arquivo "main.py" e a variável "app"
# na porta 10000, aceitando conexões de qualquer lugar.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]