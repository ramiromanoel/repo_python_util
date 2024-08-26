import os
import pandas as pd

def convert_xlsx_to_csv(input_dir, output_dir):
    # Verifica se o diretório de output existe, caso contrário, cria
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Percorre o diretório de input e seus subdiretórios
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.xlsx'):
                file_path = os.path.join(root, file)
                output_file_path = os.path.join(output_dir, f"{os.path.splitext(file)[0]}.csv")
                
                try:
                    # Lê o arquivo .xlsx usando pandas
                    df = pd.read_excel(file_path, engine='openpyxl')
                    
                    # Converte e salva como .csv no diretório de output
                    df.to_csv(output_file_path, index=False)
                    print(f"Arquivo convertido: {file_path} -> {output_file_path}")
                
                except Exception as e:
                    print(f"Erro ao converter {file_path}: {e}")

if __name__ == "__main__":
    input_dir = input("Digite o caminho do diretório de input: ")
    output_dir = input("Digite o caminho do diretório de output: ")
    convert_xlsx_to_csv(input_dir, output_dir)
