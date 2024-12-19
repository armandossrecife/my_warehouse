import pandas as pd
import sqlite3
import utilidades

# Carregar os dados do CSV
PATH_MOVIMENTACOES = "resultados/movimentacoes.csv"

def carrega_dados_movimentacoes():
    df_movimentacoes = pd.read_csv(PATH_MOVIMENTACOES)
    return df_movimentacoes

def carrega_dados_itens(df_movimentacoes):
    # Cria um dataframe com itens unicos
    df_itens = df_movimentacoes[['itemId', 'itemDescricao']]
    df_itens.drop_duplicates(inplace=True)
    return df_itens

def extrai_dados_usuarios(df_movimentacoes): 
    # Extrai dados dos usuarios
    s_users = df_movimentacoes['usuarioId']
    user_info_list = s_users.apply(utilidades.extract_user_info).tolist()
    user_info_list = list(set(user_info_list))
    # Create a DataFrame from the extracted information
    df_users = pd.DataFrame(user_info_list, columns=['usuarioId', 'nome'])
    return df_users

def extrai_dados_fabricantes(df_movimentacoes):
    # Extract unique FabricanteDescricao values
    unique_fabricantes = df_movimentacoes['FabricanteDescricao'].unique()
    # Create a new DataFrame with a single column named 'FabricanteDescricao'
    df_fabricantes = pd.DataFrame({'FabricanteDescricao': unique_fabricantes})
    # Create a new column with an auto-incrementing numeric index
    df_fabricantes['id'] = df_fabricantes.index + 1 

    # Set 'id' as the index
    df_fabricantes.set_index('id', inplace=True)    
    return df_fabricantes

def extrai_dados_lotes(df_movimentacoes):
    df_lotes = df_movimentacoes[['LoteId',	'LoteValidade']]
    df_lotes.drop_duplicates(inplace=True)
    return df_lotes

def extrai_dados_itens_movimentacoes(df_movimentacoes):
    colunas_uteis = ["itemId","itemDescricao","tipo","tipoItem","especificacao","loteQuantidade","data","precoMedio","valorTotal", "usuarioId", "LoteId", "fabricanteId"]
    df_itens_movimentacoes = df_movimentacoes[colunas_uteis]
    return df_itens_movimentacoes

def add_user_to_movimentacoes(df_users, df_movimentacoes):
    # Merge df_movimentacoes with df_users to add 'usuarioId' to df_movimentacoes
	# First, extract just the user_id from the original user column
    df_movimentacoes['temp_usuarioId'] = df_movimentacoes['usuarioId'].apply(lambda x: utilidades.extract_user_info(x)[0] if utilidades.extract_user_info(x) else None)
	#Merge the dataframes using the temporary user_id
    df_movimentacoes = pd.merge(df_movimentacoes, df_users, left_on='temp_usuarioId', right_on='usuarioId', how='left', suffixes=('', '_y'))
	#Drop the temporary user id
    df_movimentacoes.drop('temp_usuarioId', axis=1, inplace=True)
	# Drop any redundant columns added by the merge operation (if any)
    df_movimentacoes.drop(columns=[col for col in df_movimentacoes.columns if col.endswith('_y')], inplace=True)
    return df_movimentacoes

def add_fabricanteid_to_movimentacoes(df_fabricantes, df_movimentacoes):
    # Create a mapping from 'FabricanteDescricao' to 'id' from df_fabricantes
    fabricante_mapping = df_fabricantes['FabricanteDescricao'].to_dict()
    fabricante_id_mapping = {v: k for k, v in fabricante_mapping.items()}

    # Add 'fabricanteId' to df_movimentacoes based on 'FabricanteDescricao'
    df_movimentacoes['fabricanteId'] = df_movimentacoes['FabricanteDescricao'].map(fabricante_id_mapping)
    return df_movimentacoes

def get_dataframes():
    df_movimentacoes = carrega_dados_movimentacoes()
    df_users = extrai_dados_usuarios(df_movimentacoes)
    df_movimentacoes = add_user_to_movimentacoes(df_users, df_movimentacoes)
    
    df_fabricantes = extrai_dados_fabricantes(df_movimentacoes)
    df_movimentacoes = add_fabricanteid_to_movimentacoes(df_fabricantes, df_movimentacoes)

    df_lotes = extrai_dados_lotes(df_movimentacoes)
    df_itens_movimentacoes = extrai_dados_itens_movimentacoes(df_movimentacoes)

    df_itens = carrega_dados_itens(df_movimentacoes)
    return df_movimentacoes, df_itens, df_users, df_fabricantes, df_lotes, df_itens_movimentacoes

def insere_dados_banco(df, nome_tabela,string_banco='databases/movimentacoes.db'):
    try: 
        conn = sqlite3.connect(string_banco)
        #df.to_sql(nome_tabela, conn, if_exists='replace', index=False) 
        df.to_sql(nome_tabela, conn, if_exists='replace') 
        conn.close()
    except Exception as ex: 
        print(f"Erro ao inserir dados na tabela {nome_tabela}: {str(ex)}")

df_movimentacoes, df_itens, df_users, df_fabricantes, df_lotes, df_itens_movimentacoes = get_dataframes()
insere_dados_banco(df_users, 'Usuarios')
insere_dados_banco(df_fabricantes, 'Fabricantes')
insere_dados_banco(df_lotes, 'Lotes')
insere_dados_banco(df_itens_movimentacoes, 'Itens')