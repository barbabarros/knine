import requests
import mimetypes
import time

url_base = "https://example.com/"   # URL destino com / no final. O nome do arquivo será a variável inicio + .pdf 
inicio = 1   # Início do intervalo contendo o nome do arquivo .pdf
fim = 2   # Fim do intervalo contendo o nome do arquivo .pdf
delay = 1.3   # Intervalo entre as requisições (1.3 = 1 segundo e 300 milissegundos) 
arquivo_txt = "URLs.txt"   # Nome do arquivo para salvar as URLs válidas. Será salvo no mesmo diretório de execução do programa

def valida_url_pdf(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content_type = response.headers.get('content-type')
            return mimetypes.guess_extension(content_type) == '.pdf'
        return False
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar URL {url}: {e}")
        return False

def gera_e_salva_as_urls_validadas():
    urls_validas = []
    for i in range(inicio, fim + 1):  # Itera dentro do intervalo especificado
        url = f"{url_base}{i:018}.pdf"  # Formata o número com 18 dígitos
        print(f"Verificando URL: {url}")
        if valida_url_pdf(url):
            urls_validas.append(url)
            print(f"URL válida encontrada: {url}")
        
        # Adiciona um atraso de x ms entre as requisições
        time.sleep(delay)

    # Salva os URLs válidos em um arquivo .txt
    with open(arquivo_txt, "w") as file:
        for url in urls_validas:
            file.write(url + "\n")

gera_e_salva_as_urls_validadas()