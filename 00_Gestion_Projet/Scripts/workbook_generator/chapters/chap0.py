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

def create_cover_page(c):
    width, height = A4
    
    # 1. Background Nude + Grid
    # We don't use draw_page_background here because cover has special layout (Blue Band)
    c.setFillColor(PDFStyle.COLOR_BG_NUDE)
    c.rect(0,0, width, height, fill=1, stroke=0)
    draw_dot_grid(c, width, height)

    # 1b. Blue Side Band (Left)
    band_width = 3.5*cm 
    c.setFillColor(PDFStyle.COLOR_ACCENT_BLUE)
    c.rect(0, 0, band_width, height, fill=1, stroke=0)

    # A. Illustration Principale (Cover)
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

    # 3. Titres
    c.setFont(PDFStyle.FONT_BODY, 14)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    c.drawRightString(width - 40, height - 210, "BILAN DE COMPÉTENCES & ALIGNEMENT") 
    
    c.setFont(PDFStyle.FONT_TITLE, 18)
    c.setFillColor(PDFStyle.COLOR_ACCENT_RED)
    c.drawRightString(width - 40, height - 240, "CHAPITRE 0 : LE PRÉLUDE")
    
    c.showPage()

def create_summary_page(c):
    """New Page: Au Programme (Blue Background)."""
    width, height = A4
    
    # 1. Full Blue Background
    c.setFillColor(PDFStyle.COLOR_ACCENT_BLUE)
    c.rect(0, 0, width, height, fill=1, stroke=0)
    
    # 2. Faint White Dot Grid
    draw_dot_grid(c, width, height, color=PDFStyle.COLOR_WHITE, opacity=0.1)

    # 3. Content
    c.setFont(PDFStyle.FONT_TITLE, 30)
    c.setFillColor(PDFStyle.COLOR_WHITE)
    c.drawString(3*cm, height - 4*cm, "AU PROGRAMME")
    
    c.setFont(PDFStyle.FONT_BODY, 12)
    c.setFillColor(PDFStyle.COLOR_WHITE)
    
    start_y = height - 6*cm
    
    intro_lines = [
        "Trouver sa place dans le monde d’aujourd’hui n’est pas chose facile ; on",
        "se réoriente, on se reforme, on réinvente la façon d’exercer son métier...",
        "Que ce soit pour une nécessité de réalisation personnelle, un besoin de",
        "vivre des expériences plus variées et stimulantes, une sérieuse remise en",
        "question du rapport à l’entreprise et au travail est en marche !",
        "",
        "La question centrale pourrait être :",
        "Quelle place dois-je accorder au travail dans mon existence et sous quelle forme ?",
        "Nous allons investiguer cette question (parmi beaucoup d’autres) dans ce travail.",
        "",
        "En voici les grandes lignes :"
    ]
    
    start_y = height - 5.5*cm
    c.setFont(PDFStyle.FONT_BODY, 10)

    for line in intro_lines:
        c.drawString(3*cm, start_y, line)
        start_y -= 14 
        
    start_y -= 0.5*cm
    
    steps = [
        ("05", "Prendre du recul", "sur vos choix passés et vos expériences."),
        ("13", "Explorer votre personnalité", "Vos forces, ce que vous aimez, vos besoins."),
        ("32", "Actions concrètes", "Explorer ces secteurs à travers divers supports."),
        ("43", "Plan d'action", "Réussir votre projet.")
    ]
    
    for page_num, title, desc in steps:
        if os.path.exists(PDFStyle.PATH_FLECHE):
             c.drawImage(PDFStyle.PATH_FLECHE, 2.8*cm, start_y - 0.1*cm, width=0.6*cm, height=0.6*cm, mask='auto', preserveAspectRatio=True)
        else:
             c.drawString(3*cm, start_y, "->")
        
        c.setFont(PDFStyle.FONT_TITLE, 11)
        c.drawString(4*cm, start_y, title)
        
        c.setFont(PDFStyle.FONT_BODY, 11)
        text_width = c.stringWidth(title, PDFStyle.FONT_TITLE, 11)
        c.drawString(4*cm + text_width + 5, start_y, " : " + desc)
        
        start_y -= 1.0*cm

    # Outro Text
    start_y -= 0.5*cm
    outro_lines = [
        "À votre disposition également, un site Notion réalisé par mes soins sur lequel",
        "vous pouvez trouver à tout moment des ressources ; sites, podcasts, articles,",
        "vidéos... Mais également des exercices complémentaires concernant la gestion",
        "de vos émotions, l’estime de soi et le détachement des attentes extérieures."
    ]
    
    c.setFont(PDFStyle.FONT_ITALIC, 10)
    for line in outro_lines:
        c.drawString(3*cm, start_y, line)
        start_y -= 12

    # Decor
    draw_leaf(c, width-100, 200, size=150, color=PDFStyle.COLOR_ACCENT_YELLOW, angle=-20, alpha=0.9)
    # Red square at bottom
    c.setFillColor(PDFStyle.COLOR_ACCENT_RED)
    c.rect(width/2 - 40, 50, 80, 80, fill=1, stroke=0)

    c.showPage()

def create_editorial_page_card(c):
    """Edito with Card UI."""
    width, height = A4
    
    draw_page_background(c, width, height)

    # Card
    card_margin = 2.5*cm
    card_width = width - 2*card_margin
    card_height = height - 6*cm
    card_y = 3*cm
    draw_card(c, card_margin, card_y, card_width, card_height)
    
    # Content inside Card
    text_x = card_margin + 1*cm
    text_top = card_y + card_height - 2*cm
    
    # Title
    draw_title(c, "Le mot d'accueil", text_x, text_top)
    
    # Icon/Quote mark
    if os.path.exists(PDFStyle.PATH_GUILLEMETS):
        c.drawImage(PDFStyle.PATH_GUILLEMETS, text_x + card_width - 3*cm, text_top - 0.5*cm, width=2.5*cm, height=2.5*cm, mask='auto', preserveAspectRatio=True, anchor='ne')
    else:
        c.setFont(PDFStyle.FONT_HAND, 60)
        c.setFillColor(PDFStyle.COLOR_ACCENT_YELLOW)
        c.drawRightString(text_x + card_width - 2*cm, text_top, ' " ')

    # Body
    text_y = text_top - 2*cm
    c.setFont(PDFStyle.FONT_BODY, 11)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    
    lines = [
        "Si vous entamez la lecture de ce livret, c’est que vous",
        "êtes aujourd’hui en questionnement sur votre parcours",
        "professionnel et que vous avez eu le courage de passer",
        "à l’action en entamant un bilan de compétences. Bravo !",
        "",
        "Ce livret va être votre guide pendant cette période de",
        "questionnements ; il sera à la fois source d’idées, d’inspirations, de",
        "remises en question... Il recueillera votre histoire, votre parcours",
        "et vos ressentis. Il sera votre boussole et vous le retrouverez entre",
        "chaque séance.",
        "",
        "Le bilan de compétences que je vous propose est un mélange",
        "de questionnements, d’activités créatives et d’échanges réflexifs.",
        "Ces exercices seront des supports de travail pour nos entretiens.",
        "N’hésitez pas à rajouter des questions ou activités qui vous",
        "intéressent et vous semblent pertinentes pour nourrir votre",
        "cheminement.",
        "",
        "Lors de votre travail personnel, je vous conseille de vous dégager",
        "des moments de calme dans un endroit chaleureux où vous vous",
        "sentez à l’aise et où vous ne serez pas dérangé(e). Ce sont des",
        "temps pour vous retrouver avec vous même et laisser libre court à",
        "votre intuition et à votre part créative."
    ]
    
    for line in lines:
        c.drawString(text_x, text_y, line)
        text_y -= 16

    c.showPage()

def create_intro_sense_page(c):
    """
    Introduction: Mettre du sens.
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
    text_x = card_margin + 1*cm
    text_top = card_y + card_height - 1.5*cm
    
    # Title
    draw_title(c, "Mettre du sens", text_x, text_top, size=22)
    
    # Body Text
    text_y = text_top - 1.5*cm
    
    paragraphs = [
        "La question du sens est centrale dans nos vies : savoir pour quelles raisons on fait les choses, c’est reprendre notre pouvoir d’agir en conscience.",
        "En étudiant la psychologie et la sociologie, on prend conscience de l’importance de notre part inconsciente, des schémas et stéréotypes qui nous façonnent, des choses que l’on croit décider, vouloir, alors que nous avons été conditionnés et influencés pour le faire. Mon travail s’attache aujourd’hui à aider les personnes à remettre du sens dans leurs décisions et leurs actions professionnelles.",
        "La question du sens va bien au-delà de l’activité professionnelle, mais c’est la porte d’entrée que je choisis ; pour une raison simple : elle concerne la majorité d’entre nous. Peu importe le milieu social ou l’origine, nous donnons tous de l’importance à nos vies par nos activités. Je pars d’un point de vue clair : nous avons tous des moyens d’apprentissage, d’adaptation, de changement. Mais nous avons tous également une nature profonde qui nous donne des facilités pour certaines choses.", 
        "Notre expérience, notre socialisation et d’autres facteurs innés font que nous avons une certaine personnalité. Elle se construit et se développe tout au long de la vie, mais nous sommes toujours différents de notre voisin. Nous avons des aptitudes différentes, des forces différentes, des goûts différents. Et c’est très bien ; c’est ce qui nous permet, en société, de pouvoir remplir des rôles et des fonctions complémentaires !",
        "Le mal-être au travail est plus que jamais un sujet central dans notre société ; la montée des burn-out, bore et brown-out en est malheureusement le témoin. Les phénomènes des Bullshits jobs (tâches inutiles, superficielles et vides de sens effectuées dans le monde du travail), les attentes différentes des nouvelles générations (millennials, Z), l’urgence climatique qui génère de l’écoanxiété… sont autant de raisons qui cohabitent. Mon objectif aujourd’hui est de vous accompagner à vous recentrer sur qui vous êtes, afin de pouvoir vous épanouir réellement dans vos choix professionnels.",
        "L’épanouissement professionnel est un objectif ambitieux, mais comme on ne va pas commencer un travail personnel avec des objectifs au ras des pâquerettes, allons-y !"
    ]
    
    style = ParagraphStyle(
        'Normal',
        fontName=PDFStyle.FONT_BODY,
        fontSize=11,
        leading=14,
        textColor=PDFStyle.COLOR_TEXT_MAIN
    )
    
    for paragraph in paragraphs:
        p = Paragraph(paragraph, style)
        w, h = p.wrap(card_width - 2*cm, height) # Max width
        
        p.drawOn(c, text_x, text_y - h)
        
        text_y -= (h + 10) 

    c.showPage()

def create_form_page_card(c):
    """Form Page with Card UI."""
    width, height = A4
    
    draw_page_background(c, width, height)
    
    # Card
    card_margin = 2*cm
    card_width = width - 2*card_margin
    card_height = height - 5*cm
    card_y = 2.5*cm
    draw_side_panel(c, card_margin, width, height)

    # Content
    text_x = card_margin + 1*cm
    text_top = card_y + card_height - 2*cm
    
    draw_title(c, "Mon Engagement", text_x, text_top)

    form = c.acroForm
    start_y = text_top - 2*cm
    
    # 1. Identité
    c.setFont(PDFStyle.FONT_BODY, 12)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    c.drawString(text_x, start_y, "Moi, ")
    
    create_input_field(form, 'nom_complet', 
                       x=text_x + 1.5*cm, y=start_y-5, width=8*cm, height=20, 
                       tooltip='Prénom Nom')
    
    # 2. Temps
    start_y -= 2*cm
    c.drawString(text_x, start_y, "décide d'investir")
    
    create_input_field(form, 'engagement_hebdo',
                       x=text_x + 3.5*cm, y=start_y-5, width=1.5*cm, height=20,
                       tooltip='Nb')
                       
    c.drawString(text_x + 5.5*cm, start_y, "heures par semaine.")
    
    # 3. Objectif
    start_y -= 2*cm
    c.drawString(text_x, start_y, "Mon objectif principal :")
    start_y -= 0.5*cm
    
    create_input_field(form, 'objectif_3_mois',
                       x=text_x, y=start_y - 2*cm, width=card_width - 2*cm, height=2*cm,
                       tooltip='Objectif', multiline=True)
                       
    # 4. Permission
    start_y -= 3*cm 
    c.drawString(text_x, start_y, "Je m'autorise à :")
    start_y -= 0.5*cm
    
    create_input_field(form, 'permission_personnelle',
                       x=text_x, y=start_y - 2*cm, width=card_width - 2*cm, height=2*cm,
                       tooltip='Permission', multiline=True)
    
    # Hidden Fields
    form.textfield(name='meta_doc_type', value='workbook_chap0', x=0, y=-10, width=0, height=0)
    form.textfield(name='meta_doc_version', value='1.3_da_v4', x=0, y=-10, width=0, height=0)

    c.showPage()

def create_premiere_etape_page(c):
    """
    New Cover Page: Première étape : Faire le point.
    Blue background, large numbers, white text.
    Refined UI: 'Plume Texture', separate '1.'
    """
    width, height = A4
    
    # 1. Full Blue Background with texture/grain if possible, but here solid blue + grid
    c.setFillColor(PDFStyle.COLOR_ACCENT_BLUE)
    c.rect(0, 0, width, height, fill=1, stroke=0)
    
    # Faint Grid
    draw_dot_grid(c, width, height, color=PDFStyle.COLOR_WHITE, opacity=0.1)

    # 2. Large Number "1."
    # Moved higher and to the left to avoid overlap, and made smaller/more transparent
    c.saveState()
    c.setFont(PDFStyle.FONT_BRANDING, 160) 
    c.setFillColor(PDFStyle.COLOR_WHITE, alpha=0.12) # Slightly more transparent
    c.drawString(1.5*cm, height - 9*cm, "1.")
    c.restoreState()

    # 3. Titles
    # Shifted down slightly to be distinct from the watermarked number
    start_y = height - 10*cm
    c.setFont(PDFStyle.FONT_BRANDING, 32)
    c.setFillColor(PDFStyle.COLOR_WHITE)
    c.drawString(2.5*cm, start_y, "Première étape :")
    c.drawString(2.5*cm, start_y - 1.2*cm, "Faire le point")

    # 4. "Appuyer sur Pause" Badge
    badge_y = start_y - 3*cm
    c.saveState()
    
    c.setFont(PDFStyle.FONT_BRANDING, 13)
    c.drawString(2*cm + 1.5*cm, badge_y, "APPUYER SUR PAUSE")
    
    # Circle
    c.setStrokeColor(PDFStyle.COLOR_WHITE)
    c.setLineWidth(1.5)
    c.circle(2.5*cm, badge_y + 0.15*cm, 0.4*cm, fill=0, stroke=1)
    # Pause bars
    c.setFillColor(PDFStyle.COLOR_WHITE)
    c.rect(2.35*cm, badge_y, 0.1*cm, 0.3*cm, fill=1, stroke=0)
    c.rect(2.55*cm, badge_y, 0.1*cm, 0.3*cm, fill=1, stroke=0)
    
    c.restoreState()

    # 5. Text Blocks
    text_y = badge_y - 2*cm
    
    style_white = ParagraphStyle(
        'NormalWhite',
        fontName=PDFStyle.FONT_BODY,
        fontSize=12,
        leading=16,
        textColor=PDFStyle.COLOR_WHITE
    )
    
    text_content = [
        "Il est l'heure de faire le point sur votre situation actuelle ! Le début d'un bilan, c'est le bon moment pour enclencher le bouton PAUSE. Il est difficile de pouvoir réfléchir à ses besoins et à ses envies quand on est ancré•e dans une routine.",
        "Il est également difficile d'avoir accès à ces réflexions dans une vie où l'on est la tête sous l'eau, que ce soit par surcharge de travail, par ennui profond, ou par manque de sens."
    ]
    
    for block in text_content:
        p = Paragraph(block, style_white)
        w, h = p.wrap(width - 5*cm, height) # Slightly narrower for better reading
        p.drawOn(c, 2.5*cm, text_y - h) # Aligned with title
        text_y -= (h + 0.8*cm)

    # 6. Illustrations (Plume Texture)
    # Replaced brindilles with plume texture, scaled down
    if os.path.exists(PDFStyle.PATH_PLUME_TEXTURE):
        # Top Right
        c.saveState()
        c.translate(width - 1*cm, height - 3*cm)
        c.rotate(30)
        # Smaller size: 5x5 cm approx
        c.drawImage(PDFStyle.PATH_PLUME_TEXTURE, 0, 0, width=5*cm, height=5*cm, mask='auto', preserveAspectRatio=True, anchor='ne')
        c.restoreState()

        # Bottom Left
        c.saveState()
        c.translate(0, 0)
        c.rotate(10)
        # Smaller size: 7x7 cm 
        c.drawImage(PDFStyle.PATH_PLUME_TEXTURE, -2*cm, -1*cm, width=7*cm, height=7*cm, mask='auto', preserveAspectRatio=True)
        c.restoreState()
    
    c.showPage()

def create_faire_le_point_pages(c):
    """
    Faire le Point : Ma Situation Actuelle.
    Split into 2 pages (4 questions each).
    """
    width, height = A4
    questions_part1 = [
        ("Comment je me sens actuellement ?", "feeling"),
        ("Quel a été le déclencheur de ce bilan ?", "trigger"),
        ("De quoi j’ai besoin en ce moment ?", "needs"),
        ("Qu’ai-je fait jusqu’à présent pour remédier à cette situation ?", "actions_taken")
    ]
    
    questions_part2 = [
        ("Qu’est ce que je n’ai pas encore changé ? Pourquoi ?", "not_changed"),
        ("Quels avantages ai-je à garder la situation telle quelle ?", "secondary_benefits"),
        ("Quels besoins sont insatisfaits dans ma vie aujourd’hui ?", "unmet_needs"),
        ("Quelles actions concrètes puis-je mettre en place ?", "concrete_actions")
    ]
    
    parts = [(questions_part1, "1/2"), (questions_part2, "2/2")]
    
    for idx_part, (questions, part_label) in enumerate(parts):
        draw_page_background(c, width, height)
        
        # Card
        card_margin = 2*cm
        card_width = width - 2*card_margin
        card_height = height - 4*cm
        card_y = 2*cm
        draw_side_panel(c, card_margin, width, height)
        
        # Header
        text_x = card_margin + 1*cm
        text_top = card_y + card_height - 1.5*cm
        
        draw_title(c, f"Faire le Point : Ma Situation ({part_label})", text_x, text_top, size=20)
        
        if idx_part == 0:
            c.setFont(PDFStyle.FONT_BODY, 10)
            c.setFillColor(PDFStyle.COLOR_ACCENT_RED)
            c.drawString(text_x, text_top - 0.7*cm, "Le début d’un bilan, c’est le bon moment pour enclencher le bouton PAUSE.")
            start_y = text_top - 2*cm
        else:
            start_y = text_top - 1.5*cm
            
        # Draw Questions
        form = c.acroForm
        field_height = 4.5*cm 
        gap = 0.8*cm
        
        current_y = start_y
        
        c.setFont(PDFStyle.FONT_SUBTITLE, 11)
        c.setFillColor(PDFStyle.COLOR_ACCENT_BLUE)

        for question, key in questions:
            # Label
            c.drawString(text_x, current_y, question)
            
            # Field position
            mid_y = current_y - field_height - 0.2*cm
            
            create_input_field(form, f's1_point_{key}',
                               x=text_x, y=mid_y,
                               width=card_width - 2*cm, height=field_height,
                               tooltip=question, multiline=True)
                           
            current_y -= (field_height + gap + 0.5*cm)

        c.showPage()

def create_domaines_de_vie_page(c):
    """
    Les Domaines de Vie.
    Ratings + Reflection.
    """
    width, height = A4
    
    draw_page_background(c, width, height)
    
    # Card
    card_margin = 2*cm
    card_width = width - 2*card_margin
    card_height = height - 4*cm
    card_y = 2*cm
    draw_side_panel(c, card_margin, width, height)

    # Title
    text_x = card_margin + 1*cm
    text_top = card_y + card_height - 1.5*cm
    
    draw_title(c, "Les Domaines de Vie", text_x, text_top, size=22)
    
    c.setFont(PDFStyle.FONT_BODY, 12)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    c.drawString(text_x, text_top - 1*cm, "Évaluez l'équilibre actuel (Note de 1 à 10)")
    
    # 8 Domains
    domains = [
        "1. Argent / Finances",
        "2. Impact / Sens",
        "3. Dév. Personnel / Spiritualité",
        "4. Famille",
        "5. Santé / Énergie",
        "6. Lieu de vie / Environnement",
        "7. Loisirs / Passions",
        "8. Travail / Carrière"
    ]
    
    form = c.acroForm
    start_y = text_top - 2.5*cm
    col_width = (card_width - 2*cm) / 2
    
    # Grid layout for domains (2 columns)
    for i, domain in enumerate(domains):
        col = i % 2
        row = i // 2
        
        x_pos = text_x + (col * col_width)
        y_pos = start_y - (row * 1.5*cm)
        
        c.setFont(PDFStyle.FONT_BODY, 11)
        c.drawString(x_pos, y_pos, domain)
        
        # Rating Box
        create_input_field(form, f's1_domaine_note_{i+1}',
                           x=x_pos + 6.5*cm, y=y_pos - 0.1*cm,
                           width=1.5*cm, height=0.6*cm,
                           tooltip='Note /10')

    # Reflection Question
    reflection_y = start_y - (4 * 1.5*cm) - 1*cm
    
    draw_title(c, "Réflexion", text_x, reflection_y, size=14)
    
    c.setFont(PDFStyle.FONT_BODY, 12)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    c.drawString(text_x, reflection_y - 0.8*cm, "Quel est l'impact de votre travail actuel sur les autres aspects de votre vie ?")
    
    # Large Text Area for Reflection
    area_height = reflection_y - 2*cm - card_y # Remaining space
    if area_height < 5*cm: area_height = 5*cm
    
    create_input_field(form, 's1_domaine_reflexion',
                       x=text_x, y=card_y + 1*cm,
                       width=card_width - 2*cm, height=area_height - 1*cm,
                       tooltip='Votre réflexion', multiline=True)

    c.showPage()

def create_entourage_page(c):
    """
    Mon Entourage.
    Soutiens vs Freins split.
    """
    width, height = A4
    
    draw_page_background(c, width, height)
    
    # Card
    card_margin = 2*cm
    card_width = width - 2*card_margin
    card_height = height - 4*cm
    card_y = 2*cm
    draw_side_panel(c, card_margin, width, height)

    # Title
    text_x = card_margin + 1*cm
    text_top = card_y + card_height - 1.5*cm
    
    draw_title(c, "Mon Entourage", text_x, text_top, size=22)
    
    # Calculate Areas
    available_height = text_top - card_y - 2*cm
    half_height = available_height / 2
    
    form = c.acroForm
    
    # Section 1: Soutiens
    y_soutiens = text_top - 1.5*cm
    draw_title(c, "Qui peut vous soutenir dans cette démarche ?", text_x, y_soutiens, size=14, color=PDFStyle.COLOR_SUCCESS)
    
    create_input_field(form, 's1_entourage_soutiens',
                       x=text_x, y=y_soutiens - half_height + 0.5*cm,
                       width=card_width - 2*cm, height=half_height - 1.5*cm,
                       tooltip='Vos soutiens', multiline=True)
                   
    # Section 2: Freins
    y_freins = y_soutiens - half_height
    draw_title(c, "Qui pourrait être un frein ?", text_x, y_freins, size=14, color=PDFStyle.COLOR_ACCENT_RED)
    
    create_input_field(form, 's1_entourage_freins',
                       x=text_x, y=y_freins - half_height + 0.5*cm,
                       width=card_width - 2*cm, height=half_height - 1.5*cm,
                       tooltip='Vos freins', multiline=True)

    c.showPage()
