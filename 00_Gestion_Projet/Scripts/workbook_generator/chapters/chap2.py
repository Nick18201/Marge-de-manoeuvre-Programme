
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm

from ..config import PDFStyle
from ..components import (
    draw_page_background, draw_dot_grid, draw_card, draw_side_panel, 
    draw_leaf, draw_title, draw_branding_logo, draw_section_separator,
    create_standard_cover, draw_circular_stamp, draw_pause_badge, draw_page_decorations
)
from ..forms import create_input_field

def create_chap2_cover(c):
    """
    Cover Page for Chapter 2: Mes Racines.
    """
    create_standard_cover(c, "CHAPITRE 2 : MES RACINES")

def create_psycho_edu_pages(c):
    """
    Psycho-education pages: Comprendre ses Racines.
    Expanded to 3 pages to cover all content from Psycho-education.md.
    """
    width, height = A4
    
    # --- PAGE 1: INTRO & HABITUS ---
    # Side Panel (Full Height)
    card_margin = 2*cm
    draw_side_panel(c, card_margin, width, height)
    draw_title(c, "Comprendre ses Racines", card_margin + 0.5*cm, height - 2.5*cm)
    c.setFont(PDFStyle.FONT_SUBTITLE, 12)
    c.setFillColor(PDFStyle.COLOR_ACCENT_BLUE)
    c.drawString(card_margin + 0.5*cm, height - 3.2*cm, "Pour choisir son avenir")

    text_x = card_margin + 0.5*cm
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

    draw_page_decorations(c, width, height, part_title="2. MES RACINES", x_offset=card_margin)
    c.showPage()
    
    # --- PAGE 2: CONTRAT & SOUFFRANCE ---
    draw_page_background(c, width, height)
    draw_side_panel(c, card_margin, width, height)
    draw_title(c, "Comprendre ses Racines (suite)", text_x, height - 2.5*cm)
    text_y = height - 4.5*cm

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

    draw_page_decorations(c, width, height, part_title="2. MES RACINES", x_offset=card_margin)
    c.showPage()

    # --- PAGE 3: PISTES ET OUTILS ---
    draw_page_background(c, width, height)
    draw_side_panel(c, card_margin, width, height)
    draw_title(c, "Les Outils pour Avancer", text_x, height - 2.5*cm)
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
    draw_card(c, card_margin + 0.5*cm, text_y - 3*cm, width - card_margin - 1.5*cm, 2.5*cm)
    c.setFont(PDFStyle.FONT_ITALIC, 11)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    center_x = card_margin + (width - card_margin) / 2.0
    c.drawCentredString(center_x, text_y - 1.5*cm, "En éclairant ces zones d'ombre, vous transformez")
    c.drawCentredString(center_x, text_y - 2*cm, "des chaînes invisibles en tremplins.")

    draw_page_decorations(c, width, height, part_title="2. MES RACINES", x_offset=card_margin)
    c.showPage()


def create_timeline_page(c):
    """
    Page: Ma Ligne de Vie.
    Vertical Layout.
    """
    width, height = A4
    draw_page_background(c, width, height)
    card_margin = 2*cm
    draw_side_panel(c, card_margin, width, height)
    draw_title(c, "Ma Ligne de Vie (Les Montagnes Russes)", card_margin + 0.5*cm, height - 3*cm)

    # Main vertical line
    center_x = card_margin + (width - card_margin) / 2.0
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
    c.drawString(card_margin + 0.5*cm, margin_top + 0.5*cm, "Les Sommets (Positifs)")
    
    c.setFillColor(PDFStyle.COLOR_ACCENT_RED)
    c.drawRightString(width - 1.5*cm, margin_top + 0.5*cm, "Les Vallées (Apprentissages)")

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
            x_box = card_margin + 0.5*cm
            c.line(center_x, y_pos, x_box + 7*cm, y_pos)
        else:
            x_box = center_x + 1*cm
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

    draw_page_decorations(c, width, height, part_title="2. MES RACINES", x_offset=card_margin)
    c.showPage()

def create_skills_transfer_page(c):
    """
    Page: Mes Compétences de Vie.
    """
    width, height = A4
    draw_page_background(c, width, height)
    card_margin = 2*cm
    draw_side_panel(c, card_margin, width, height)
    draw_title(c, "Mes Compétences de Vie", card_margin + 0.5*cm, height - 3*cm)

    c.setFont(PDFStyle.FONT_BODY, 11)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    c.drawString(card_margin + 0.5*cm, height - 4*cm, "Transformons votre vécu en capital. Je ne pars pas de zéro, je pars de mon expérience.")

    # Table Headers
    y_start = height - 6*cm
    center_x = card_margin + (width - card_margin) / 2.0
    col1_x = card_margin + 0.5*cm
    col2_x = center_x + 1*cm
    col_width = (width - card_margin - 3*cm) / 2
    
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

    draw_page_decorations(c, width, height, part_title="SÉANCE 3", x_offset=card_margin)
    c.showPage()

def create_heritage_page(c):
    """
    Page: Mon Héritage (3FVS - Genogramme Simplifié).
    Focus: Transmissions, Loyautés, Mandats.
    """
    width, height = A4
    draw_page_background(c, width, height)
    card_margin = 2*cm
    draw_side_panel(c, card_margin, width, height)
    draw_title(c, "Mon Héritage (Matrice 3FVS)", card_margin + 0.5*cm, height - 3*cm)
    
    c.setFont(PDFStyle.FONT_BODY, 11)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    c.drawString(card_margin + 0.5*cm, height - 4*cm, "Identifiez ce que vous avez reçu pour décider de ce que vous en faites.")

    form = c.acroForm
    
    # BOXES LAYOUT
    text_x = card_margin + 0.5*cm
    box_w = width - text_x - 1*cm
    box_h = 3*cm
    y_cursor = height - 5.5*cm
    
    c.setFont(PDFStyle.FONT_SUBTITLE, 12)
    c.setFillColor(PDFStyle.COLOR_ACCENT_BLUE)
    c.drawString(text_x, y_cursor, "1. FORCES (Ce que je garde / Résilience)")
    
    c.setFont(PDFStyle.FONT_BODY, 10)
    c.setFillColor(PDFStyle.COLOR_TEXT_SECONDARY)
    c.drawString(2*cm, y_cursor - 0.5*cm, "Quelles qualités, valeurs ou savoir-faire de ma famille sont des atouts pour moi ?")
    
    create_input_field(form, 'heritage_forces', x=2*cm, y=y_cursor - 4*cm, width=box_w, height=3*cm, multiline=True)
    
    y_cursor -= 6*cm
    c.setFont(PDFStyle.FONT_SUBTITLE, 12)
    c.setFillColor(PDFStyle.COLOR_ACCENT_RED)
    c.drawString(2*cm, y_cursor, "2. VIGILANCES (Ce que je laisse / Schémas)")
    
    c.setFont(PDFStyle.FONT_BODY, 10)
    c.setFillColor(PDFStyle.COLOR_TEXT_SECONDARY)
    c.drawString(2*cm, y_cursor - 0.5*cm, "Quels comportements ou croyances limitantes je décide de ne pas reproduire ?")
    
    create_input_field(form, 'heritage_vigilances', x=2*cm, y=y_cursor - 4*cm, width=box_w, height=3*cm, multiline=True)
    
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

    draw_page_decorations(c, width, height, part_title="SÉANCE 2", x_offset=card_margin)
    c.showPage()

def create_mentors_page(c):
    """
    Page: Mentors & Anti-Modèles.
    """
    width, height = A4
    draw_page_background(c, width, height)
    card_margin = 2*cm
    draw_side_panel(c, card_margin, width, height)
    draw_title(c, "Mentors & Anti-Modèles", card_margin + 0.5*cm, height - 3*cm)

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
                       
    draw_page_decorations(c, width, height, part_title="SÉANCE 2", x_offset=card_margin)
    c.showPage()

def create_work_image_page(c):
    """
    New Page: Image du Monde du Travail.
    Based on Exercice_Image_Travail.md
    """
    width, height = A4
    draw_page_background(c, width, height)
    card_margin = 2*cm
    draw_side_panel(c, card_margin, width, height)
    draw_title(c, "Image du Monde du Travail", card_margin + 0.5*cm, height - 3*cm)

    form = c.acroForm
    y_cursor = height - 4.5*cm

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

    draw_page_decorations(c, width, height, part_title="SÉANCE 2", x_offset=card_margin)
    c.showPage()

def create_analysis_parcours_pages(c):
    """
    Pages: Analyse du Parcours & des Moteurs.
    1 & 2. Blocs d'Expériences (Pro, Etudes, Perso)
    3. Bilan & Moteurs (Schémas et Moteurs)
    """
    width, height = A4
    form = c.acroForm
    card_margin = 2*cm
    
    # --- PAGES 1 & 2: BLOCS D'EXPERIENCES ---
    for page_num in range(2):
        draw_page_background(c, width, height)
        draw_side_panel(c, card_margin, width, height)
        draw_title(c, "Analyse du Parcours", card_margin + 0.5*cm, height - 3*cm)
        
        c.setFont(PDFStyle.FONT_BODY, 11)
        c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
        if page_num == 0:
            c.drawString(2*cm, height - 4*cm, "Transformez votre vécu (études, expériences pro ou persos) en capital compétences.")
        
        y_cursor = height - 5.5*cm
        
        for block_idx in range(2):
            global_exp_idx = page_num * 2 + block_idx + 1
            
            # Draw block Background/Border
            c.setStrokeColor(PDFStyle.COLOR_ACCENT_BLUE if block_idx == 0 else PDFStyle.COLOR_ACCENT_RED)
            c.setLineWidth(1)
            c.roundRect(1.5*cm, y_cursor - 9.5*cm, width - 3*cm, 10*cm, 0.5*cm)
            
            c.setFont(PDFStyle.FONT_SUBTITLE, 11)
            c.setFillColor(PDFStyle.COLOR_ACCENT_BLUE if block_idx == 0 else PDFStyle.COLOR_ACCENT_RED)
            c.drawString(2*cm, y_cursor, f"Expérience {global_exp_idx}")
            
            # Inputs
            # Ligne 1: Titre / Année
            c.setFont(PDFStyle.FONT_BODY, 9)
            c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
            c.drawString(2*cm, y_cursor - 0.7*cm, "Titre de poste et entreprise (ou Sujet d'étude) :")
            create_input_field(form, f'exp_{global_exp_idx}_titre', x=2*cm, y=y_cursor - 1.5*cm, width=10*cm, height=0.6*cm)
            
            c.drawString(13*cm, y_cursor - 0.7*cm, "Année(s) :")
            create_input_field(form, f'exp_{global_exp_idx}_annee', x=13*cm, y=y_cursor - 1.5*cm, width=6*cm, height=0.6*cm)
            
            # Ligne 2: Missions & Compétences (2 columns)
            col_w = (width - 5*cm) / 2
            col1_x = 2*cm
            col2_x = 2.5*cm + col_w
            
            c.drawString(col1_x, y_cursor - 2.2*cm, "Fiche de poste / Missions principales :")
            create_input_field(form, f'exp_{global_exp_idx}_missions', x=col1_x, y=y_cursor - 4.2*cm, width=col_w, height=1.8*cm, multiline=True)
            
            c.drawString(col2_x, y_cursor - 2.2*cm, "Compétences développées (Tech / Softskills) :")
            create_input_field(form, f'exp_{global_exp_idx}_competences', x=col2_x, y=y_cursor - 4.2*cm, width=col_w, height=1.8*cm, multiline=True)
            
            # Ligne 3: Aimé / Pas Aimé (2 columns)
            c.drawString(col1_x, y_cursor - 4.9*cm, "Ce que j'ai aimé :")
            create_input_field(form, f'exp_{global_exp_idx}_aime', x=col1_x, y=y_cursor - 6.9*cm, width=col_w, height=1.8*cm, multiline=True)
            
            c.drawString(col2_x, y_cursor - 4.9*cm, "Ce que je n'ai pas aimé :")
            create_input_field(form, f'exp_{global_exp_idx}_paime', x=col2_x, y=y_cursor - 6.9*cm, width=col_w, height=1.8*cm, multiline=True)
            
            y_cursor -= 10.5*cm

        draw_page_decorations(c, width, height, part_title="SÉANCE 3", x_offset=card_margin)
        c.showPage()

    # --- PAGE 3: BILAN & MOTEURS ---
    draw_page_background(c, width, height)
    draw_side_panel(c, card_margin, width, height)
    draw_title(c, "Analyse Transversale & Moteurs", card_margin + 0.5*cm, height - 3*cm)

    # Introduction Text to the Approach
    text_y = height - 4.2*cm
    c.setFont(PDFStyle.FONT_BODY, 10)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    
    intro_lines = [
        "Maintenant que nous avons balayé vos différentes expériences, prenons de la hauteur.",
        "L'objectif est de dépasser la chronologie pour comprendre votre logique interne.",
        "",
        "Cette analyse sert à identifier votre 'fil rouge' :"
    ]
    for line in intro_lines:
        c.drawString(2*cm, text_y, line)
        text_y -= 0.5*cm
        
    y_cursor = text_y - 1*cm
    c.setFont(PDFStyle.FONT_SUBTITLE, 12)
    c.setFillColor(PDFStyle.COLOR_ACCENT_RED)
    c.drawString(2*cm, y_cursor, "1. Mes Schémas (Mon Fil Rouge)")
    
    y_cursor -= 0.8*cm
    c.setFont(PDFStyle.FONT_BODY, 10)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    c.drawString(2*cm, y_cursor, "En regardant votre parcours global, quelles répétitions ou schémas observez-vous ?")
    c.drawString(2*cm, y_cursor - 0.5*cm, "(Ex: Choisir souvent sous la pression, rechercher l'expertise, aller au clash au bout d'un an, etc.)")
    
    y_cursor -= 4*cm
    create_input_field(form, 'bilan_schemas', x=2*cm, y=y_cursor, width=width-4*cm, height=3.5*cm, multiline=True)

    y_cursor -= 1.5*cm
    c.setFont(PDFStyle.FONT_SUBTITLE, 12)
    c.setFillColor(PDFStyle.COLOR_ACCENT_BLUE)
    c.drawString(2*cm, y_cursor, "2. Mes Moteurs Fondamentaux")
    y_cursor -= 0.5*cm
    c.setFont(PDFStyle.FONT_ITALIC, 10)
    c.drawString(2*cm, y_cursor, "Qu'est-ce qui vous fait intimement avancer durablement ?")
    c.drawString(2*cm, y_cursor - 0.4*cm, "(Ex: Indépendance, Sécurité financière, Apprendre, Altruisme, Compétition, Rôle d'expert...)")
    
    y_cursor -= 1.5*cm
    for i in range(1, 6):
        create_input_field(form, f'moteur_{i}', x=2*cm, y=y_cursor, width=width-4*cm, height=0.7*cm)
        c.drawString(1.2*cm, y_cursor + 0.2*cm, f"{i}.")
        y_cursor -= 1.0*cm

    draw_page_decorations(c, width, height, part_title="SÉANCE 3", x_offset=card_margin)
    c.showPage()

def create_tree_of_life_page(c):
    """
    New Page: L'Arbre de Vie.
    Distinct from Genogramme.
    Structure: Racines, Sol, Tronc, Branches, Feuilles, Fruits.
    Improved UI/UX with organic drawing and full explanatory text.
    v3: Layout Fixes preventing overlaps.
    """
    width, height = A4
    draw_page_background(c, width, height)
    card_margin = 2*cm
    draw_side_panel(c, card_margin, width, height)
    draw_title(c, "Mon Arbre de Vie", card_margin + 0.5*cm, height - 2.5*cm)

    # --- 1. INTRO & OBJECTIF ---
    # Reserve top 4.5cm for header/intro
    y_cursor = height - 3.5*cm
    
    # Objectif styling
    c.setFillColor(PDFStyle.COLOR_ACCENT_BLUE)
    c.setFont(PDFStyle.FONT_SUBTITLE, 11)
    c.drawString(2*cm, y_cursor, "Objectif :")
    
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    c.setFont(PDFStyle.FONT_BODY, 10)
    obj_text = (
        "Restaurer votre identité narrative. Cet exercice permet de voir que les épreuves (trauma, échec...) "
        "ne sont que des cicatrices sur l'écorce, et non l'arbre tout entier."
    )
    # Simple wrapping
    text_obj = c.beginText(4*cm, y_cursor)
    text_obj.setFont(PDFStyle.FONT_BODY, 10)
    text_obj.setTextOrigin(4*cm, y_cursor)
    from reportlab.lib.utils import simpleSplit
    # Constrain width to avoid hitting right margin
    lines = simpleSplit(obj_text, PDFStyle.FONT_BODY, 10, width - 6*cm)
    for line in lines:
        text_obj.textLine(line)
    c.drawText(text_obj)
    
    # --- 2. LAYOUT COORDINATES ---
    center_x = card_margin + (width - card_margin) / 2.0
    cx = center_x
    
    # Ground Level (Base of trunk)
    ground_y = 5*cm
    
    # Trunk
    trunk_width_base = 4*cm
    trunk_width_top = 3.5*cm
    trunk_height = 9*cm
    trunk_top_y = ground_y + trunk_height # 14cm
    
    # Crown (Branches area)
    crown_top_y = height - 5.5*cm # Leave space for header
    
    form = c.acroForm

    # --- 3. ORGANIC TREE DRAWING ---
    c.saveState()
    c.setStrokeColor(PDFStyle.COLOR_TEXT_SECONDARY)
    c.setLineWidth(1.5)
    c.setLineJoin(1) 
    c.setLineCap(1) 

    # A. Sol (Uneven ground) - Draw first to be behind roots if needed, or foundation
    p = c.beginPath()
    p.moveTo(1*cm, ground_y)
    # Gentle hills
    p.curveTo(4*cm, ground_y + 0.5*cm, 6*cm, ground_y - 0.5*cm, cx, ground_y - 0.2*cm)
    p.curveTo(width - 6*cm, ground_y + 0.4*cm, width - 4*cm, ground_y - 0.3*cm, width - 1*cm, ground_y)
    c.drawPath(p, stroke=1, fill=0)

    # B. Racines (Roots) - Below ground
    # Central Root
    p = c.beginPath()
    p.moveTo(cx, ground_y - 0.2*cm)
    p.curveTo(cx - 0.5*cm, ground_y - 1.5*cm, cx + 0.5*cm, ground_y - 2.5*cm, cx, ground_y - 3.5*cm)
    c.drawPath(p, stroke=1, fill=0)
    # Left Root
    p = c.beginPath()
    p.moveTo(cx - 1.5*cm, ground_y)
    p.curveTo(cx - 2*cm, ground_y - 1*cm, cx - 3.5*cm, ground_y - 1.5*cm, cx - 5*cm, ground_y - 3*cm)
    c.drawPath(p, stroke=1, fill=0)
    # Right Root
    p = c.beginPath()
    p.moveTo(cx + 1.5*cm, ground_y)
    p.curveTo(cx + 2*cm, ground_y - 1*cm, cx + 3.5*cm, ground_y - 1.5*cm, cx + 5*cm, ground_y - 3*cm)
    c.drawPath(p, stroke=1, fill=0)

    # C. Tronc (Trunk) - Wide and solid
    p = c.beginPath()
    # Left side
    p.moveTo(cx - 1.8*cm, ground_y)
    p.curveTo(cx - 1.5*cm, ground_y + 3*cm, cx - 1.5*cm, ground_y + 6*cm, cx - 1.8*cm, trunk_top_y)
    # Right side
    p.moveTo(cx + 1.8*cm, ground_y)
    p.curveTo(cx + 1.5*cm, ground_y + 3*cm, cx + 1.5*cm, ground_y + 6*cm, cx + 1.8*cm, trunk_top_y)
    c.drawPath(p, stroke=1, fill=0)
    
    # Textures/Cicatrices
    c.setLineWidth(0.5)
    c.arc(cx - 0.5*cm, ground_y + 2*cm, cx + 0.5*cm, ground_y + 2.8*cm, startAng=160, extent=50)
    c.arc(cx + 0.2*cm, ground_y + 5*cm, cx + 1.0*cm, ground_y + 5.6*cm, startAng=200, extent=40)

    # D. Crown Branches - Supporting the boxes
    c.setLineWidth(1.5)
    
    # Left Branch (Holds Leaves Box) -> Aim for (1.5cm, 18cm)
    p = c.beginPath()
    p.moveTo(cx - 1.8*cm, trunk_top_y)
    p.curveTo(cx - 4*cm, trunk_top_y + 2*cm, cx - 6*cm, trunk_top_y + 1*cm, 5*cm, trunk_top_y + 4*cm) 
    c.drawPath(p, stroke=1, fill=0)
    
    # Right Branch (Holds Fruits Box) -> Aim for (Width-1.5cm, 18cm)
    p = c.beginPath()
    p.moveTo(cx + 1.8*cm, trunk_top_y)
    p.curveTo(cx + 4*cm, trunk_top_y + 2*cm, cx + 6*cm, trunk_top_y + 1*cm, width - 5*cm, trunk_top_y + 4*cm)
    c.drawPath(p, stroke=1, fill=0)
    
    # Center Branch (Holds Branches/Projects Box) -> Aim for Top Center
    p = c.beginPath()
    p.moveTo(cx, trunk_top_y) # Start slightly lower
    p.curveTo(cx - 2*cm, trunk_top_y + 3*cm, cx + 2*cm, trunk_top_y + 5*cm, cx, crown_top_y - 2*cm)
    c.drawPath(p, stroke=1, fill=0)

    c.restoreState()

    # --- 4. INPUT ZONES & LABELS ---
    
    def draw_zone(title, subtitle, x, y, w, h, align='left', color_title=PDFStyle.COLOR_TEXT_MAIN):
        # Draw background for better readability over lines? No, looks cleaner transparent if placed well.
        
        # Title
        c.setFont(PDFStyle.FONT_SUBTITLE, 10)
        c.setFillColor(color_title)
        
        # Calculate text anchor positions
        if align == 'center':
            tx, ty = x + w/2, y + h + 0.5*cm
            sx, sy = x + w/2, y + h + 0.1*cm
            c.drawCentredString(tx, ty, title)
            c.setFont(PDFStyle.FONT_ITALIC, 9)
            c.setFillColor(PDFStyle.COLOR_TEXT_SECONDARY)
            c.drawCentredString(sx, sy, subtitle)
        elif align == 'right':
            tx, ty = x + w, y + h + 0.5*cm
            sx, sy = x + w, y + h + 0.1*cm
            c.drawRightString(tx, ty, title)
            c.setFont(PDFStyle.FONT_ITALIC, 9)
            c.setFillColor(PDFStyle.COLOR_TEXT_SECONDARY)
            c.drawRightString(sx, sy, subtitle)
        else:
            tx, ty = x, y + h + 0.5*cm
            sx, sy = x, y + h + 0.1*cm
            c.drawString(tx, ty, title)
            c.setFont(PDFStyle.FONT_ITALIC, 9)
            c.setFillColor(PDFStyle.COLOR_TEXT_SECONDARY)
            c.drawString(sx, sy, subtitle)
            
        create_input_field(form, f'arbre_{title.split()[1].lower()}', x=x, y=y, width=w, height=h, multiline=True)
    
    draw_page_decorations(c, width, height, part_title="BONUS", x_offset=card_margin)
    c.showPage()

    # Position: y=1.5cm to y=3.5cm
    draw_zone("1. RACINES", "Mon histoire, mes origines...", 
              cx - 4.5*cm, 1.2*cm, 9*cm, 2.3*cm, align='center', color_title=PDFStyle.COLOR_ACCENT_RED)

    # Position: y=4cm to y=6cm, Left side.
    draw_zone("2. SOL", "Mes besoins actuels", 
              1.5*cm, 4*cm, 5*cm, 2.5*cm, align='left')

    # Position: y=7cm to y=11.5cm centered on trunk.
    # Widen box slightly to fit trunk width approx
    c.setFont(PDFStyle.FONT_SUBTITLE, 10)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    c.drawCentredString(cx, 12*cm, "3. TRONC")
    c.setFont(PDFStyle.FONT_ITALIC, 9)
    c.setFillColor(PDFStyle.COLOR_TEXT_SECONDARY)
    c.drawCentredString(cx, 11.6*cm, "Compétences & Valeurs")
    
    # Field overlaps the trunk drawing significantly, but that's okay, it's the "content" of the trunk.
    create_input_field(form, 'arbre_tronc', x=cx - 2.2*cm, y=7.5*cm, width=4.4*cm, height=4*cm, multiline=True)

    # Position: y=17cm approx (trunk top is 14cm).
    draw_zone("5. FEUILLES", "Club de Vie (Soutiens)", 
              1.5*cm, trunk_top_y + 2*cm, 5.5*cm, 3*cm, align='left')

    # Position: y=17cm approx
    draw_zone("6. FRUITS", "Cadeaux & Réussites", 
              width - 7*cm, trunk_top_y + 2*cm, 5.5*cm, 3*cm, align='right')

    # Position: y=22cm approx. WELL below the header (29.7 - 5 = 24.7).
    # Box top at y+h = 22+2.5 = 24.5. Just fits.
    draw_zone("4. BRANCHES", "Projets & Rêves", 
              cx - 4.5*cm, trunk_top_y + 7.5*cm, 9*cm, 2.5*cm, align='center', color_title=PDFStyle.COLOR_ACCENT_BLUE)

    draw_page_decorations(c, width, height, part_title="BONUS", x_offset=card_margin)
    c.showPage()

def create_interview_page(c):
    """
    New Page: Interview avec une personne passionnée (Bonus).
    """
    width, height = A4
    draw_page_background(c, width, height)
    card_margin = 2*cm
    draw_side_panel(c, card_margin, width, height)
    draw_title(c, "Interview avec une personne passionnée", card_margin + 0.5*cm, height - 3*cm)

    c.setFont(PDFStyle.FONT_BODY, 11)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    c.drawString(2*cm, height - 4*cm, "Rencontrez quelqu'un qui a un métier ou une vie qui vous inspire.")
    
    form = c.acroForm
    y_cursor = height - 5.5*cm
    
    col1_x = 2*cm
    col2_x = 10*cm
    
    c.setFont(PDFStyle.FONT_SUBTITLE, 10)
    c.setFillColor(PDFStyle.COLOR_ACCENT_BLUE)
    c.drawString(col1_x, y_cursor, "Personne interviewée :")
    create_input_field(form, 'interview_nom', x=col1_x, y=y_cursor - 0.8*cm, width=7*cm, height=0.6*cm)
    
    c.drawString(col2_x, y_cursor, "Son métier / Activité :")
    create_input_field(form, 'interview_metier', x=col2_x, y=y_cursor - 0.8*cm, width=9*cm, height=0.6*cm)
    
    y_cursor -= 2*cm
    
    questions = [
        ("Qu'aimez-vous le plus dans ce que vous faites ?", "interview_q1", 2.5*cm),
        ("Quelles sont les difficultés ou contraintes cachées ?", "interview_q2", 2.5*cm),
        ("Quel conseil donneriez-vous à quelqu'un qui veut se lancer ?", "interview_q3", 2.5*cm),
        ("Ce que j'en retiens pour moi (Mon ressenti) :", "interview_q4", 3.5*cm)
    ]
    
    for q_text, q_id, q_height in questions:
        c.setFont(PDFStyle.FONT_SUBTITLE, 11)
        c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
        c.drawString(2*cm, y_cursor, q_text)
        y_cursor -= q_height + 0.2*cm
        create_input_field(form, q_id, x=2*cm, y=y_cursor, width=width-4*cm, height=q_height, multiline=True)
        y_cursor -= 0.8*cm

    draw_page_decorations(c, width, height, part_title="BONUS", x_offset=card_margin)
    c.showPage()
