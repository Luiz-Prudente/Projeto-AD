import pandas as pd 
from config import RAW_DATA_DIR

def load_csv_files():
    '''
    Método para resolver problemas de encoding e arquivos que esperavam 2 colunas e apareciam mais colunas
    dfs = DataFrames
    '''
    files = list(RAW_DATA_DIR.glob('*.csv')) # O metodo glob permite encontrar arquivos com base em sua extensão, nesse caso *.csv (todos os arquivos csv)
    dfs = []
    
    for file in files:
        for enc in ('utf-8-sig','latin1'):
            try:
                df = pd.read_csv(
                    file,
                    sep=None, #Detectará o separador do CSV autoaticamente
                    engine='python', #Engine mais tolerante
                    encoding='latin1', #Resolve os problemas de encoding, como acentos
                    on_bad_lines='skip' # Caso não dê jeito
                )
                dfs.append(df)

            except Exception as e:
                print(f'Erro em {file}: {e}')
    
    return dfs