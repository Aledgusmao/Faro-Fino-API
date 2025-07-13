from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import pytz

# Define a base para nossos modelos de tabela. É um padrão do SQLAlchemy.
Base = declarative_base()

# Define o fuso horário padrão para todas as datas
TIMEZONE_BR = pytz.timezone('America/Sao_Paulo')

# Tabela para armazenar os usuários
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    subscription_status = Column(String, default="inactive")
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(TIMEZONE_BR))
    
    # Relacionamento: um usuário pode ter muitas palavras-chave
    keywords = relationship("Keyword", back_populates="owner")

# Tabela para armazenar as palavras-chave
class Keyword(Base):
    __tablename__ = "keywords"

    id = Column(Integer, primary_key=True, index=True)
    keyword_text = Column(String, index=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    # Relacionamento: uma palavra-chave pertence a um usuário
    owner = relationship("User", back_populates="keywords")

# (Vamos adicionar a tabela de histórico de artigos mais tarde, para manter simples por agora)
