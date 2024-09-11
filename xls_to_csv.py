import os
import pandas as pd
import chardet
from tqdm import tqdm

def detect_encoding(file_path):
    """
    Detecta o encoding de um arquivo.
    """
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

def convert_xls_to_csv(input_dir, output_dir, separator):
    # Verifica se o diretório de output existe, caso contrário, cria
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Lista de todos os arquivos .xls para contar o total
    xls_files = []
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.xls'):
                xls_files.append(os.path.join(root, file))

    total_files = len(xls_files)
    print(f"Total de arquivos para converter: {total_files}")

    # Converte os arquivos com barra de progresso
    for idx, file_path in enumerate(tqdm(xls_files, desc="Convertendo arquivos", unit="arquivo")):
        # Obtém o nome da pasta onde o arquivo está localizado
        directory_name = os.path.basename(os.path.dirname(file_path))
        
        # Define o nome do arquivo de saída com o prefixo do diretório
        output_file_name = f"{directory_name}_{os.path.splitext(os.path.basename(file_path))[0]}.csv"
        output_file_path = os.path.join(output_dir, output_file_name)
        
        # Detecta o encoding do arquivo
        detected_encoding = detect_encoding(file_path)
        print(f"Encoding detectado para {file_path}: {detected_encoding}")
        
        # Pergunta ao usuário qual encoding deseja usar
        encoding_to_use = input(f"Qual encoding deseja usar para {file_path}? (Padrão: {detected_encoding}): ")
        if not encoding_to_use:
            encoding_to_use = detected_encoding
        
        try:
            # Lê o arquivo .xls usando pandas com engine 'xlrd'
            df = pd.read_excel(file_path, engine='xlrd')
            
            # Converte e salva como .csv no diretório de output com encoding especificado
            df.to_csv(output_file_path, index=False, encoding=encoding_to_use, sep=separator, errors='replace')
            print(f"{idx + 1}/{total_files} - Arquivo convertido: {file_path} -> {output_file_path}")
        
       
