import os

script_path = os.path.abspath(__file__)
BASE_PATH = os.path.dirname(script_path)
SEPARATOR = os.path.sep

LETTERS_MAP: tuple[tuple[str,str]] = (
    ('a', '!'),
    ('A', '!'),
    ('e', '@'),
    ('E', '@'),
    ('i', '#'),
    ('I', '#'),
    ('o', '$'),
    ('O', '$'),
    ('u', '%'),
    ('U', '%'),
)

def replaceLetters(line: str) -> str:
    for _, (old, new) in enumerate(LETTERS_MAP):
        line = line.replace(old, new)

    return line

def processFile(path: str) -> str | None:
    processed:str = ""
    try:
        with open(BASE_PATH  + SEPARATOR + path, 'r', encoding="utf-8") as file:
            for line in file.readlines():
                processed += replaceLetters(line)
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return
    except Exception as e:
        print(f"Erro: {e}")
        return

    return processed

def saveFile(name: str, data: str):
    try:
        with open(BASE_PATH  + SEPARATOR + name, "w", encoding="utf-8") as file:
            file.write(data)
        print("Arquivo processado com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

input_file = "musica.txt"

encryptedFile = processFile(input_file)

if(encryptedFile is None):
    exit(0)

output_file = input("Digite o nome do arquivo de saída: ")

saveFile(output_file + ".txt", encryptedFile)