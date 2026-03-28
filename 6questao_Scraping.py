# A estrutura do site pode variar, então o scraping pode exigir ajustes conforme o HTML real da página.
# esse desafio exige muita logica de web scraping, tive que pesquisar bastante para conseguir fazer algo que funcionasse, o site do inmet tem uma estrutura bem complexa 
# e as vezes os dados nao estavam disponiveis, entao tive que fazer um codigo mais generico para tentar pegar os dados isso foi desafiardor e to 3 horas pensando em como fazer isso kkkk,
#  espero que esteja certo gostei muito desse desafio e me diverti muito fazendo ele, espero que gostem do resultado final e gostria de me apronfudar mais em aprende sobre web scraping e como lidar com dados em geral,
#  se tiver algo errado me avisem que e algo que tenho que e me aprofundar mais.

import requests
from bs4 import BeautifulSoup
from datetime import datetime

def pegar_dados_inmet(cidade, estado):
    url = "https://portal.inmet.gov.br/dadoshistoricos" 

# A estrutura do site pode variar, então o código abaixo é um exemplo genérico de como extrair os dados.
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    dados = {}

    # Exemplo genérico (depende da estrutura real do site)
    linhas = soup.find_all('tr')

    for linha in linhas:
        colunas = linha.find_all('td')

        if len(colunas) >= 3:
            hora = colunas[0].text.strip()
            temperatura = colunas[1].text.strip()
            umidade = colunas[2].text.strip()

            # filtro simples (evitar valores vazios)
            if hora and temperatura and umidade:
                dados[hora] = (temperatura, umidade)

    return dados