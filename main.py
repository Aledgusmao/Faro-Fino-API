import os
from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 1. Pega a URL do banco de dados da variável de ambiente que configuramos no Render.
DATABASE_URL = os.getenv("DATABASE_URL")

# Verifica se a DATABASE_URL foi carregada
if not DATABASE_URL:
    logger.error("A variável de ambiente DATABASE_URL não foi encontrada!")
    # Você pode querer que a aplicação pare aqui em um cenário real
    # raise ValueError("DATABASE_URL não configurada")

# 2. Cria o "motor" de conexão com o banco de dados.
engine = create_engine(DATABASE_URL, pool_recycle=300)

# 3. Cria uma "fábrica" de sessões para conversar com o banco de dados.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função para obter uma sessão de banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Cria a instância da nossa aplicação.
app = FastAPI()

# 4. Define a rota principal para testar a conexão.
@app.get("/")
def read_root(db: Session = Depends(get_db)):
    if not DATABASE_URL:
        return {"status": "error", "message": "API online, mas a DATABASE_URL não está configurada no ambiente."}
    try:
        # 5. Executa um comando SQL muito simples para testar a conexão.
        db.execute(text("SELECT 1"))
        
        # 6. Se o comando acima não der erro, a conexão foi um sucesso.
        logger.info("Conexão com o banco de dados bem-sucedida!")
        return {"status": "success", "message": "API online e conectada ao banco de dados!"}
    
    except Exception as e:
        # 7. Se der qualquer erro, a conexão falhou.
        logger.error(f"Falha ao conectar com o banco de dados: {e}")
        return {"status": "error", "message": "API online, mas falha ao conectar com o banco de dados."}
