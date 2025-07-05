import json

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
    <h1>Carros à Venda</h1>
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

print("escort/index.html generated!") 