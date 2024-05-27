import psycopg2
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.colors import orange, black, gray, white, silver
from reportlab.lib.units import cm, mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch

width, height = letter

def fetch_data_from_db():
    conn = psycopg2.connect(
        dbname="postgres",
        user="user",
        password="admin",
        host="localhost",
        port="54320"
    )
    cur = conn.cursor()
    cur.execute("SELECT nom, prenoms, email, poste, role_id FROM employees_da WHERE id_da='1'")
    employee_data = cur.fetchone() 

    cur.execute("SELECT nom FROM membres_assurance")
    membres_assurance_data = cur.fetchall()  
    cur.close()
    conn.close()
    return employee_data, membres_assurance_data

def draw_curved_lines(c, width, height):
    c.setStrokeColor(white)
    c.setLineWidth(0.5)
    # First curve
    path = c.beginPath()
    path.moveTo(0, height - 160)
    path.curveTo(width / 8, height - 100, width / 5, height - 90, width, height - 105)
    c.drawPath(path, stroke=True, fill=False)
    # Second curve
    path = c.beginPath()
    path.moveTo(0, height - 155)
    path.curveTo(width / 8, height - 95, width / 6, height - 88, width, height - 100)
    c.drawPath(path, stroke=True, fill=False)
    # Third curve
    path = c.beginPath()
    path.moveTo(0, height - 140)
    path.curveTo(width / 8, height - 95, width / 6, height - 88, width, height - 96)
    c.drawPath(path, stroke=True, fill=False)
    # Fourth curve
    path = c.beginPath()
    path.moveTo(0, height - 130)
    path.curveTo(width / 8, height - 95, width / 6, height - 88, width, height - 90 )
    c.drawPath(path, stroke=True, fill=False)

def draw_table_on_canvas(c, width, height, employee_data, membres_assurance_data):
    styles = getSampleStyleSheet()
    style_footer = ParagraphStyle(
        name='Footer',
        fontSize=12,
        alignment=TA_CENTER,
        textColor=colors.black,
        spaceBefore=10
    )
    
    employee_name = employee_data[1] 
    footer_text = f"Source : Direction des Assurances {employee_name} Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa quae corrupti, excepturi quo itaque nemo reiciendis accusantium dolores libero perferendis? Est, officiis voluptatem adipisci delectus natus maiores quae impedit commodi?"   
    footer = Paragraph(footer_text, style_footer)

    # Table data for employees_da
    employee_table_data = [["Nom", "Prénoms", "Email", "Poste", "Rôle"]]  # Table headers
    employee_table_data.append(employee_data)  # Adding the data row

    employee_table = Table(employee_table_data, rowHeights=20, repeatRows=1, colWidths=[0.8*inch, 1.5*inch, 2*inch, 2*inch, 1.3*inch])
    employee_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#E87945")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (0, 1), 10),
        ('FONTSIZE', (2, 0), (3, 0), 6),
        ('BACKGROUND', (0, 1), (-1, -2), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -2), colors.black),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor("#E87945")),
        ('TEXTCOLOR', (0, -1), (-1, -1), colors.white),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
    ]))

    employee_table.wrapOn(c, 500, 900)
    employee_table.drawOn(c, 20, height - 460)

    # Table data for membres_assurance
    membres_assurance_table_data = [["Nom"]]  # Table header
    membres_assurance_table_data.extend(membres_assurance_data)  # Adding the data rows

    membres_assurance_table = Table(membres_assurance_table_data, rowHeights=20, repeatRows=1, colWidths=[2*inch])
    membres_assurance_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#E87945")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (0, 1), 10),
        ('BACKGROUND', (0, 1), (-1, -2), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -2), colors.black),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor("#E87945")),
        ('TEXTCOLOR', (0, -1), (-1, -1), colors.white),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
    ]))

    membres_assurance_table.wrapOn(c, 500, 900)
    membres_assurance_table.drawOn(c, 20, height - 560)

    footer.wrapOn(c, width, height)
    footer.drawOn(c, 10, 350)

def draw_layout():
    c = canvas.Canvas("dbconn.pdf", pagesize=A4)
    width, height = A4
    employee_data, membres_assurance_data = fetch_data_from_db()

    
    if employee_data:
        nom, prenoms, email, poste, role = employee_data 
        display_text = f"Nom: {nom}, Prénoms: {prenoms}, Email: {email}, Poste: {poste}, Rôle: {role}"
        c.drawString(width - 500, height - 250, display_text)
    else:
        c.drawString(width - 270, height - 250, "No data available")

    # Drawing the rest of the layout as per your code
    draw_curved_lines(c, width, height)
    
    # Draw the tables with the data from the database
    draw_table_on_canvas(c, width, height, employee_data, membres_assurance_data)

    c.save()

draw_layout()
