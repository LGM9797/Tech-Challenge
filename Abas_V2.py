import os
import requests
import pandas as pd
import json
import csv

urls= ['http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv',
       'http://vitibrasil.cnpuv.embrapa.br/download/ExpEspumantes.csv',
       'http://vitibrasil.cnpuv.embrapa.br/download/ExpUva.csv',
       'http://vitibrasil.cnpuv.embrapa.br/download/ExpSuco.csv',
       'http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv',
       'http://vitibrasil.cnpuv.embrapa.br/download/ImpEspumantes.csv',
       'http://vitibrasil.cnpuv.embrapa.br/download/ImpFrescas.csv',
       'http://vitibrasil.cnpuv.embrapa.br/download/ImpPassas.csv',
       'http://vitibrasil.cnpuv.embrapa.br/download/ImpSuco.csv',
       'http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv',
       'http://vitibrasil.cnpuv.embrapa.br/download/ProcessaAmericanas.csv',
       'http://vitibrasil.cnpuv.embrapa.br/download/ProcessaMesa.csv',
       'http://vitibrasil.cnpuv.embrapa.br/download/ProcessaSemclass.csv',
       'http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv',
       'http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv'
       ]

diretorio_CSV = ['Repository_CSV/Comercio.csv','Repository_CSV/ExpEspumantes.csv','Repository_CSV/ExpSuco.csv','Repository_CSV/ExpUva.csv','Repository_CSV/ExpVinho.csv',
'Repository_CSV/ImpEspumantes.csv','Repository_CSV/ImpFrescas.csv','Repository_CSV/ImpPassas.csv','Repository_CSV/ImpSuco.csv','Repository_CSV/ImpVinhos.csv',
'Repository_CSV/ProcessaAmericanas.csv','Repository_CSV/ProcessaMesa.csv','Repository_CSV/ProcessaSemclass.csv','Repository_CSV/PRocessaViniferas.csv',
'Repository_CSV/Producao.csv']

diretorio_JSON = ['Repository_JSON/Comercio.json','Repository_JSON/ExpEspumantes.json','Repository_JSON/ExpSuco.json','Repository_JSON/ExpUva.json','Repository_JSON/ExpVinho.json',
'Repository_JSON/ImpEspumantes.json','Repository_JSON/ImpFrescas.json','Repository_JSON/ImpPassas.json','Repository_JSON/ImpSuco.json','Repository_JSON/ImpVinhos.json',
'Repository_JSON/ProcessaAmericanas.json','Repository_JSON/ProcessaMesa.json','Repository_JSON/ProcessaSemclass.json','Repository_JSON/PRocessaViniferas.json',
'Repository_JSON/Producao.json']

abas = ['Comercio', 'Exportacao', 'Importacao','Processamento','Producao']

def baixar_arquivos_csv(lista_urls, diretorio_saida):
    """
    Função para baixar arquivos CSV da Embrapa VitiBrasil.
    Args:
        lista_urls (list): Lista de URLs dos arquivos CSV.
        diretorio_saida (str): Caminho do diretório para salvar os arquivos baixados.
    """
    if os.path.exists(diretorio_saida):
        print("Arquivo já existe, não é necessário fazer o download.")
    else:
        # Fazendo a requisição GET para a URL
        response = requests.get(lista_urls)
        
        # Verifica se a conexão ocorreu corretamente
        if response.status_code == 200:
            with open(diretorio_saida, 'wb') as file:
                file.write(response.content)
            print("Arquivo baixado com sucesso!")
        else:
            print("Falha ao baixar o arquivo. Status code:", response.status_code)

def csv_para_json(csv_file, json_file):
    """Converte um arquivo CSV para JSON.

    Args:
        csv_file (str): O caminho para o arquivo CSV.
        json_file (str): O caminho para o arquivo JSON de saída.
    """

    data = []
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            # Converte os valores numéricos para inteiros
            for key, value in row.items():
                if key != 'produto' and key != 'cultivar' and key != 'País':
                    try:
                        row[key] = int(value)
                    except ValueError:
                        pass  # Deixa como string se não for um número
            data.append(row)

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def inicio():

    for i,j in zip(urls,diretorio_CSV):
        baixar_arquivos_csv(i,j)

    for i,j in zip(diretorio_CSV, diretorio_JSON):
        csv_para_json(i, j)

# inicio()