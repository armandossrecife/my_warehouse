import dataset
import time
import utilidades

def importa_dados_movimentacao_xml():
    print("Importando dados de movimetações de estoque 2024...")
    t1 = time.time()
    try: 
        df_movimentacoes_2024 = dataset.get_df_from_xml(path=dataset.PATH_MOVIMENTACAO_ESTOQUE_2024, codificacao='ISO-8859-1')
    except Exception as ex:
        print(f"Erro: {str(ex)}")
    t2 = time.time()
    print("Concluído.")
    print(f"Tempo de importação: {round(t2-t1, 2)}s")
    tamanho = df_movimentacoes_2024.shape
    print(f"Linhas: {tamanho[0]}, colunas: {tamanho[1]}")
    print(df_movimentacoes_2024.info())

def convert_xml_to_json():
    print("Importando dados de movimetações de estoque 2024...")
    t1 = time.time()
    try: 
        utilidades.xml_to_json(dataset.PATH_MOVIMENTACAO_ESTOQUE_2024, 'movimentacoes_2024.json', codificacao='ISO-8859-1')
    except Exception as ex:
        print(f"Erro: {str(ex)}")
    t2 = time.time()
    print("Concluído.")
    print(f"Tempo de importação: {round(t2-t1, 2)}s")

def convert_csv_to_json():
    print("Importando dados de movimetações de estoque 2024...")
    t1 = time.time()
    try: 
        utilidades.csv_to_json(dataset.PATH_MOVIMENTO_ESTOQUE_JANEIRO_DEZEMBRO_2024, 'movimentacoes_jan_dez_2024.json', codificacao='utf-8')
    except Exception as ex:
        print(f"Erro: {str(ex)}")
    t2 = time.time()
    print("Concluído.")
    print(f"Tempo de importação: {round(t2-t1, 2)}s")

def extrai_dados_agrupadores():
    print("Extraindo os agrupadores...")
    try: 
        t1 = time.time()    
        # Extraindo os agrupadores
        lista_agrupadores = utilidades.extract_agrupadores(file='movimentacoes_2024.json')
        t2 = time.time()
        print("Concluído.")
        print(f"Tempo de leitura: {round(t2-t1, 2)}s")
    except Exception as ex:
        print(f"Erro: {str(ex)}")
    return lista_agrupadores

def extrai_informacoes_agrupadores():
    print("Extraindo informações dos agrupadores...")
    df_movimentacoes = None
    try: 
        t1 = time.time()    
        df_movimentacoes = utilidades.extrair_dados_informacao_agrupadores(arquivo_json='movimentacoes_2024.json')
        t2 = time.time()
        print("Concluído.")
        print(f"Tempo de leitura: {round(t2-t1, 2)}s")
    except Exception as ex:
        print(f"Erro: {str(ex)}")
    return df_movimentacoes

def convert_csv_to_json2():
    print("Importando compras por fornecedor 2024...")
    t1 = time.time()
    try: 
        utilidades.csv_to_json(dataset.PATH_COMPRAS_FORNECEDOR_2024, 'Compras_fornecedor_2024.json', codificacao='utf-8')
    except Exception as ex:
        print(f"Erro: {str(ex)}")
    t2 = time.time()
    print("Concluído.")
    print(f"Tempo de importação: {round(t2-t1, 2)}s")

def dados_movimentacoes_2024():
    df = extrai_informacoes_agrupadores()
    print(df.info())
    df.to_csv('movimentacoes.csv', index=False)

dados_movimentacoes_2024()