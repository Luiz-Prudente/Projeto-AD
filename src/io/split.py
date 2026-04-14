from config.settings import  PROCESSED_DATA_DIR
import pandas as pd
from src.io.file_handler import save_csv

def region_partition(csv):
    '''
    Divide o dataframe em regioes e os agrupa em um dict com df : regiao
    '''
    df = pd.read_csv(csv)
    df_regions = []
    regions_desc = {
        'S':'sul',
        'SE':'sudeste',
        'N':'norte',
        'NE':'nordeste',
        'CO':'centro_oeste'
    }

    return {
        regions_desc.get(region, 'unknow'): df_temp
        for region, df_temp in df.groupby('regiao')
    }


def export_partitions(df):
    '''
    Exporta os dataframes, nomeados por regiao, para serem processados
    '''
    dfs = region_partition(csv)
    for region, df in dfs.items():
        save_csv(df, PROCESSED_DATA_DIR, f'precos_comb_{region}.csv')
    