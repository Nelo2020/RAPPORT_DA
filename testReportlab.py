from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def draw_elephant_design(c):
    # Définir la couleur orange utilisée dans le design
    orange_color = colors.HexColor("#F17F0A")  # Valeurs Hex pour l'orange

    # Définir les coordonnées et dimensions de l'éléphant et des lignes courbes
    width, height = letter

    # Couleur de fond orange
    c.setFillColor(orange_color)
    c.rect(0, 0, width, height, fill=True, stroke=False)

    # Dessiner l'éléphant (simplifié)
    c.setStrokeColor(colors.black)
    c.setLineWidth(3)

    # Tête de l'éléphant
    c.circle(300, 500, 100, stroke=1, fill=0)
    # Oreille gauche
    c.arc(200, 450, 300, 550)
    # Oreille droite
    c.arc(300, 450, 400, 550)
    # Trompe
    c.line(300, 500, 300, 400)
    # Yeux
    c.circle(270, 530, 5, stroke=1, fill=1)

    # Dessiner les lignes courbes
    c.setStrokeColor(colors.white)
    c.setLineWidth(2)
    
    # Courbes manuelles utilisant les chemins (paths)
    c.beginPath()
    c.moveTo(50, 150)
    c.curveTo(150, 200, 250, 100, 350, 150)
    c.curveTo(450, 200, 550, 100, 650, 150)
    c.stroke()

    # Ajouter des courbes supplémentaires
    for i in range(1, 5):
        c.setLineWidth(0.5 + i * 0.5)
        c.beginPath()
        c.moveTo(50, 150 + i * 20)
        c.curveTo(150, 200 + i * 20, 250, 100 + i * 20, 350, 150 + i * 20)
        c.curveTo(450, 200 + i * 20, 550, 100 + i * 20, 650, 150 + i * 20)
        c.stroke()

# Créer un document PDF
pdf_path = "elephant_design.pdf"
c = canvas.Canvas(pdf_path, pagesize=letter)

# Dessiner le design de l'éléphant
draw_elephant_design(c)

# Sauvegarder le PDF
c.save()
