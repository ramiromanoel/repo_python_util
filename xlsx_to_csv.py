import os
import pandas as pd
from tqdm import tqdm

def convert_xlsx_to_csv(input_dir, output_dir, separator):
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
        # Obtém o nome da pasta onde o arquivo está localizado
        directory_name = os.path.basename(os.path.dirname(file_path))
        
        # Define o nome do arquivo de saída com o prefixo do diretório
        output_file_name = f"{directory_name}_{os.path.splitext(os.path.basename(file_path))[0]}.csv"
        output_file_path = os.path.join(output_dir, output_file_name)
        
        try:
            # Lê o arquivo .xlsx usando pandas
            df = pd.read_excel(file_path, engine='openpyxl')
            
            # Converte e salva como .csv no diretório de output com encoding ISO-8859-1
            df.to_csv(output_file_path, index=False, encoding='ISO-8859-1', sep=separator, errors='replace')
            print(f"{idx + 1}/{total_files} - Arquivo convertido: {file_path} -> {output_file_path}")
        
        except Exception as e:
            print(f"Erro ao converter {file_path}: {e}")

if __name__ == "__main__":
    input_dir = input("Digite o caminho do diretório de input: ")
    output_dir = input("Digite o caminho do diretório de output: ")
    separator = input("Digite o separador desejado (por exemplo, ',' para vírgula ou ';' para ponto e vírgula): ")
    
    # Validar o separador se estiver vazio
    if not separator:
        separator = ','  # Definindo a vírgula como separador padrão
    
    convert_xlsx_to_csv(input_dir, output_dir, separator)
