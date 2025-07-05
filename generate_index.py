import json
import os

with open('escort/vehicles.json', encoding='utf-8') as f:
    vehicles = json.load(f)

html_start = '''<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Carros à Venda</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <img src="img/logo.png" alt="Logo">
  </header>
  <main class="grid">
'''

html_end = '''
  </main>
</body>
</html>
'''

cards = ""
for v in vehicles:
    cards += f'''
    <a href="{v["link"]}" class="card">
      <img src="{v["image"]}" alt="{v["title"]}">
      <div class="info">
        <h3>{v["title"]}</h3>
        <p>{v["price"]} • {v["location"]}</p>
      </div>
    </a>
    '''

with open('escort/index.html', 'w', encoding='utf-8') as f:
    f.write(html_start + cards + html_end)

# Generate detail pages for each vehicle
detail_template = '''<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="stylesheet" href="../css/style.css">
</head>
<body>
  <header>
    <a href="../index.html">
      <img src="../img/logo.png" alt="Logo">
    </a>
  </header>
  <main class="detalhes">
    <img src="../{image}" alt="{title}">
    <h2>{title}</h2>
    <p><strong>Preço:</strong> {price}</p>
    <p><strong>Localização:</strong> {location}</p>
    <p>{description}</p>
    <p><a href="../index.html">&larr; Voltar para a listagem</a></p>
  </main>
</body>
</html>
'''

os.makedirs('escort/anuncios', exist_ok=True)
for v in vehicles:
    detail_html = detail_template.format(
        title=v["title"],
        image=v["image"],
        price=v["price"],
        location=v["location"],
        description=v.get("description", "")
    )
    # Extract filename from link
    filename = v["link"].split('/')[-1]
    with open(f'escort/anuncios/{filename}', 'w', encoding='utf-8') as f:
        f.write(detail_html)

print("escort/index.html and detail pages generated!") 