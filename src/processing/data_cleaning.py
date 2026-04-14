import pandas as pd
import os
from config.settings import INTERIM_DATA_DIR, PROCESSED_DATA_DIR


def drop_columns(dataframe):
    '''
    Retira Colunas que não serão utilizadas do DF
    '''
    dataframe = dataframe.drop(columns=['CNPJ da Revenda', 'Nome da Rua', 'Numero Rua', 'Cep', 'Valor de Compra', 'Complemento'])
    return dataframe

def normalize_columns(dataframe):
    '''
    padroniza a nomencalatura das colunas do dataframe
    '''
    dataframe.columns = (
        dataframe.columns
        .str.lower()
        .str.replace('-', '', regex=False)
        .str.replace(' ', '_')
        .str.replace('__', '_')
    )
    return dataframe

def normalize_name(dataframe):
    '''
    Renomeia colunas do dataframe
    '''
    return dataframe.rename(columns={
        'regiao_sigla': 'regiao',
        'estado_sigla': 'estado',
        'revenda': 'posto',
        "data_da_coleta": "data_coleta",
        "valor_de_venda": "valor_venda",
        "unidade_de_medida": "unidade_medida"
    })

def drop_missing_values(dataframe):
    '''
    Exclui registros NA do dataframe, caso todas as colunas do registro forem nulas
    '''
    dataframe = dataframe.dropna(how='all')
    return dataframe


def normalize_dataframe(dataframe):
    '''
    aplica todas as funções de normalização criadas nesse arquivo
    '''
    df = drop_columns(dataframe)
    df = normalize_columns(df)
    df = normalize_name(df)
    df = drop_missing_values(df)

    return df

