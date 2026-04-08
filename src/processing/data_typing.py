import pandas as pd


def convert_category(df):
    cols = ['regiao', 'estado', 'produto', 'unidade_de_medida', 'bandeira']
    df[cols] = df[cols].astype('category')
    return df


def convert_string(df):
    cols = ['municipio', 'posto', 'bairro']
    df[cols] = df[cols].astype('string')
    return df


def convert_date(df):
    df['data_da_coleta'] = pd.to_datetime(
        df['data_da_coleta'],
        dayfirst=True,
        errors='coerce'
    )
    return df


def convert_float(df):
    df['valor_de_venda'] = (
        df['valor_de_venda']
        .astype('string')
        .str.replace(',', '.', regex=False)
        .astype('float32')
    )
    return df


def enforce_schema(df):
    df = convert_category(df)
    df = convert_string(df)
    df = convert_date(df)
    df = convert_float(df)

    return df