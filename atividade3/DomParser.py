from xml.dom.minidom import parse
import sys

sys.stdout.reconfigure(encoding='utf-8')

BancoDocument = parse('map2.osm')

print("Starting DOM Parser...")

with open("saidaDom.csv", "w", encoding="utf-8") as f:

    f.write("lat,lon,amenity,nome\n")

    for c in BancoDocument.getElementsByTagName("node"):
        tags = c.getElementsByTagName("tag")

        amenity = ""
        nome = ""

        for tag in tags:
            if tag.getAttribute("k") == "amenity":
                amenity = tag.getAttribute("v")

            if tag.getAttribute("k") == "name":
                nome = tag.getAttribute("v")

        if amenity != "" and nome != "":
            linha = f"{c.getAttribute("lat")},{c.getAttribute("lon")},{amenity},{nome}"
            print(linha)
            f.write(linha + "\n")
