import pandas as pd
import os
from collections import Counter
from config.settings import RAW_DATA_DIR, INTERIM_DATA_DIR

def load_csv_files():
    '''
    Método para resolver problemas de encoding e arquivos que esperavam 2 colunas e apareciam mais colunas
    dfs = DataFrames
    '''
    files = list(RAW_DATA_DIR.glob('*.csv')) # O metodo glob permite encontrar arquivos com base em sua extensão, nesse caso *.csv (todos os arquivos csv)
    dfs = []
    for file in files:
        sucess = False
        for enc in ('utf-8-sig','latin1', 'cp1252'):
            try:
                df = pd.read_csv(
                    file,
                    sep=None, #Detectará o separador do CSV autoaticamente
                    engine='python', #Engine mais tolerante
                    encoding=enc, #Resolve os problemas de encoding, como acentos
                    on_bad_lines='skip' # Caso não dê jeito
                )
                #Remove o ï»¿ de algumas colunas
                df.columns = [col.replace('\ufeff','').replace('ï»¿', '').strip() for col in df.columns]
                
                dfs.append(df)
                sucess = True
                break

            except Exception as e:
                continue
        if not sucess:
            print(f'Erro em {file}: Nenhum ecoding encontrado')
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
            final_df.to_csv(os.path.join(INTERIM_DATA_DIR, 'precos_comb_unificados.csv'), index=False) # o uso de os.path.join evita problemas com sistemas diferentes
            print("Dados unificados com sucesso, dataframe salvo")
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
        print(f' Quantidade de linhas nos arquivos diferentes, somados os dataframes individuais possuem {dataframes_rows} e o novo dataframe concatenado possui {new_dataframes_rows}')
        return False
    else:
        return True