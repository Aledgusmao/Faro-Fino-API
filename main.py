# 1. Importa o FastAPI, que é o nosso "chefe de cozinha" para a API.
from fastapi import FastAPI

# 2. Cria a "instância" da nossa aplicação. Pense nisso como abrir as portas da cozinha.
app = FastAPI()

# 3. Define a rota principal ("/"). É o endereço mais básico da nossa API.
#    Quando alguém visitar "app.farofino.com.br/", esta função será executada.
@app.get("/")
def read_root():
    # 4. Retorna uma mensagem simples em formato JSON.
    return {"message": "Bem-vindo à API do Faro Fino News!"}