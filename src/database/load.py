from src.database.connection import get_engine
from sqlalchemy import text
import pandas as pd

engine = get_engine()

def persist(dataframe):
    '''
    Salvando o dataframe no banco de dados
    '''
    name = 'combustiveis'
    dataframe.to_sql(
        name, #Esse sera o nome da tabela
        engine,
        if_exists='replace', # Criando a tabela
        index=False
    )
    print(f'Dados salvos na tabela {name} com sucesso')