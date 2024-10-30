import os

def rename_files(directory):
    # Verifica se o diretório existe
    if not os.path.exists(directory):
        print(f"O diretório '{directory}' não existe.")
        return

    # Itera sobre todos os arquivos no diretório
    for filename in os.listdir(directory):
        # Define o caminho completo do arquivo
        old_file:str = os.path.join(directory, filename)
        print(old_file)

        # Verifica se é um arquivo
        if os.path.isfile(old_file) and ("space" in old_file):
            # Substitui espaços por sublinhados
            new_filename = filename.replace(" ", "_").replace("(", "").replace(")", "")
            new_file = os.path.join(directory, new_filename)

            # Renomeia o arquivo
            os.rename(old_file, new_file)
            print(f"Renomeado: '{old_file}' para '{new_file}'")

# Exemplo de uso
if __name__ == "__main__":
    # Substitua pelo caminho da sua pasta
    directory_path = "c:/Users/LuisCunha/Documents/GitHub/Python-Dump/voucher/oferta2/html/nasa/img/"
    rename_files(directory_path)
