import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm

from ..config import PDFStyle
from ..components import (
    draw_page_background, draw_dot_grid, draw_card, draw_side_panel, 
    draw_leaf, draw_title, draw_branding_logo
)
from ..forms import create_input_field

def create_chap1_cover(c):
    """
    Cover Page for Chapter 1: L'État des Lieux.
    """
    width, height = A4
    
    # 1. Background Nude + Grid
    c.setFillColor(PDFStyle.COLOR_BG_NUDE)
    c.rect(0,0, width, height, fill=1, stroke=0)
    draw_dot_grid(c, width, height)

    # 1b. Blue Side Band (Left)
    band_width = 3.5*cm 
    c.setFillColor(PDFStyle.COLOR_ACCENT_BLUE)
    c.rect(0, 0, band_width, height, fill=1, stroke=0)

    # A. Illustration Principale (Cover)
    # Using the same logic as Chap 0 for now, or a placeholder if a specific Chap 1 image exists
    # For now, we reuse the cover illustration or a shape
    if os.path.exists(PDFStyle.PATH_ILLU_COVER):
        content_width = width - band_width
        img_width = content_width * 0.95 
        center_x = band_width + (content_width - img_width) / 2
        
        c.drawImage(PDFStyle.PATH_ILLU_COVER, center_x, height * 0.20, width=img_width, height=height*0.5, mask='auto', preserveAspectRatio=True, anchor='sw')
    else:
        # Fallback
        c.setFillColor(PDFStyle.COLOR_WHITE)
        c.circle(width*0.35, height*0.55, 160, fill=1, stroke=0)

    # 2b. Marque Header
    logo_x = band_width + 1.5*cm
    logo_y = height - 3*cm
    draw_branding_logo(c, logo_x, logo_y, size=40)

    # 2c. Stamp Rouge
    if os.path.exists(PDFStyle.PATH_STAMP):
        c.saveState()
        c.translate(width - 4*cm, 4*cm)
        c.rotate(-15)
        c.drawImage(PDFStyle.PATH_STAMP, -2*cm, -2*cm, width=4*cm, height=4*cm, mask='auto', preserveAspectRatio=True, anchor='c')
        c.restoreState()

    # 3. Titres Specific to Chap 1
    c.setFont(PDFStyle.FONT_BODY, 14)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    c.drawRightString(width - 40, height - 210, "BILAN DE COMPÉTENCES & ALIGNEMENT") 
    
    c.setFont(PDFStyle.FONT_TITLE, 18)
    c.setFillColor(PDFStyle.COLOR_ACCENT_RED)
    c.drawRightString(width - 40, height - 240, "CHAPITRE 1 : L'ÉTAT DES LIEUX")
    
    c.showPage()

def create_engagement_page(c):
    """
    Page 1: Mon Engagement.
    Text heavy page with signature.
    """
    width, height = A4
    draw_page_background(c, width, height)
    
    # Card
    card_margin = 2*cm
    card_width = width - 2*card_margin
    card_height = height - 4*cm
    card_y = 2*cm
    draw_card(c, card_margin, card_y, card_width, card_height)

    # Content
    text_x = card_margin + 1.5*cm
    text_top = card_y + card_height - 2*cm
    
    draw_title(c, "Mon Engagement", text_x, text_top)
    
    # Body
    text_y = text_top - 2*cm
    c.setFont(PDFStyle.FONT_BODY, 11)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    
    lines = [
        "Je m'engage aujourd'hui à prendre ce temps pour moi.",
        "À regarder ma situation avec honnêteté et bienveillance.",
        "À accepter de ne pas avoir toutes les réponses tout de suite.",
        "À explorer, tester, et avancer pas à pas.",
        "",
        "Ce travail est pour moi, et je décide de m'y investir pleinement."
    ]
    
    for line in lines:
        c.drawString(text_x, text_y, line)
        text_y -= 18

    # Signature Area
    sig_y = text_y - 4*cm
    c.drawString(text_x, sig_y + 2*cm, "Date et Signature :")
    
    # Signature Box
    form = c.acroForm
    create_input_field(form, 'signature_engagement',
                       x=text_x, y=sig_y, width=10*cm, height=1.5*cm,
                       tooltip='Votre Signature')
                       
    c.showPage()

def create_concept_page(c):
    """
    Page 2: Chapter Cover - 1. Concept
    Blue background, large watermark.
    """
    width, height = A4
    
    # 1. Full Blue Background
    c.setFillColor(PDFStyle.COLOR_ACCENT_BLUE)
    c.rect(0, 0, width, height, fill=1, stroke=0)
    
    # Faint Grid
    draw_dot_grid(c, width, height, color=PDFStyle.COLOR_WHITE, opacity=0.1)

    # 2. Large Number "1."
    c.saveState()
    c.setFont(PDFStyle.FONT_BRANDING, 160) 
    c.setFillColor(PDFStyle.COLOR_WHITE, alpha=0.12)
    c.drawString(1.5*cm, height - 9*cm, "1.")
    c.restoreState()

    # 3. Titles
    start_y = height - 10*cm
    c.setFont(PDFStyle.FONT_BRANDING, 32)
    c.setFillColor(PDFStyle.COLOR_WHITE)
    c.drawString(2.5*cm, start_y, "Concept")
    
    # Points
    points = [
        ("Moment :", "Généré suite à la Séance 1"),
        ("Objectif :", "Clarifier la demande, poser la 'Boussole' et vider le 'Sac à dos'."),
        ("Mots-clés :", "Clarté, Soulagement, Direction")
    ]
    
    text_y = start_y - 3*cm
    c.setFont(PDFStyle.FONT_BODY, 14)
    
    for label, desc in points:
        c.setFont(PDFStyle.FONT_TITLE, 14)
        c.drawString(2.5*cm, text_y, label)
        
        c.setFont(PDFStyle.FONT_BODY, 14)
        label_width = c.stringWidth(label, PDFStyle.FONT_TITLE, 14)
        c.drawString(2.5*cm + label_width + 10, text_y, desc)
        
        text_y -= 1.5*cm

    # Decor (Plume)
    if os.path.exists(PDFStyle.PATH_PLUME_TEXTURE):
        c.saveState()
        c.translate(width - 1*cm, height - 3*cm)
        c.rotate(30)
        c.drawImage(PDFStyle.PATH_PLUME_TEXTURE, 0, 0, width=5*cm, height=5*cm, mask='auto', preserveAspectRatio=True, anchor='ne')
        c.restoreState()

    c.showPage()

def create_meteo_page(c):
    """
    Page 3: Ma Météo Intérieure.
    """
    width, height = A4
    draw_page_background(c, width, height)
    
    card_margin = 2*cm
    card_width = width - 2*card_margin
    card_height = height - 4*cm
    card_y = 2*cm
    draw_card(c, card_margin, card_y, card_width, card_height)

    text_x = card_margin + 1.5*cm
    text_top = card_y + card_height - 2*cm
    
    draw_title(c, "Mon État d'Esprit Actuel", text_x, text_top)
    
    form = c.acroForm
    
    # 1. Visual Options (Soleil, Nuage, Orage) - Represented by text checkboxes
    y_opts = text_top - 2*cm
    c.setFont(PDFStyle.FONT_SUBTITLE, 12)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    c.drawString(text_x, y_opts, "Aujourd'hui, je me sens :")
    
    # Text input for "Émotion dominante" (Un mot pour décrire l'instant)
    create_input_field(form, 'meteo_emotion_word', 
                       x=text_x + 5.5*cm, y=y_opts-5, 
                       width=8*cm, height=20, 
                       tooltip='Un mot pour décrire l\'instant')

    # Options
    options = ["Soleil ☀️", "Nuageux ☁️", "Pluvieux 🌧️", "Orageux ⛈️"]
    opt_x = text_x
    opt_y = y_opts - 1.5*cm
    
    for opt in options:
        create_input_field(form, f'meteo_{opt.split()[0]}', x=opt_x, y=opt_y, width=0.6*cm, height=0.6*cm, tooltip=opt)
        c.drawString(opt_x + 1*cm, opt_y + 0.15*cm, opt)
        opt_x += 4*cm
        
    # 2. Jauge Energie
    y_energy = opt_y - 3*cm
    c.drawString(text_x, y_energy, "Mon niveau d'énergie (/10) :")
    
    # Draw a line 0-10
    c.setStrokeColor(PDFStyle.COLOR_ACCENT_BLUE)
    c.setLineWidth(2)
    c.line(text_x, y_energy - 1*cm, text_x + 10*cm, y_energy - 1*cm)
    
    for i in range(11):
        x_mark = text_x + i*cm
        c.line(x_mark, y_energy - 1.1*cm, x_mark, y_energy - 0.9*cm)
        c.setFont(PDFStyle.FONT_BODY, 8)
        c.drawCentredString(x_mark, y_energy - 1.5*cm, str(i))
        
    # Input for value
    create_input_field(form, 'meteo_energy_val', x=text_x + 11*cm, y=y_energy - 1.2*cm, width=1.5*cm, height=0.8*cm, tooltip='Note')

    # 3. Pensée envahissante
    y_thought = y_energy - 4*cm
    c.setFont(PDFStyle.FONT_SUBTITLE, 12)
    c.drawString(text_x, y_thought, "Ce qui prend le plus de place dans ma tête :")
    
    create_input_field(form, 'meteo_pensee', 
                       x=text_x, y=y_thought - 3*cm, 
                       width=card_width - 3*cm, height=2.5*cm, 
                       tooltip='Pensée envahissante', multiline=True)

    c.showPage()

def create_vision_page(c):
    """
    Page 4: Ma Vision 'Boule à Facettes'.
    4 Quadrants.
    """
    width, height = A4
    draw_page_background(c, width, height)
    
    # Title
    draw_title(c, "Ma Vision 360°", 3*cm, height - 3*cm)
    
    # Instruction
    c.setFont(PDFStyle.FONT_BODY, 11)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    c.drawString(3*cm, height - 4*cm, "Instruction : Pour chaque domaine, écrivez une phrase de synthèse sur votre aspiration.")

    # Center
    center_x = width / 2
    center_y = height / 2 - 1*cm # Shift down slightly
    
    # Draw Axes
    c.setLineWidth(1)
    c.setStrokeColor(PDFStyle.COLOR_ACCENT_BLUE)
    
    # Draw a circle to contain the axes visually (Radar chart style)
    c.circle(center_x, center_y, 7*cm, stroke=1, fill=0)
    c.setLineWidth(0.5)
    c.circle(center_x, center_y, 3.5*cm, stroke=1, fill=0) # Inner circle
    
    c.line(center_x, center_y - 7*cm, center_x, center_y + 7*cm) # Vertical
    c.line(center_x - 7*cm, center_y, center_x + 7*cm, center_y)  # Horizontal

    # Quadrants Labels & Inputs
    # Strict labels from Markdown
    axes = [
        ("Professionnel (Sens, Mission, Salaire)", -1, 1), # Top Left
        ("Personnel (Temps pour soi, Santé)", 1, 1), # Top Right
        ("Social/Familial (Relations, Équilibre)", -1, -1), # Bottom Left
        ("Hiérarchie/Structure (Besoin de cadre vs Liberté)", 1, -1)   # Bottom Right
    ]
    
    form = c.acroForm
    
    for title, dx, dy in axes:
        # Determine specific area center
        # dx, dy are -1 or 1
        q_center_x = center_x + (dx * (3.5*cm)) # Move text closer to center of quadrants
        q_center_y = center_y + (dy * (3.5*cm))
        
        # Draw Title with word wrapping if needed
        c.setFont(PDFStyle.FONT_SUBTITLE, 10)
        c.setFillColor(PDFStyle.COLOR_ACCENT_BLUE) # Blue titles for clarity
        
        # Simple wrap manually for long titles
        words = title.split('(')
        main_title = words[0].strip()
        sub_title = "(" + words[1] if len(words) > 1 else ""
        
        # Adjust text position based on quadrant
        text_y = q_center_y + 1*cm

        c.drawCentredString(q_center_x, text_y, main_title)
        if sub_title:
             c.setFont(PDFStyle.FONT_BODY, 9)
             c.setFillColor(PDFStyle.COLOR_TEXT_SECONDARY)
             c.drawCentredString(q_center_x, text_y - 0.5*cm, sub_title)
        
        # Input Field: "Une phrase de synthèse pour chaque axe" (Phrase de synthèse)
        f_x = q_center_x - 3.5*cm
        f_y = text_y - 3*cm
        create_input_field(form, f'vision_{main_title.strip()}', x=f_x, y=f_y, width=7*cm, height=2*cm, tooltip="Phrase de synthèse", multiline=True)

    c.showPage()

def create_boussole_page(c):
    """
    Page 5: Mon Objectif Boussole.
    """
    width, height = A4
    draw_page_background(c, width, height)
    
    card_margin = 2*cm
    card_width = width - 2*card_margin
    card_height = height - 4*cm
    card_y = 2*cm
    draw_card(c, card_margin, card_y, card_width, card_height)

    text_x = card_margin + 1.5*cm
    text_top = card_y + card_height - 2*cm
    
    draw_title(c, "Mon Objectif Boussole", text_x, text_top)
    
    form = c.acroForm
    
    # Visual Compass (Placeholder Circle)
    c.setStrokeColor(PDFStyle.COLOR_ACCENT_RED)
    c.setLineWidth(3)
    c.circle(width/2, text_top - 3*cm, 1.5*cm, fill=0, stroke=1)
    # North mark
    c.setFont(PDFStyle.FONT_BRANDING, 20)
    c.setFillColor(PDFStyle.COLOR_ACCENT_RED)
    c.drawCentredString(width/2, text_top - 3*cm + 0.8*cm, "N")

    # Main Goal Structure
    # "D'ici 3 mois, je veux avoir clarifié [Enjeu principal] pour pouvoir [Bénéfice concret]."
    
    y_goal = text_top - 6*cm
    c.setFont(PDFStyle.FONT_SUBTITLE, 13)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    c.drawString(text_x, y_goal, "D'ici 3 mois, je veux avoir clarifié :")
    
    create_input_field(form, 'boussole_enjeu', 
                       x=text_x, y=y_goal - 2*cm, 
                       width=card_width - 3*cm, height=1.5*cm, 
                       tooltip='Enjeu principal', multiline=True)
                       
    y_benefit = y_goal - 3*cm
    c.drawString(text_x, y_benefit, "Pour pouvoir :")
    
    create_input_field(form, 'boussole_benefice', 
                       x=text_x, y=y_benefit - 2*cm, 
                       width=card_width - 3*cm, height=1.5*cm, 
                       tooltip='Bénéfice concret', multiline=True)

    # Success Indicator
    y_succes = y_benefit - 3.5*cm
    c.drawString(text_x, y_succes, "Je saurai que j'ai réussi quand :")
    
    create_input_field(form, 'boussole_succes_preuve',
                       x=text_x, y=y_succes - 2.5*cm,
                       width=card_width - 3*cm, height=2*cm,
                       tooltip='Preuve concrète', multiline=True)

    c.showPage()

def create_sac_a_dos_page(c):
    """
    Page 6: Le Sac à Dos.
    Specific prompts from Markdown.
    """
    width, height = A4
    draw_page_background(c, width, height)
    
    card_margin = 2*cm
    card_width = width - 2*card_margin
    card_height = height - 4*cm
    card_y = 2*cm
    draw_card(c, card_margin, card_y, card_width, card_height)

    text_x = card_margin + 1.5*cm
    text_top = card_y + card_height - 2*cm
    
    draw_title(c, "Ce que je dépose aujourd'hui", text_x, text_top)
    c.setFont(PDFStyle.FONT_BODY, 11)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    c.drawString(text_x, text_top - 0.7*cm, "Allégeons le sac à dos. Je décide de déposer :")
    
    form = c.acroForm
    start_y = text_top - 3*cm
    
    # 1. Croyance
    c.setFont(PDFStyle.FONT_SUBTITLE, 12)
    c.setFillColor(PDFStyle.COLOR_ACCENT_BLUE) # Requested Blue
    c.drawString(text_x, start_y, "Je lâche cette croyance :")
    create_input_field(form, 'sac_croyance',
                       x=text_x, y=start_y - 1.5*cm,
                       width=card_width - 3*cm, height=1.2*cm,
                       tooltip='Croyance à lâcher', multiline=True)
    
    # 2. Situation
    start_y -= 2.5*cm
    c.setFillColor(PDFStyle.COLOR_ACCENT_BLUE) # Requested Blue
    c.drawString(text_x, start_y, "Je ne veux plus subir :")
    create_input_field(form, 'sac_subir',
                       x=text_x, y=start_y - 1.5*cm,
                       width=card_width - 3*cm, height=1.2*cm,
                       tooltip='Situation à ne plus subir', multiline=True)

    # 3. Peur
    start_y -= 2.5*cm
    c.setFillColor(PDFStyle.COLOR_ACCENT_BLUE) # Requested Blue
    c.drawString(text_x, start_y, "Ma plus grande peur est :")
    create_input_field(form, 'sac_peur',
                       x=text_x, y=start_y - 1.5*cm,
                       width=card_width - 3*cm, height=1.2*cm,
                       tooltip='Votre peur', multiline=True)
                       
    c.setFont(PDFStyle.FONT_ITALIC, 11)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN) # Reset to black/main for body
    c.drawString(text_x, start_y - 2.2*cm, "...et je décide de la regarder en face.")

    c.showPage()
