import os
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging

# Importa os nossos modelos de tabela do novo arquivo
from models import Base

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Pega a URL do banco de dados da variável de ambiente
DATABASE_URL = os.getenv("DATABASE_URL")

# Cria o "motor" de conexão
engine = create_engine(DATABASE_URL, pool_recycle=300)

# --- NOVA LINHA ---
# Esta é a linha mágica: ela diz ao SQLAlchemy para criar todas as tabelas
# definidas em 'models.py' (que importamos como 'Base') se elas ainda não existirem.
Base.metadata.create_all(bind=engine)
# --- FIM DA NOVA LINHA ---

# Cria a "fábrica" de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria a instância da nossa aplicação.
app = FastAPI()

# Nossa rota de teste agora não precisa mais testar a conexão,
# pois a linha 'create_all' já faria o app quebrar se a conexão falhasse.
@app.get("/")
def read_root():
    logger.info("A rota raiz foi acessada.")
    return {"status": "ok", "message": "API do Faro Fino News está online e o banco de dados está sincronizado."}
