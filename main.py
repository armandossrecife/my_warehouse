import utilidades
import dataset

# Assuming this script is in the main directory
main_dir = utilidades.get_script_dir(__file__)

def criar_banco():
    print("Criando o banco de testes...")
    utilidades.criar_banco(my_script='script_banco.sql')
    print("Banco criado com sucesso!")

def lista_dados_basicos():
    print("Produtos")
    print(dataset.df_produtos.head(2))
    print("Fornecedores")
    print(dataset.df_fornecedores.head(2))
    print("Consumo Interno")
    print(dataset.df_consumo_interno.head(2))
    print("Compras")
    print(dataset.df_compras.head(2))
    print("Itens compras")
    print(dataset.df_itens_compras.head(2))
    print("Sugestão Compras")
    print(dataset.df_sugestao_compras.head(2))

def criar_banco_movimentacoes(script, nome_banco):
    print("Criando o banco movimentações...")
    try: 
        utilidades.criar_banco(my_script=script, nome_banco=nome_banco)
    except Exception as ex: 
        print(f"Erro ao criar o banco: {str(ex)}")
    print("Banco criado com sucesso!")

criar_banco_movimentacoes(script='scripts/script_movimentacoes.sql', nome_banco='movimentacoes.db')