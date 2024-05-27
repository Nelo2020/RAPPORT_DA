from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.colors import orange, black, gray, white, silver
from reportlab.lib.units import cm, mm
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
# ParagraphStyle
from reportlab.lib.pagesizes import letter

from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch

width, height = letter

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
    
    
    # 4 curve
    path = c.beginPath()
    path.moveTo(0, height - 130)
    path.curveTo(width / 8, height - 95, width / 6, height - 88, width, height - 90 )
    c.drawPath(path, stroke=True, fill=False)
    
    # # Second curve
    # path = c.beginPath()
    # path.moveTo(0, height - 120)
    # path.curveTo(width / 4, height - 140, width / 2, height - 100, width, height - 120)
    # c.drawPath(path, stroke=True, fill=False)
    
    # # Third curve
    # path = c.beginPath()
    # path.moveTo(0, height - 140)
    # path.curveTo(width / 4, height - 160, width / 2, height - 120, width, height - 140)
    # c.drawPath(path, stroke=True, fill=False)
    
    # # 4 curve
    # path = c.beginPath()
    # path.moveTo(0, height - 20)
    # path.curveTo(width / 4, height - 160, width / 2, height - 120, width, height - 140)
    # c.drawPath(path, stroke=True, fill=False)
def draw_table_on_canvas(c, width, height):
    # Styles
    styles = getSampleStyleSheet()
    
    # Styles personnalisés
     # Définir des styles personnalisés
    custom_style_normal = ParagraphStyle(
        name='CustomNormal',
        parent=styles['Normal'],
        textColor=colors.black
    )

    custom_style_header = ParagraphStyle(
        name='CustomHeader',
        parent=styles['Normal'],
        textColor=colors.white
    )

    style_footer = ParagraphStyle(
        name='Footer',
        fontSize=10,
        alignment=TA_CENTER,
        textColor=colors.black,
        spaceBefore=10
    )

    # Title et Subtitle (commenté pour l'exemple)
    # title_text = "ANNEXE 1"
    # subtitle_text = "EVOLUTION DU CHIFFRE D'AFFAIRES SOCIETE VIE TRIMESTRE 3 2023"
    # title = Paragraph(title_text, style_title)
    # subtitle = Paragraph(subtitle_text, style_subtitle)
    footer = Paragraph("Source : Direction des Assurances", style_footer)

    # Data avec Paragraph pour le wrapping du texte
    data = [
        [Paragraph("N°" , custom_style_header), Paragraph("COMPAGNIES", custom_style_header), Paragraph("CHIFFRE D'AFFAIRES 3ème TRIMESTRE 2023", custom_style_header), 
         Paragraph("CHIFFRE D'AFFAIRES 3ème TRIMESTRE 2022", custom_style_header), Paragraph("EVOLUTION %", custom_style_header)],
        [Paragraph("1", styles['Normal']), Paragraph("ALLIANZ-VIE", styles['Normal']), Paragraph("8 238 062 410", styles['Normal']), 
         Paragraph("8 308 456 229", styles['Normal']), Paragraph("-0,85%", styles['Normal'])],
        [Paragraph("2", styles['Normal']), Paragraph("ATLANTIQUE VIE", styles['Normal']), Paragraph("390 966 3457", styles['Normal']), 
         Paragraph("2 823 183 467", styles['Normal']), Paragraph("38,48%", styles['Normal'])],
        [Paragraph("3", styles['Normal']), Paragraph("LEADWAY VIE", styles['Normal']), Paragraph("496 751 528,7", styles['Normal']), 
         Paragraph("607 999 212,8", styles['Normal']), Paragraph("-18,30%", styles['Normal'])],
        [Paragraph("4", styles['Normal']), Paragraph("NSIA VIE", styles['Normal']), Paragraph("9 355 408 832", styles['Normal']), 
         Paragraph("10 203 159 641", styles['Normal']), Paragraph("-8,31%", styles['Normal'])],
        [Paragraph("5", styles['Normal']), Paragraph("PRUD BELIFE", styles['Normal']), Paragraph("4 604 782 008", styles['Normal']), 
         Paragraph("5 237 615 883", styles['Normal']), Paragraph("-12,08%", styles['Normal'])],
        [Paragraph("6", styles['Normal']), Paragraph("SAAR VIE", styles['Normal']), Paragraph("290 328 648", styles['Normal']), 
         Paragraph("169 999 761", styles['Normal']), Paragraph("70,78%", styles['Normal'])],
        [Paragraph("7", styles['Normal']), Paragraph("SANLAM VIE", styles['Normal']), Paragraph("7 177 768 378", styles['Normal']), 
         Paragraph("5 760 212 198", styles['Normal']), Paragraph("24,61%", styles['Normal'])],
        [Paragraph("8", styles['Normal']), Paragraph("SOMAVIE", styles['Normal']), Paragraph("25 396 781", styles['Normal']), 
         Paragraph("42 955 508", styles['Normal']), Paragraph("-40,88%", styles['Normal'])],
        [Paragraph("9", styles['Normal']), Paragraph("SONAM VIE", styles['Normal']), Paragraph("31 181 610", styles['Normal']), 
         Paragraph("", styles['Normal']), Paragraph("", styles['Normal'])],
        [Paragraph("10", styles['Normal']), Paragraph("SUNU VIE", styles['Normal']), Paragraph("19 442 801 924", styles['Normal']), 
         Paragraph("14 454 274 045", styles['Normal']), Paragraph("34,51%", styles['Normal'])],
        [Paragraph("11", styles['Normal']), Paragraph("WAFA VIE", styles['Normal']), Paragraph("4 838 534 047", styles['Normal']), 
         Paragraph("4 592 128 428", styles['Normal']), Paragraph("5,37%", styles['Normal'])],
        [Paragraph("12", styles['Normal']), Paragraph("YAKO VIE", styles['Normal']), Paragraph("2 637 484 698", styles['Normal']), 
         Paragraph("2 516 349 360", styles['Normal']), Paragraph("4,81%", styles['Normal'])],
        [Paragraph("", styles['Normal']), Paragraph("TOTAL", custom_style_header), Paragraph("61 048 164 321", custom_style_header), 
         Paragraph("54 716 334 092", custom_style_header), Paragraph("11,57%", custom_style_header)]
    ]
    
    # Définir les largeurs des colonnes (en points)
    col_widths = [26, 150, 150, 150, 70]

# Définir les hauteurs des lignes (en points)
    row_heights = [26, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 25]  # Augmenter la hauteur de la dernière ligne

# Créer le tableau avec les largeurs de colonnes et hauteurs de lignes spécifiées
    table = Table(data, colWidths=col_widths, rowHeights=row_heights)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#E87945")),  # Header row background
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  # Header row text color
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Bold font for header row
        ('FONTSIZE', (0, 0), (0, 1), 10),  # Font size for header row
        ('FONTSIZE', (2, 0), (3, 0), 8),  # Font size for header row
        # ('TOPPADDING', (2, 0), (3, 0), 4),  # Padding for header row
        ('BACKGROUND', (0, 1), (-1, -2), colors.white),  # Background color for data rows
        ('TEXTCOLOR', (0, 1), (-1, -2), colors.black),  # Text color for data rows
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Grid lines
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor("#E87945")),  # Background for total row
        ('TEXTCOLOR', (0, -1), (-1, -1), colors.white),  # Text color for total row
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),  # Bold font for total row
    ]))

    # Draw table
    table.wrapOn(c, 500, 900)
    table.drawOn(c, 20, height - 610)

    # Draw footer
    footer.wrapOn(c, width, height)
    footer.drawOn(c, 10, 205)
def draw_table_on_canvas_annexe2(c, width, height):
    # Styles
    styles = getSampleStyleSheet()
    
    # Définir des styles personnalisés
    custom_style_normal = ParagraphStyle(
        name='CustomNormal',
        parent=styles['Normal'],
        textColor=colors.black
    )

    custom_style_header = ParagraphStyle(
        name='CustomHeader',
        parent=styles['Normal'],
        textColor=colors.white
    )

    style_footer = ParagraphStyle(
        name='Footer',
        fontSize=10,
        alignment=TA_CENTER,
        textColor=colors.black,
        spaceBefore=10
    )

    footer = Paragraph("Source : Direction des Assurances", style_footer)

    # Data avec Paragraph pour les colonnes de chiffres d'affaires
    data = [
        [Paragraph("N°", custom_style_header), Paragraph("COMPAGNIES", custom_style_header), 
         Paragraph("CHIFFRE D'AFFAIRES 3ème TRIMESTRE 2023", custom_style_header), 
         Paragraph("CHIFFRE D'AFFAIRES 3ème TRIMESTRE 2022", custom_style_header), 
         Paragraph("EVOLUTION %", custom_style_header)],
        [Paragraph("1", custom_style_normal), Paragraph("2ACI", custom_style_normal), 
         Paragraph("503 580 625", custom_style_normal), Paragraph("564 953 665", custom_style_normal), 
         Paragraph("-10,86%", custom_style_normal)],
        [Paragraph("2", custom_style_normal), Paragraph("ACTIVA", custom_style_normal), 
         Paragraph("1 673 984 607", custom_style_normal), Paragraph("2 880 782 550", custom_style_normal), 
         Paragraph("-41,89%", custom_style_normal)],
        [Paragraph("3", custom_style_normal), Paragraph("ALLIANZ", custom_style_normal), 
         Paragraph("6 489 276 743", custom_style_normal), Paragraph("6 376 027 748", custom_style_normal), 
         Paragraph("1,78%", custom_style_normal)],
        [Paragraph("4", custom_style_normal), Paragraph("AMSA", custom_style_normal), 
         Paragraph("2 378 938 260", custom_style_normal), Paragraph("2 013 695 704", custom_style_normal), 
         Paragraph("18,14%", custom_style_normal)],
        [Paragraph("5", custom_style_normal), Paragraph("ATLANTA", custom_style_normal), 
         Paragraph("1 218 706 352", custom_style_normal), Paragraph("973 704 699", custom_style_normal), 
         Paragraph("25,16%", custom_style_normal)],
        [Paragraph("6", custom_style_normal), Paragraph("ATLANTIQUE", custom_style_normal), 
         Paragraph("3 555 888 830", custom_style_normal), Paragraph("4 149 837 777", custom_style_normal), 
         Paragraph("-14,31%", custom_style_normal)],
        [Paragraph("7", custom_style_normal), Paragraph("AXA CI", custom_style_normal), 
         Paragraph("5 505 729 475", custom_style_normal), Paragraph("4 940 977 433", custom_style_normal), 
         Paragraph("11,43%", custom_style_normal)],
        [Paragraph("8", custom_style_normal), Paragraph("COMAR", custom_style_normal), 
         Paragraph("999 292 812", custom_style_normal), Paragraph("1 072 752 461", custom_style_normal), 
         Paragraph("-6,85%", custom_style_normal)],
        [Paragraph("9", custom_style_normal), Paragraph("CORIS", custom_style_normal), 
         Paragraph("61 964 603", custom_style_normal), "", ""],
        [Paragraph("10", custom_style_normal), Paragraph("GNA", custom_style_normal), 
         Paragraph("4 320 200 956", custom_style_normal), Paragraph("12 225 774 567", custom_style_normal), 
         Paragraph("-64,66%")],
        [Paragraph("11", custom_style_normal), Paragraph("LEADWAY", custom_style_normal), 
         Paragraph("1 127 153 007", custom_style_normal), "", ""],
        [Paragraph("12", custom_style_normal), Paragraph("LA LOYALE", custom_style_normal), 
         Paragraph("660 405 489", custom_style_normal), Paragraph("299 011 942", custom_style_normal), 
         Paragraph("120,86%")],
        [Paragraph("13", custom_style_normal), Paragraph("MATCA", custom_style_normal), 
         Paragraph("1 242 247 195", custom_style_normal), Paragraph("1 643 599 867", custom_style_normal), 
         Paragraph("-24,42%")],
        [Paragraph("14", custom_style_normal), Paragraph("NSIA", custom_style_normal), 
         Paragraph("3 433 560 773", custom_style_normal), Paragraph("4 938 320 212", custom_style_normal), 
         Paragraph("-30,47%")],
        [Paragraph("15", custom_style_normal), Paragraph("SAAR", custom_style_normal), 
         Paragraph("1 183 965 166", custom_style_normal), Paragraph("713 804 444", custom_style_normal), 
         Paragraph("65,87%")],
        [Paragraph("16", custom_style_normal), Paragraph("SANLAM", custom_style_normal), 
         Paragraph("13 894 750 203", custom_style_normal), Paragraph("13 680 829 261", custom_style_normal), 
         Paragraph("1,56%")],
        [Paragraph("17", custom_style_normal), Paragraph("SCHIBA", custom_style_normal), 
         Paragraph("976 220 545", custom_style_normal), "", ""],
        [Paragraph("18", custom_style_normal), Paragraph("SERENITY", custom_style_normal), 
         Paragraph("2 024 850 774", custom_style_normal), Paragraph("1 677 826 070", custom_style_normal), 
         Paragraph("20,68%")],
        [Paragraph("19", custom_style_normal), Paragraph("SIDAM", custom_style_normal), 
         Paragraph("1 026 191 634", custom_style_normal), Paragraph("1 390 304 454", custom_style_normal), 
         Paragraph("-26,19%")],
        [Paragraph("20", custom_style_normal), Paragraph("SMABTP", custom_style_normal), 
         Paragraph("1 555 881 008", custom_style_normal), Paragraph("2 078 077 446", custom_style_normal), 
         Paragraph("-25,13%")],
        [Paragraph("21", custom_style_normal), Paragraph("SONAM", custom_style_normal), 
         Paragraph("193 854 017", custom_style_normal), Paragraph("441 455 727", custom_style_normal), 
         Paragraph("-56,09%")],
        [Paragraph("22", custom_style_normal), Paragraph("SUNU", custom_style_normal), 
         Paragraph("4 808 476 340", custom_style_normal), Paragraph("5 706 164 566", custom_style_normal), 
         Paragraph("-15,73%")],
        [Paragraph("23", custom_style_normal), Paragraph("WAFA", custom_style_normal), 
         Paragraph("1 131 369 518", custom_style_normal), Paragraph("692 976 818", custom_style_normal), 
         Paragraph("63,26%")],
        ["", Paragraph("TOTAL", custom_style_header), Paragraph("59 966 488 932", custom_style_header), 
         Paragraph("68 404 242 301", custom_style_header), Paragraph("-12,34%", custom_style_header)]
    ]

    c_width = [24, 80, 150, 150, 85]
    row_heights = [26] + [20] * (len(data) - 1)  # Hauteur différente pour la première ligne
        
    # Table
    table = Table(data , rowHeights=row_heights, repeatRows=1, colWidths=c_width)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#76A646")),  # Header row background in green
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Header row text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
        ('FONTNAME', (0, 0), (-1, 0), 'Times-Bold'),  # Bold font for header row
        ('FONTSIZE', (0, 0), (0, 1), 10),  # Font size for header row
        ('FONTSIZE', (2, 0), (3, 0), 4),  # Font size for header row
        # ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Padding for header row
        ('BACKGROUND', (0, 1), (-1, -2), colors.white),  # Background color for data rows
        ('TEXTCOLOR', (0, 1), (-1, -2), colors.black),  # Text color for data rows
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Grid lines
        ('ALIGN', (2, 1), (2, -2), 'CENTER'),  # Center align text in "CHIFFRE D'AFFAIRES 3ème TRIMESTRE 2023" column
        ('ALIGN', (3, 1), (3, -2), 'CENTER'),  # Center align text in "CHIFFRE D'AFFAIRES 3ème TRIMESTRE 2022" column
        ('VALIGN', (2, 1), (2, -2), 'MIDDLE'),  # Middle vertical align text in "CHIFFRE D'AFFAIRES 3ème TRIMESTRE 2023" column
        ('VALIGN', (3, 1), (3, -2), 'MIDDLE'),  # Middle vertical align text in "CHIFFRE D'AFFAIRES 3ème TRIMESTRE 2022" column
        ('LINEBELOW', (2, 1), (2, 1), 0, colors.black),  # Remove grid line below first data row in the third column
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor("#8DC63F")),  # Background for total row in green
        ('TEXTCOLOR', (0, -1), (-1, -1), colors.white),  # Text color for total row
        ('FONTNAME', (0, -1), (-1, -1), 'Times-Bold'),  # Bold font for total row
    ]))

    # Draw table
    table.wrapOn(c, 500, 600)
    table.drawOn(c, 35, height - 680)

    footer.wrapOn(c, width, height)
    footer.drawOn(c, 10, 130)
    
def draw_table_on_canvas_annexe3(c, width, height):
    # Styles
    styles = getSampleStyleSheet()
    # style_title = ParagraphStyle(
    #     name='Title',
    #     fontSize=14,
    #     alignment=TA_CENTER,
    #     textColor=colors.white,
    #     backColor=colors.HexColor("#E87945"),
    #     spaceAfter=10
    # )
    # style_subtitle = ParagraphStyle(
    #     name='Subtitle',
    #     fontSize=12,
    #     alignment=TA_CENTER,
    #     textColor=colors.black,
    #     backColor=colors.HexColor("#D3E8AF"),  # Light green color for the subtitle
    #     spaceAfter=10
    # )
    style_footer = ParagraphStyle(
        name='Footer',
        fontSize=12,
        alignment=TA_CENTER,
        textColor=colors.black,
        spaceBefore=10
    )

    # Title
    # title = Paragraph("ANNEXE 3", style_title)
    # subtitle = Paragraph("LES CARTES PROFESSIONNELLES EDITEES AU TROISIEME TRIMESTRE 2023", style_subtitle)
    footer = Paragraph("Source : Direction des Assurances", style_footer)

    # Data
    data = [
        ["Type d'agent", "Société assurance mandante", "Total"],
        ["BANQUE", "ALLIANZ COTE D'IVOIRE ASSURANCES", "27"],
        ["", "ATLANTIQUE ASSURANCE VIE2", "2"],
        ["", "LA LOYALE VIE5", "1"],
        ["", "YAKO AFRICA ASSURANCES VIE CÔTE D'IVOIRE", "16"],
        ["", "Total BANQUE", "116"],
        ["GENERAL", "AMSA ASSURANCES CÔTE D'IVOIRE", "1"],
        ["", "GNA ASSURANCES", "7"],
        ["", "NSIA ASSURANCES 5", ""],
        ["", "SANLAM ASSURANCE CÔTE D'IVOIRE9", ""],
        ["", "SUNU ASSURANCES IARD1", ""],
        ["", "Total GENERAL", "23"],
        ["MANDATAIRE", "ALLIANZ COTE D'IVOIRE ASSURANCES", "5"],
        ["", "AMSA ASSURANCES CÔTE D'IVOIRE", "4"],
        ["", "ATLANTIQUE ASSURANCE VIE5", ""],
        ["", "ATLANTIQUE ASSURANCES CÔTE D'IVOIRE", "7"],
        ["", "GNA ASSURANCES", "6"],
        ["", "NSIA VIE ASSURANCES 4", ""],
        ["", "SANLAM ASSURANCE VIE CÔTE D'IVOIRE", ""],
        ["", "Total MANDATAIRE", "121"],
        ["", "Total général", "260"]
    ]

     
    c_width=[1.1*inch,4*inch,1*inch]
    # Table
    table = Table(data,rowHeights=20,repeatRows=1,colWidths=c_width)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.white),  # Header row background in light green
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Header row text color
        # ('ALIGN', (0, 4), (0, 4), 'TOP'),  # Center align all cells
        ('SPAN',(0,1),(0,4)),
        ('SPAN',(0,5),(0,5)),
        ('SPAN',(1,5),(1,5)),
         
    # Retirer le trait vertical entre la deuxième et la troisième colonne
        ('LINEBEFORE', (0, 11), (0, 11), 0, colors.white),
        ('VALIGN', (0, 5), (1, 5), 'MIDDLE'),  # Aligne verticalement le texte au milieu de la cellule fusionnée
        ('ALIGN', (0, 5), (1, 5), 'CENTER'),  # Centre le texte horizontalement
        ('SPAN',(0,6),(0,10)),
        ('VALIGN', (0, 6), (0, 8), 'TOP'),  # Aligne verticalement le texte en haut de la cellule fusionnée
        ('ALIGN', (0, 5), (0, 8), 'CENTER'),  # Centre le texte horizontalement
        ('TOPPADDING', (0, 6), (0, 8), 45),
        ('VALIGN', (0, 0), (0, 18), 'TOP'),  # Aligne verticalement le texte en haut de la cellule fusionnée
        ('ALIGN', (0, 0), (0, 4), 'CENTER'),  # Centre le texte horizontalement
        ('TOPPADDING', (0, 1), (0, 4), 30),
        ('VALIGN', (0, 0), (0, 4), 'TOP'),  # Aligne verticalement le texte en haut de la cellule fusionnée
        ('ALIGN', (0, 0), (0, 4), 'CENTER'),  # Centre le texte horizontalement
        ('TOPPADDING', (0, 11), (0, 19), 60),
        ('SPAN',(0,12),(0,18)),
        # ('SPAN',(0,20),(1,20)),
        # ('SPAN',(0,19),(1,19)),
        ('VALIGN', (1, 0), (1, 0), 'MIDDLE'),  # Aligne verticalement le texte au milieu de la cellule fusionnée
        ('ALIGN', (1, 0), (1, 0), 'CENTER'),  # Centre le texte horizontalement
        ('VALIGN', (0, 19), (1, 19), 'MIDDLE'),  # Aligne verticalement le texte au milieu de la cellule fusionnée
        ('ALIGN', (0, 19), (1, 19), 'CENTER'),  # Centre le texte horizontalement
        ('VALIGN', (0, 19), (1, 20), 'MIDDLE'),  # Aligne verticalement le texte au milieu de la cellule fusionnée
        ('ALIGN', (0, 19), (1, 20), 'CENTER'),  # Centre le texte horizontalement
        ('VALIGN', (0, 11), (1, 11), 'MIDDLE'),  # Aligne verticalement le texte au milieu de la cellule fusionnée
        ('ALIGN', (0, 11), (1, 11), 'CENTER'),  # Centre le texte horizontalement
        ('FONTNAME', (0, 0), (2, 0), 'Times-Bold'),  # Bold font for header row
        ('FONTNAME', (0, 5), (-1, 5), 'Times-Bold'),  # Bold font for header row
        ('FONTNAME', (0, 11), (-1, 11), 'Times-Bold'),  # Bold font for header row
        ('FONTNAME', (0, 19), (-1, 19), 'Times-Bold'),  # Bold font for header row
        ('FONTNAME', (0, 10), (0, 10), 'Times-Bold'),  # Bold font for header row
        
        ('FONTSIZE', (0, 0), (-1, 0), 12),  # Font size for header row
         
        ('FONTSIZE', (0, 18), (0, 18), 50),  # Font size for header row
        ('FONTSIZE', (0, 5), (-1, 5), 12),  # Font size for header row
        ('FONTSIZE', (0, 11), (-1, 11), 12),  # Font size for header row
        ('FONTSIZE', (0, 19), (-1, 19), 12),  # Font size for header row
        ('FONTSIZE', (0, 20), (-1, 20), 12),  # Font size for header row
        # ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Padding for header row
        ('BACKGROUND', (0, 1), (-1, -2), colors.white),  # Background color for data rows
        ('TEXTCOLOR', (0, 1), (-1, -2), colors.black),  # Text color for data rows
         ('TEXTCOLOR', (1, 20), (-1, 20), colors.white),  # Text color for data rows
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Grid lines
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor("#F27B35")),  # Background for total row in light green
        ('BACKGROUND', (0, 5), (-1, 5), colors.HexColor("#76A646")), # Background for total row in light green
        ('BACKGROUND', (0, 11), (-1, 11), colors.HexColor("#76A646")),
        ('BACKGROUND', (0, 19), (-1, 19), colors.HexColor("#76A646")),
        ('TEXTCOLOR', (0, -1), (-1, 2), colors.black),  # Text color for total row
        ('FONTNAME', (0, -1), (-1, -1), 'Times-Bold'),  # Bold font for total row
    ]))

    # Draw title, subtitle, and table
    # title.wrapOn(c, width, 300)
    # title.drawOn(c, 0, height - 72)

    # subtitle.wrapOn(c, 380, 5)
    # subtitle.drawOn(c, 72, height - 110)

    table.wrapOn(c, 200, 100)
    table.drawOn(c, 50, height - 600)

    footer.wrapOn(c, width, height)
    footer.drawOn(c, 10, 210)
    
def draw_page_annexe4(c, width, height):
    # Styles
    styles = getSampleStyleSheet()
    # style_title = ParagraphStyle(
    #     name='Title',
    #     fontSize=14,
    #     alignment=TA_CENTER,
    #     textColor=colors.white,
    #     backColor=colors.HexColor("#E87945"),
    #     spaceAfter=10
    # )
    # style_subtitle = ParagraphStyle(
    #     name='Subtitle',
    #     fontSize=15,
    #     alignment=0,
    #     textColor=colors.white,
    #     backColor=colors.HexColor("#0C9526"),
    #     spaceAfter=10
    # )
    style_footer = ParagraphStyle(
        name='Footer',
        fontSize=10,
        alignment=TA_CENTER,
        textColor=colors.black,
        spaceBefore=10
    )

    # Title
    # title = Paragraph("ANNEXE 4", style_title)
    # subtitle = Paragraph("SITUATION GEOGRAPHIQUE DES COMPAGNIES D’ASSURANCE", style_subtitle)
    footer = Paragraph("Source : Direction des Assurances", style_footer)

    # Draw title and subtitle
    # title.wrapOn(c, width, height)
    # title.drawOn(c, 0, height - 100)

    # subtitle.wrapOn(c, width - 50, 80)
    # subtitle.drawOn(c, 72, height - 150)

    # Draw image
    image_path = "images/map2.png"  # Chemin de l'image à ajouter
    c.drawImage(image_path, 72, height - 450, width - 144, height / 3)  # Ajuster la position et la taille selon vos besoins

    # Draw footer
    footer.wrapOn(c, width, height)
    footer.drawOn(c, 10, 370)

def draw_layout():
    c = canvas.Canvas("conjoncture_marche_ivoirien.pdf", pagesize=A4)
    width, height = A4

    # Définir les couleurs
    color_orange = HexColor('#FFA500')
    color_orange2 = HexColor("#F27B35")
    color_green = HexColor('#0C9526')
    color_white = HexColor('#FFFFFF')
    color_beige = HexColor('#FFE4C4')
    color_green2 = HexColor('#76A646')
    # #D0D3D4
    color_gray = HexColor('#D0D3D4')

    # Dessiner le fond vert
    c.setFillColor( color_white)
    c.rect(0, 0, width/2, height, fill=True, stroke=False)

    # Dessiner le fond orange
    c.setFillColor(color_white)
    c.rect(width/2, 0, width/2, height, fill=True, stroke=False)
    # Dessiner le triangle vert en haut à gauche
    path = c.beginPath()
    path.moveTo(200, height)  # Haut gauche de la page
    path.lineTo(0, height - 85)  # Descend verticalement
    path.lineTo(30, height)  # Diagonale vers le haut
    path.close()
    c.setFillColor(color_green)
    c.drawPath(path, fill=1, stroke=0)
      # Draw the beige trapezoid
# Draw the beige trapezoid
    c.setFillColorRGB(0.99, 0.94, 0.88)  # Beige color
    path = c.beginPath()
    path.moveTo(0, 0)
    path.lineTo(70, 0)
    path.lineTo(480, 160)
    path.lineTo(0, height-28)
    path.close()
    c.drawPath(path, fill=1, stroke=0)


#     # Dessiner un triangle blanc
#     path = c.beginPath()  # Démarre un nouveau chemin
#     path.moveTo(width/2, height*0.8)  # Déplace le crayon au point de départ du triangle
#     path.lineTo(width*0.48, height)  # Trace une ligne jusqu'à ce point
#     path.lineTo(width*0.52, height)  # Trace une ligne jusqu'à ce point
#     path.close()  # Ferme le chemin pour compléter le triangle
    #c.setFillColor(color_white)
    c.drawPath(path, fill=1, stroke=0)
    c.drawImage("images/image060-removebg-preview (1).png", width - 240, height - 120,  width=110, height=100)
    c.setFont("Times-Roman", 14)
    c.setFillColor(HexColor('#000000'))
    c.drawString(width - 260, height - 140, "MINISTÈRE DES FINANCES ")
    #ET DU BUDGET
    #image061.png
    c.drawString(width - 230, height - 156, "ET DU BUDGET ")
    c.setFont("Times-Bold", 16)
    c.drawString(width - 235, height - 180, "- - - - - - - - - - - ")
    c.setFont("Times-Roman", 14)
    c.drawString(width - 280, height - 200, "DIRECTION GÉNÉRALE DU TRÉSOR")
    c.drawString(width - 283, height - 215, "ET DE LA COMPTABILITÉ PUBLIQUE")
#     c.setFillColor(HexColor('#000000'))
    c.setFont("Times-Bold", 16)
    c.drawString(width - 235, height - 230, "- - - - - - - - - - - ")
    c.setFont("Times-Roman", 14)
    c.drawString(width - 270, height - 250, "DIRECTION DES ASSURANCES")
    c.drawImage("images/image061-removebg-preview.png", width - 230, height - 400,  width=120, height=120)
    
#     c.setFont("Times-Bold", 18)
#     c.drawString(width - 80, height - 300, "NOTE DE CONJONCTURE")
#     c.drawString(width - 90, height - 325, "DU MARCHÉ IVOIRIEN")
#     c.drawString(width - 94, height - 350, "DES ASSURANCES")

#     # Ajouter du texte
#     #c.setFont("Bahnschrift Light", 14)
#     c.setFillColor(HexColor('#000000'))
#     c.drawString(72, height - 180, "DIRECTION GÉNÉRALE DU TRÉSOR")
#     c.drawString(72, height - 140, "ET DE LA COMPTABILITÉ PUBLIQUE")
#     c.setFont("Times-Bold", 16)
#     c.drawString(width - 190, height - 220, "- - - - - - - - - - ")
#     c.drawString(72, height - 160, "DIRECTION DES ASSURANCES")
#     # Assurez-vous d'avoir un logo valide pour l'utiliser ici

    color_beige = HexColor('#FFE4C4')  # Couleur beige pour le fond

#     # Dimensions et positions des éléments de texte
#     text_x = 72
#     text_y_start = height - 500
#     line_height = 25

#     # Calculer la hauteur totale du bloc de texte
#     num_lines = 10  # Nombre de lignes de texte
#     block_height = num_lines * line_height + 10

#     # Dessiner le rectangle beige derrière le texte
#     c.setFillColor(color_beige)
#     c.rect(text_x - 10, text_y_start - block_height + line_height, 300, block_height, fill=1, stroke=0)
    # Dessiner le fond beige pour le texte
#     path = c.beginPath()
#     path.moveTo(60, height - 250)
#     path.lineTo(60, height - 550)
#     path.lineTo(300, height - 550)
#     path.lineTo(60, height - 250)
#     path.close()
#     c.setFillColor(color_beige)
#     c.drawPath(path, fill=1, stroke=0)

    c.setFont("Times-Bold", 24)
    c.drawString(72, height - 500, "NOTE DE")
    c.drawString(72, height - 525, "CONJONCTURE")
    c.drawString(72, height - 550, "DU MARCHÉ IVOIRIEN")
    c.drawString(72, height - 575, "DES ASSURANCES")
    #Capture d'écran 2024-05-14 114527-Photoroom.png
    # c.drawImage("images/Capture d'écran 2024-05-14 114527-Photoroom.png", width - 100, height - 1000,  width=150, height=150)
    c.drawImage("images/Afaq_9001-fond-blanc-1-440x430-removebg-preview.png", width - 180, height - 860,  width=150, height=150)
    # Définir la couleur et la largeur de la ligne orange
    c.setStrokeColorRGB(1, 0.5, 0)  # Couleur orange
    c.setLineWidth(2)
# Coordonner la figure avec la ligne orange
 
    x1, y1 = 25, height - 860
    x2, y2 = width - 30, 190

    # Dessiner la ligne orange
    c.line(x1, y1, x2, y2)
# Dessiner le triangle vert en bas à gauche
    path = c.beginPath()
    path.moveTo(0, 0)  # Point bas gauche
    path.lineTo(0, height / 10)  # Point haut gauche du triangle
    path.lineTo(width / 10, 0)  # Point bas droit du triangle
    path.close()
    c.setFillColor(color_green)
    c.drawPath(path, fill=1, stroke=0)
  # Dessiner la figure orange en haut à gauche du triangle vert
    path = c.beginPath()
    path.moveTo(0, height / 2)  # Commence en haut à gauche du triangle vert
    path.lineTo(0, height)  # Haut gauche de la page
    path.lineTo(35, height)  # Déplacement à droite en haut de la page
    path.lineTo(0, height /20 + 20)  # Retourne vers le bas pour former la pointe
    path.close()
    c.setFillColor(color_orange)
    c.drawPath(path, fill=1, stroke=0)
    
   # Dessiner le design vert
    path = c.beginPath()
    path.moveTo(35, height)  # Commence à droite en haut de la figure orange
    path.lineTo(35, height )  # Descend un peu
    path.lineTo(width * 0.5, height * 10)  # Pointe du triangle vert
    path.lineTo(width * 0.35, height)  # Remonte à droite
    path.close()
    c.setFillColor(color_green)
    c.drawPath(path, fill=1, stroke=0)

    
    # Définir les couleurs
    color_green = HexColor('#008000')

     # Dessiner le triangle vert en haut à droite
    path = c.beginPath()
    path.moveTo(width, 0)  # Point en bas à droite de la page
    path.lineTo(width, height-50)  # Point en haut à droite de la page
    path.lineTo(width - 40, 0)  # Point à gauche en bas
    path.close()
    c.setFillColor(color_green)
    c.drawPath(path, fill=1, stroke=0)
   # Position et dimensions du rectangle
    rect_x = 70
    rect_y = height - 630
    rect_width = 288
    rect_height = 36
# Dessiner le rectangle avec bordure orange
    c.setStrokeColor(color_orange)
    c.setLineWidth(2)
    c.setFillColor(color_orange)
    c.rect(rect_x, rect_y, rect_width, rect_height, fill=1)

    # Écrire le texte à l'intérieur du rectangle
    c.setFillColorRGB(1, 1, 1)  # Texte en blanc pour contraster avec l'orange
    c.setFont("Times-Bold", 24)
    text_x = rect_x + 10
    text_y = rect_y + 15  # Ajuster pour centrer verticalement
    c.drawString(text_x, text_y, "3ÈME TRIMESTRE 2023")
    #   # Position et dimensions de l'image
    # img_x = width - 160
    # img_y = 50
    #  # Dessiner le tracer orange
    # c.setStrokeColor(color_orange)
    # c.setLineWidth(2)
    
    # # Définir le chemin pour le tracer orange
    # path = c.beginPath()
    # path.moveTo(img_x, img_y + 180)  # Commence au-dessus de l'image
    # path.lineTo(width, 0)  # Descend jusqu'à la fin de la page

    # c.drawPath(path, fill=0, stroke=1)
    # c.translate(inch,inch) #starting point of coordinate to one inch
    # c.setStrokeColorRGB(1,0,0) # red colour of line
    # c.setLineWidth(4) #width of the line 
    # c.line(0,8*inch,5*inch,4*inch) # draw line 
    #c.rotate(-180)
    #Afaq_9001-fond-blanc-1-440x430-removebg-preview.png
   # Couleur de la ligne
    #orange_color = HexColor('#FFA500')  # Code couleur hexadécimal pour l'orange


#     #c.drawString(72, height - 575, "3ÈME TRIMESTRE 2023")
#     # Draw the orange line
#     c.setStrokeColorRGB(1, 0.6, 0)  # Orange color
#     c.setLineWidth(2)  # Line width
#     c.line(3, 0, width, height)  # Draw line from bottom-left to top-right
# Commencer une nouvelle page
    c.showPage()
    
    # Placer l'image comme arrière-plan de la deuxième page
    c.drawImage("images/RAPPORT ASSURANCE_ VF_121223-3.jpg", 0, 0, width=width, height=height)

    # Ajouter d'autres éléments sur la deuxième page si nécessaire
    # ... votre code pour la deuxième page ...
    # Commencez une nouvelle page pour la troisième page
    c.showPage()

#     # Définir les couleurs
#     color_orange = HexColor('#FF6F00')
#     color_white = HexColor('#FFFFFF')
    color_silver = HexColor("#EAEDED ")
    
#     # Ajouter un fond orange pour l'en-tête
#     c.setFillColor(color_orange)
#     c.rect(0, height - 100, width, 100, fill=True, stroke=False)

#     # Ajouter le texte de l'en-tête en blanc
#     c.setFillColor(color_white)
#     c.setFont("Helvetica-Bold", 18)
#     c.drawCentredString(width / 2, height - 70, "NOTE DE CONJONCTURE 3EME TRIMESTRE DU MARCHÉ IVOIRIEN DES ASSURANCES")

    # Ajouter le texte de l'introduction
    #image006.gif
    # Écrire le texte à l'intérieur du rectangle
    # c.setFillColor('black') # Texte en blanc pour contraster avec l'orange
    # c.setFont("Times-Bold", 10)
    # text_x = rect_x + 40
    # text_y = rect_y + 60  # Ajuster pour centrer verticalement
    # c.drawString(text_x, text_y, "NOTE DE CONJONCTURE 3EME TRIMESTRE DU MARCHÉ IVOIRIEN DES ASSURANCES")
    c.drawImage("images/1.png", width - 180, height -51.2,  width=146, height=18)
    # Définir la taille et la position du rectangle gris clair
    rect_x = 65
    rect_y = height - 50
    rect_width = 345
    rect_height = 14

    # Dessiner le rectangle gris clair
    c.setFillColor(color_silver)
    c.rect(rect_x, rect_y, rect_width, rect_height, fill=True, stroke=False)

    # Ajouter le texte centré
    text = "NOTE DE CONJONCTURE 3EME TRIMESTRE DU MARCHÉ IVOIRIEN DES ASSURANCES"
    c.setFont("Helvetica-Bold", 8)
    c.setFillColorRGB(0, 0, 0)
    text_x = 238
    text_y = rect_y + rect_height / 4  # Ajustement vertical pour centrer le texte
    c.drawCentredString(text_x, text_y, text)
    c.setFillColor('black')
    c.setFont("Times-Bold", 14)
    c.drawString(width - 566, height - 90, "INTRODUCTION")
#     text_object = c.beginText(50, height - 150)
#     text_object.textLines("""
# L'industrie de l’assurance joue un rôle clé dans la stabilité économique et financière d’un pays. Elle offre non seulement une protection financière aux individus et aux entreprises face à une multitude de risques, mais elle contribue aussi de manière significative à la formation du capital et à l’investissement à long terme.

# Chaque trimestre, la dynamique du marché des assurances connaît des évolutions en fonction des conditions économiques, des changements réglementaires, des tendances technologiques et des comportements des consommateurs. Cette note de conjoncture vise à dresser un aperçu des principales activités qui ont marqué le secteur des assurances au cours du troisième trimestre 2023. Elle s’attache à présenter les chiffres clés, les tendances émergentes, afin de fournir aux parties prenantes une vue claire et actualisée du marché.
# """)
#     c.drawText(text_object)
    c.showPage()
    # Couleurs
    orange = HexColor("#F57E37")
    white = HexColor("#FFFFFF")
    grey = HexColor("#F0F0F0")

    # Dessiner le fond orange pour la section de gauche
    c.setFillColor(orange)
    c.rect(0, 0, 2.5 * inch, height, fill=True, stroke=False)
    
     # Définir les dimensions et la position du carré blanc
    square_size = 5.6  # Taille du carré en points
    x_position = 12  # Position X du coin inférieur gauche du carré
    y_position = height - 176 # Position Y du coin inférieur gauche du carré
    
     # Définir la couleur de remplissage en blanc
    c.setFillColorRGB(1, 1, 1)
    # Dessiner le carré blanc
    c.rect(x_position, y_position, square_size, square_size, fill=1, stroke=0)

    # Ajouter le texte de la section gauche
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(0.3 * inch, height - 2.5 * inch, "FORMATION :")
    c.setFont("Helvetica", 70)
    c.drawString(0.5 * inch, height - 3.33 * inch, "02")
    
    # Définir les dimensions et la position du carré blanc
    square_size = 5.6  # Taille du carré en points
    x_position = 12  # Position X du coin inférieur gauche du carré
    y_position = height - 281.8 # Position Y du coin inférieur gauche du carré
    
     # Définir la couleur de remplissage en blanc
    c.setFillColorRGB(1, 1, 1)
    # Dessiner le carré blanc
    c.rect(x_position, y_position, square_size, square_size, fill=1, stroke=0)

    c.setFont("Helvetica-Bold", 18)
    c.drawString(0.3 * inch, height - 4 * inch, "RENCONTRES :")
    c.setFont("Helvetica", 70)
    c.drawString(0.5 * inch, height - 5 * inch, "02")
    
        
    # Définir les dimensions et la position du carré blanc
    square_size = 5.6  # Taille du carré en points
    x_position = 12  # Position X du coin inférieur gauche du carré
    y_position = height - 402 # Position Y du coin inférieur gauche du carré
    
     # Définir la couleur de remplissage en blanc
    c.setFillColorRGB(1, 1, 1)
    # Dessiner le carré blanc
    c.rect(x_position, y_position, square_size, square_size, fill=1, stroke=0)

    c.setFont("Times-Bold", 18)
    c.drawString(0.3 * inch, height - 5.6 * inch, "AGREMENTS :")
    c.setFont("Times-Roman", 15)
    c.drawString(0.36 * inch, height - 5.9 * inch, "Courtiers")
    c.setFont("Times-Roman", 70)
    c.drawString(0.38 * inch, height - 6.69 * inch, "07")
    c.setFont("Times-Roman", 15)
    c.drawString(0.36 * inch, height - 7.2 * inch, "Cartes professionnelles")
    c.setFont("Times-Roman", 70)
    c.drawString(0.40 * inch, height - 8.15 * inch, "260")
    
    
     # Définir les dimensions et la position du carré blanc
    square_size = 5.6  # Taille du carré en points
    x_position = 17  # Position X du coin inférieur gauche du carré
    y_position = height - 630.5 # Position Y du coin inférieur gauche du carré
    
     # Définir la couleur de remplissage en blanc
    c.setFillColorRGB(1, 1, 1)
    # Dessiner le carré blanc
    c.rect(x_position, y_position, square_size, square_size, fill=1, stroke=0)

    c.setFont("Times-Bold", 18)
    c.drawString(0.3 * inch, height - 8.8 * inch, " CONTRÔLE :")
    c.setFont("Times-Roman", 70)
    c.drawString(0.38 * inch, height - 9.7 * inch, "08")
    c.setFont("Times-Roman", 15)
    c.drawString(0.44 * inch, height - 9.99 * inch, "Sociétés")
    
    # Définir les dimensions et la position du carré blanc
    square_size = 5.6  # Taille du carré en points
    x_position = 13  # Position X du coin inférieur gauche du carré
    y_position = height - 745 # Position Y du coin inférieur gauche du carré
    
     # Définir la couleur de remplissage en blanc
    c.setFillColorRGB(1, 1, 1)
    # Dessiner le carré blanc
    c.rect(x_position, y_position, square_size, square_size, fill=1, stroke=0)

    c.setFont("Times-Bold", 18)
    c.drawString(0.3 * inch, height - 10.4 * inch, "SANCTIONS :")
    c.setFont("Times-Roman", 70)
    c.drawString(0.38 * inch, height - 11.3 * inch, "00")

   # Ajouter le titre de la section principale
   # 
    c.setFillColor(orange)
    c.rect(2.5 * inch, height - 1.48 * inch, width - 2.5 * inch, 3* inch, fill=True, stroke=False)
    c.setFillColor(white)
    c.setFont("Times-Bold", 25)
    c.drawString(2.6 * inch, height - 0.77 * inch, "I. ACTUALITÉS DU MARCHÉ")
    # Draw the curved lines
    draw_curved_lines(c, width, height)
    c.drawImage("images/18.png", width - 444, height - 834,  width=45, height=45)
    # Définir la couleur orange (approximation, utilisez l'outil pipette pour précision)
    orange_rgb = (243, 112, 33)  # R: 243, G: 112, B: 33 (approximation)

    # Définir la couleur de la ligne à orange
    c.setStrokeColorRGB(orange_rgb[0]/255, orange_rgb[1]/255, orange_rgb[2]/255)
    c.setLineWidth(0.5)  # Définir l'épaisseur de la ligne (ajustez si nécessaire)

    # Dessiner la ligne orange (ajustez les coordonnées pour correspondre à l'image)
    x1 = 520
    x2 = width - 395
    y = 25 # Position verticale (ajustez pour correspondre à l'image)
    
    c.drawImage("images/modified_image1.png", width - 600, height - 92,  width=180, height=90)

    c.line(x1, y, x2, y)
    # Define dimensions
    footer_height = 0.4 * inch
    margin = 0.9 * inch
    line_thickness = 0.1 * inch
    right_bar_width = 0.3 * inch
    
# #c.translate(inch,inch) #starting point of coordinate to one inch
#     c.setStrokeColorRGB(1,0,0) # red colour of line
#     c.setLineWidth(0.1) #width of the line 
#     c.line(0,8*inch,4*inch,5*inch) # draw line 
 
    # # c.line(0,0,0,1.7*inch)
    # c.line(0,0,1*inch,0)

    # Draw the orange line at the bottom
    c.setFillColor(orange)
    # c.rect(margin, footer_height, width - 2 * margin - 8, line_thickness- 8, fill=True, stroke=False)
    
    # Draw the right orange bar with number
    c.rect(width - margin - right_bar_width, 0, right_bar_width, footer_height + line_thickness, fill=True, stroke=False)
    c.setFillColor(white)
    c.setFont("Times-Bold", 12)
    c.drawCentredString(width - margin - right_bar_width / 2, footer_height / 2 + line_thickness / 2 - 3, "1")

    # Draw the centered text
    c.setFillColor(black)
    c.setFont("Times-Roman", 7.5)
    c.drawCentredString(width / 1.70, footer_height / 2 + line_thickness / 2 - 3, "NOTE DE CONJONCTURE 3EME TRIMESTRE DU MARCHÉ IVOIRIEN DES ASSURANCES")

 
    
    c.showPage()
    
    
    
    
    
    
    
    #c.setFillColor(color_white)
    
    # Définir la taille et la position du rectangle gris clair
    rect_x = 196
    rect_y = height - 50
    rect_width = 345
    rect_height = 14

    # Dessiner le rectangle gris clair
    c.setFillColor(color_silver)
    c.rect(rect_x, rect_y, rect_width, rect_height, fill=True, stroke=False)

    # Ajouter le texte centré
    text = "NOTE DE CONJONCTURE 3EME TRIMESTRE DU MARCHÉ IVOIRIEN DES ASSURANCES"
    c.setFont("Helvetica-Bold", 8)
    c.setFillColorRGB(0, 0, 0)
    text_x = 368
    text_y = rect_y + rect_height / 4  # Ajustement vertical pour centrer le texte
    c.drawCentredString(text_x, text_y, text)
    
    c.drawImage("images/2.png", width - 548, height -51,  width=146, height=18)
    c.setFont("Times-Bold", 14)
    c.setFont("Times-Bold", 13)
    c.drawString(width - 560, height - 80, "Rencontres:")
    c.drawImage("images/image053.png", 0, 70, 0, height=height)
   # Chemin vers votre image
    image_path = "images/image068-removebg-preview.png"
    image_width = 50  # Largeur de l'image
    image_height = 23  # Hauteur de l'image

    # Dupliquer l'image jusqu'à la fin de la page
    image_x = width - 56  # Position X de l'image
    for y in range(0, int(height), image_height):
        c.drawImage(image_path, image_x, y, width=image_width, height=image_height)
       # Définir la couleur de la ligne
    ## Définir l'épaisseur et la couleur de la ligne
    c.setLineWidth(4)  # Épaisseur de la ligne
    c.setStrokeColorRGB(1, 0.5, 0)  # Orange

    # Dessiner la ligne verticale le long du bord droit de la page
    c.line(width, 0, width, height)
    # Ajouter l'image
    # c.drawImage("images/Capture_d_écran_2024-05-17_201729-removebg-preview.png", width - 100, height - 200, width=200, height=100)

    #image053.png
    
    # Draw the orange line at the bottom
    c.setFillColor(orange)
    # c.rect(margin, footer_height, width - 2 * margin - 8, line_thickness- 8, fill=True, stroke=False)
    
    # Draw the right orange bar with number
    c.rect(width - margin - right_bar_width, 0, right_bar_width, footer_height + line_thickness, fill=True, stroke=False)
    c.setFillColor(white)
    c.setFont("Times-Bold", 12)
    c.drawCentredString(width - margin - right_bar_width / 2, footer_height / 2 + line_thickness / 2 - 3, "2")

    # Draw the centered text
    c.setFillColor(black)
    c.setFont("Times-Roman", 8.5)
    c.drawCentredString(width / 1.97, footer_height / 2 + line_thickness / 2 - 3, "NOTE DE CONJONCTURE 3EME TRIMESTRE DU MARCHÉ IVOIRIEN DES ASSURANCES")
    
    c.drawImage("images/image061-removebg-preview.png", width - 502, height - 834,  width=32, height=32)
    
    # Définir la couleur orange (approximation, utilisez l'outil pipette pour précision)
    orange_rgb = (243, 112, 33)  # R: 243, G: 112, B: 33 (approximation)

    # Définir la couleur de la ligne à orange
    c.setStrokeColorRGB(orange_rgb[0]/255, orange_rgb[1]/255, orange_rgb[2]/255)
    c.setLineWidth(0.7)  # Définir l'épaisseur de la ligne (ajustez si nécessaire)
    
    # Dessiner la ligne orange (ajustez les coordonnées pour correspondre à l'image)
    x1 = 520
    x2 = width - 466.5
    y = 25 # Position verticale (ajustez pour correspondre à l'image)
    
    c.line(x1, y, x2, y)
    
    
    
    c.showPage()
    
     # Couleurs
    orange = HexColor("#F57E37")
    white = HexColor("#FFFFFF")
    grey = HexColor("#F0F0F0")

    # Dessiner le fond orange pour la section de gauche
    c.setFillColor(orange)
    c.rect(0, 0, 2.5 * inch, height, fill=True, stroke=False)
    
     # Définir les dimensions et la position du carré blanc
    square_size = 5.6  # Taille du carré en points
    x_position = 12  # Position X du coin inférieur gauche du carré
    y_position = height - 165 # Position Y du coin inférieur gauche du carré
    
     # Définir la couleur de remplissage en blanc
    c.setFillColorRGB(1, 1, 1)
    # Dessiner le carré blanc
    c.rect(x_position, y_position, square_size, square_size, fill=1, stroke=0)

    # Ajouter le texte de la section gauche
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.3 * inch, height - 2.3 * inch, "NOMBRE DE ")
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.3 * inch, height - 2.5 * inch, "SOCIÉTÉS:")
    # SOCIÉTÉS
    c.setFont("Helvetica", 60)
    c.drawString(0.22 * inch, height - 3.2 * inch, "35")
    
    # # Définir les dimensions et la position du carré blanc
    # square_size = 5.6  # Taille du carré en points
    # x_position = 12  # Position X du coin inférieur gauche du carré
    # y_position = height - 269 # Position Y du coin inférieur gauche du carré
    
    #  # Définir la couleur de remplissage en blanc
    # c.setFillColorRGB(1, 1, 1)
    # # Dessiner le carré blanc
    # c.rect(x_position, y_position, square_size, square_size, fill=1, stroke=0)

    c.setFont("Helvetica-Bold", 14)
    c.drawString(0.4 * inch, height - 3.5* inch, "VIE")
    c.setFont("Helvetica", 60)
    c.drawString(0.25 * inch, height - 4.2 * inch, "12")
    
    
    c.setFont("Helvetica-Bold", 14)
    c.drawString(0.4 * inch, height - 4.5* inch, " NON VIE")
    c.setFont("Helvetica", 60)
    c.drawString(0.34 * inch, height - 5.2 * inch, "23")
    
    
     # Définir les dimensions et la position du carré blanc
    square_size = 5.6  # Taille du carré en points
    x_position = 15  # Position X du coin inférieur gauche du carré
    y_position = height - 396 # Position Y du coin inférieur gauche du carré
    
     # Définir la couleur de remplissage en blanc
    c.setFillColorRGB(1, 1, 1)
    # Dessiner le carré blanc
    c.rect(x_position, y_position, square_size, square_size, fill=1, stroke=0)

    # Ajouter le texte de la section gauche
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.34 * inch, height - 5.55 * inch, "NOMBRE DE ")
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.34 * inch, height - 5.8 * inch, "COURTIERS:")
    # # SOCIÉTÉS
    c.setFont("Helvetica", 60)
    c.drawString(0.22 * inch, height - 6.5 * inch, "327")
    
    # Définir les dimensions et la position du carré blanc
    square_size = 5.6  # Taille du carré en points
    x_position = 17  # Position X du coin inférieur gauche du carré
    y_position = height - 495 # Position Y du coin inférieur gauche du carré
    
     # Définir la couleur de remplissage en blanc
    c.setFillColorRGB(1, 1, 1)
    # Dessiner le carré blanc
    c.rect(x_position, y_position, square_size, square_size, fill=1, stroke=0)

    # Ajouter le texte de la section gauche
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.34 * inch, height - 6.88 * inch, "CHIFFRE D'AFFAIRE :")
    c.setFont("Helvetica", 45)
    c.drawString(0.22 * inch, height - 7.5* inch, "127,01")
    c.setFont("Helvetica", 16)
    c.drawString(0.35 * inch, height - 7.8* inch, "Milliards")
    
    # Définir les dimensions et la position du carré blanc
    square_size = 5.6  # Taille du carré en points
    x_position = 17  # Position X du coin inférieur gauche du carré
    y_position = height - 582 # Position Y du coin inférieur gauche du carré
    
     # Définir la couleur de remplissage en blanc
    c.setFillColorRGB(1, 1, 1)
    # Dessiner le carré blanc
    c.rect(x_position, y_position, square_size, square_size, fill=1, stroke=0)

    # Ajouter le texte de la section gauche
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.34 * inch, height - 8.1 * inch, "EVOLUTION PAR ")
    c.setFont("Helvetica", 13)
    c.drawString(0.34 * inch, height - 8.3* inch, "RAPPORT A T2 2022 ")
    c.setFont("Helvetica", 40)
    c.drawString(0.24 * inch, height - 8.9* inch, "-1,76%")
    
    
    # Définir les dimensions et la position du carré blanc
    square_size = 5.6  # Taille du carré en points
    x_position = 17  # Position X du coin inférieur gauche du carré
    y_position = height - 666# Position Y du coin inférieur gauche du carré
    
     # Définir la couleur de remplissage en blanc
    c.setFillColorRGB(1, 1, 1)
    # Dessiner le carré blanc
    c.rect(x_position, y_position, square_size, square_size, fill=1, stroke=0)

    # Ajouter le texte de la section gauche
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.34 * inch, height - 9.3 * inch, "PRESTATION ET")
    c.setFont("Helvetica", 13)
    c.drawString(0.34 * inch, height - 9.5* inch, "SINISTRE PAYES T2:")
    c.setFont("Helvetica", 34)
    c.drawString(0.34 * inch, height - 10* inch, "72,84")
    
      # Définir les dimensions et la position du carré blanc
    square_size = 5.6  # Taille du carré en points
    x_position = 17  # Position X du coin inférieur gauche du carré
    y_position = height - 745 # Position Y du coin inférieur gauche du carré
    
     # Définir la couleur de remplissage en blanc
    c.setFillColorRGB(1, 1, 1)
    # Dessiner le carré blanc
    c.rect(x_position, y_position, square_size, square_size, fill=1, stroke=0)

    # Ajouter le texte de la section gauche
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(0.34 * inch, height - 10.4 * inch, "EVOLUTION PAR ")
    c.setFont("Helvetica", 12)
    c.drawString(0.34 * inch, height - 10.6* inch, "RAPPORT A T2 2022 ")
    c.setFont("Helvetica", 34)
    c.drawString(0.24 * inch, height - 11.1* inch, "+17,62%")
    
        
    # # Définir les dimensions et la position du carré blanc
    # square_size = 5.6  # Taille du carré en points
    # x_position = 12  # Position X du coin inférieur gauche du carré
    # y_position = height - 402 # Position Y du coin inférieur gauche du carré
    
    #  # Définir la couleur de remplissage en blanc
    # c.setFillColorRGB(1, 1, 1)
    # # Dessiner le carré blanc
    # c.rect(x_position, y_position, square_size, square_size, fill=1, stroke=0)

    # c.setFont("Times-Bold", 18)
    # c.drawString(0.3 * inch, height - 5.6 * inch, "AGREMENTS :")
    # c.setFont("Times-Roman", 15)
    # c.drawString(0.36 * inch, height - 5.9 * inch, "Courtiers")
    # c.setFont("Times-Roman", 70)
    # c.drawString(0.38 * inch, height - 6.69 * inch, "07")
    # c.setFont("Times-Roman", 15)
    # c.drawString(0.36 * inch, height - 7.2 * inch, "Cartes professionnelles")
    # c.setFont("Times-Roman", 70)
    # c.drawString(0.40 * inch, height - 8.15 * inch, "260")
    
    
    #  # Définir les dimensions et la position du carré blanc
    # square_size = 5.6  # Taille du carré en points
    # x_position = 17  # Position X du coin inférieur gauche du carré
    # y_position = height - 630.5 # Position Y du coin inférieur gauche du carré
    
    #  # Définir la couleur de remplissage en blanc
    # c.setFillColorRGB(1, 1, 1)
    # # Dessiner le carré blanc
    # c.rect(x_position, y_position, square_size, square_size, fill=1, stroke=0)

    # c.setFont("Times-Bold", 18)
    # c.drawString(0.3 * inch, height - 8.8 * inch, " CONTRÔLE :")
    # c.setFont("Times-Roman", 70)
    # c.drawString(0.38 * inch, height - 9.7 * inch, "08")
    # c.setFont("Times-Roman", 15)
    # c.drawString(0.44 * inch, height - 9.99 * inch, "Sociétés")
    
    # # Définir les dimensions et la position du carré blanc
    # square_size = 5.6  # Taille du carré en points
    # x_position = 13  # Position X du coin inférieur gauche du carré
    # y_position = height - 745 # Position Y du coin inférieur gauche du carré
    
    #  # Définir la couleur de remplissage en blanc
    # c.setFillColorRGB(1, 1, 1)
    # # Dessiner le carré blanc
    # c.rect(x_position, y_position, square_size, square_size, fill=1, stroke=0)

    # c.setFont("Times-Bold", 18)
    # c.drawString(0.3 * inch, height - 10.4 * inch, "SANCTIONS :")
    # c.setFont("Times-Roman", 70)
    # c.drawString(0.38 * inch, height - 11.3 * inch, "00")

   # Ajouter le titre de la section principale
   # 
    c.setFillColor(orange)
    c.rect(2.5 * inch, height - 1.48 * inch, width - 2.5 * inch, 3* inch, fill=True, stroke=False)
    c.setFillColor(white)
    c.setFont("Times-Bold", 25)
    c.drawString(2.6 * inch, height - 0.70 * inch, "II. CHIFFRE DU SECTEUR")
    c.setFillColor(white)
    c.setFont("Times-Bold", 25)
    c.drawString(2.6 * inch, height - 1.1 * inch, "DE L'ASSURANCES")
    # Draw the curved lines
    draw_curved_lines(c, width, height)
    c.drawImage("images/18.png", width - 444, height - 834,  width=45, height=45)
    # Définir la couleur orange (approximation, utilisez l'outil pipette pour précision)
    orange_rgb = (243, 112, 33)  # R: 243, G: 112, B: 33 (approximation)

    # Définir la couleur de la ligne à orange
    c.setStrokeColorRGB(orange_rgb[0]/255, orange_rgb[1]/255, orange_rgb[2]/255)
    c.setLineWidth(0.5)  # Définir l'épaisseur de la ligne (ajustez si nécessaire)

    # Dessiner la ligne orange (ajustez les coordonnées pour correspondre à l'image)
    x1 = 520
    x2 = width - 395
    y = 25 # Position verticale (ajustez pour correspondre à l'image)
    
    c.drawImage("images/modified_image1.png", width - 600, height - 92,  width=180, height=90)

    c.line(x1, y, x2, y)
    # Define dimensions
    footer_height = 0.4 * inch
    margin = 0.9 * inch
    line_thickness = 0.1 * inch
    right_bar_width = 0.3 * inch
    
# #c.translate(inch,inch) #starting point of coordinate to one inch
#     c.setStrokeColorRGB(1,0,0) # red colour of line
#     c.setLineWidth(0.1) #width of the line 
#     c.line(0,8*inch,4*inch,5*inch) # draw line 
 
    # # c.line(0,0,0,1.7*inch)
    # c.line(0,0,1*inch,0)

    # Draw the orange line at the bottom
    c.setFillColor(orange)
    # c.rect(margin, footer_height, width - 2 * margin - 8, line_thickness- 8, fill=True, stroke=False)
    
    # Draw the right orange bar with number
    c.rect(width - margin - right_bar_width, 0, right_bar_width, footer_height + line_thickness, fill=True, stroke=False)
    c.setFillColor(white)
    c.setFont("Times-Bold", 12)
    c.drawCentredString(width - margin - right_bar_width / 2, footer_height / 2 + line_thickness / 2 - 3, "1")

    # Draw the centered text
    c.setFillColor(black)
    c.setFont("Times-Roman", 7.5)
    c.drawCentredString(width / 1.70, footer_height / 2 + line_thickness / 2 - 3, "NOTE DE CONJONCTURE 3EME TRIMESTRE DU MARCHÉ IVOIRIEN DES ASSURANCES")
    
   
  
 
    
    c.showPage()
    
    # Chemin vers votre image
    image_path = "images/image068-removebg-preview.png"
    image_width = 50  # Largeur de l'image
    image_height = 23  # Hauteur de l'image

    # Dupliquer l'image jusqu'à la fin de la page
    image_x = width - 56  # Position X de l'image
    for y in range(0, int(height), image_height):
        c.drawImage(image_path, image_x, y, width=image_width, height=image_height)
    # c.setFillColor(color_white)
    # Définir la taille et la position du rectangle gris clair
    rect_x = 196
    rect_y = height - 50
    rect_width = 345
    rect_height = 14

    # Dessiner le rectangle gris clair
    c.setFillColor(color_silver)
    c.rect(rect_x, rect_y, rect_width, rect_height, fill=True, stroke=False)

    # Ajouter le texte centré
    text = "NOTE DE CONJONCTURE 3EME TRIMESTRE DU MARCHÉ IVOIRIEN DES ASSURANCES"
    c.setFont("Helvetica-Bold", 8)
    c.setFillColorRGB(0, 0, 0)
    text_x = 368
    text_y = rect_y + rect_height / 4  # Ajustement vertical pour centrer le texte
    c.drawCentredString(text_x, text_y, text)
    
    c.drawImage("images/2.png", width - 548, height -51,  width=146, height=18)
    c.setFont("Times-Bold", 14)
    c.setFont("Times-Bold", 13)
    c.drawString(width - 560, height - 80, "•Prestations et sinistres payés")
    
    # Draw the orange line at the bottom
    c.setFillColor(orange)
    # c.rect(margin, footer_height, width - 2 * margin - 8, line_thickness- 8, fill=True, stroke=False)
    
    # Draw the right orange bar with number
    c.rect(width - margin - right_bar_width, 0, right_bar_width, footer_height + line_thickness, fill=True, stroke=False)
    c.setFillColor(white)
    c.setFont("Times-Bold", 12)
    c.drawCentredString(width - margin - right_bar_width / 2, footer_height / 2 + line_thickness / 2 - 3, "3")

    # Draw the centered text
    c.setFillColor(black)
    c.setFont("Times-Roman", 8.5)
    c.drawCentredString(width / 1.97, footer_height / 2 + line_thickness / 2 - 3, "NOTE DE CONJONCTURE 3EME TRIMESTRE DU MARCHÉ IVOIRIEN DES ASSURANCES")
    
    c.drawImage("images/image061-removebg-preview.png", width - 502, height - 834,  width=32, height=32)
    
    # Définir la couleur orange (approximation, utilisez l'outil pipette pour précision)
    orange_rgb = (243, 112, 33)  # R: 243, G: 112, B: 33 (approximation)

    # Définir la couleur de la ligne à orange
    c.setStrokeColorRGB(orange_rgb[0]/255, orange_rgb[1]/255, orange_rgb[2]/255)
    c.setLineWidth(0.7)  # Définir l'épaisseur de la ligne (ajustez si nécessaire)
    
    # Dessiner la ligne orange (ajustez les coordonnées pour correspondre à l'image)
    x1 = 520
    x2 = width - 466.5
    y = 25 # Position verticale (ajustez pour correspondre à l'image)
    
    c.line(x1, y, x2, y)
    
    c.showPage()
    
    # Définir la taille et la position du rectangle gris clair
    rect_x = 72
    rect_y = height - 50
    rect_width = 345
    rect_height = 14

    # Dessiner le rectangle gris clair
    c.setFillColor(color_silver)
    c.rect(rect_x, rect_y, rect_width, rect_height, fill=True, stroke=False)

    # Ajouter le texte centré
    text = "NOTE DE CONJONCTURE 3EME TRIMESTRE DU MARCHÉ IVOIRIEN DES ASSURANCES"
    c.setFont("Helvetica-Bold", 8)
    c.setFillColorRGB(0, 0, 0)
    text_x = 242
    text_y = rect_y + rect_height / 4  # Ajustement vertical pour centrer le texte
    c.drawCentredString(text_x, text_y, text)
    c.drawImage("images/1.png", width - 176, height -51,  width=146, height=18)
    c.setFont("Times-Bold", 14)
    c.drawString(width - 560, height - 80, "• Comparaison du cumul du CA des trois premiers trimestres 2022 et 2023 ")
    # Draw the orange line at the bottom
    c.setFillColor(orange)
    # c.rect(margin, footer_height, width - 2 * margin - 8, line_thickness- 8, fill=True, stroke=False)
    
    # Draw the right orange bar with number
    c.rect(width - margin - right_bar_width, 0, right_bar_width, footer_height + line_thickness, fill=True, stroke=False)
    c.setFillColor(white)
    c.setFont("Times-Bold", 12)
    c.drawCentredString(width - margin - right_bar_width / 2, footer_height / 2 + line_thickness / 2 - 3, "4")

    # Draw the centered text
    c.setFillColor(black)
    c.setFont("Times-Roman", 8.5)
    c.drawCentredString(width / 1.97, footer_height / 2 + line_thickness / 2 - 3, "NOTE DE CONJONCTURE 3EME TRIMESTRE DU MARCHÉ IVOIRIEN DES ASSURANCES")
    
    c.drawImage("images/image061-removebg-preview.png", width - 502, height - 834,  width=32, height=32)
    
    # Définir la couleur orange (approximation, utilisez l'outil pipette pour précision)
    orange_rgb = (243, 112, 33)  # R: 243, G: 112, B: 33 (approximation)

    # Définir la couleur de la ligne à orange
    c.setStrokeColorRGB(orange_rgb[0]/255, orange_rgb[1]/255, orange_rgb[2]/255)
    c.setLineWidth(0.7)  # Définir l'épaisseur de la ligne (ajustez si nécessaire)
    
    # Dessiner la ligne orange (ajustez les coordonnées pour correspondre à l'image)
    x1 = 520
    x2 = width - 466.5
    y = 25 # Position verticale (ajustez pour correspondre à l'image)
    
    c.line(x1, y, x2, y)
    
    c.showPage()
    
    
      
     # Couleurs
    orange = HexColor("#F57E37")
    white = HexColor("#FFFFFF")
    grey = HexColor("#F0F0F0")

    # Dessiner le fond orange pour la section de gauche
    c.setFillColor(orange)
    c.rect(0, 0, 2.5 * inch, height, fill=True, stroke=False)
    
     # Définir les dimensions et la position du carré blanc
    square_size = 5.6  # Taille du carré en points
    x_position = 12  # Position X du coin inférieur gauche du carré
    y_position = height - 165 # Position Y du coin inférieur gauche du carré
    
     # Définir la couleur de remplissage en blanc
    c.setFillColorRGB(1, 1, 1)
    # Dessiner le carré blanc
    c.rect(x_position, y_position, square_size, square_size, fill=1, stroke=0)

    # Ajouter le texte de la section gauche
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.3 * inch, height - 2.3 * inch, "CHIFFRE")
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.3 * inch, height - 2.5 * inch, "D'AFFAIRES T3")
    # SOCIÉTÉS
    c.setFont("Helvetica", 40)
    c.drawString(0.3 * inch, height - 3 * inch, "61,05")
    c.setFont("Helvetica", 14)
    c.drawString(0.34 * inch, height - 3.3 * inch, "Milliards")
    

    c.setFont("Helvetica-Bold", 14)
    c.drawString(0.3 * inch, height - 3.7* inch, "Evolution par")
    c.setFont("Helvetica", 14)
    c.drawString(0.3 * inch, height - 3.88 * inch, "rapport à T3 2023")
    c.setFont("Helvetica", 38)
    c.drawString(0.20 * inch, height - 4.4 * inch, "+11,57%")
    
    
    # Définir les dimensions et la position du carré blanc
    square_size = 5.6  # Taille du carré en points
    x_position = 12  # Position X du coin inférieur gauche du carré
    y_position = height - 342 # Position Y du coin inférieur gauche du carré
    
     # Définir la couleur de remplissage en blanc
    c.setFillColorRGB(1, 1, 1)
    # Dessiner le carré blanc
    c.rect(x_position, y_position, square_size, square_size, fill=1, stroke=0)

    # Ajouter le texte de la section gauche
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.3 * inch, height - 4.8 * inch, "PRESTATION")
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.3 * inch, height - 5 * inch, "PAYEES T3:")
    # # SOCIÉTÉS
    c.setFont("Helvetica", 40)
    c.drawString(0.3 * inch, height - 5.54 * inch, "41,81")
    c.setFont("Helvetica", 14)
    c.drawString(0.34 * inch, height - 5.8 * inch, "Milliards")
    
    c.setFont("Helvetica-Bold", 14)
    c.drawString(0.3 * inch, height - 6.1* inch, "EVOLUTION PAR")
    c.setFont("Helvetica", 14)
    c.drawString(0.3 * inch, height - 6.3* inch, "RAPPORT A T3 2022")
    c.setFont("Helvetica", 38)
    c.drawString(0.20 * inch, height - 6.8 * inch, "+19,32%")
    
    
    # Définir les dimensions et la position du carré blanc
    square_size = 5.6  # Taille du carré en points
    x_position = 12  # Position X du coin inférieur gauche du carré
    y_position = height - 515 # Position Y du coin inférieur gauche du carré
    
     # Définir la couleur de remplissage en blanc
    c.setFillColorRGB(1, 1, 1)
    # Dessiner le carré blanc
    c.rect(x_position, y_position, square_size, square_size, fill=1, stroke=0)

    # Ajouter le texte de la section gauche
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.3 * inch, height - 7.2 * inch, "PROVISIONS")
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.3 * inch, height - 7.4 * inch, "MATHEMATIQUES:")
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 40)
    c.drawString(0.3 * inch, height - 7.9* inch, "760,67")
    
    
    # Définir les dimensions et la position du carré blanc
    square_size = 5.6  # Taille du carré en points
    x_position = 12  # Position X du coin inférieur gauche du carré
    y_position = height - 602 # Position Y du coin inférieur gauche du carré
    
     # Définir la couleur de remplissage en blanc
    c.setFillColorRGB(1, 1, 1)
    # Dessiner le carré blanc
    c.rect(x_position, y_position, square_size, square_size, fill=1, stroke=0)

    # Ajouter le texte de la section gauche
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.3 * inch, height - 8.4 * inch, "NOMBRE DE CONTRATS")
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 40)
    c.drawString(0.3 * inch, height - 9 * inch, "357316")
    
    
     # Définir les dimensions et la position du carré blanc
    square_size = 5.6  # Taille du carré en points
    x_position = 12  # Position X du coin inférieur gauche du carré
    y_position = height - 680 # Position Y du coin inférieur gauche du carré
    
     # Définir la couleur de remplissage en blanc
    c.setFillColorRGB(1, 1, 1)
    # Dessiner le carré blanc
    c.rect(x_position, y_position, square_size, square_size, fill=1, stroke=0)

    # Ajouter le texte de la section gauche
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.3 * inch, height - 9.5 * inch, "EFFECTIF DU")
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.3 * inch, height - 9.7 * inch, "PERSONNEL T3")
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 40)
    c.drawString(0.3 * inch, height - 10.2 * inch, "836")
    

   # Ajouter le titre de la section principale
   # 
    c.setFillColor(orange)
    c.rect(2.5 * inch, height - 1.48 * inch, width - 2.5 * inch, 3* inch, fill=True, stroke=False)
    c.setFillColor(white)
    c.setFont("Times-Bold", 23)
    c.drawString(2.8 * inch, height - 0.70 * inch, "II.2. ASSURANCE VIE")
    # c.setFillColor(white)
    # c.setFont("Times-Bold", 25)
    # c.drawString(2.6 * inch, height - 1.1 * inch, "DE L'ASSURANCES")
    # Draw the curved lines
    draw_curved_lines(c, width, height)
    c.drawImage("images/18.png", width - 444, height - 834,  width=45, height=45)
    # Définir la couleur orange (approximation, utilisez l'outil pipette pour précision)
    orange_rgb = (243, 112, 33)  # R: 243, G: 112, B: 33 (approximation)

    # Définir la couleur de la ligne à orange
    c.setStrokeColorRGB(orange_rgb[0]/255, orange_rgb[1]/255, orange_rgb[2]/255)
    c.setLineWidth(0.5)  # Définir l'épaisseur de la ligne (ajustez si nécessaire)

    # Dessiner la ligne orange (ajustez les coordonnées pour correspondre à l'image)
    x1 = 520
    x2 = width - 395
    y = 25 # Position verticale (ajustez pour correspondre à l'image)
    
    c.drawImage("images/modified_image1.png", width - 600, height - 92,  width=180, height=90)

    c.line(x1, y, x2, y)
    # Define dimensions
    footer_height = 0.4 * inch
    margin = 0.9 * inch
    line_thickness = 0.1 * inch
    right_bar_width = 0.3 * inch
    
# #c.translate(inch,inch) #starting point of coordinate to one inch
#     c.setStrokeColorRGB(1,0,0) # red colour of line
#     c.setLineWidth(0.1) #width of the line 
#     c.line(0,8*inch,4*inch,5*inch) # draw line 
 
    # # c.line(0,0,0,1.7*inch)
    # c.line(0,0,1*inch,0)

    # Draw the orange line at the bottom
    c.setFillColor(orange)
    # c.rect(margin, footer_height, width - 2 * margin - 8, line_thickness- 8, fill=True, stroke=False)
    
    # Draw the right orange bar with number
    c.rect(width - margin - right_bar_width, 0, right_bar_width, footer_height + line_thickness, fill=True, stroke=False)
    c.setFillColor(white)
    c.setFont("Times-Bold", 12)
    c.drawCentredString(width - margin - right_bar_width / 2, footer_height / 2 + line_thickness / 2 - 3, "1")

    # Draw the centered text
    c.setFillColor(black)
    c.setFont("Times-Roman", 7.5)
    c.drawCentredString(width / 1.70, footer_height / 2 + line_thickness / 2 - 3, "NOTE DE CONJONCTURE 3EME TRIMESTRE DU MARCHÉ IVOIRIEN DES ASSURANCES")
    
   
  
 
    
    c.showPage()
    
    
     # Couleurs
    orange = HexColor("#F57E37")
    white = HexColor("#FFFFFF")
    grey = HexColor("#F0F0F0")

    # Dessiner le fond orange pour la section de gauche
    c.setFillColor(orange)
    c.rect(0, 0, 2.5 * inch, height, fill=True, stroke=False)
    
     # Définir les dimensions et la position du carré blanc
    square_size = 5.6  # Taille du carré en points
    x_position = 12  # Position X du coin inférieur gauche du carré
    y_position = height - 165 # Position Y du coin inférieur gauche du carré
    
     # Définir la couleur de remplissage en blanc
    c.setFillColorRGB(1, 1, 1)
    # Dessiner le carré blanc
    c.rect(x_position, y_position, square_size, square_size, fill=1, stroke=0)

    # Ajouter le texte de la section gauche
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 12.7)
    c.drawString(0.3 * inch, height - 2.3 * inch, "CHIFFRE D'AFFAIRES T3")
    # c.setFillColor(white)
    # c.setFont("Helvetica-Bold", 13)
    # c.drawString(0.3 * inch, height - 2.5 * inch, "D'AFFAIRES T3")
    # # SOCIÉTÉS
    c.setFont("Helvetica", 40)
    c.drawString(0.3 * inch, height - 2.8* inch, "59,97")
    c.setFont("Helvetica", 14)
    c.drawString(0.34 * inch, height - 3.1* inch, "Milliards")
    

    c.setFont("Helvetica-Bold", 14)
    c.drawString(0.3 * inch, height - 3.7* inch, "Evolution par")
    c.setFont("Helvetica", 14)
    c.drawString(0.3 * inch, height - 3.88 * inch, "rapport à T3 2022")
    c.setFont("Helvetica", 38)
    c.drawString(0.20 * inch, height - 4.4 * inch, "-12,40%")
    
    
    # Définir les dimensions et la position du carré blanc
    square_size = 5.6  # Taille du carré en points
    x_position = 12  # Position X du coin inférieur gauche du carré
    y_position = height - 342 # Position Y du coin inférieur gauche du carré
    
     # Définir la couleur de remplissage en blanc
    c.setFillColorRGB(1, 1, 1)
    # Dessiner le carré blanc
    c.rect(x_position, y_position, square_size, square_size, fill=1, stroke=0)

    # Ajouter le texte de la section gauche
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.3 * inch, height - 4.8 * inch, "SINISTRES")
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.3 * inch, height - 5 * inch, "PAYEES T3:")
    # # SOCIÉTÉS
    c.setFont("Helvetica", 40)
    c.drawString(0.3 * inch, height - 5.54 * inch, "31,02")
    c.setFont("Helvetica", 14)
    c.drawString(0.34 * inch, height - 5.8 * inch, "Milliards")
    
    c.setFont("Helvetica-Bold", 14)
    c.drawString(0.3 * inch, height - 6.1* inch, "EVOLUTION PAR")
    c.setFont("Helvetica", 14)
    c.drawString(0.3 * inch, height - 6.3* inch, "RAPPORT A T3 2022")
    c.setFont("Helvetica", 38)
    c.drawString(0.20 * inch, height - 6.8 * inch, "+15,36%")
    
    
    # Définir les dimensions et la position du carré blanc
    square_size = 5.6  # Taille du carré en points
    x_position = 12  # Position X du coin inférieur gauche du carré
    y_position = height - 515 # Position Y du coin inférieur gauche du carré
    
     # Définir la couleur de remplissage en blanc
    c.setFillColorRGB(1, 1, 1)
    # Dessiner le carré blanc
    c.rect(x_position, y_position, square_size, square_size, fill=1, stroke=0)

    # Ajouter le texte de la section gauche
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.3 * inch, height - 7.2 * inch, "SINISTRES A PAYER:")
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 40)
    c.drawString(0.24 * inch, height - 7.8 * inch, "141,20")
    c.setFillColor(white)
    c.setFont("Helvetica", 13)
    c.drawString(0.40 * inch, height - 8.1* inch, "Milliards")
    
    
    # Définir les dimensions et la position du carré blanc
    square_size = 5.6  # Taille du carré en points
    x_position = 12  # Position X du coin inférieur gauche du carré
    y_position = height - 602 # Position Y du coin inférieur gauche du carré
    
     # Définir la couleur de remplissage en blanc
    c.setFillColorRGB(1, 1, 1)
    # Dessiner le carré blanc
    c.rect(x_position, y_position, square_size, square_size, fill=1, stroke=0)

    # Ajouter le texte de la section gauche
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.3 * inch, height - 8.4 * inch, "NOMBRE DE CONTRATS")
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 40)
    c.drawString(0.3 * inch, height - 9 * inch, "357316")
    
    
     # Définir les dimensions et la position du carré blanc
    square_size = 5.6  # Taille du carré en points
    x_position = 12  # Position X du coin inférieur gauche du carré
    y_position = height - 680 # Position Y du coin inférieur gauche du carré
    
     # Définir la couleur de remplissage en blanc
    c.setFillColorRGB(1, 1, 1)
    # Dessiner le carré blanc
    c.rect(x_position, y_position, square_size, square_size, fill=1, stroke=0)

    # Ajouter le texte de la section gauche
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.3 * inch, height - 9.5 * inch, "EFFECTIF DU")
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.3 * inch, height - 9.7 * inch, "PERSONNEL T3")
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 40)
    c.drawString(0.3 * inch, height - 10.2 * inch, "1398")
    

   # Ajouter le titre de la section principale
   # 
    c.setFillColor(orange)
    c.rect(2.5 * inch, height - 1.48 * inch, width - 2.5 * inch, 3* inch, fill=True, stroke=False)
    c.setFillColor(white)
    c.setFont("Times-Bold", 23)
    c.drawString(2.8 * inch, height - 0.70 * inch, "II.3. ASSURANCE NON-VIE")
    # c.setFillColor(white)
    # c.setFont("Times-Bold", 25)
    # c.drawString(2.6 * inch, height - 1.1 * inch, "DE L'ASSURANCES")
    # Draw the curved lines
    draw_curved_lines(c, width, height)
    c.drawImage("images/18.png", width - 444, height - 834,  width=45, height=45)
    # Définir la couleur orange (approximation, utilisez l'outil pipette pour précision)
    orange_rgb = (243, 112, 33)  # R: 243, G: 112, B: 33 (approximation)

    # Définir la couleur de la ligne à orange
    c.setStrokeColorRGB(orange_rgb[0]/255, orange_rgb[1]/255, orange_rgb[2]/255)
    c.setLineWidth(0.5)  # Définir l'épaisseur de la ligne (ajustez si nécessaire)

    # Dessiner la ligne orange (ajustez les coordonnées pour correspondre à l'image)
    x1 = 520
    x2 = width - 395
    y = 25 # Position verticale (ajustez pour correspondre à l'image)
    
    c.drawImage("images/modified_image1.png", width - 600, height - 92,  width=180, height=90)

    c.line(x1, y, x2, y)
    # Define dimensions
    footer_height = 0.4 * inch
    margin = 0.9 * inch
    line_thickness = 0.1 * inch
    right_bar_width = 0.3 * inch
    
# #c.translate(inch,inch) #starting point of coordinate to one inch
#     c.setStrokeColorRGB(1,0,0) # red colour of line
#     c.setLineWidth(0.1) #width of the line 
#     c.line(0,8*inch,4*inch,5*inch) # draw line 
 
    # # c.line(0,0,0,1.7*inch)
    # c.line(0,0,1*inch,0)

    # Draw the orange line at the bottom
    c.setFillColor(orange)
    # c.rect(margin, footer_height, width - 2 * margin - 8, line_thickness- 8, fill=True, stroke=False)
    
    # Draw the right orange bar with number
    c.rect(width - margin - right_bar_width, 0, right_bar_width, footer_height + line_thickness, fill=True, stroke=False)
    c.setFillColor(white)
    c.setFont("Times-Bold", 12)
    c.drawCentredString(width - margin - right_bar_width / 2, footer_height / 2 + line_thickness / 2 - 3, "1")

    # Draw the centered text
    c.setFillColor(black)
    c.setFont("Times-Roman", 7.5)
    c.drawCentredString(width / 1.70, footer_height / 2 + line_thickness / 2 - 3, "NOTE DE CONJONCTURE 3EME TRIMESTRE DU MARCHÉ IVOIRIEN DES ASSURANCES")
    
   
  
 
    
    c.showPage()
    
     
     # Couleurs
    orange = HexColor("#F57E37")
    white = HexColor("#FFFFFF")
    grey = HexColor("#F0F0F0")

    # Dessiner le fond orange pour la section de gauche
    c.setFillColor(orange)
    c.rect(0, 0, 2.5 * inch, height, fill=True, stroke=False)
    
     # Définir les dimensions et la position du carré blanc
    square_size = 5.6  # Taille du carré en points
    x_position = 12  # Position X du coin inférieur gauche du carré
    y_position = height - 165 # Position Y du coin inférieur gauche du carré
    
     # Définir la couleur de remplissage en blanc
    c.setFillColorRGB(1, 1, 1)
    # Dessiner le carré blanc
    c.rect(x_position, y_position, square_size, square_size, fill=1, stroke=0)

    # Ajouter le texte de la section gauche
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 12.7)
    c.drawString(0.3 * inch, height - 2.3 * inch, "STOCK DE SINISTRES")
    # c.setFillColor(white)
    # c.setFont("Helvetica-Bold", 13)
    # c.drawString(0.3 * inch, height - 2.5 * inch, "D'AFFAIRES T3")
    # # SOCIÉTÉS
    c.setFont("Helvetica-Bold", 12.7)
    c.drawString(0.3 * inch, height - 2.5* inch, "BON A PAYER:")
    c.setFont("Helvetica", 40)
    c.drawString(0.34 * inch, height - 3.1* inch, "37,67")
    
    
        
     # Définir les dimensions et la position du carré blanc
    square_size = 5.6  # Taille du carré en points
    x_position = 12  # Position X du coin inférieur gauche du carré
    y_position = height - 286 # Position Y du coin inférieur gauche du carré
    
     # Définir la couleur de remplissage en blanc
    c.setFillColorRGB(1, 1, 1)
    # Dessiner le carré blanc
    c.rect(x_position, y_position, square_size, square_size, fill=1, stroke=0)
    
    
    # Ajouter le texte de la section gauche
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 12.7)
    c.drawString(0.3 * inch, height - 4 * inch, "NOMBRE DE")
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.3 * inch, height - 4.2 * inch, "DE CONTRATS:")
 
    c.setFont("Helvetica-Bold", 40)
    c.drawString(0.3 * inch, height - 4.8* inch, "450 864")
    
    
    
    
         # Définir les dimensions et la position du carré blanc
    square_size = 5.6  # Taille du carré en points
    x_position = 12  # Position X du coin inférieur gauche du carré
    y_position = height - 399.8 # Position Y du coin inférieur gauche du carré
    
     # Définir la couleur de remplissage en blanc
    c.setFillColorRGB(1, 1, 1)
    # Dessiner le carré blanc
    c.rect(x_position, y_position, square_size, square_size, fill=1, stroke=0)
    
    
    # Ajouter le texte de la section gauche
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 12.7)
    c.drawString(0.3 * inch, height - 5.6* inch, "CHIFFRE D'AFFAIRE")
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.3 * inch, height - 5.8 * inch, "CREDIT-CAUTION:")
 
    c.setFont("Helvetica-Bold", 40)
    c.drawString(0.3 * inch, height - 6.4* inch, "1,541")
    c.setFont("Helvetica-Bold", 12)
    c.drawString(0.42 * inch, height - 6.7* inch, "Milliards")
    
      # Ajouter le texte de la section gauche
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.3 * inch, height - 7.7* inch, "EVOLUTION PAR")
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.3 * inch, height - 7.9 * inch, "RAPPORT A T3 2022")
 
    c.setFont("Helvetica-Bold", 40)
    c.drawString(0.20 * inch, height - 8.5* inch, "-2,84%")
    
    
    
    # c.setFont("Helvetica", 14)
    # c.drawString(0.34 * inch, height - 4* inch, "450 864")
    
    

    # c.setFont("Helvetica-Bold", 14)
    # c.drawString(0.3 * inch, height - 3.7* inch, "Evolution par")
    # c.setFont("Helvetica", 14)
    # c.drawString(0.3 * inch, height - 3.88 * inch, "rapport à T3 2022")
    # c.setFont("Helvetica", 38)
    # c.drawString(0.20 * inch, height - 4.4 * inch, "-12,40%")
    
    
    # # Définir les dimensions et la position du carré blanc
    # square_size = 5.6  # Taille du carré en points
    # x_position = 12  # Position X du coin inférieur gauche du carré
    # y_position = height - 342 # Position Y du coin inférieur gauche du carré
    
    #  # Définir la couleur de remplissage en blanc
    # c.setFillColorRGB(1, 1, 1)
    # # Dessiner le carré blanc
    # c.rect(x_position, y_position, square_size, square_size, fill=1, stroke=0)

    # # Ajouter le texte de la section gauche
    # c.setFillColor(white)
    # c.setFont("Helvetica-Bold", 13)
    # c.drawString(0.3 * inch, height - 4.8 * inch, "SINISTRES")
    # c.setFillColor(white)
    # c.setFont("Helvetica-Bold", 13)
    # c.drawString(0.3 * inch, height - 5 * inch, "PAYEES T3:")
    # # # SOCIÉTÉS
    # c.setFont("Helvetica", 40)
    # c.drawString(0.3 * inch, height - 5.54 * inch, "31,02")
    # c.setFont("Helvetica", 14)
    # c.drawString(0.34 * inch, height - 5.8 * inch, "Milliards")
    
    # c.setFont("Helvetica-Bold", 14)
    # c.drawString(0.3 * inch, height - 6.1* inch, "EVOLUTION PAR")
    # c.setFont("Helvetica", 14)
    # c.drawString(0.3 * inch, height - 6.3* inch, "RAPPORT A T3 2022")
    # c.setFont("Helvetica", 38)
    # c.drawString(0.20 * inch, height - 6.8 * inch, "+15,36%")
    
    
    # # Définir les dimensions et la position du carré blanc
    # square_size = 5.6  # Taille du carré en points
    # x_position = 12  # Position X du coin inférieur gauche du carré
    # y_position = height - 515 # Position Y du coin inférieur gauche du carré
    
    #  # Définir la couleur de remplissage en blanc
    # c.setFillColorRGB(1, 1, 1)
    # # Dessiner le carré blanc
    # c.rect(x_position, y_position, square_size, square_size, fill=1, stroke=0)

    # # Ajouter le texte de la section gauche
    # c.setFillColor(white)
    # c.setFont("Helvetica-Bold", 13)
    # c.drawString(0.3 * inch, height - 7.2 * inch, "SINISTRES A PAYER:")
    # c.setFillColor(white)
    # c.setFont("Helvetica-Bold", 40)
    # c.drawString(0.24 * inch, height - 7.8 * inch, "141,20")
    # c.setFillColor(white)
    # c.setFont("Helvetica", 13)
    # c.drawString(0.40 * inch, height - 8.1* inch, "Milliards")
    
    
    # # Définir les dimensions et la position du carré blanc
    # square_size = 5.6  # Taille du carré en points
    # x_position = 12  # Position X du coin inférieur gauche du carré
    # y_position = height - 602 # Position Y du coin inférieur gauche du carré
    
    #  # Définir la couleur de remplissage en blanc
    # c.setFillColorRGB(1, 1, 1)
    # # Dessiner le carré blanc
    # c.rect(x_position, y_position, square_size, square_size, fill=1, stroke=0)

    # # Ajouter le texte de la section gauche
    # c.setFillColor(white)
    # c.setFont("Helvetica-Bold", 13)
    # c.drawString(0.3 * inch, height - 8.4 * inch, "NOMBRE DE CONTRATS")
    # c.setFillColor(white)
    # c.setFont("Helvetica-Bold", 40)
    # c.drawString(0.3 * inch, height - 9 * inch, "357316")
    
    
    #  # Définir les dimensions et la position du carré blanc
    # square_size = 5.6  # Taille du carré en points
    # x_position = 12  # Position X du coin inférieur gauche du carré
    # y_position = height - 680 # Position Y du coin inférieur gauche du carré
    
    #  # Définir la couleur de remplissage en blanc
    # c.setFillColorRGB(1, 1, 1)
    # # Dessiner le carré blanc
    # c.rect(x_position, y_position, square_size, square_size, fill=1, stroke=0)

    # # Ajouter le texte de la section gauche
    # c.setFillColor(white)
    # c.setFont("Helvetica-Bold", 13)
    # c.drawString(0.3 * inch, height - 9.5 * inch, "EFFECTIF DU")
    # c.setFillColor(white)
    # c.setFont("Helvetica-Bold", 13)
    # c.drawString(0.3 * inch, height - 9.7 * inch, "PERSONNEL T3")
    # c.setFillColor(white)
    # c.setFont("Helvetica-Bold", 40)
    # c.drawString(0.3 * inch, height - 10.2 * inch, "1398")
    

#    # Ajouter le titre de la section principale
#    # 
#     c.setFillColor(orange)
#     c.rect(2.5 * inch, height - 1.48 * inch, width - 2.5 * inch, 3* inch, fill=True, stroke=False)
#     c.setFillColor(white)
#     c.setFont("Times-Bold", 23)
#     c.drawString(2.8 * inch, height - 0.70 * inch, "II.3. ASSURANCE NON-VIE")
    # c.setFillColor(white)
    # c.setFont("Times-Bold", 25)
    # c.drawString(2.6 * inch, height - 1.1 * inch, "DE L'ASSURANCES")
    # Draw the curved lines
    # draw_curved_lines(c, width, height)
    c.drawImage("images/18.png", width - 444, height - 834,  width=45, height=45)
    # Définir la couleur orange (approximation, utilisez l'outil pipette pour précision)
    orange_rgb = (243, 112, 33)  # R: 243, G: 112, B: 33 (approximation)

    # Définir la couleur de la ligne à orange
    c.setStrokeColorRGB(orange_rgb[0]/255, orange_rgb[1]/255, orange_rgb[2]/255)
    c.setLineWidth(0.5)  # Définir l'épaisseur de la ligne (ajustez si nécessaire)

    # Dessiner la ligne orange (ajustez les coordonnées pour correspondre à l'image)
    x1 = 520
    x2 = width - 395
    y = 25 # Position verticale (ajustez pour correspondre à l'image)
    
    c.drawImage("images/modified_image1.png", width - 600, height - 850,  width=160, height=120)

    c.line(x1, y, x2, y)
    # Define dimensions
    footer_height = 0.4 * inch
    margin = 0.9 * inch
    line_thickness = 0.1 * inch
    right_bar_width = 0.3 * inch
    
# #c.translate(inch,inch) #starting point of coordinate to one inch
#     c.setStrokeColorRGB(1,0,0) # red colour of line
#     c.setLineWidth(0.1) #width of the line 
#     c.line(0,8*inch,4*inch,5*inch) # draw line 
 
    # # c.line(0,0,0,1.7*inch)
    # c.line(0,0,1*inch,0)

    # Draw the orange line at the bottom
    c.setFillColor(orange)
    # c.rect(margin, footer_height, width - 2 * margin - 8, line_thickness- 8, fill=True, stroke=False)
    
    # Draw the right orange bar with number
    c.rect(width - margin - right_bar_width, 0, right_bar_width, footer_height + line_thickness, fill=True, stroke=False)
    c.setFillColor(white)
    c.setFont("Times-Bold", 12)
    c.drawCentredString(width - margin - right_bar_width / 2, footer_height / 2 + line_thickness / 2 - 3, "1")

    # Draw the centered text
    c.setFillColor(black)
    c.setFont("Times-Roman", 7.5)
    c.drawCentredString(width / 1.70, footer_height / 2 + line_thickness / 2 - 3, "NOTE DE CONJONCTURE 3EME TRIMESTRE DU MARCHÉ IVOIRIEN DES ASSURANCES")
    
   
  
 
    
    c.showPage()
    
    
    # Placer l'image comme arrière-plan de la deuxième page
    c.drawImage("images/RAPPORT ASSURANCE_ VF_121223-24.jpg", 0, 0, width=width, height=height)
    
    c.showPage()
    
    
    
       # Chemin vers votre image
    image_path = "images/image068-removebg-preview.png"
    image_width = 50  # Largeur de l'image
    image_height = 23  # Hauteur de l'image

    # Dupliquer l'image jusqu'à la fin de la page
    image_x = width - 56  # Position X de l'image
    for y in range(0, int(height), image_height):
        c.drawImage(image_path, image_x, y, width=image_width, height=image_height)
    
    
     # Titre "ANNEXE 1"
    c.setFillColor(color_orange2)
    c.setStrokeColor(color_orange2)
    c.rect(0, height - 40 * mm, width - 98 * mm, 14 * mm, fill=1)
    c.setFillColor(white)
    
    c.setFont("Helvetica-Bold", 18)
    c.drawString(65 * mm, height - 36 * mm, "ANNEXE 1")
    
    # Sous-titre "EVOLUTION DU CHIFFRE D'AFFAIRES SOCIETE VIE TRIMESTRE 3 2023"
    c.setFillColor(color_orange2)
    c.rect(20, height - 58 * mm, width - 30 * mm, 10 * mm, fill=1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(20 * mm, height - 55 * mm, "EVOLUTION DU CHIFFRE D'AFFAIRES SOCIETE VIE TRIMESTRE 3 2023")
    # Ajouter une nouvelle page avec le tableau
    draw_table_on_canvas(c, width, height)
    # Draw the orange line at the bottom
    c.setFillColor(orange)
    # c.rect(margin, footer_height, width - 2 * margin - 8, line_thickness- 8, fill=True, stroke=False)
    
    # Draw the right orange bar with number
    c.rect(width - margin - right_bar_width, 0, right_bar_width, footer_height + line_thickness, fill=True, stroke=False)
    c.setFillColor(white)
    c.setFont("Times-Bold", 12)
    c.drawCentredString(width - margin - right_bar_width / 2, footer_height / 2 + line_thickness / 2 - 3, "6")

    # Draw the centered text
    c.setFillColor(black)
    c.setFont("Times-Roman", 8.5)
    c.drawCentredString(width / 1.97, footer_height / 2 + line_thickness / 2 - 3, "NOTE DE CONJONCTURE 3EME TRIMESTRE DU MARCHÉ IVOIRIEN DES ASSURANCES")
    
    c.drawImage("images/image061-removebg-preview.png", width - 502, height - 834,  width=32, height=32)
    
    # Définir la couleur orange (approximation, utilisez l'outil pipette pour précision)
    orange_rgb = (243, 112, 33)  # R: 243, G: 112, B: 33 (approximation)

    # Définir la couleur de la ligne à orange
    c.setStrokeColorRGB(orange_rgb[0]/255, orange_rgb[1]/255, orange_rgb[2]/255)
    c.setLineWidth(0.7)  # Définir l'épaisseur de la ligne (ajustez si nécessaire)
    
    # Dessiner la ligne orange (ajustez les coordonnées pour correspondre à l'image)
    x1 = 520
    x2 = width - 466.5
    y = 25 # Position verticale (ajustez pour correspondre à l'image)
    
    c.line(x1, y, x2, y)
    c.showPage()
    # Titre "ANNEXE 2"
    c.setFillColor(color_orange2)
    c.setStrokeColor(color_orange2)
    c.rect(0, height - 40 * mm, width - 98 * mm, 14 * mm, fill=1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(65 * mm, height - 36 * mm, "ANNEXE 2")
    
    # Sous-titre "EVOLUTION DU CHIFFRE D'AFFAIRES SOCIETE NON VIE TRIMESTRE 3 2023"
    c.setFillColor(color_green2)
    c.setStrokeColor(color_green2)
    c.rect(20, height - 58 * mm, width - 28 * mm, 10 * mm, fill=1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(12 * mm, height - 55 * mm, "EVOLUTION DU CHIFFRE D'AFFAIRES SOCIETE NON VIE TRIMESTRE 3 2023")
    
       # Chemin vers votre image
    image_path = "images/image068-removebg-preview.png"
    image_width = 50  # Largeur de l'image
    image_height = 23  # Hauteur de l'image

    # Dupliquer l'image jusqu'à la fin de la page
    image_x = width - 56  # Position X de l'image
    for y in range(0, int(height), image_height):
        c.drawImage(image_path, image_x, y, width=image_width, height=image_height)
    
        

    
     # Définir la taille et la position du rectangle gris clair
    rect_x = 196
    rect_y = height - 50
    rect_width = 346
    rect_height = 14

    # Dessiner le rectangle gris clair
    c.setFillColor(color_silver)
    c.rect(rect_x, rect_y, rect_width, rect_height, fill=True, stroke=False)

    # Ajouter le texte centré
    text = "NOTE DE CONJONCTURE 3EME TRIMESTRE DU MARCHÉ IVOIRIEN DES ASSURANCES"
    c.setFont("Helvetica-Bold", 8)
    c.setFillColorRGB(0, 0, 0)
    text_x = 368
    text_y = rect_y + rect_height / 4  # Ajustement vertical pour centrer le texte
    c.drawCentredString(text_x, text_y, text)
    c.setFont("Times-Bold", 14)
    #c.setFillColor(color_white)
    c.drawImage("images/2.png", width - 542, height -50,  width=140, height=16)
    #c.setFont("Times-Bold", 14)
    # Ajouter une page contenant le tableau de l'annexe 2
    draw_table_on_canvas_annexe2(c, width, height)
     # Ajouter une page contenant le tableau de l'annexe 3
    # Draw the orange line at the bottom
    c.setFillColor(orange)
    # c.rect(margin, footer_height, width - 2 * margin - 8, line_thickness- 8, fill=True, stroke=False)
    
    # Draw the right orange bar with number
    c.rect(width - margin - right_bar_width, 0, right_bar_width, footer_height + line_thickness, fill=True, stroke=False)
    c.setFillColor(white)
    c.setFont("Times-Bold", 12)
    c.drawCentredString(width - margin - right_bar_width / 2, footer_height / 2 + line_thickness / 2 - 3, "7")

    # Draw the centered text
    c.setFillColor(black)
    c.setFont("Times-Roman", 8.5)
    c.drawCentredString(width / 1.97, footer_height / 2 + line_thickness / 2 - 3, "NOTE DE CONJONCTURE 3EME TRIMESTRE DU MARCHÉ IVOIRIEN DES ASSURANCES")
    
    c.drawImage("images/image061-removebg-preview.png", width - 502, height - 834,  width=32, height=32)
    
    # Définir la couleur orange (approximation, utilisez l'outil pipette pour précision)
    orange_rgb = (243, 112, 33)  # R: 243, G: 112, B: 33 (approximation)

    # Définir la couleur de la ligne à orange
    c.setStrokeColorRGB(orange_rgb[0]/255, orange_rgb[1]/255, orange_rgb[2]/255)
    c.setLineWidth(0.7)  # Définir l'épaisseur de la ligne (ajustez si nécessaire)
    
    # Dessiner la ligne orange (ajustez les coordonnées pour correspondre à l'image)
    x1 = 520
    x2 = width - 466.5
    y = 25 # Position verticale (ajustez pour correspondre à l'image)
    
    c.line(x1, y, x2, y)
    c.showPage()
    
    # Chemin vers votre image
    image_path = "images/image068-removebg-preview.png"
    image_width = 50  # Largeur de l'image
    image_height = 23  # Hauteur de l'image

    # Dupliquer l'image jusqu'à la fin de la page
    image_x = 6  # Position X de l'image (proche du bord gauche)
    for y in range(0, int(height), image_height):
        c.drawImage(image_path, image_x, y, width=image_width, height=image_height)
    
    # Titre "ANNEXE 2"
    c.setFillColor(orange)
    c.setStrokeColor(color_orange2)
    c.rect(0, height - 40 * mm, width - 98 * mm, 14 * mm, fill=1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(65 * mm, height - 36 * mm, "ANNEXE 3")
    
    # Sous-titre "EVOLUTION DU CHIFFRE D'AFFAIRES SOCIETE NON VIE TRIMESTRE 3 2023"
    color_green4 = HexColor("#76A646")
    c.setFillColor(color_green4)
    c.setStrokeColor(color_green4)
    c.rect(20, height - 58 * mm, width - 28 * mm, 10 * mm, fill=1)
    c.setFillColor(black)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(12 * mm, height - 55 * mm, "LES CARTES PROFESSIONNELLES EDITEES AU TROISIEME TRIMESTRE 2023")
    
     # Définir la taille et la position du rectangle gris clair
    rect_x = 72
    rect_y = height - 50
    rect_width = 345
    rect_height = 14

    # Dessiner le rectangle gris clair
    c.setFillColor(color_silver)
    c.rect(rect_x, rect_y, rect_width, rect_height, fill=True, stroke=False)

    # Ajouter le texte centré
    text = "NOTE DE CONJONCTURE 3EME TRIMESTRE DU MARCHÉ IVOIRIEN DES ASSURANCES"
    c.setFont("Helvetica-Bold", 8)
    c.setFillColorRGB(0, 0, 0)
    text_x = 242
    text_y = rect_y + rect_height / 4  # Ajustement vertical pour centrer le texte
    c.drawCentredString(text_x, text_y, text)
    c.drawImage("images/1.png", width - 176, height -51,  width=146, height=18)
    draw_table_on_canvas_annexe3(c, width, height)
    
    # Draw the orange line at the bottom
    c.setFillColor(orange)
    # c.rect(margin, footer_height, width - 2 * margin - 8, line_thickness- 8, fill=True, stroke=False)
    
    # Draw the right orange bar with number
    c.rect(width - margin - right_bar_width, 0, right_bar_width, footer_height + line_thickness, fill=True, stroke=False)
    c.setFillColor(white)
    c.setFont("Times-Bold", 12)
    c.drawCentredString(width - margin - right_bar_width / 2, footer_height / 2 + line_thickness / 2 - 3, "8")

    # Draw the centered text
    c.setFillColor(black)
    c.setFont("Times-Roman", 8.5)
    c.drawCentredString(width / 1.97, footer_height / 2 + line_thickness / 2 - 3, "NOTE DE CONJONCTURE 3EME TRIMESTRE DU MARCHÉ IVOIRIEN DES ASSURANCES")
    
    c.drawImage("images/image061-removebg-preview.png", width - 502, height - 834,  width=32, height=32)
    
    # Définir la couleur orange (approximation, utilisez l'outil pipette pour précision)
    orange_rgb = (243, 112, 33)  # R: 243, G: 112, B: 33 (approximation)

    # Définir la couleur de la ligne à orange
    c.setStrokeColorRGB(orange_rgb[0]/255, orange_rgb[1]/255, orange_rgb[2]/255)
    c.setLineWidth(0.7)  # Définir l'épaisseur de la ligne (ajustez si nécessaire)
    
    # Dessiner la ligne orange (ajustez les coordonnées pour correspondre à l'image)
    x1 = 520
    x2 = width - 466.5
    y = 25 # Position verticale (ajustez pour correspondre à l'image)
    
    c.line(x1, y, x2, y)
    
    c.showPage()
    
     # Titre "ANNEXE 2"
    c.setFillColor(orange)
    c.setStrokeColor(color_orange2)
    c.rect(0, height - 40 * mm, width - 98 * mm, 14 * mm, fill=1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(65 * mm, height - 36 * mm, "ANNEXE 4")
    
    # Sous-titre "EVOLUTION DU CHIFFRE D'AFFAIRES SOCIETE NON VIE TRIMESTRE 3 2023"
    color_green3 = HexColor('#46A637')
    c.setFillColor(color_green3)
    c.setStrokeColor(color_green3)
    c.rect(74, height - 58 * mm, width - 50 * mm, 10 * mm, fill=1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(29* mm, height - 55 * mm, "SITUATION GEOGRAPHIQUE DES COMPAGNIES D’ASSURANCE")
    
       # Chemin vers votre image
    image_path = "images/image068-removebg-preview.png"
    image_width = 50  # Largeur de l'image
    image_height = 23  # Hauteur de l'image

    # Dupliquer l'image jusqu'à la fin de la page
    image_x = width - 56  # Position X de l'image
    for y in range(0, int(height), image_height):
        c.drawImage(image_path, image_x, y, width=image_width, height=image_height)
    # Ajouter une page contenant le tableau de l'annexe 4
     # Définir la taille et la position du rectangle gris clair
    rect_x = 196
    rect_y = height - 50
    rect_width = 346
    rect_height = 14

    # Dessiner le rectangle gris clair
    c.setFillColor(color_silver)
    c.rect(rect_x, rect_y, rect_width, rect_height, fill=True, stroke=False)

    # Ajouter le texte centré
    text = "NOTE DE CONJONCTURE 3EME TRIMESTRE DU MARCHÉ IVOIRIEN DES ASSURANCES"
    c.setFont("Helvetica-Bold", 8)
    c.setFillColorRGB(0, 0, 0)
    text_x = 368
    text_y = rect_y + rect_height / 4  # Ajustement vertical pour centrer le texte
    c.drawCentredString(text_x, text_y, text)
    c.setFont("Times-Bold", 14)
    #c.setFillColor(color_white)
    c.drawImage("images/2.png", width - 542, height -50,  width=140, height=16)
    draw_page_annexe4(c, width, height)
    # Draw the orange line at the bottom
    c.setFillColor(orange)
    # c.rect(margin, footer_height, width - 2 * margin - 8, line_thickness- 8, fill=True, stroke=False)
    
    # Draw the right orange bar with number
    c.rect(width - margin - right_bar_width, 0, right_bar_width, footer_height + line_thickness, fill=True, stroke=False)
    c.setFillColor(white)
    c.setFont("Times-Bold", 12)
    c.drawCentredString(width - margin - right_bar_width / 2, footer_height / 2 + line_thickness / 2 - 3, "9")

    # Draw the centered text
    c.setFillColor(black)
    c.setFont("Times-Roman", 8.5)
    c.drawCentredString(width / 1.97, footer_height / 2 + line_thickness / 2 - 3, "NOTE DE CONJONCTURE 3EME TRIMESTRE DU MARCHÉ IVOIRIEN DES ASSURANCES")
    
    c.drawImage("images/image061-removebg-preview.png", width - 502, height - 834,  width=32, height=32)
    
    # Définir la couleur orange (approximation, utilisez l'outil pipette pour précision)
    orange_rgb = (243, 112, 33)  # R: 243, G: 112, B: 33 (approximation)

    # Définir la couleur de la ligne à orange
    c.setStrokeColorRGB(orange_rgb[0]/255, orange_rgb[1]/255, orange_rgb[2]/255)
    c.setLineWidth(0.7)  # Définir l'épaisseur de la ligne (ajustez si nécessaire)
    
    # Dessiner la ligne orange (ajustez les coordonnées pour correspondre à l'image)
    x1 = 520
    x2 = width - 466.5
    y = 25 # Position verticale (ajustez pour correspondre à l'image)
    
    c.line(x1, y, x2, y)
    c.showPage()
    
    # Placer l'image comme arrière-plan de la deuxième page
    c.drawImage("images/RAPPORT ASSURANCE_ VF_121223-29.jpg", 0, 0, width=width, height=height)



    c.save()

draw_layout()
