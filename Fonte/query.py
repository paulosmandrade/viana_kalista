from sqlalchemy import select
from database import session


from model import PessoaJuridica

def consulta_clientes():
    clientes = session.scalars(
        select(PessoaJuridica)
    ).all()

    return clientes


def consultar_cliente_cnpj(cnpj):
    cliente = session.scalar(
        select(PessoaJuridica)
        .where(PessoaJuridica.cnpj == cnpj)
    )

    if cliente:
        return cliente
    
    else:
        return None
    
def consultar_cliente_razao_social(razao_social):
    cliente = session.scalars(
        select(PessoaJuridica)
        .where(PessoaJuridica.razao_social.like(f"%{razao_social}%")
        )
    ).all()

    if cliente:
        return cliente
    else:
        return None