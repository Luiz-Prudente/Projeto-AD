from config.settings import RAW_DATA_DIR, INTERIM_DATA_DIR, PROCESSED_DATA_DIR
from src.ingestion.load_csv import *
from src.processing.data_cleaning import normalize_dataframe
from src.processing.data_typing import enforce_schema
from src.io.export import export_partitions
import os

# Ingestão
files = get_csv_files()
dfs = load_csv_files(files)
concat_dataframe(dfs)

# Normalização
file = os.path.join(INTERIM_DATA_DIR, 'precos_comb_unificados.csv')
interim_df = load_csv(file)
normalized_df = normalize_dataframe(interim_df)

save_csv(normalized_df, INTERIM_DATA_DIR, 'precos_comb_normalized.csv')

# Tipagem
file = os.path.join(INTERIM_DATA_DIR, 'precos_comb_normalized.csv')
temp_df = load_csv(file)
typed_df = enforce_schema(temp_df)

# Export final
save_csv(typed_df, PROCESSED_DATA_DIR, 'precos_comb_brasil.csv')

# Partições
file = os.path.join(PROCESSED_DATA_DIR, 'precos_comb_brasil.csv')
export_partitions(file)