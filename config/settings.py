from pathlib import Path
from dotenv import load_dotenv
import os


#Pasta principal
BASE_DIR = Path(__file__).resolve().parent.parent

#Pastas principal de data
DATA_DIR = BASE_DIR / 'data'

#Subpastas de data
RAW_DATA_DIR = DATA_DIR / 'raw'
INTERIM_DATA_DIR = DATA_DIR / 'interim'
PROCESSED_DATA_DIR = DATA_DIR / 'processed'


# Loading env variables
load_dotenv()


DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "port": os.getenv("DB_PORT"),
}
