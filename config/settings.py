from pathlib import Path

#Pasta principal
BASE_DIR = Path(__file__).resolve().parent.parent

#Pastas principal de dado
DATA_DIR = BASE_DIR / 'data'

#Subpastas de data
RAW_DATA_DIR = DATA_DIR / 'raw'
INTERIM_DATA_DIR = DATA_DIR / 'interim'
PROCESSED_DATA_DIR = DATA_DIR / 'processed'