import os
import requests
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Spacer, Frame, PageTemplate, NextPageTemplate
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

# --- 1. CONFIGURATION & CONSTANTS (DA V4 - CARD UI & BLUE PAGES) ---

# A. Palette de Couleurs
COLOR_BG_NUDE = colors.HexColor("#FFF0E6")       # Fond Papier
COLOR_ACCENT_BLUE = colors.HexColor("#3434C2")   # Indigo Électrique
COLOR_TEXT_MAIN = colors.HexColor("#2A2A35")     # Gunmetal
COLOR_ACCENT_RED = colors.HexColor("#FF4D4D")    # Rouge Vif
COLOR_ACCENT_YELLOW = colors.HexColor("#FFEB3B") # Jaune Soleil
COLOR_WHITE = colors.HexColor("#FFFFFF")         # Blanc Pur

# B. Typography (Updated V4)
FONTS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets", "fonts")
try:
    os.makedirs(FONTS_DIR, exist_ok=True)
except OSError:
    pass

# Font Names & Fallbacks
FONT_TITLE = "Helvetica-Bold" 
FONT_BODY = "Helvetica"
FONT_ITALIC = "Helvetica-Oblique"
FONT_HAND = "Helvetica" # Placeholder for Amatic/Caveat

# Attempt to register true fonts
# Paths
PATH_MONTSERRAT = os.path.join(FONTS_DIR, "Montserrat-Bold.ttf")
PATH_LATO_REG = os.path.join(FONTS_DIR, "Lato-Regular.ttf")
PATH_LATO_ITA = os.path.join(FONTS_DIR, "Lato-Italic.ttf")
PATH_AMATIC = os.path.join(FONTS_DIR, "AmaticSC-Regular.ttf")
PATH_CAVEAT = os.path.join(FONTS_DIR, "Caveat-Regular.ttf")

if os.path.exists(PATH_MONTSERRAT):
    pdfmetrics.registerFont(TTFont('Montserrat-Bold', PATH_MONTSERRAT))
    FONT_TITLE = 'Montserrat-Bold'

if os.path.exists(PATH_LATO_REG):
    pdfmetrics.registerFont(TTFont('Lato-Regular', PATH_LATO_REG))
    FONT_BODY = 'Lato-Regular'

if os.path.exists(PATH_LATO_ITA):
    pdfmetrics.registerFont(TTFont('Lato-Italic', PATH_LATO_ITA))
    FONT_ITALIC = 'Lato-Italic'

if os.path.exists(PATH_AMATIC):
    pdfmetrics.registerFont(TTFont('AmaticSC-Regular', PATH_AMATIC))
    FONT_HAND = 'AmaticSC-Regular'
elif os.path.exists(PATH_CAVEAT):
    pdfmetrics.registerFont(TTFont('Caveat-Regular', PATH_CAVEAT))
    FONT_HAND = 'Caveat-Regular'
# --- 1.C ILLUSTRATIONS ---
ILLUS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets", "illustrations")
PATH_ILLU_COVER = os.path.join(ILLUS_DIR, "01a_ILLU.png")
PATH_GUILLEMETS = os.path.join(ILLUS_DIR, "guillemets.png")
PATH_FLECHE = os.path.join(ILLUS_DIR, "fleche.png")
PATH_STAMP = os.path.join(ILLUS_DIR, "stamp_rouge.png")

# --- 2. GRAPHIC COMPONENTS ---

def draw_dot_grid(c, width, height, color=COLOR_ACCENT_BLUE, opacity=0.25):
    """Draws the signature Dot Grid. V4: Higher opacity."""
    step = 20
    c.saveState()
    c.setFillColor(color, alpha=opacity) 
    for x in range(0, int(width), step):
        for y in range(0, int(height), step):
            c.circle(x, y, 0.6, fill=1, stroke=0) # Slightly larger dots
    c.restoreState()

def draw_marginal_signature(c, height):
    """Draws vertical 'marge de manœuvre' signature on the left."""
    c.saveState()
    c.translate(1.2*cm, height/2)
    c.rotate(90)
    c.setFont(FONT_BODY, 8)
    c.setFillColor(colors.HexColor("#808090")) 
    c.drawCentredString(0, 0, "m a r g e   d e   m a n œ u v r e")
    c.restoreState()

def draw_leaf(c, x, y, size=50, color=COLOR_ACCENT_BLUE, angle=0, alpha=1.0):
    """Draws a simple leaf shape using bezier curves."""
    c.saveState()
    c.translate(x, y)
    c.rotate(angle)
    c.scale(size/100.0, size/100.0)
    p = c.beginPath()
    p.moveTo(0, 0)
    p.curveTo(30, 20, 50, 60, 0, 100)
    p.curveTo(-50, 60, -30, 20, 0, 0)
    if isinstance(color, colors.Color):
        r, g, b = color.red, color.green, color.blue
        c.setFillColorRGB(r, g, b, alpha)
    else:
         c.setFillColor(color)
    c.drawPath(p, fill=1, stroke=0)
    c.restoreState()

def draw_card_background(c, x, y, width, height):
    """Draws a white rounded card."""
    c.saveState()
    # Shadow
    c.setFillColor(colors.black, alpha=0.05)
    c.roundRect(x+3, y-3, width, height, 10, fill=1, stroke=0)
    # Card
    c.setFillColor(COLOR_WHITE)
    c.roundRect(x, y, width, height, 10, fill=1, stroke=0)
    c.restoreState()

# --- 3. PAGE DRAWING FUNCTIONS ---

def create_cover_page(c):
    width, height = A4
    
    # 1. Background Nude + Grid
    c.setFillColor(COLOR_BG_NUDE)
    c.rect(0,0, width, height, fill=1, stroke=0)
    draw_dot_grid(c, width, height)

    # A. Illustration Principale (Cover)
    if os.path.exists(PATH_ILLU_COVER):
        # On centre l'image dans la partie haute/centrale
        # Taille approximative : Largeur 2/3 de la page
        img_width = width * 0.85
        # Modification: On baisse l'image encore un peu pour faire de la place au header
        # y=height*0.2
        c.drawImage(PATH_ILLU_COVER, (width - img_width)/2, height * 0.20, width=img_width, height=height*0.5, mask='auto', preserveAspectRatio=True, anchor='c')
    else:
        # Fallback: Composition Artistique Géométrique
        c.setFillColor(COLOR_WHITE)
        c.circle(width*0.35, height*0.55, 160, fill=1, stroke=0)

    # 2b. Marque Header (Top Left)
    # "Marge de Manoeuvre" en Rouge (Montserrat Bold)
    c.saveState()
    c.setFont(FONT_TITLE, 14) # Montserrat Bold si dispo
    c.setFillColor(COLOR_ACCENT_RED)
    # En haut à gauche, avec une marge
    c.drawString(1.5*cm, height - 2*cm, "Marge de Manœuvre")
    c.restoreState()

    # 2c. Stamp Rouge
    if os.path.exists(PATH_STAMP):
        # On le place en bas à droite de la page
        c.saveState()
        c.translate(width - 5*cm, 4*cm) # Positionné en bas à droite
        c.rotate(-15) # Légère rotation opposée pour le style
        c.drawImage(PATH_STAMP, -2*cm, -2*cm, width=4*cm, height=4*cm, mask='auto', preserveAspectRatio=True, anchor='c')
        c.restoreState()

    # 3. Titres
    # Fix: Font size reduced to fit width, or split lines.
    # Let's try splitting lines and slightly smaller font.
    c.setFont(FONT_TITLE, 42) 
    c.setFillColor(COLOR_ACCENT_BLUE)
    
    # "MON LIVRE"
    c.drawRightString(width - 40, height - 120, "MON LIVRE")
    # "DE TRANSITION"
    c.drawRightString(width - 40, height - 170, "DE TRANSITION")
    
    c.setFont(FONT_BODY, 14)
    c.setFillColor(COLOR_TEXT_MAIN)
    c.drawRightString(width - 40, height - 210, "BILAN DE COMPÉTENCES & ALIGNEMENT") 
    
    c.setFont(FONT_TITLE, 18)
    c.setFillColor(COLOR_ACCENT_RED)
    c.drawRightString(width - 40, height - 240, "CHAPITRE 0 : LE PRÉLUDE")
    
    c.showPage()

def create_summary_page(c):
    """New Page: Au Programme (Blue Background)."""
    width, height = A4
    
    # 1. Full Blue Background
    c.setFillColor(COLOR_ACCENT_BLUE)
    c.rect(0, 0, width, height, fill=1, stroke=0)
    
    # 2. Faint White Dot Grid
    draw_dot_grid(c, width, height, color=COLOR_WHITE, opacity=0.1)

    # 3. Content
    c.setFont(FONT_TITLE, 30)
    c.setFillColor(COLOR_WHITE)
    c.drawString(3*cm, height - 4*cm, "AU PROGRAMME")
    
    c.setFont(FONT_BODY, 12)
    c.setFillColor(COLOR_WHITE)
    
    start_y = height - 6*cm
    
    intro_lines = [
        "Trouver sa place dans le monde d'aujourd'hui n'est pas chose facile.",
        "Quelle place dois-je accorder au travail dans mon existence ?",
        "",
        "Voici les grandes lignes :"
    ]
    
    for line in intro_lines:
        c.drawString(3*cm, start_y, line)
        start_y -= 18
        
    start_y -= 1*cm
    
    steps = [
        ("05", "Prendre du recul", "sur vos choix passés et vos expériences."),
        ("13", "Explorer votre personnalité", "Vos forces, ce que vous aimez, vos besoins."),
        ("32", "Actions concrètes", "Explorer ces secteurs à travers divers supports."),
        ("43", "Plan d'action", "Réussir votre projet.")
    ]
    
    for page_num, title, desc in steps:
        # Arrow/Bullet
        if os.path.exists(PATH_FLECHE):
             c.drawImage(PATH_FLECHE, 2.8*cm, start_y - 0.1*cm, width=0.6*cm, height=0.6*cm, mask='auto', preserveAspectRatio=True)
        else:
             c.drawString(3*cm, start_y, "->")
        
        # Text
        c.setFont(FONT_TITLE, 12)
        c.drawString(4*cm, start_y, title)
        
        c.setFont(FONT_BODY, 12)
        text_width = c.stringWidth(title, FONT_TITLE, 12)
        c.drawString(4*cm + text_width + 5, start_y, " : " + desc)
        
        # Page Num (dotted line approx)
        c.drawRightString(width - 3*cm, start_y, page_num)
        
        start_y -= 1.5*cm

    # Decor
    draw_leaf(c, width-100, 200, size=150, color=COLOR_ACCENT_YELLOW, angle=-20, alpha=0.9)
    # Red square at bottom
    c.setFillColor(COLOR_ACCENT_RED)
    c.rect(width/2 - 40, 50, 80, 80, fill=1, stroke=0)

    c.showPage()

def create_editorial_page_card(c):
    """Edito with Card UI."""
    width, height = A4
    
    # Background
    c.setFillColor(COLOR_BG_NUDE)
    c.rect(0,0, width, height, fill=1, stroke=0)
    draw_dot_grid(c, width, height)
    draw_marginal_signature(c, height)

    # Card
    card_margin = 2.5*cm
    card_width = width - 2*card_margin
    card_height = height - 6*cm
    card_y = 3*cm
    draw_card_background(c, card_margin, card_y, card_width, card_height)
    
    # Content inside Card
    text_x = card_margin + 1*cm
    text_top = card_y + card_height - 2*cm
    
    # Title
    c.setFont(FONT_TITLE, 24)
    c.setFillColor(COLOR_ACCENT_BLUE)
    c.drawString(text_x, text_top, "Le mot d'accueil")
    
    # Icon/Quote mark
    if os.path.exists(PATH_GUILLEMETS):
        # Image en haut à droite
        c.drawImage(PATH_GUILLEMETS, text_x + card_width - 3*cm, text_top - 0.5*cm, width=2.5*cm, height=2.5*cm, mask='auto', preserveAspectRatio=True, anchor='ne')
    else:
        c.setFont(FONT_HAND, 60)
        c.setFillColor(COLOR_ACCENT_YELLOW)
        c.drawRightString(text_x + card_width - 2*cm, text_top, ' " ')

    # Body
    text_y = text_top - 2*cm
    c.setFont(FONT_BODY, 11)
    c.setFillColor(COLOR_TEXT_MAIN)
    
    lines = [
        "Si vous entamez la lecture de ce livret, c'est que vous êtes aujourd'hui",
        "en questionnement sur votre parcours professionnel. Bravo !",
        "",
        "Ce livret va être votre guide pendant cette période.",
        "Il sera à la fois source d'idées, d'inspirations, de remises en question...",
        "",
        "Le bilan de compétences que je vous propose est un mélange",
        "de questionnements, d'activités créatives et d'échanges réflexifs.",
        "",
        "Prenez ce temps pour vous retrouver avec vous-même."
    ]
    
    for line in lines:
        c.drawString(text_x, text_y, line)
        text_y -= 16

    c.showPage()

def create_form_page_card(c):
    """Form Page with Card UI."""
    width, height = A4
    
    # Background
    c.setFillColor(COLOR_BG_NUDE)
    c.rect(0,0, width, height, fill=1, stroke=0)
    draw_dot_grid(c, width, height)
    draw_marginal_signature(c, height)
    
    # Card
    card_margin = 2*cm
    card_width = width - 2*card_margin
    card_height = height - 5*cm
    card_y = 2.5*cm
    draw_card_background(c, card_margin, card_y, card_width, card_height)

    # Content
    text_x = card_margin + 1*cm
    text_top = card_y + card_height - 2*cm
    
    c.setFont(FONT_TITLE, 24)
    c.setFillColor(COLOR_ACCENT_BLUE)
    c.drawString(text_x, text_top, "Mon Engagement")

    form = c.acroForm
    start_y = text_top - 2*cm
    
    # 1. Identité
    c.setFont(FONT_BODY, 12)
    c.setFillColor(COLOR_TEXT_MAIN)
    c.drawString(text_x, start_y, "Moi, ")
    
    form.textfield(name='nom_complet', tooltip='Prénom Nom',
                   x=text_x + 1.5*cm, y=start_y-5, width=8*cm, height=20,
                   borderStyle='solid', borderColor=COLOR_ACCENT_BLUE, 
                   forceBorder=True, fillColor=COLOR_WHITE)
    
    # 2. Temps
    start_y -= 2*cm
    c.drawString(text_x, start_y, "décide d'investir")
    form.textfield(name='engagement_hebdo', tooltip='Nb',
                   x=text_x + 3.5*cm, y=start_y-5, width=1.5*cm, height=20,
                   borderStyle='solid', borderColor=COLOR_ACCENT_BLUE,
                   forceBorder=True, fillColor=COLOR_WHITE)
    c.drawString(text_x + 5.5*cm, start_y, "heures par semaine.")
    
    # 3. Objectif
    start_y -= 2*cm
    c.drawString(text_x, start_y, "Mon objectif principal :")
    start_y -= 2.5*cm
    form.textfield(name='objectif_3_mois', tooltip='Objectif',
                   x=text_x, y=start_y, width=card_width - 2*cm, height=2*cm,
                   borderStyle='solid', borderColor=colors.lightgrey, borderWidth=0.5,
                   forceBorder=True, fillColor=COLOR_WHITE)
                   
    # 4. Permission
    start_y -= 2*cm
    c.drawString(text_x, start_y, "Je m'autorise à :")
    start_y -= 2.5*cm
    form.textfield(name='permission_personnelle', tooltip='Permission',
                   x=text_x, y=start_y, width=card_width - 2*cm, height=2*cm,
                   borderStyle='solid', borderColor=colors.lightgrey, borderWidth=0.5,
                   forceBorder=True, fillColor=COLOR_WHITE)
    
    # 5. Signature Area
    start_y -= 3*cm
    c.drawString(text_x, start_y, "Date :")
    form.textfield(name='date_signature', tooltip='Date',
                   x=text_x + 1.5*cm, y=start_y-5, width=4*cm, height=20,
                   borderStyle='solid', forceBorder=True, fillColor=COLOR_WHITE)
    
    c.drawString(text_x + 8*cm, start_y, "Signature :")
    form.textfield(name='signature', tooltip='Signature',
                   x=text_x + 10.5*cm, y=start_y-15, width=5*cm, height=30,
                   borderStyle='solid', forceBorder=True, fillColor=COLOR_WHITE)

    # Hidden Fields
    form.textfield(name='meta_doc_type', value='workbook_chap0', x=0, y=-10, width=0, height=0)
    form.textfield(name='meta_doc_version', value='1.2_da_v4', x=0, y=-10, width=0, height=0)

    c.showPage()

def build_complete_pdf_v4(output_filename):
    c = canvas.Canvas(output_filename, pagesize=A4)
    create_cover_page(c)
    create_summary_page(c)     # New Blue Page
    create_editorial_page_card(c) # New Card UI Page
    create_form_page_card(c)      # New Card UI Page
    c.save()
    print(f"PDF 'DA V4' Generated: {output_filename}")

if __name__ == "__main__":
    final_output = "Workbook_Chap0_Final.pdf"
    build_complete_pdf_v4(final_output)
