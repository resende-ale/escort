import csv
import os
import re

def natural_sort_key(text):
    """
    Convert a string into a list of string and number chunks.
    "car-name-2.jpg" becomes ["car-name-", 2, ".jpg"]
    This allows for proper numerical sorting.
    """
    import re
    def atoi(text):
        return int(text) if text.isdigit() else text
    return [atoi(c) for c in re.split(r'(\d+)', text)]

def format_brazilian_phone(phone):
    """
    Format Brazilian phone number from +5511980553559 to (11) 98055-3559
    """
    # Remove +55 and any non-digit characters
    digits = re.sub(r'[^\d]', '', phone)
    
    # If it starts with 55, remove it (Brazil country code)
    if digits.startswith('55'):
        digits = digits[2:]
    
    # Format as (XX) XXXXX-XXXX
    if len(digits) == 11:  # Mobile number
        return f"({digits[:2]}) {digits[2:7]}-{digits[7:]}"
    elif len(digits) == 10:  # Landline number
        return f"({digits[:2]}) {digits[2:6]}-{digits[6:]}"
    else:
        return phone  # Return original if format is unexpected

# Read vehicles from CSV
vehicles = []
with open('vehicles.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        vehicles.append(row)

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
    # Check if vehicle should be published (shown on main page)
    publish = v.get("publish", "true").lower() == "true"
    
    # Main image: first image in natural order from the folder
    img_folder = f"img/{v['image_folder']}"
    main_img = "img/placeholder.jpg"  # fallback placeholder
    if os.path.isdir(img_folder):
        imgs = sorted([f for f in os.listdir(img_folder) if not f.startswith('.')], key=natural_sort_key)
        if imgs:
            main_img = f"img/{v['image_folder']}/{imgs[0]}"
    
    # Generate link automatically from image_folder name
    link = f"anuncios/{v['image_folder']}.html"
    
    # Only add card to main page if published
    if publish:
        cards += f'''
        <a href="{link}" class="card">
          <img src="{main_img}" alt="{v["title"]}">
          <div class="info">{v["title"]}</div>
        </a>
        '''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_start + cards + html_end)

# Generate detail pages for each vehicle
detail_template = '''<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="stylesheet" href="../css/style.css">
  <link rel="stylesheet" href="../css/basicLightbox.min.css">
  <style>
    .lightbox-arrow {{ position: fixed; top: 50%; transform: translateY(-50%); font-size: 2.5em; color: #fff; background: rgba(0,0,0,0.3); border: none; z-index: 1100; cursor: pointer; padding: 0 18px; border-radius: 8px; user-select: none; }}
    .lightbox-arrow.left {{ left: 20px; }}
    .lightbox-arrow.right {{ right: 20px; }}
    .lightbox-close {{ position: fixed; top: 24px; left: 24px; font-size: 2.2em; color: #fff; background: rgba(0,0,0,0.3); border: none; z-index: 1200; cursor: pointer; border-radius: 50%; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; }}
    .lightbox-close:hover {{ background: rgba(0,0,0,0.5); }}
  </style>
</head>
<body>
  <header>
    <a href="../index.html">
      <img src="../img/logo.png" alt="Logo">
    </a>
  </header>
  <main class="car-page">
    <aside class="car-sidebar">
      <img class="car-main-photo" src="../{main_img}" alt="{title}">
      <div class="car-title">{title}</div>
      <a class="whatsapp-btn" href="https://wa.me/{whatsapp_link}" target="_blank">
        <img src="../img/whats-logo.png" alt="WhatsApp" class="whats-icon">{whatsapp_display}
      </a>
      <ul class="car-details">
        <li><strong>Marca:</strong> {make}</li>
        <li><strong>Modelo:</strong> {model}</li>
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
      {gallery}
      <p><a href="../index.html">&larr; Voltar para a listagem</a></p>
    </section>
  </main>
  <script src="../js/basicLightbox.min.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', function() {{
      var images = Array.from(document.querySelectorAll('.gallery-img'));
      function showLightbox(idx) {{
        var instance = basicLightbox.create(`
          <button class="lightbox-close">&times;</button>
          <button class="lightbox-arrow left">&#8592;</button>
          <img src="${{images[idx].src}}" style="max-width:90vw;max-height:90vh;display:block;margin:auto;">
          <button class="lightbox-arrow right">&#8594;</button>
        `, {{
          onShow: (inst) => {{
            var closeBtn = inst.element().querySelector('.lightbox-close');
            var left = inst.element().querySelector('.lightbox-arrow.left');
            var right = inst.element().querySelector('.lightbox-arrow.right');
            closeBtn.onclick = function(e) {{ e.stopPropagation(); inst.close(); }};
            left.onclick = function(e) {{ e.stopPropagation(); inst.close(); showLightbox((idx-1+images.length)%images.length); }};
            right.onclick = function(e) {{ e.stopPropagation(); inst.close(); showLightbox((idx+1)%images.length); }};
            document.onkeydown = function(ev) {{
              if(ev.key === 'ArrowLeft') {{ inst.close(); showLightbox((idx-1+images.length)%images.length); }}
              if(ev.key === 'ArrowRight') {{ inst.close(); showLightbox((idx+1)%images.length); }}
              if(ev.key === 'Escape') {{ inst.close(); }}
            }};
          }},
          onClose: () => {{ document.onkeydown = null; }}
        }});
        instance.show();
      }}
      images.forEach(function(img, i) {{
        img.setAttribute('data-index', i);
        img.addEventListener('click', function() {{ showLightbox(i); }});
      }});
    }});
  </script>
</body>
</html>
'''

os.makedirs('anuncios', exist_ok=True)
for v in vehicles:
    img_folder = f"img/{v['image_folder']}"
    gallery = ""
    main_img = "img/placeholder.jpg"  # fallback placeholder
    gallery_imgs = []
    if os.path.isdir(img_folder):
        imgs = sorted([f for f in os.listdir(img_folder) if not f.startswith('.')], key=natural_sort_key)
        if imgs:
            main_img = f"img/{v['image_folder']}/{imgs[0]}"
            gallery_imgs = [f"img/{v['image_folder']}/{img}" for img in imgs]
    # Gallery HTML
    if gallery_imgs:
        gallery += '<div class="car-gallery">'
        for idx, img in enumerate(gallery_imgs):
            gallery += f'<img src="../{img}" class="gallery-img" loading="lazy" data-index="{idx}">'  # add data-index
        gallery += '</div>'
    # Format WhatsApp number for display and link
    whatsapp_raw = v.get("whatsapp", "")
    whatsapp_display = format_brazilian_phone(whatsapp_raw)
    whatsapp_link = re.sub(r'[^\d]', '', whatsapp_raw)  # Remove all non-digits for the link
    
    detail_html = detail_template.format(
        title=v["title"],
        main_img=main_img,
        price=v.get("price", ""),
        location=v.get("location", ""),
        description=v.get("description", ""),
        whatsapp_link=whatsapp_link,
        whatsapp_display=whatsapp_display,
        make=v.get("make", "-"),
        model=v.get("model", "-"),
        year=v.get("year", "-"),
        color=v.get("color", "-"),
        mileage=v.get("mileage", "-"),
        power=v.get("power", "-"),
        gallery=gallery
    )
    # Generate filename from image_folder name
    filename = f"{v['image_folder']}.html"
    with open(f'anuncios/{filename}', 'w', encoding='utf-8') as f:
        f.write(detail_html)

print("index.html and detail pages generated!") 