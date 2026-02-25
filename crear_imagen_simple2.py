from PIL import Image, ImageDraw

# Crear imagen en blanco
width, height = 1200, 628  # Tamaño ideal para Twitter
img = Image.new('RGB', (width, height), color = (30, 30, 30))

draw = ImageDraw.Draw(img)

# Añadir título principal usando texto simple
# Usar tamaño de fuente por defecto
draw.text((50, 50), 'EL TERREMOTO TECNOLÓGICO', fill=(255, 255, 255))
draw.text((50, 110), 'QUE NADIE VIÓ VENIR', fill=(255, 255, 255))

# Añadir subtítulo
draw.text((50, 180), '20 de Febrero, 2026 - El día que Wall Street entró en pánico', fill=(200, 200, 200))

# Gráfico de caída de acciones
stock_data = [
    ('CrowdStrike', -7.9, (255, 99, 132)),
    ('Okta', -9.6, (54, 162, 235)),
    ('Cloudflare', -8.0, (255, 205, 86)),
    ('Zscaler', -4.0, (75, 192, 192)),
    ('Global X Cybersecurity ETF', -4.6, (153, 102, 255))
]

y_start = 280
bar_width = 100
max_height = 150

for i, (company, change, color) in enumerate(stock_data):
    bar_height = (abs(change) / 10) * max_height
    x = 50 + i * (bar_width + 30)
    draw.rectangle([x, y_start + max_height - bar_height, x + bar_width, y_start + max_height], fill=color)
    draw.text((x, y_start + max_height + 10), company, fill=(255, 255, 255))
    draw.text((x, y_start + max_height - bar_height - 30), f'{change}%', fill=(255, 255, 255))

# Línea de base
draw.line([(50, y_start + max_height), (width - 50, y_start + max_height)], fill=(100, 100, 100), width=2)

# Destacados
highlights = [
    ('Claude Code Security', 'encontró 500+ vulnerabilidades', (255, 255, 255)),
    ('Comando /security-review', 'gratis desde Agosto 2025', (255, 255, 255)),
    ('Google Principal Engineer', '1 año vs 1 hora', (255, 255, 255))
]

y_highlight = 500
for i, (title, description, color) in enumerate(highlights):
    draw.text((50, y_highlight + i * 40), f'• {title}: {description}', fill=color)

# Logo de Claude Code (símbolo estilizado)
logo_size = 60
logo_x = width - 120
logo_y = height - 100
draw.ellipse([logo_x - logo_size/2, logo_y - logo_size/2, logo_x + logo_size/2, logo_y + logo_size/2], outline=(255, 255, 255), width=3)
draw.line([(logo_x - 15, logo_y - 10), (logo_x + 15, logo_y + 10)], fill=(255, 255, 255), width=3)
draw.line([(logo_x - 15, logo_y + 10), (logo_x + 15, logo_y - 10)], fill=(255, 255, 255), width=3)

# Hashtags finales
draw.text((50, height - 50), '#ClaudeCode #TechDisruption #Cybersecurity #Innovation', fill=(150, 150, 150))

# Guardar imagen
img.save('publicacion_claude_code.jpg')
print("Imagen creada: publicacion_claude_code.jpg")