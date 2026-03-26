import csv
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

dados = []  # lista para armazenar todos os pontos

with open('saidaDOM.csv', mode='r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor)

    id = 0

    for linha in leitor:
        
        loc = {
            "type": "Point",
            "coordinates": [
                float(linha[1]),  # lon
                float(linha[0])   # lat
            ]
        }

        prop = {
            "nome": linha[3],
            "tipo": linha[2]
        }

        feature = {
            "type": "Feature",
            "geometry": loc,
            "properties": prop,
            "id": id
        }

        dados.append(feature)  # adiciona na lista

        id += 1

with open("dados.json", "w", encoding="utf-8") as arquivo2:
    arquivoJson = {
        "type": "FeatureCollection",
        "features": dados
    }
    json.dump(arquivoJson, arquivo2, ensure_ascii=False, indent=4)