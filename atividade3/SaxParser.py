import xml.sax
import sys

sys.stdout.reconfigure(encoding='utf-8')

class Listener(xml.sax.ContentHandler):
    def __init__(self):
        #usa o self para armazenar o arquivo
        self.file = open("saidaSAX.csv", "w", encoding="utf-8")
        self.file.write("lat,lon,amenity,nome\n")

        self.lat = ""
        self.lon = ""
        self.amenity = ""
        self.nome = ""

    def startElement(self, tag, attributes):
        if tag == "node":
            self.lat = attributes.get("lat")
            self.lon = attributes.get("lon")
            self.amenity = ""
            self.nome = ""

        elif tag == "tag":
            k = attributes.get("k")
            v = attributes.get("v")

            if k == "amenity":
                self.amenity = v

            elif k == "name":
                self.nome = v

    def endElement(self, tag):
        if tag == "node":
            # só salva se tiver amenity
            if self.amenity != "" and self.nome != "":
                linha = f"{self.lat},{self.lon},{self.amenity},{self.nome}\n"
                print(linha.strip())
                self.file.write(linha)

    def endDocument(self):
        self.file.close()

parser = xml.sax.make_parser()
parser.setContentHandler(Listener())

print("Starting SAX Parser...")
parser.parse("map2.osm")