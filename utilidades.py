import sqlite3
import os
import pandas as pd
import xmltodict
import json
import csv

def get_df_from_csv(path):
    try: 
        my_df = pd.read_csv(path, encoding='unicode_escape')
    except Exception as ex:
        my_df = None
        raise ValueError(f"Erro: {str(ex)}")
    return my_df

def get_df_from_xml(path, codificacao='utf-8'):
    try: 
        my_df = pd.read_xml(path, encoding=codificacao)
    except Exception as ex:
        my_df = None
        raise ValueError(f"Erro: {str(ex)}")
    return my_df

def get_script_dir(path):
    return os.path.dirname(os.path.abspath(path))

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
        cursor = conn.cursor()
        cursor.executescript(sql_script)
        conn.commit()
        print("Tabelas criadas com sucesso!")
    except sqlite3.Error as error:
        raise ValueError(f"Erro ao criar as tabelas: {error}")
    finally:
        if conn:
            conn.close()

def convert_to_utf8(input_file, output_file):
    """
    Converts a CSV file to UTF-8 encoding.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.
    """
    try:
        df = pd.read_csv(input_file, encoding='latin-1')
        df.to_csv(output_file, encoding='utf-8', index=False)
    except Exception as ex:
        raise ValueError(f"Erro: {checa_valor(ex)}")

def convert_to_ascii(input_file, output_file):
    """
    Converts a text file to ASCII encoding.
    Args:
        input_file (str): Path to the input text file.
        output_file (str): Path to the output text file.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()

        # Convert to ASCII, ignoring characters that cannot be represented
        ascii_text = text.encode('ascii', 'ignore').decode('ascii')

        with open(output_file, 'w', encoding='ascii') as f:
            f.write(ascii_text)
    except Exception as ex:
        raise ValueError(f"Erro: {checa_valor(ex)}")

def xml_to_json(xml_file, json_file, codificacao='utf-8'):
    """
    Converts an XML file to a JSON file.
    Args:
        xml_file (str): Path to the XML file.
        json_file (str): Path to the output JSON file.
    """

    try:
        with open(xml_file, 'r', encoding=codificacao) as f:
            xml_data = f.read()

        dict_data = xmltodict.parse(xml_data)

        # Convert Python dictionary to JSON
        with open(json_file, 'w') as f:
            json.dump(dict_data, f, indent=4)

        print(f"XML file '{xml_file}' successfully converted to JSON file '{json_file}'")

    except FileNotFoundError:
        print(f"Error: XML file '{xml_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def csv_to_json(csv_file, json_file, codificacao='utf-8'):
    """
    Converts a CSV file to a JSON file.
    Args:
        csv_file (str): Path to the CSV file.
        json_file (str): Path to the output JSON file.
    """
    try:
        with open(csv_file, 'r', encoding=codificacao) as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)

        with open(json_file, 'w', encoding=codificacao) as jsonfile:
            json.dump(data, jsonfile, indent=4)

        print(f"CSV file '{csv_file}' successfully converted to JSON file '{json_file}'")
    except FileNotFoundError:
        print(f"Error: CSV file '{csv_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def extract_agrupadores(file):
    """Extrai os valores de @Agrupador de um JSON e os adiciona a uma lista.
        data (dict): O dicionário Python obtido a partir do JSON.
    Args:
        file: Arquivo JSON
    Returns:
        list: Uma lista contendo os valores de @Agrupador.
    """
    agrupadores = []
    try: 
        # Carregando o JSON (assumindo que está em um arquivo chamado 'dados.json')
        with open(file, 'r') as f:
            data = json.load(f)

        for agrupamento in data['relatorioMovimentacao']['SelecionarCentraisEstoque']['centraisEstoque']['relatorioMovimentacao']['agrupamento']:
            agrupadores.append(agrupamento['@Agrupador'])
    except Exception as ex:
        print(f"Erro: {checa_valor(ex)}")
    return agrupadores

def checa_valor(item):
    if item:
        return item
    else:
        return None

def extrair_dados_informacao_agrupadores(arquivo_json):
    """
    Extrai os dados de 'informacao' para cada 'Agrupador' e cria um DataFrame.
    Args:
        arquivo_json (str): Caminho para o arquivo JSON.
    Returns:
        pd.DataFrame: DataFrame com os dados extraídos.
    """
    dados_dataframe = []
    try:
        with open(arquivo_json, 'r') as f:
            data = json.load(f)
    
        for agrupamento in data['relatorioMovimentacao']['SelecionarCentraisEstoque']['centraisEstoque']['relatorioMovimentacao']['agrupamento']:
            agrupador = agrupamento['@Agrupador']
            if agrupador: 
                if len(agrupamento['informacao']) > 0 and isinstance(agrupamento['informacao'], list): 
                    for informacao in agrupamento['informacao']:
                        if informacao: 
                            if isinstance(informacao, dict): 
                                dados_dataframe.append({
                                    "Agrupador": agrupador,
                                    "itemId": checa_valor(informacao["itemId"]),
                                    "itemDescricao": checa_valor(informacao["itemDescricao"]),
                                    "data": checa_valor(informacao["data"]),
                                    "tipo": checa_valor(informacao["tipo"]),
                                    "tipoItem": checa_valor(informacao["tipoItem"]),
                                    "especificacao": checa_valor(informacao["especificacao"]),
                                    "documentoId": checa_valor(informacao["documentoId"]),
                                    "usuarioId": checa_valor(informacao["usuarioId"]),
                                    "loteQuantidade": checa_valor(informacao["loteQuantidade"]),
                                    "centroCusto": checa_valor(informacao["centroCusto"]),
                                    "processo": checa_valor(informacao["processo"]),
                                    "precoMedio": checa_valor(informacao["precoMedio"]),
                                    "saldoAnterior": checa_valor(informacao["saldoAnterior"]),
                                    "saldo": checa_valor(informacao["saldo"]),
                                    "justificativa": checa_valor(informacao["justificativa"]),
                                    "LoteId": checa_valor(informacao["LoteId"]),
                                    "LoteValidade": checa_valor(informacao["LoteValidade"]),
                                    "valorTotal": checa_valor(informacao["valorTotal"]),
                                    "FabricanteDescricao": checa_valor(informacao["FabricanteDescricao"]),
                                })
                else:
                    dados_dataframe.append({
                                    "Agrupador": "?",
                                    "itemId": checa_valor(agrupamento['informacao']["itemId"]),
                                    "itemDescricao": checa_valor(agrupamento['informacao']["itemDescricao"]),
                                    "data": checa_valor(agrupamento['informacao']["data"]),
                                    "tipo": checa_valor(agrupamento['informacao']["tipo"]),
                                    "tipoItem": checa_valor(agrupamento['informacao']["tipoItem"]),
                                    "especificacao": checa_valor(agrupamento['informacao']["especificacao"]),
                                    "documentoId": checa_valor(agrupamento['informacao']["documentoId"]),
                                    "usuarioId": checa_valor(agrupamento['informacao']["usuarioId"]),
                                    "loteQuantidade": checa_valor(agrupamento['informacao']["loteQuantidade"]),
                                    "centroCusto": checa_valor(agrupamento['informacao']["centroCusto"]),
                                    "processo": checa_valor(agrupamento['informacao']["processo"]),
                                    "precoMedio": checa_valor(agrupamento['informacao']["precoMedio"]),
                                    "saldoAnterior": checa_valor(agrupamento['informacao']["saldoAnterior"]),
                                    "saldo": checa_valor(agrupamento['informacao']["saldo"]),
                                    "justificativa": checa_valor(agrupamento['informacao']["justificativa"]),
                                    "LoteId": checa_valor(agrupamento['informacao']["LoteId"]),
                                    "LoteValidade": checa_valor(agrupamento['informacao']["LoteValidade"]),
                                    "valorTotal": checa_valor(agrupamento['informacao']["valorTotal"]),
                                    "FabricanteDescricao": checa_valor(agrupamento['informacao']["FabricanteDescricao"]),
                        })
        df = pd.DataFrame(dados_dataframe)
    except Exception as ex:
        print(f"Erro: {checa_valor(ex)}")
    return df

def extract_user_info(user_str):
    """
    Extracts user ID and name from a string in the format "0399 - FRANCISCO DAS".
    Args:
        user_str: The string containing user ID and name.
    Returns:
        tuple: A tuple containing (user_id, user_name).
    """
    try:
        user_id, user_name = user_str.split(" - ")
        return user_id, user_name
    except ValueError:
        return None, None