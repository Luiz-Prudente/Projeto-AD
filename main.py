from config.settings import RAW_DATA_DIR
from src.ingestion.load_csv import load_csv_files, concat_dataframe

dfs = load_csv_files()
concat_dataframe(dfs)