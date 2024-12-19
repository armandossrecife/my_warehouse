import utilidades

PATH_PRODUTOS = 'data/produtos.csv'
PATH_FORNECEDORES = 'data/fornecedores.csv'
PATH_CONSUMO_INTERNO = 'data/consumo_interno.csv'
PATH_COMPRAS = 'data/compras.csv'
PATH_ITENS_COMPRAS = 'data/itens_compras.csv'
PATH_SUGESTAO_COMPRAS = 'data/sugestao_compras.csv'

PATH_COMPRAS_FORNECEDOR_JANEIRO_DEZEMBRO_2024 = "secret/Compras_por_fornecedor_Janeiro_a_Dezembro_2024.csv"
PATH_MOVIMENTO_ESTOQUE_JANEIRO_DEZEMBRO_2024 = "secret/Movimento_estoque_Janeiro_Dezembro_2024.csv"
PATH_MOVIMENTACAO_ESTOQUE_2024 = "secret/Movimentacao_estoque_2024.xml"
PATH_COMPRAS_FORNECEDOR_2024 = "secret/Compras_por_fornecedor_2024.csv"

df_produtos = utilidades.get_df_from_csv(PATH_PRODUTOS)
df_fornecedores = utilidades.get_df_from_csv(PATH_FORNECEDORES)
df_consumo_interno = utilidades.get_df_from_csv(PATH_CONSUMO_INTERNO)
df_compras = utilidades.get_df_from_csv(PATH_COMPRAS)
df_itens_compras = utilidades.get_df_from_csv(PATH_ITENS_COMPRAS)
df_sugestao_compras = utilidades.get_df_from_csv(PATH_SUGESTAO_COMPRAS)