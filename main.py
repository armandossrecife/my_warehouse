import pandas as pd
import os
import sqlite3

def criar_banco(my_script, nome_banco='almoxarifado.db'):
    """
    Cria o banco de dados 'almoxarifado.db' e as tabelas especificadas.
    Args:
        None
    Returns:
        None
    """
    conn = None
    try:
        conn = sqlite3.connect(nome_banco)        
        with open(my_script, mode='r') as sql_file:
            sql_script = sql_file.read()
        # Cria um cursor para executar os comandos SQL
        cursor = conn.cursor()
        # Executa os comandos SQL para criar as tabelas
        cursor.executescript(sql_script)
        # Confirma as alterações no banco de dados
        conn.commit()
        print("Tabelas criadas com sucesso!")
    except sqlite3.Error as error:
        print(f"Erro ao criar as tabelas: {error}")
    finally:
        if conn:
            conn.close()

def get_script_dir(path):
    return os.path.dirname(os.path.abspath(path))

print("Criando o banco...")
criar_banco(my_script='script_banco.sql')
print("Banco criado com sucesso!")

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