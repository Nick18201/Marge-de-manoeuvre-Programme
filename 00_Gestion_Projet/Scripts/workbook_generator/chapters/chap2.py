
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm

from ..config import PDFStyle
from ..components import (
    draw_page_background, draw_dot_grid, draw_card, draw_side_panel, 
    draw_leaf, draw_title, draw_branding_logo, draw_section_separator
)
from ..forms import create_input_field

def create_chap2_cover(c):
    """
    Cover Page for Chapter 2: Mes Racines.
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
    # Using Chap 0 logic or placeholder
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

    # 3. Titres Specific to Chap 2
    c.setFont(PDFStyle.FONT_BODY, 14)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    c.drawRightString(width - 40, height - 210, "BILAN DE COMPÉTENCES & ALIGNEMENT") 
    
    c.setFont(PDFStyle.FONT_TITLE, 18)
    c.setFillColor(PDFStyle.COLOR_ACCENT_RED)
    c.drawRightString(width - 40, height - 240, "CHAPITRE 2 : MES RACINES")
    
    c.showPage()

def create_psycho_edu_pages(c):
    """
    Psycho-education pages: Comprendre ses Racines.
    Expanded to 3 pages to cover all content from Psycho-education.md.
    """
    width, height = A4
    
    # --- PAGE 1: INTRO & HABITUS ---
    draw_page_background(c, width, height)
    draw_title(c, "Comprendre ses Racines", 2*cm, height - 2.5*cm)
    c.setFont(PDFStyle.FONT_SUBTITLE, 12)
    c.setFillColor(PDFStyle.COLOR_ACCENT_BLUE)
    c.drawString(2*cm, height - 3.2*cm, "Pour choisir son avenir")

    text_x = 2*cm
    text_y = height - 4.5*cm
    line_height = 14 # Slightly tighter
    
    def draw_paragraph_block(canvas, title, lines, y_start, color_title=PDFStyle.COLOR_ACCENT_RED):
        curr_y = y_start
        if title:
            canvas.setFont(PDFStyle.FONT_SUBTITLE, 12)
            canvas.setFillColor(color_title)
            canvas.drawString(text_x, curr_y, title)
            curr_y -= line_height * 1.5
        
        canvas.setFont(PDFStyle.FONT_BODY, 10)
        canvas.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
        for line in lines:
            if line.strip() == "":
                curr_y -= line_height * 0.5
            else:
                canvas.drawString(text_x, curr_y, line)
                curr_y -= line_height
        return curr_y - line_height * 1.5

    # Introduction
    intro_lines = [
        "Dans un bilan de compétences, on pense souvent qu'il suffit de lister ses savoir-faire pour trouver sa",
        "voie. C'est une erreur. Vous n'êtes pas seulement une somme de compétences techniques ; vous êtes",
        "le résultat d'une histoire.",
        "",
        "Votre façon de travailler, votre rapport à l'argent, à l'autorité ou à la réussite ne viennent pas de",
        "nulle part. Ils ont été façonnés par votre famille et votre milieu d'origine. Ce document a pour but",
        "de vous aider à repérer ces « bagages invisibles » pour faire le tri : que voulez-vous garder ?",
        "Que devez-vous laisser au vestiaire pour enfin vous épanouir professionnellement ?"
    ]
    text_y = draw_paragraph_block(c, "Introduction : Pourquoi regarder en arrière ?", intro_lines, text_y)

    # 1. Le Sac à Dos Social
    habitus_lines = [
        "Imaginez que vous avez un logiciel installé en vous depuis l'enfance. Ce logiciel, c'est l'Habitus :",
        "votre manière spontanée de réagir, de parler, de vous tenir, héritée de vos parents et de votre",
        "milieu social.",
        "",
        "Pourquoi c'est important ? Si vous changez de milieu professionnel (exemple : d'une famille",
        "d'ouvriers vers un poste de cadre, ou l'inverse), ce logiciel peut bugger.",
        "Vous pouvez ressentir un décalage permanent, une gêne, comme si vous portiez un costume mal taillé."
    ]
    text_y = draw_paragraph_block(c, "1. Le « Sac à Dos » Social (L'Habitus)", habitus_lines, text_y)

    # Sentiment d'illégitimité
    imposteur_lines = [
        "« Un jour, ils vont se rendre compte que je ne suis pas à la hauteur »...",
        "C'est souvent le signe d'une Névrose de Classe. Ce n'est pas une maladie, mais un conflit intérieur.",
        "",
        "• Le Parvenu : Si vous réussissez mieux que vos parents, vous pouvez ressentir une culpabilité",
        "  (peur de les abandonner).",
        "• Le Déclassé : Si votre situation est moins prestigieuse, vous pouvez ressentir de la honte.",
        "",
        "Ce sentiment freine : il peut empêcher de demander une augmentation ou pousser à l'épuisement."
    ]
    text_y = draw_paragraph_block(c, "Le sentiment d'illégitimité (Syndrome de l'Imposteur)", imposteur_lines, text_y, color_title=PDFStyle.COLOR_TEXT_MAIN)

    c.showPage()
    
    # --- PAGE 2: CONTRAT & SOUFFRANCE ---
    draw_page_background(c, width, height)
    draw_title(c, "Comprendre ses Racines (suite)", 2*cm, height - 2.5*cm)
    text_y = height - 4.5*cm

    # 2. Le Contrat Familial
    contrat_lines = [
        "Chaque famille possède un « Grand Livre de Comptes » invisible. On y inscrit ce que l'on doit",
        "à ses parents.",
        "",
        "• Les Loyautés Invisibles (Le « Pilote Automatique ») :",
        "  Parfois, on s'auto-sabote juste avant le but. Pourquoi ? Peut-être pour ne pas dépasser",
        "  inconsciemment ses parents. L'échec devient une façon de dire « Je reste comme vous ».",
        "",
        "• La Réparation :",
        "  Avez-vous choisi votre métier par passion ou pour réparer un drame familial (injustice, maladie) ?",
        "",
        "• Le Mythe Familial :",
        "  « Chez nous, on est des intellectuels », « Chez nous, on est solidaires... ».",
        "  Si votre projet contredit ce mythe, vous rencontrerez une résistance interne."
    ]
    text_y = draw_paragraph_block(c, "2. Le Contrat Familial Secret", contrat_lines, text_y)

    # 3. Souffrance au Travail
    souffrance_lines = [
        "Le travail, ce n'est pas juste exécuter une tâche. C'est y mettre du sien.",
        "Quand on ne peut pas faire son travail « bien » (selon ses propres critères), on souffre.",
        "C'est l'activité empêchée.",
        "",
        "Votre souffrance n'est pas une faiblesse. C'est un signal d'intelligence : elle montre que",
        "vous tenez à ce que vous faites.",
        "Le but est de transformer cette plainte en pouvoir d'agir : retrouver une marge de manœuvre."
    ]
    text_y = draw_paragraph_block(c, "3. La Souffrance et le Plaisir au Travail", souffrance_lines, text_y)

    c.showPage()

    # --- PAGE 3: PISTES ET OUTILS ---
    draw_page_background(c, width, height)
    draw_title(c, "Les Outils pour Avancer", 2*cm, height - 2.5*cm)
    text_y = height - 4.5*cm

    pistes_lines = [
        "Voici trois pistes pour débloquer votre situation et transformer votre héritage :",
        ""
    ]
    text_y = draw_paragraph_block(c, "4. Pistes pour votre Bilan", pistes_lines, text_y)

    # A. Génogramme du Coeur
    geno_lines = [
        "Ne restez pas seul avec votre arbre généalogique officiel. Identifiez vos « tuteurs de résilience ».",
        "Qui vous a donné confiance ? Qui vous a transmis des valeurs positives ?",
        "Appuyez-vous sur eux plutôt que sur les figures qui vous ont jugé."
    ]
    text_y = draw_paragraph_block(c, "A. Le Génogramme du Cœur", geno_lines, text_y, color_title=PDFStyle.COLOR_ACCENT_BLUE)

    # B. Roman Familial
    roman_lines = [
        "Repérez les répétitions et les « phrases poisons » (« Il faut souffrir pour réussir »).",
        "Prendre conscience de ces phrases, c'est ne plus les laisser diriger votre vie."
    ]
    text_y = draw_paragraph_block(c, "B. Le Roman Familial", roman_lines, text_y, color_title=PDFStyle.COLOR_ACCENT_BLUE)

    # C. Objectif
    obj_lines = [
        "L'objectif est de Réussir sans Trahir.",
        "Vous avez le droit de changer, de réussir, de gagner de l'argent, sans que cela soit une insulte",
        "à votre famille.",
        "Comment honorer les valeurs familiales (courage, honnêteté) sous une forme qui VOUS appartient ?",
        "C'est la différenciation : rester en lien, tout en étant libre d'être soi-même."
    ]
    text_y = draw_paragraph_block(c, "C. L'Objectif : La Différenciation", obj_lines, text_y, color_title=PDFStyle.COLOR_ACCENT_BLUE)

    # Conclusion Box
    draw_card(c, 2*cm, text_y - 3*cm, width - 4*cm, 2.5*cm)
    c.setFont(PDFStyle.FONT_ITALIC, 11)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    c.drawCentredString(width/2, text_y - 1.5*cm, "En éclairant ces zones d'ombre, vous transformez")
    c.drawCentredString(width/2, text_y - 2*cm, "des chaînes invisibles en tremplins.")

    c.showPage()


def create_timeline_page(c):
    """
    Page: Ma Ligne de Vie.
    Vertical Layout.
    """
    width, height = A4
    draw_page_background(c, width, height)
    draw_title(c, "Ma Ligne de Vie (Les Montagnes Russes)", 2*cm, height - 3*cm)

    # Main vertical line
    center_x = width / 2
    margin_top = height - 5*cm
    margin_bottom = 3*cm
    c.setStrokeColor(PDFStyle.COLOR_TEXT_SECONDARY)
    c.setLineWidth(2)
    c.line(center_x, margin_top, center_x, margin_bottom)
    
    # Arrow head at top
    c.line(center_x, margin_top, center_x - 0.2*cm, margin_top - 0.5*cm)
    c.line(center_x, margin_top, center_x + 0.2*cm, margin_top - 0.5*cm)

    # Nodes (Alternating)
    # 3 Sommets (Left), 2 Vallées (Right)
    
    form = c.acroForm
    
    c.setFont(PDFStyle.FONT_SUBTITLE, 12)
    c.setFillColor(PDFStyle.COLOR_ACCENT_BLUE)
    c.drawString(2*cm, margin_top + 0.5*cm, "Les Sommets (Positifs)")
    
    c.setFillColor(PDFStyle.COLOR_ACCENT_RED)
    c.drawRightString(width - 2*cm, margin_top + 0.5*cm, "Les Vallées (Apprentissages)")

    positions = [
        ("Sommet 1", "left", margin_top - 3*cm),
        ("Vallée 1", "right", margin_top - 7*cm),
        ("Sommet 2", "left", margin_top - 11*cm),
        ("Vallée 2", "right", margin_top - 15*cm),
        ("Sommet 3", "left", margin_top - 19*cm),
    ]

    for label, side, y_pos in positions:
        # Dot on line
        c.setFillColor(PDFStyle.COLOR_WHITE)
        c.setStrokeColor(PDFStyle.COLOR_TEXT_MAIN)
        c.circle(center_x, y_pos, 0.15*cm, fill=1, stroke=1)
        
        # Connector
        c.setStrokeColor(PDFStyle.COLOR_TEXT_SECONDARY)
        c.setDash([2, 2])
        if side == "left":
            x_box = 2*cm
            c.line(center_x, y_pos, x_box + 7*cm, y_pos)
        else:
            x_box = center_x + 2*cm
            c.line(center_x, y_pos, x_box, y_pos)
        c.setDash([])

        # Input Box
        # Title placeholder
        c.setFont(PDFStyle.FONT_BODY, 10)
        c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
        c.drawString(x_box, y_pos + 1.2*cm, f"{label} (Date + Quoi) :")
        
        create_input_field(form, f'timeline_{label.replace(" ", "_")}_titre', 
                           x=x_box, y=y_pos + 0.6*cm, 
                           width=7*cm, height=0.5*cm)

        c.drawString(x_box, y_pos + 0.2*cm, "Ce que j'en retiens :" if "Vallée" in label else "Ce que j'ai aimé :")
        create_input_field(form, f'timeline_{label.replace(" ", "_")}_desc', 
                           x=x_box, y=y_pos - 1.5*cm, 
                           width=7*cm, height=1.6*cm, multiline=True)

    c.showPage()

def create_skills_transfer_page(c):
    """
    Page: Mes Compétences de Vie.
    """
    width, height = A4
    draw_page_background(c, width, height)
    draw_title(c, "Mes Compétences de Vie", 2*cm, height - 3*cm)

    c.setFont(PDFStyle.FONT_BODY, 11)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    c.drawString(2*cm, height - 4*cm, "Transformons votre vécu en capital. Je ne pars pas de zéro, je pars de mon expérience.")

    # Table Headers
    y_start = height - 6*cm
    col1_x = 2*cm
    col2_x = width/2 + 1*cm
    col_width = (width - 5*cm) / 2
    
    c.setFont(PDFStyle.FONT_SUBTITLE, 12)
    c.setFillColor(PDFStyle.COLOR_ACCENT_BLUE)
    c.drawString(col1_x, y_start, "L'Expérience Vécue")
    c.drawString(col1_x, y_start - 0.5*cm, "(Ex: Divorce, Voyage, Asso...)")
    
    c.setFillColor(PDFStyle.COLOR_ACCENT_RED)
    c.drawString(col2_x, y_start, "Le Talent Caché / Compétence")
    c.drawString(col2_x, y_start - 0.5*cm, "(Ex: Négociation, Logistique...)")
    
    form = c.acroForm
    
    # Rows
    y_row = y_start - 2*cm
    row_height = 3*cm
    
    for i in range(5):
        # Arrow between columns
        c.setStrokeColor(PDFStyle.COLOR_TEXT_SECONDARY)
        c.setLineWidth(1)
        arrow_y = y_row + row_height/2
        c.line(width/2 - 0.5*cm, arrow_y, width/2 + 0.5*cm, arrow_y)
        c.line(width/2 + 0.5*cm, arrow_y, width/2 + 0.2*cm, arrow_y + 0.1*cm)
        c.line(width/2 + 0.5*cm, arrow_y, width/2 + 0.2*cm, arrow_y - 0.1*cm)
        
        # Left Input
        create_input_field(form, f'skill_exp_{i+1}', 
                           x=col1_x, y=y_row, 
                           width=col_width, height=row_height - 0.5*cm, 
                           multiline=True, tooltip=f"Expérience {i+1}")
        
        # Right Input
        create_input_field(form, f'skill_talent_{i+1}', 
                           x=col2_x, y=y_row, 
                           width=col_width, height=row_height - 0.5*cm, 
                           multiline=True, tooltip=f"Talent {i+1}")

        y_row -= row_height

    c.showPage()

def create_heritage_page(c):
    """
    Page: Mon Héritage (3FVS - Genogramme Simplifié).
    Focus: Transmissions, Loyautés, Mandats.
    """
    width, height = A4
    draw_page_background(c, width, height)
    draw_title(c, "Mon Héritage (Matrice 3FVS)", 2*cm, height - 3*cm)
    
    c.setFont(PDFStyle.FONT_BODY, 11)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    c.drawString(2*cm, height - 4*cm, "Identifiez ce que vous avez reçu pour décider de ce que vous en faites.")

    form = c.acroForm
    
    # BOXES LAYOUT
    box_w = width - 4*cm
    box_h = 3*cm
    y_cursor = height - 5.5*cm
    
    # 1. FORCES (Ce que je garde)
    c.setFont(PDFStyle.FONT_SUBTITLE, 12)
    c.setFillColor(PDFStyle.COLOR_ACCENT_BLUE)
    c.drawString(2*cm, y_cursor, "1. FORCES (Ce que je garde / Résilience)")
    
    c.setFont(PDFStyle.FONT_BODY, 10)
    c.setFillColor(PDFStyle.COLOR_TEXT_SECONDARY)
    c.drawString(2*cm, y_cursor - 0.5*cm, "Quelles qualités, valeurs ou savoir-faire de ma famille sont des atouts pour moi ?")
    
    create_input_field(form, 'heritage_forces', x=2*cm, y=y_cursor - 4*cm, width=box_w, height=3*cm, multiline=True)
    
    # 2. VIGILANCES (Ce que je laisse)
    y_cursor -= 6*cm
    c.setFont(PDFStyle.FONT_SUBTITLE, 12)
    c.setFillColor(PDFStyle.COLOR_ACCENT_RED)
    c.drawString(2*cm, y_cursor, "2. VIGILANCES (Ce que je laisse / Schémas)")
    
    c.setFont(PDFStyle.FONT_BODY, 10)
    c.setFillColor(PDFStyle.COLOR_TEXT_SECONDARY)
    c.drawString(2*cm, y_cursor - 0.5*cm, "Quels comportements ou croyances limitantes je décide de ne pas reproduire ?")
    
    create_input_field(form, 'heritage_vigilances', x=2*cm, y=y_cursor - 4*cm, width=box_w, height=3*cm, multiline=True)
    
    # 3. SOUHAITS (Mandats & Dettes)
    y_cursor -= 6*cm
    c.setFont(PDFStyle.FONT_SUBTITLE, 12)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    c.drawString(2*cm, y_cursor, "3. SOUHAITS & COMPTES (Mandats Familiaux)")
    
    c.setFont(PDFStyle.FONT_BODY, 10)
    c.setFillColor(PDFStyle.COLOR_TEXT_SECONDARY)
    c.drawString(2*cm, y_cursor - 0.5*cm, "Qu'est-ce qu'on voulait pour moi ? A qui ai-je l'impression de devoir quelque chose ?")
    
    create_input_field(form, 'heritage_souhaits', x=2*cm, y=y_cursor - 4*cm, width=box_w, height=3*cm, multiline=True)

    # Note bas de page
    c.setFont(PDFStyle.FONT_ITALIC, 10)
    c.drawCentredString(width/2, 2*cm, "On ne trahit pas ses origines en choisissant sa propre voie. On les honore différemment.")

    c.showPage()

def create_mentors_page(c):
    """
    Page: Mentors & Anti-Modèles.
    """
    width, height = A4
    draw_page_background(c, width, height)
    draw_title(c, "Mentors & Anti-Modèles", 2*cm, height - 3*cm)

    # 1. Mentors
    y_start = height - 5*cm
    c.setFont(PDFStyle.FONT_SUBTITLE, 14)
    c.setFillColor(PDFStyle.COLOR_ACCENT_BLUE)
    c.drawString(2*cm, y_start, "Mes Mentors (Inspirations)")
    
    c.setFont(PDFStyle.FONT_BODY, 11)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    c.drawString(2*cm, y_start - 0.7*cm, "Qui est votre héros professionnel (réel ou fictif) et pourquoi ?")
    
    form = c.acroForm
    create_input_field(form, 'mentors_positif', 
                       x=2*cm, y=y_start - 6*cm, 
                       width=width - 4*cm, height=5*cm, 
                       multiline=True, tooltip="J'admire X pour...")

    # 2. Anti-Modèles
    y_anti = y_start - 7.5*cm
    c.setFont(PDFStyle.FONT_SUBTITLE, 14)
    c.setFillColor(PDFStyle.COLOR_ACCENT_RED)
    c.drawString(2*cm, y_anti, "Mes Anti-Modèles (Repoussoirs)")
    
    c.setFont(PDFStyle.FONT_BODY, 11)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    c.drawString(2*cm, y_anti - 0.7*cm, "Identifiez des comportements ou situations que vous refusez de reproduire.")
    c.drawString(2*cm, y_anti - 1.2*cm, "Cela ne signifie pas rejeter la personne entière, mais trier l'héritage.")
    
    create_input_field(form, 'mentors_negatif', 
                       x=2*cm, y=y_anti - 6.5*cm, 
                       width=width - 4*cm, height=5*cm, 
                       multiline=True, tooltip="Je ne veux pas reproduire...")
                       
    c.showPage()

def create_work_image_page(c):
    """
    New Page: Image du Monde du Travail.
    Based on Exercice_Image_Travail.md
    """
    width, height = A4
    draw_page_background(c, width, height)
    draw_title(c, "Image du Monde du Travail", 2*cm, height - 3*cm)

    form = c.acroForm
    y_cursor = height - 4.5*cm

    # 1. Consigne de Visualisation
    c.setFont(PDFStyle.FONT_SUBTITLE, 12)
    c.setFillColor(PDFStyle.COLOR_ACCENT_BLUE)
    c.drawString(2*cm, y_cursor, "1. Exploration Sensorielle & Emotionnelle")
    
    y_cursor -= 1*cm
    c.setFont(PDFStyle.FONT_BODY, 10)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    c.drawString(2*cm, y_cursor, "Fermez les yeux. Visualisez le lieu de travail de vos parents (ou figures parentales).")
    y_cursor -= 0.5*cm
    c.drawString(2*cm, y_cursor, "Quelles sont les odeurs ? Les bruits ? La lumière ? L'ambiance générale ?")
    
    y_cursor -= 3*cm
    create_input_field(form, 'image_sensorielle', 
                       x=2*cm, y=y_cursor, 
                       width=width - 4*cm, height=2.5*cm, 
                       multiline=True, tooltip="Décrivez l'ambiance sensorielle du travail de vos parents...")
    
    # 2. Héritage Familial
    y_cursor -= 1.5*cm
    c.setFont(PDFStyle.FONT_SUBTITLE, 12)
    c.setFillColor(PDFStyle.COLOR_ACCENT_RED)
    c.drawString(2*cm, y_cursor, "2. L'Héritage Familial")
    
    questions = [
        ("Quel était le travail de vos parents / grands-parents ?", "image_metiers", 1.5*cm),
        ("Quelle était leur relation au travail ? (Plaisir, Souffrance, Ennui...)", "image_relation", 1.5*cm),
        ("Comment leur travail influençait-il la vie de famille ? (Stress, Absences, Argent...)", "image_impact_famille", 1.5*cm),
        ("Comment ont-ils influencé vos choix ? (Encouragements, Dissuasions...)", "image_influence_choix", 1.5*cm)
    ]

    y_cursor -= 0.8*cm
    for q_text, q_id, q_height in questions:
        c.setFont(PDFStyle.FONT_BODY, 10)
        c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
        c.drawString(2*cm, y_cursor, q_text)
        y_cursor -= q_height + 0.2*cm
        create_input_field(form, q_id, x=2*cm, y=y_cursor, width=width-4*cm, height=q_height, multiline=True)
        y_cursor -= 0.6*cm

    # 3. Les Mots du Travail
    # Split into 2 columns
    y_cursor -= 1*cm
    c.setFont(PDFStyle.FONT_SUBTITLE, 12)
    c.setFillColor(PDFStyle.COLOR_ACCENT_BLUE)
    c.drawString(2*cm, y_cursor + 0.5*cm, "3. Changer de Regard")

    col_width = (width - 5*cm) / 2
    
    # Col 1: Avant
    c.setFont(PDFStyle.FONT_ITALIC, 10)
    c.setFillColor(PDFStyle.COLOR_TEXT_SECONDARY)
    c.drawString(2*cm, y_cursor, "5 Mots associés au travail (Héritage) :")
    create_input_field(form, 'image_mots_heritage', x=2*cm, y=y_cursor - 3*cm, width=col_width, height=2.8*cm, multiline=True)

    # Col 2: Futur
    c.setFillColor(PDFStyle.COLOR_ACCENT_BLUE)
    c.drawString(width/2 + 0.5*cm, y_cursor, "5 Mots pour mon futur travail (Désir) :")
    create_input_field(form, 'image_mots_futur', x=width/2 + 0.5*cm, y=y_cursor - 3*cm, width=col_width, height=2.8*cm, multiline=True)

    c.showPage()

def create_analysis_parcours_pages(c):
    """
    New Pages: Analyse du Parcours & des Moteurs.
    3 Pages:
    1. Etudes & Formations
    2. Expériences Pro
    3. Bilan & Moteurs
    """
    width, height = A4
    form = c.acroForm
    
    # --- PAGE 1: FORMATIONS ---
    draw_page_background(c, width, height)
    draw_title(c, "Analyse du Parcours : Études & Formations", 2*cm, height - 3*cm)
    
    c.setFont(PDFStyle.FONT_BODY, 11)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    c.drawString(2*cm, height - 4*cm, "Analysez vos motivations pour chaque étape majeure de votre formation.")

    # Table Header
    y_header = height - 5.5*cm
    col_x = [2*cm, 4*cm, 9*cm, 14*cm] # x positions for Année, Nom, Motiv, Compétences
    col_w = [2*cm, 5*cm, 5*cm, 5*cm]
    
    headers = ["Année", "Formation / Sujet", "Motivations (Pourquoi ?)", "Compétences acquises"]
    
    c.setFillColor(PDFStyle.COLOR_ACCENT_BLUE)
    c.setFont(PDFStyle.FONT_SUBTITLE, 10)
    for i, h in enumerate(headers):
        c.drawString(col_x[i], y_header, h)
        
    # Table Rows (4 rows)
    y_row = y_header - 1*cm
    row_h = 3*cm
    
    for i in range(5):
        for j, w in enumerate(col_w):
            create_input_field(form, f'form_row{i}_col{j}', 
                               x=col_x[j], y=y_row - row_h + 0.2*cm, 
                               width=w - 0.2*cm, height=row_h - 0.4*cm, 
                               multiline=True)
        y_row -= row_h

    c.showPage()

    # --- PAGE 2: EXPERIENCES PRO ---
    draw_page_background(c, width, height)
    draw_title(c, "Analyse du Parcours : Expériences Pro", 2*cm, height - 3*cm)
    
    c.setFont(PDFStyle.FONT_BODY, 11)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    c.drawString(2*cm, height - 4*cm, "Vos expériences les plus significatives (Salarié, Stage, Bénévolat...).")

    # Table Header
    y_header = height - 5.5*cm
    col_x = [2*cm, 4*cm, 9*cm, 14*cm] 
    col_w = [2*cm, 5*cm, 5*cm, 5*cm]
    
    headers = ["Année", "Poste / Structure", "Motivations pour ce poste", "Missions principales"]
    
    c.setFillColor(PDFStyle.COLOR_ACCENT_RED)
    c.setFont(PDFStyle.FONT_SUBTITLE, 10)
    for i, h in enumerate(headers):
        c.drawString(col_x[i], y_header, h)
        
    y_row = y_header - 1*cm
    for i in range(5):
        for j, w in enumerate(col_w):
            create_input_field(form, f'exp_row{i}_col{j}', 
                               x=col_x[j], y=y_row - row_h + 0.2*cm, 
                               width=w - 0.2*cm, height=row_h - 0.4*cm, 
                               multiline=True)
        y_row -= row_h

    c.showPage()

    # --- PAGE 3: BILAN & MOTEURS ---
    draw_page_background(c, width, height)
    draw_title(c, "Analyse Transversale & Moteurs", 2*cm, height - 3*cm)
    
    # 3.1 J'aime / J'aime pas
    y_cursor = height - 4.5*cm
    c.setFont(PDFStyle.FONT_SUBTITLE, 12)
    c.setFillColor(PDFStyle.COLOR_ACCENT_BLUE)
    c.drawString(2*cm, y_cursor, "1. Ce que j'ai appris sur mes goûts")
    
    y_cursor -= 0.8*cm
    col1_x = 2*cm
    col2_x = width/2 + 0.5*cm
    w_box = (width - 5*cm)/2
    
    c.setFont(PDFStyle.FONT_BODY, 10)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    c.drawString(col1_x, y_cursor, "Ce que j'ai AIMÉ (Tâches, ambiances...) :")
    c.drawString(col2_x, y_cursor, "Ce que je n'ai PAS AIMÉ :")
    
    y_cursor -= 4*cm
    create_input_field(form, 'bilan_jaime', x=col1_x, y=y_cursor, width=w_box, height=3.5*cm, multiline=True)
    create_input_field(form, 'bilan_padjaime', x=col2_x, y=y_cursor, width=w_box, height=3.5*cm, multiline=True)

    # 3.2 Analyse Transversale
    y_cursor -= 1.5*cm
    c.setFont(PDFStyle.FONT_SUBTITLE, 12)
    c.setFillColor(PDFStyle.COLOR_ACCENT_RED)
    c.drawString(2*cm, y_cursor, "2. Analyse Transversale (Les Schémas)")
    
    y_cursor -= 0.8*cm
    c.setFont(PDFStyle.FONT_BODY, 10)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    c.drawString(2*cm, y_cursor, "En regardant votre parcours, qu'observez-vous ? (Répétitions, Choix par défaut, Hasard...)")
    
    y_cursor -= 3*cm
    create_input_field(form, 'bilan_schemas', x=2*cm, y=y_cursor, width=width-4*cm, height=2.5*cm, multiline=True)

    # 3.3 Les Moteurs
    y_cursor -= 1.5*cm
    c.setFont(PDFStyle.FONT_SUBTITLE, 12)
    c.setFillColor(PDFStyle.COLOR_ACCENT_BLUE)
    c.drawString(2*cm, y_cursor, "3. Mes 5 Moteurs Principaux")
    c.setFont(PDFStyle.FONT_ITALIC, 10)
    c.drawString(2*cm, y_cursor - 0.5*cm, "Qu'est-ce qui vous fait avancer ? (Ex: Argent, Reconnaissance, Utilité, Apprendre, Autonomie...)")
    
    y_cursor -= 1.5*cm
    for i in range(1, 6):
        create_input_field(form, f'moteur_{i}', x=2*cm, y=y_cursor, width=width-4*cm, height=0.8*cm)
        c.drawString(1.2*cm, y_cursor + 0.2*cm, f"{i}.")
        y_cursor -= 1.2*cm


    c.showPage()

def create_tree_of_life_page(c):
    """
    New Page: L'Arbre de Vie.
    Distinct from Genogramme.
    Structure: Racines, Sol, Tronc, Branches, Feuilles, Fruits.
    """
    width, height = A4
    draw_page_background(c, width, height)
    draw_title(c, "Mon Arbre de Vie", 2*cm, height - 3*cm)

    c.setFont(PDFStyle.FONT_BODY, 11)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    c.drawString(2*cm, height - 4*cm, "Restaurer son identité narrative : vous n'êtes pas réduit à vos cicatrices.")

    form = c.acroForm
    
    # Visual Layout
    # Center X
    cx = width / 2
    ground_y = 6*cm
    
    # DRAWING THE TREE (Schematic)
    c.setStrokeColor(PDFStyle.COLOR_TEXT_SECONDARY)
    c.setLineWidth(2)
    
    # 1. Sol (Line)
    c.line(2*cm, ground_y, width-2*cm, ground_y)
    
    # 2. Tronc (Rect)
    trunk_w = 4*cm
    trunk_h = 8*cm
    trunk_bottom = ground_y
    c.rect(cx - trunk_w/2, trunk_bottom, trunk_w, trunk_h, stroke=1, fill=0)
    
    # 3. Racines (Lines below)
    c.line(cx - 1*cm, ground_y, cx - 3*cm, ground_y - 2*cm)
    c.line(cx + 1*cm, ground_y, cx + 3*cm, ground_y - 2*cm)
    c.line(cx, ground_y, cx, ground_y - 2.5*cm)
    
    # 4. Branches (Lines above)
    crown_bottom = trunk_bottom + trunk_h
    c.line(cx, crown_bottom, cx, crown_bottom + 4*cm)
    c.line(cx - 2*cm, crown_bottom, cx - 5*cm, crown_bottom + 3*cm)
    c.line(cx + 2*cm, crown_bottom, cx + 5*cm, crown_bottom + 3*cm)
    
    # --- INPUT ZONES ---
    
    # Zone 1: RACINES (Bottom Center)
    c.setFont(PDFStyle.FONT_SUBTITLE, 10)
    c.setFillColor(PDFStyle.COLOR_ACCENT_RED)
    c.drawCentredString(cx, 3.5*cm, "1. RACINES (D'où je viens, mon histoire)")
    create_input_field(form, 'arbre_racines', x=cx - 4*cm, y=1.5*cm, width=8*cm, height=1.8*cm, multiline=True)

    # Zone 2: SOL (Left Bottom)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    c.drawString(3.5*cm, ground_y + 1*cm, "2. SOL (Besoins actuels)")
    create_input_field(form, 'arbre_sol', x=1*cm, y=ground_y - 1.5*cm, width=5*cm, height=2*cm, multiline=True)

    # Zone 3: TRONC (Center Middle)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    c.drawCentredString(cx, ground_y + trunk_h/2 + 3.5*cm, "3. TRONC (Compétences & Valeurs)")
    create_input_field(form, 'arbre_tronc', x=cx - 1.8*cm, y=ground_y + 1*cm, width=3.6*cm, height=6*cm, multiline=True)

    # Zone 4: BRANCHES (Top Center)
    c.setFillColor(PDFStyle.COLOR_ACCENT_BLUE)
    c.drawCentredString(cx, height - 5*cm, "4. BRANCHES (Projets & Espoirs)")
    create_input_field(form, 'arbre_branches', x=cx - 4*cm, y=height - 7*cm, width=8*cm, height=1.8*cm, multiline=True)

    # Zone 5: FEUILLES (Left Top)
    c.setFillColor(PDFStyle.COLOR_TEXT_SECONDARY)
    c.drawString(3*cm, height - 6*cm, "5. FEUILLES (Club de Vie)")
    create_input_field(form, 'arbre_feuilles', x=1*cm, y=height - 9*cm, width=5*cm, height=2.5*cm, multiline=True, tooltip="Personnes soutiens")

    # Zone 6: FRUITS (Right Top)
    c.drawString(width - 3*cm, height - 6*cm, "6. FRUITS (Cadeaux de la vie)")
    create_input_field(form, 'arbre_fruits', x=width - 6*cm, y=height - 9*cm, width=5*cm, height=2.5*cm, multiline=True, tooltip="Réussites, bonheurs")

    c.showPage()
