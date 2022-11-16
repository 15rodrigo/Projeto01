import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

page = requests.get("https://produto.mercadolivre.com.br/MLB-2901821860")
souped = BeautifulSoup(page.content, "html.parser")
imgs = souped.find_all("img")
imgs = imgs[13:-1]

for img in imgs:
    imglink = img.attrs.get("data-zoom")
    print(imglink)
    # imagem = requests.get(imglink).content
    # filename = r"fotos" + imglink[imglink.rfind("/"):]
    # with open (filename, "wb") as file:
    #     file.write(imagem)
   