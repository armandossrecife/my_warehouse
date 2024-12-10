import pandas as pd
import os

def get_script_dir(path):
    return os.path.dirname(os.path.abspath(path))

# Assuming this script is in the main directory
main_dir = get_script_dir(__file__)

PATH_PRODUTOS = 'data/produtos.csv'
PATH_FORNECEDORES = 'data/fornecedores.csv'
PATH_CONSUMO_INTERNO = 'data/consumo_interno.csv'
PATH_COMPRAS = 'data/compras.csv'
PATH_ITENS_COMPRAS = 'data/itens_compras.csv'
PATH_SUGESTAO_COMPRAS = 'data/sugestao_compras.csv'

df_produtos = pd.read_csv(PATH_PRODUTOS)
df_fornecedores = pd.read_csv(PATH_FORNECEDORES)
df_consumo_interno = pd.read_csv(PATH_CONSUMO_INTERNO)
df_compras = pd.read_csv(PATH_COMPRAS)
df_itens_compras = pd.read_csv(PATH_ITENS_COMPRAS)
df_sugestao_compras = pd.read_csv(PATH_SUGESTAO_COMPRAS)

print("Produtos")
print(df_produtos.head(2))

print("Fornecedores")
print(df_fornecedores.head(2))

print("Consumo Interno")
print(df_consumo_interno.head(2))

print("Compras")
print(df_compras.head(2))

print("Itens compras")
print(df_itens_compras.head(2))

print("Sugestão Compras")
print(df_sugestao_compras.head(2))