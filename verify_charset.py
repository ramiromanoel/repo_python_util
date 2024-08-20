import os
import chardet
import pandas as pd

def detect_encoding(file_path):
    # Detect the file encoding
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
    return result['encoding']

def get_files_encoding(directory):
    # Prepare lists to store information
    file_paths = []
    file_names = []
    encodings = []
    
    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                encoding = detect_encoding(file_path)
            except Exception as e:
                encoding = f"Error: {e}"
                
            # Append information to lists
            file_paths.append(file_path)
            file_names.append(file)
            encodings.append(encoding)
    
    # Create a DataFrame
    df = pd.DataFrame({
        'Full Path': file_paths,
        'File Name': file_names,
        'Encoding': encodings
    })
    
    return df

# Input directory
directory = input("Informe o diretório a ser verificado: ")

# Get the DataFrame with file encodings
df_encodings = get_files_encoding(directory)

# Show the DataFrame
print(df_encodings)
