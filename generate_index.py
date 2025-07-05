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
      <div class="info">{v["title"]}</div>
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
  <main class="car-page">
    <aside class="car-sidebar">
      <img class="car-main-photo" src="../{image}" alt="{title}">
      <div class="car-title">{title}</div>
      <a class="whatsapp-btn" href="https://wa.me/{whatsapp_link}" target="_blank">
        <img src="../img/whats-logo.png" alt="WhatsApp" class="whats-icon">{whatsapp_display}
      </a>
      <ul class="car-details">
        <li><strong>Marca:</strong> {make}</li>
        <li><strong>Ano:</strong> {year}</li>
        <li><strong>Cor:</strong> {color}</li>
        <li><strong>Quilometragem:</strong> {mileage}</li>
        <li><strong>Potência:</strong> {power}</li>
        <li><strong>Preço:</strong> {price}</li>
        <li><strong>Localização:</strong> {location}</li>
        <li><strong>Descrição:</strong> {description}</li>
      </ul>
    </aside>
    <section class="car-content">
      <p><a href="../index.html">&larr; Voltar para a listagem</a></p>
    </section>
  </main>
</body>
</html>
'''

os.makedirs('escort/anuncios', exist_ok=True)
for v in vehicles:
    # WhatsApp formatting
    whatsapp_link = v.get("whatsapp", "").replace("+", "").replace(" ", "")
    whatsapp_display = v.get("whatsapp_display", v.get("whatsapp", ""))
    detail_html = detail_template.format(
        title=v["title"],
        image=v["image"],
        price=v.get("price", ""),
        location=v.get("location", ""),
        description=v.get("description", ""),
        whatsapp_link=whatsapp_link,
        whatsapp_display=whatsapp_display,
        make=v.get("make", "-"),
        year=v.get("year", "-"),
        color=v.get("color", "-"),
        mileage=v.get("mileage", "-"),
        power=v.get("power", "-")
    )
    # Extract filename from link
    filename = v["link"].split('/')[-1]
    with open(f'escort/anuncios/{filename}', 'w', encoding='utf-8') as f:
        f.write(detail_html)

print("escort/index.html and detail pages generated!") 