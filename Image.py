from PIL import Image

# Charger l'image
input_path = "images/Capture d'écran 2024-05-16 225531.png"
image = Image.open(input_path)

# Convertir l'image en mode RGBA pour gérer la transparence
image = image.convert("RGBA")

# Accéder aux pixels de l'image
pixels = image.load()

# Définir la couleur blanche à supprimer
white_color = (255, 255, 255, 255)

# Parcourir tous les pixels de l'image et remplacer les pixels blancs par des pixels transparents
for y in range(image.height):
    for x in range(image.width):
        if pixels[x, y] == white_color:
            pixels[x, y] = (255, 255, 255, 0)  # Mettre le pixel à transparent

# Sauvegarder l'image modifiée
output_path = "images/modified_image.png"
image.save(output_path, "PNG")

output_path
