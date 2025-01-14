import pytz
from datetime import datetime

from database import engine
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

BR_TZ = pytz.timezone('America/Sao_Paulo')

def current_time_saopaulo():
    return datetime.now(BR_TZ)


class PessoaJuridica(Base):
    __tablename__ = "pessoas_juridica"
    id = Column(Integer, primary_key= True, autoincrement= True)
    creat_at = Column(DateTime, default=current_time_saopaulo)
    update_at = Column(
        DateTime, default=current_time_saopaulo, onupdate=current_time_saopaulo
    )
    razao_social = Column(String(80))
    cnpj = Column(String(14), unique= True)
    regime_tributario = Column(String(15))
    inscricao_estadual = Column(String(15))
    status = Column(Boolean())


Base.metadata.create_all(engine)
