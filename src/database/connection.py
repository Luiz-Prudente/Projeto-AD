from sqlalchemy import create_engine
from config.settings import DB_CONFIG
from sqlalchemy import text

def get_engine():
    '''
    Criando conexão para poder acessar o banco de dados
    '''
    return create_engine(
        f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}"
        f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    )
