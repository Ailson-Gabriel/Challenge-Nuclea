import os
from docx import Document
from buscar import encontrar_nomes, encontrar_cpf, encontrar_cnpj
from criptografar_arquivo import criptografar_arquivo_caminho

def processar(arquivo):
    """
    Processa um arquivo .docx, procurando por nomes e CPFs.

    Argumento:
        arquivo (str): O caminho para o arquivo .docx a ser processado.
    """

    print("Processando docx:", os.path.basename(arquivo))
    
    texto_docx = extrair_texto(arquivo)

    encontrados_nomes = encontrar_nomes(texto_docx) # Encontrar nomes nos arquivos .docx
    encontrados_cpf = encontrar_cpf(texto_docx) # Encontrar CPFs no arquivo .docx
    encontrados_cnpj = encontrar_cnpj(texto_docx) # Encontra CNPJs no texto extraido do arquivo .docx

    if encontrados_nomes or encontrados_cpf or encontrados_cnpj:
        criptografar_arquivo_caminho(arquivo)

    # -------------------------------------- Imprime os resultados -------------------------------------- #
    if encontrados_nomes:
        print(f"Nomes encontrados no arquivo {os.path.basename(arquivo)}\n")
        print(encontrados_nomes,"\n")
    else:
        print(f"Não foram encontrados nomes no arquivo {os.path.basename(arquivo)}\n")

    if encontrados_cpf:
        print(f"CPF encontrado no arquivo {os.path.basename(arquivo)}\n")
    else:
        print(f"Não encontrado CPFs no arquivo {os.path.basename(arquivo)}\n")

    if encontrados_cnpj:
        print(f"CNPJ encontrado no arquivo {os.path.basename(arquivo)}\n")
    else:
        print(f"Não encontrado CNPJs no arquivo {os.path.basename(arquivo)}\n")
    # -------------------------------------- Imprime os resultados -------------------------------------- #
        
def extrair_texto(arquivo):
    """
    Extrai texto de um arquivo DOCX.

    Argumento:
        arquivo (str): O caminho para o arquivo DOCX a ser processado.

    Retorna:
        str: O texto extraído do arquivo DOCX.
    """
    document = Document(arquivo) # Abre o arquivo .docx e extrai o texto
    texto = ""
    for paragraph in document.paragraphs: # Repete sobre os parágrafos do documento e concatena seus textos
        texto += paragraph.text + "\n"
    return texto