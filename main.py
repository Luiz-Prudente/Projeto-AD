from config.settings import RAW_DATA_DIR, INTERIM_DATA_DIR
from src.ingestion.load_csv import *
from src.processing.data_cleaning import *
import os

#Aglomerando os arquivos CSV de registor de preços dos combustiveis
files = get_csv_files()
dfs = load_csv_files(files)
concat_dataframe(dfs)


#Aplicando normalizações preliminares
file = os.path.join(INTERIM_DATA_DIR, 'precos_comb_unificados.csv')
interim_df = load_csv(file)
normalized_df = normalize_dataframe(interim_df)
save_csv(normalized_df, INTERIM_DATA_DIR, 'precos_comb_normalized.csv')