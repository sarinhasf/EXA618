import requests
import xml.sax
import io
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class MeuHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.file = open("saidaSAX.csv", "w", encoding="utf-8")
        self.file.write("url,title,img\n")

        self.title = ""
        self.current_url = ""

    def startElement(self, name, attrs):
        if name == "img":
            img = attrs.get("src", "").strip()

            if img:
                img_url = urljoin(self.current_url, img)

                linha = f'"{self.current_url}","{self.title}","{img_url}"\n'
                print(linha)
                self.file.write(linha)


parser = xml.sax.make_parser()
handler = MeuHandler()
parser.setContentHandler(handler)

with open("./seeds.txt", "r", encoding="utf-8") as f:
    for linha in f:
        url = linha.strip()

        if not url:
            continue

        print("\nURL:", url)

        try:
            r = requests.get(url, timeout=10)
            r.raise_for_status()
        except requests.RequestException as e:
            print(f"Erro ao acessar {url}: {e}")
            continue

        handler.current_url = url

        conteudo = r.content.decode("utf-8", errors="ignore")

        soup = BeautifulSoup(conteudo, "html.parser")

        if soup.title and soup.title.string:
            handler.title = soup.title.string.strip()
        else:
            handler.title = "Sem título"

        conteudo_formatado = soup.prettify()

        stream = io.StringIO(conteudo_formatado)

        parser.parse(stream)

handler.file.close()