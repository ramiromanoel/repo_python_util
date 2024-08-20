import os
import chardet
import pandas as pd

def detect_encoding(file_path):
    # Detecta o encoding do arquivo
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
    return result['encoding']

def get_files_encoding(directory):
    # Listas para armazenar informações
    file_paths = []
    file_names = []
    encodings = []
    
    # Percorre os subdiretórios
    for root, dirs, files in os.walk(directory):
        if root == directory:  # Ignora o diretório raiz
            continue
        for file in files:
            file_path = os.path.join(root, file)
            try:
                encoding = detect_encoding(file_path)
            except Exception as e:
                encoding = f"Error: {e}"
            
            # Exibe o arquivo e a pasta sendo lidos
            print(f"Lendo arquivo: {file}")
            print(f"Na pasta: {root}")
                
            # Armazena as informações nas listas
            file_paths.append(file_path)
            file_names.append(file)
            encodings.append(encoding)
    
    # Cria um DataFrame
    df = pd.DataFrame({
        'Full Path': file_paths,
        'File Name': file_names,
        'Encoding': encodings
    })
    
    return df

# Solicita o diretório de entrada e de saída
directory = input("Informe o diretório a ser verificado: ")
output_dir = input("Informe o caminho onde deseja salvar o arquivo de saída: ")

# Concatena o caminho de saída com o nome do arquivo
output_path = os.path.join(output_dir, "encode.xlsx")

# Obtém o DataFrame com os encodings dos arquivos
df_encodings = get_files_encoding(directory)

# Salva o DataFrame em um arquivo Excel
df_encodings.to_excel(output_path, index=False)

print(f"Análise concluída e salva em: {output_path}")
