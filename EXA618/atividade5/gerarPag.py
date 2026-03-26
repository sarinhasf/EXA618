import csv

input_file = "saidaSAX.csv"
output_file = "resultado.html"
html_cards = ""

with open(input_file, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        url = row["url"]
        title = row["title"].strip() if row["title"] else "Sem título"
        img = row["img"]

        html_cards += f"""
        <div class="card">
            <h2><a href="{url}" target="_blank">{title}</a></h2>
            <img src="{img}">
            <p class="fonte">Fonte: <a href="{url}" target="_blank">{url}</a></p>
        </div>
        """

html_final = f"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Resultado</title>
    <style>
        body {{
            font-family: Arial;
            background: #f4f4f9;
            padding: 40px;
        }}
        .card {{
            background: white;
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 8px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        }}
        img {{
            max-width: 300px;
            display: block;
            margin-top: 10px;
            border-radius: 5px;
        }}
        a {{
            color: #007bff;
            text-decoration: none;
        }}
    </style>
</head>
<body>
    <h1>Resultados</h1>
    {html_cards}
</body>
</html>
"""

with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_final)

print("HTML gerado com sucesso!")