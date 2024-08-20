import pandas as pd

def csv_to_xlsx(csv_file_path, xlsx_file_path):
    # Lee el archivo CSV con la codificación UTF-8
    df = pd.read_csv(csv_file_path, encoding='utf-8')
    
    # Guarda el DataFrame en un archivo Excel
    df.to_excel(xlsx_file_path, index=False)

# Ejemplo de uso
csv_to_xlsx('input.csv', 'output.xlsx')