from email import utils
from operator import le
from urllib.request import Request, urlopen
from attr import attr
from bs4 import BeautifulSoup
import math
import utils


class leilao:
    def __init__(self, link, title, date, value):
        self.link = link
        self.title = title
        self.date = date
        self.value = value

newLlist = []
url = 'https://www.zukerman.com.br/leiloes-extrajudiciais'
req = Request(url, headers={'User-Agent': 'XYZ/3.0'})
webpage = urlopen(req, timeout=10).read()
soup = BeautifulSoup(webpage, 'html.parser')

qtd_itens = soup.find(
    'div', attrs={'class': 'd-sum'}).get_text().strip().replace(' ', '')
print(qtd_itens)

indexInit = qtd_itens.find('de')
indexFim = qtd_itens.find('resultados')
qtd = qtd_itens[indexInit+2:indexFim]
qtdpages = math.ceil(int(qtd)/20)

for i in range(1, qtdpages+1):
    urlPage = url + '?pagina=' + str(i)

    req = Request(urlPage, headers={'User-Agent': 'XYZ/3.0'})
    webpage = urlopen(req, timeout=10).read()
    soup = BeautifulSoup(webpage, 'html.parser')

    leiloes = soup.find_all('div', attrs={'class': 'cd-it-sc'})

    for item in leiloes:

        try:
            tituloLeilao = item.find(
                'div', attrs={'class': 'h-t'}).text.strip()
            utlLeilao = item.find(
                'a', attrs={'class': 'l-cid'}).get('href').strip()
            dataLeilao = item.find_all('li')[0].text.strip()
            valorLeilao = item.find_all('li')[1].text.strip()
            newLlist.append(
                leilao(utlLeilao, tituloLeilao, dataLeilao, valorLeilao))
        except:
            continue

utils.GenerateExcel(newLlist)
