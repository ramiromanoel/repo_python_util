import os
import pandas as pd
from tqdm import tqdm

def convert_xlsx_to_csv(input_dir, output_dir):
    # Verifica se o diretório de output existe, caso contrário, cria
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Lista de todos os arquivos .xlsx para contar o total
    xlsx_files = []
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.xlsx'):
                xlsx_files.append(os.path.join(root, file))

    total_files = len(xlsx_files)
    print(f"Total de arquivos para converter: {total_files}")

    # Converte os arquivos com barra de progresso
    for idx, file_path in enumerate(tqdm(xlsx_files, desc="Convertendo arquivos", unit="arquivo")):
        output_file_path = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(file_path))[0]}.csv")
        
        try:
            # Lê o arquivo .xlsx usando pandas
            df = pd.read_excel(file_path, engine='openpyxl')
            
            # Converte e salva como .csv no diretório de output com encoding UTF-8
            df.to_csv(output_file_path, index=False, encoding='utf-8')
            print(f"{idx + 1}/{total_files} - Arquivo convertido: {file_path} -> {output_file_path}")
        
        except Exception as e:
            print(f"Erro ao converter {file_path}: {e}")

if __name__ == "__main__":
    input_dir = input("Digite o caminho do diretório de input: ")
    output_dir = input("Digite o caminho do diretório de output: ")
    convert_xlsx_to_csv(input_dir, output_dir)
