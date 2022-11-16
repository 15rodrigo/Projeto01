from xml.dom.minidom import Attr
from xml.sax.xmlreader import AttributesImpl
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

lista_peças = []

options = Options()
#options.add_argument('--headledd')
options.add_argument('window-size=1020,720')

navegador = webdriver.Chrome(options=options)

navegador.get('https://lista.mercadolivre.com.br/')

sleep(0.5)

entendiButton = navegador.find_elements_by_tag_name('button')[1]
entendiButton.click()

sleep(0.5)

input_place = navegador.find_elements_by_tag_name('input')[1]
input_place.send_keys('Mi Band 5')
input_place.submit()

primeiro_botao = navegador.find_element_by_tag_name('h2')
primeiro_botao.click()

sleep(1)

# page_content = navegador.page_source

# site = BeautifulSoup(page_content, 'html.parser')

# titulo = site.find('h1', attrs={'class' : 'ui-pdp-title'})

# real = site.find('span', attrs={'class' : 'andes-money-amount__fraction'})
# centavos = site.find('span', attrs={'class' : 'andes-money-amount__cents andes-money-amount__cents--superscript-36'})

# observacao = site.find('p', attrs={'class' : 'ui-pdp-description__content'})

# img1 = site.find('div', attrs={'img' : 'ui-pdp-image'})

# print('titulo: ', titulo.text)

# if (centavos):
#     print('Preço: R$', real.text + ',' + centavos.text)
# else :
#     print('Preço: R$', real.text)

# print('descrição: ', observacao.text)


# #pecas = pd.DataFrame(lista_pecas, columns=['titulo','Descrição', 'real','centavos', 'urlink'])

# #pecas.to_excel('pecas.xlsx', index=[False])





# site = BeautifulSoup(navegador.page_source, 'html.parser')

# print(site.prettify())
