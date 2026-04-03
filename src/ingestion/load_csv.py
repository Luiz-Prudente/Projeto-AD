import pandas as pd
import os
from collections import Counter
from config.settings import RAW_DATA_DIR, INTERIM_DATA_DIR
from src.io.file_handler import save_csv

def get_csv_files():
    '''
    Lista os arquivos csv de uma pasta
    '''
    files = list(RAW_DATA_DIR.glob('*.csv'))
    return files


def load_csv(file):
    '''
    Transforma o arquivo csv em um dataframe, levando em consideração seu encoding
    '''
    sucess = False
    df = None

    for enc in ('utf-8-sig', 'latin1', 'cp1252'):
        try:
            df = pd.read_csv(
                file,
                sep=None,
                engine='python',
                encoding=enc,
                on_bad_lines='skip'
            )

            # Remove sujeira das colunas
            df.columns = [
                col.replace('\ufeff', '').replace('ï»¿', '').strip()
                for col in df.columns
            ]

            sucess = True
            break

        except Exception:
            continue

    if not sucess:
        print(f'Erro em {file}: Nenhum encoding encontrado')
        return None

    return df


def load_csv_files(files):
    '''
    Transforma os arquivos csv em dataframes e os junta em uma lista
    '''
    dfs = []
    for file in files:
        df = load_csv(file)
        if df is not None:
            dfs.append(df)
    return dfs

def shape_validation(dataframes : list):
    '''
    Função que valida se os dataframes a serem concatenados possuem a mesma quantidade de colunas
    Retorna True se todos seguem o padrão mais comum, False caso contrário
    '''
    colunas = {}
    for df in dataframes:
        for coluna in df.columns:
            if coluna in colunas:
                colunas[coluna] +=1
            else:
                colunas[coluna] = 1

    for chave, valor in colunas.items():
        print(f'{chave}: {valor}')
    if len(set(colunas.values())) == 1:
        return True
    else:
        return False

def concat_dataframe(dataframes : list):
    '''
    Concatena os dataframes caso todos os requisitos tenham sido atendidos
    '''
    if shape_validation(dataframes):
        final_df = pd.concat(dataframes, ignore_index= True)
        if rows_quantity(dataframes, final_df):
            save_csv(final_df, INTERIM_DATA_DIR, 'precos_comb_unificados.csv')
            
    else:
        print('Dados inconsistentes, verifique')

def rows_quantity(dataframes: list, final_df):
    '''
    Verifica se a quantidade de linhas dos dataframes que serão unificados é igual a quantidade de linhas do dataframe concatenado
    '''
    dataframes_rows = 0
    new_dataframe_rows = final_df.shape[0]
    for df in dataframes:
        dataframes_rows += df.shape[0]

    if dataframes_rows != new_dataframe_rows:
        print(f' Quantidade de linhas nos arquivos diferentes, somados os dataframes individuais possuem {dataframes_rows} e o novo dataframe concatenado possui {new_dataframe_rows}')
        return False
    else:
        return True