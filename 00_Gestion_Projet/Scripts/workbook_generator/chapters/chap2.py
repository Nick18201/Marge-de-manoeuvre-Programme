
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
    This content is dense, split across 2 pages if possible, or one very dense page.
    Given the length, we will split into 2 pages comfortably.
    """
    width, height = A4
    
    # --- PAGE 1 ---
    draw_page_background(c, width, height)
    
    # Header
    draw_title(c, "Comprendre ses Racines", 2*cm, height - 2.5*cm)
    c.setFont(PDFStyle.FONT_SUBTITLE, 12)
    c.setFillColor(PDFStyle.COLOR_ACCENT_BLUE)
    c.drawString(2*cm, height - 3.2*cm, "Pour choisir son avenir")

    # Content Area
    text_x = 2*cm
    text_y = height - 4.5*cm
    line_height = 16
    
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
            canvas.drawString(text_x, curr_y, line)
            curr_y -= line_height
        return curr_y - line_height # Extra space after block

    # Intro
    intro_lines = [
        "Dans un bilan de compétences, on pense souvent qu'il suffit de lister ses savoir-faire pour trouver sa voie.",
        "C'est une erreur. Vous n'êtes pas seulement une somme de compétences techniques ; vous êtes le résultat d'une histoire.",
        "",
        "Votre façon de travailler, votre rapport à l'argent, à l'autorité ou à la réussite ne viennent pas de nulle part.",
        "Ils ont été façonnés par votre famille et votre milieu d'origine. Ce document a pour but de vous aider à repérer",
        "ces « bagages invisibles » pour faire le tri : que voulez-vous garder ?",
        "Que devez-vous laisser au vestiaire pour enfin vous épanouir professionnellement ?"
    ]
    text_y = draw_paragraph_block(c, "Introduction : Pourquoi regarder en arrière ?", intro_lines, text_y)

    # 1. Habitus
    habitus_lines = [
        "Imaginez que vous avez un logiciel installé en vous depuis l'enfance. C'est l'Habitus : votre manière spontanée",
        "de réagir, de parler, de vous tenir, héritée de vos parents et de votre milieu social.",
        "",
        "Pourquoi c'est important ? Si vous changez de milieu professionnel (transfuge de classe), ce logiciel peut bugger.",
        "Vous pouvez ressentir un décalage permanent, une gêne, comme si vous portiez un costume mal taillé."
    ]
    text_y = draw_paragraph_block(c, "1. Le « Sac à Dos » Social (L'Habitus)", habitus_lines, text_y)

    # Imposteur
    imposteur_lines = [
        "« Un jour, ils vont se rendre compte que je ne suis pas à la hauteur »... C'est souvent le signe d'une Névrose de Classe.",
        "Ce n'est pas une maladie, mais un conflit intérieur.",
        "• Le Parvenu : Culpabilité de réussir mieux que ses parents (les abandonner).",
        "• Le Déclassé : Honte d'avoir une situation moins prestigieuse.",
        "",
        "Ce sentiment vous freine : il peut empêcher de demander une augmentation ou pousser à l'épuisement."
    ]
    text_y = draw_paragraph_block(c, "Le sentiment d'illégitimité", imposteur_lines, text_y, color_title=PDFStyle.COLOR_TEXT_MAIN)

    c.showPage()
    
    # --- PAGE 2 ---
    draw_page_background(c, width, height)
    draw_title(c, "Comprendre ses Racines (suite)", 2*cm, height - 2.5*cm)
    text_y = height - 4.5*cm

    # 2. Contrat Familial
    contrat_lines = [
        "Chaque famille possède un « Grand Livre de Comptes » invisible. On y inscrit ce que l'on doit à ses parents.",
        "• Les Loyautés Invisibles : Parfois, on s'auto-sabote juste avant le but pour ne pas dépasser ses parents.",
        "• La Réparation : Avez-vous choisi votre métier par passion ou pour réparer un drame familial ?",
        "• Le Mythe Familial : « Chez nous, on est des intellectuels/solidaires... ». Si votre projet contredit ce mythe,",
        "  vous rencontrerez une résistance interne."
    ]
    text_y = draw_paragraph_block(c, "2. Le Contrat Familial Secret", contrat_lines, text_y)

    # 3. Souffrance
    souffrance_lines = [
        "Le travail, ce n'est pas juste exécuter une tâche. Quand on ne peut pas faire son travail « bien », on souffre.",
        "C'est l'activité empêchée. Votre souffrance est un signal d'intelligence : elle montre que vous tenez à ce que vous faites.",
        "Le but est de transformer cette plainte en pouvoir d'agir : retrouver une marge de manœuvre."
    ]
    text_y = draw_paragraph_block(c, "3. La Souffrance et le Plaisir au Travail", souffrance_lines, text_y)

    # 4. Pistes
    pistes_lines = [
        "A. Le Génogramme du Cœur : Identifiez vos « tuteurs de résilience » (ceux qui ont donné confiance) plutôt que ceux qui jugent.",
        "",
        "B. Le Roman Familial : Repérez les répétitions et les « phrases poisons » sur le travail (« Il faut souffrir pour réussir »).",
        "",
        "C. L'Objectif : Réussir sans Trahir. Comment honorer les valeurs familiales sous une forme qui VOUS appartient ?",
        "C'est la différenciation."
    ]
    text_y = draw_paragraph_block(c, "4. Pistes pour votre Bilan", pistes_lines, text_y)
    
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
    Page: Mon Héritage (3FVS).
    Tree Metaphor.
    """
    width, height = A4
    draw_page_background(c, width, height)
    draw_title(c, "Mon Héritage (3FVS)", 2*cm, height - 3*cm)
    
    # Tree Trunk Visual (Simplified)
    c.setStrokeColor(PDFStyle.COLOR_TEXT_SECONDARY)
    c.setLineWidth(30)
    c.line(width/2, 5*cm, width/2, height/2) # Trunk
    
    # Roots
    c.setLineWidth(5)
    c.line(width/2, 5*cm, width/2 - 4*cm, 2*cm)
    c.line(width/2, 5*cm, width/2 + 4*cm, 2*cm)
    
    # Branches
    c.line(width/2, height/2, width/2 - 5*cm, height/2 + 5*cm)
    c.line(width/2, height/2, width/2 + 5*cm, height/2 + 5*cm)
    c.line(width/2, height/2 + 2*cm, width/2, height/2 + 7*cm)

    form = c.acroForm
    
    # 1. Force (Racines/Tronc)
    box_width = 8*cm
    box_height = 2.5*cm
    
    x_force = 2*cm
    y_force = 6*cm
    c.setFont(PDFStyle.FONT_SUBTITLE, 12)
    c.setFillColor(PDFStyle.COLOR_ACCENT_BLUE)
    c.drawString(x_force, y_force + box_height + 0.2*cm, "FORCE (Ce que je garde)")
    create_input_field(form, 'heritage_force', x=x_force, y=y_force, width=box_width, height=box_height, multiline=True, tooltip="De ma famille, je garde la valeur...")

    # 2. Vigilance (Racines côté obscur)
    x_vigilance = width - 2*cm - box_width
    y_vigilance = 6*cm
    c.setFillColor(PDFStyle.COLOR_ACCENT_RED)
    c.drawString(x_vigilance, y_vigilance + box_height + 0.2*cm, "VIGILANCE (Ce que je laisse)")
    create_input_field(form, 'heritage_vigilance', x=x_vigilance, y=y_vigilance, width=box_width, height=box_height, multiline=True, tooltip="Je décide de ne pas reproduire le schéma...")

    # 3. Souhait (Branches)
    x_souhait = width/2 - box_width/2
    y_souhait = height/2 + 3*cm
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    c.drawCentredString(width/2, y_souhait + box_height + 0.2*cm, "SOUHAIT (Le message reçu / mandats)")
    create_input_field(form, 'heritage_souhait', x=x_souhait, y=y_souhait, width=box_width, height=box_height, multiline=True, tooltip="Le message secret transmis...")

    # Bottom Note
    c.setFont(PDFStyle.FONT_ITALIC, 10)
    c.drawCentredString(width/2, 3*cm, "Les racines nourrissent l'arbre, mais ce sont les nouvelles branches qui portent les fruits.")

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
    c.drawString(2*cm, y_anti - 0.7*cm, "Je ne serai jamais comme... car je refuse...")
    
    create_input_field(form, 'mentors_negatif', 
                       x=2*cm, y=y_anti - 6*cm, 
                       width=width - 4*cm, height=5*cm, 
                       multiline=True, tooltip="Je ne veux pas reproduire...")
                       
    c.showPage()
