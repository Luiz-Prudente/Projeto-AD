import os
import pandas as pd

def save_csv(dataframe, path, filename):
    '''
    Salva o Dataframe, definindo o nome e o path
    '''
    full_path = os.path.join(path, filename)
    dataframe.to_csv(full_path, index=False)
    name = filename.strip('.csv')
    print(f'Dados unificados com sucesso, dataframe {name} salvo')