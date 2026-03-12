from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from .config import PDFStyle

import math

def draw_page_background(c, width, height, use_blobs=False):
    """Refactored: Standard background with Nude color, Dot Grid, and Waves."""
    c.setFillColor(PDFStyle.COLOR_BG_NUDE)
    c.rect(0, 0, width, height, fill=1, stroke=0)
    
    if use_blobs:
        draw_background_blobs(c, width, height)
    else:
        draw_wavy_background(c, width, height)
        
    draw_dot_grid(c, width, height)
    draw_marginal_signature(c, height)
    
def draw_page_decorations(c, width, height, part_title=None, x_offset=0):
    """Draws Header (Logo + part title) and Footer (Page num) on top of the content."""
    if part_title is not None:
        draw_page_header(c, part_title, width, height, x_offset=x_offset)
    draw_page_footer(c, width, height, x_offset=x_offset)

def draw_wavy_background(c, width, height):
    """Draws subtle organic wave shapes in the background."""
    c.saveState()
    c.setFillColor(colors.HexColor("#F8E8DA"), alpha=0.4) # Subtle darker nude
    
    # Top Left Wave
    p1 = c.beginPath()
    p1.moveTo(0, height)
    p1.curveTo(width*0.3, height, width*0.5, height*0.85, 0, height*0.65)
    c.drawPath(p1, fill=1, stroke=0)
    
    # Bottom Right Wave
    p2 = c.beginPath()
    p2.moveTo(width, 0)
    p2.curveTo(width*0.7, 0, width*0.5, height*0.15, width, height*0.35)
    c.drawPath(p2, fill=1, stroke=0)
    
    c.restoreState()

def draw_background_blobs(c, width, height):
    """Draws large soft organic blobs (circles/ellipses) at Top-Right and Bottom-Left."""
    c.saveState()
    # Use the specifically defined pink blob color
    c.setFillColor(PDFStyle.COLOR_BG_BLOB, alpha=0.5)
    
    # Top Right Blob - slightly larger
    c.circle(width * 0.95, height * 0.92, 140, fill=1, stroke=0)
    
    # Bottom Blob - spans full width, starts higher, ends lower
    # We'll use a large ellipse for the bottom one
    # Moved center a bit higher (~15% of height) and made it very wide
    ellipse_w = width * 1.4
    ellipse_h = height * 0.4
    c.ellipse(-width*0.2, -height*0.1, width*1.2, height*0.35, fill=1, stroke=0)
    
    # Alternatively, use multiple circles to create a "wavy" fill at the bottom
    # but based on "traverser toute la largeur", a large horizontal ellipse or rect-to-curve is better.
    # Let's use a path for organic feel
    p = c.beginPath()
    p.moveTo(0, height * 0.25) # Starts higher
    p.curveTo(width * 0.3, height * 0.3, width * 0.7, height * 0.1, width, height * 0.2)
    p.lineTo(width, 0)
    p.lineTo(0, 0)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    
    c.restoreState()

def draw_page_header(c, part_title, width, height, x_offset=0):
    """Draws the standard header: small logo left, part title right."""
    c.saveState()
    # Left Logo - Shifted by x_offset + internal padding
    logo_y = height - 1.5*cm
    draw_branding_logo(c, x_offset + 0.8*cm, logo_y, size=12)
    
    # Right Part Title - Shifted from right edge
    if part_title:
        c.setFont(PDFStyle.FONT_TITLE, 10)
        c.setFillColor(PDFStyle.COLOR_ACCENT_RED)
        c.drawRightString(width - 1.2*cm, logo_y, part_title.upper())
    c.restoreState()

def draw_page_footer(c, width, height, x_offset=0):
    """Draws the standard footer: page number centered relative to the content area."""
    c.saveState()
    page_num = c.getPageNumber()
    c.setFont(PDFStyle.FONT_TITLE, 10)
    c.setFillColor(PDFStyle.COLOR_ACCENT_RED)
    
    # Center relative to the panel if x_offset is provided
    content_area_center = x_offset + (width - x_offset) / 2.0
    c.drawCentredString(content_area_center, 1.5*cm, str(page_num))
    c.restoreState()


def draw_dot_grid(c, width, height, color=PDFStyle.COLOR_ACCENT_BLUE, opacity=0.25):
    """Draws the signature Dot Grid."""
    step = 20
    c.saveState()
    c.setFillColor(color, alpha=opacity) 
    for x in range(0, int(width), step):
        for y in range(0, int(height), step):
            c.circle(x, y, 0.6, fill=1, stroke=0)
    c.restoreState()

def draw_marginal_signature(c, height):
    """Draws vertical 'marge de manœuvre' signature on the left."""
    c.saveState()
    c.translate(1.2*cm, height/2)
    c.rotate(90)
    c.setFont(PDFStyle.FONT_BODY, 8)
    c.setFillColor(PDFStyle.COLOR_ACCENT_RED) 
    c.drawCentredString(0, 0, "m a r g e   d e   m a n œ u v r e")
    c.restoreState()

def draw_card(c, x, y, width, height):
    """Draws a creme rounded card with shadow."""
    c.saveState()
    # Soft Shadow
    c.setFillColor(colors.black, alpha=0.03)
    c.roundRect(x+3, y-3, width, height, PDFStyle.CARD_RADIUS, fill=1, stroke=0)
    # Card
    c.setFillColor(PDFStyle.COLOR_CARD_CREME)
    c.roundRect(x, y, width, height, PDFStyle.CARD_RADIUS, fill=1, stroke=0)
    c.restoreState()

def draw_side_panel(c, x, page_width, page_height):
    """Draws a creme panel extending to Top, Bottom, Right."""
    c.saveState() 
    # Shadow (Left side only)
    c.setFillColor(colors.black, alpha=0.05)
    c.rect(x-3, 0, page_width - x + 3, page_height, fill=1, stroke=0)
    
    # Main Creme Panel
    c.setFillColor(PDFStyle.COLOR_CARD_CREME)
    c.rect(x, 0, page_width - x, page_height, fill=1, stroke=0)
    c.restoreState()

def draw_leaf(c, x, y, size=50, color=PDFStyle.COLOR_ACCENT_BLUE, angle=0, alpha=1.0):
    """Leaf decoration."""
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

def draw_title(c, text, x, y, size=24, color=PDFStyle.COLOR_ACCENT_BLUE):
    """Refactored: Standard H1 title."""
    c.saveState()
    c.setFont(PDFStyle.FONT_TITLE, size)
    c.setFillColor(color)
    c.drawString(x, y, text)
    c.restoreState()

def draw_branding_logo(c, x, y, size=40, align='left'):
    """
    Draws the 'marge de manœuvre' logo with underline.
    align: 'left' or 'center'
    """
    c.saveState()
    c.setFont(PDFStyle.FONT_BRANDING, size)
    c.setFillColor(PDFStyle.COLOR_ACCENT_RED)
    
    line_height = size * 1.1 # Approx line height based on font size font
    
    # Calculate underline length adaptable to size
    length = 9 * cm * (size / 40.0)
    
    if align == 'center':
        c.drawCentredString(x, y, "marge")
        c.drawCentredString(x, y - line_height, "de manœuvre")
    else:
        c.drawString(x, y, "marge")
        c.drawString(x, y - line_height, "de manœuvre")
    
    # Underline
    underline_y = y - line_height - 0.3*cm
    c.setLineWidth(3 * (size/40.0))
    c.setStrokeColor(PDFStyle.COLOR_ACCENT_RED)
    
    if align == 'center':
        c.line(x - length/2, underline_y, x + length/2, underline_y)
    else:
        c.line(x, underline_y, x + length, underline_y)
    c.restoreState()

def create_closing_page(c):
    """
    Standard Closing Page.
    """
    width, height = A4
    draw_page_background(c, width, height)
    
    # 1. Logo Centered
    logo_x = width/2
    logo_y = height/2 + 2*cm
    
    draw_branding_logo(c, logo_x, logo_y, size=40, align='center')
    
    # 2. Encouraging Text
    text_y = logo_y - 4*cm
    c.setFont(PDFStyle.FONT_TITLE, 14)
    c.setFillColor(PDFStyle.COLOR_TEXT_MAIN)
    
    messages = [
        "Félicitations pour ce temps pris pour vous.",
        "Laissez infuser ces réflexions.",
        "À très vite pour la suite de votre exploration."
    ]
    
    for msg in messages:
        c.drawCentredString(width/2, text_y, msg)
        text_y -= 1.0*cm

    c.showPage()

def draw_section_separator(c, x, y, width, color=PDFStyle.COLOR_ACCENT_BLUE):
    """
    Draws a simple separator line with a centered dot/symbol.
    """
    c.saveState()
    c.setStrokeColor(color)
    c.setLineWidth(1)
    
    # Line left
    c.line(x, y, x + width/2 - 0.5*cm, y)
    # Dot center
    c.setFillColor(color)
    c.circle(x + width/2, y, 0.1*cm, fill=1, stroke=0)
    # Line right
    c.line(x + width/2 + 0.5*cm, y, x + width, y)
    
    c.restoreState()
import os

def draw_circular_stamp(c, x, y, text, radius=1.8*cm):
    """Draws text curved around a central point, simulating a stamp."""
    c.saveState()
    c.translate(x, y)
    c.rotate(-15) # slight tilt
    
    c.setFont(PDFStyle.FONT_TITLE, 8)
    c.setFillColor(PDFStyle.COLOR_ACCENT_RED)
    
    chars = text + " · "
    angle_step = 360 / len(chars)
    for i, char in enumerate(chars):
        c.saveState()
        angle = math.radians(i * angle_step)
        char_x = radius * math.sin(angle)
        char_y = radius * math.cos(angle)
        c.translate(char_x, char_y)
        c.rotate(-math.degrees(angle))
        c.drawCentredString(0, 0, char)
        c.restoreState()
        
    c.setStrokeColor(PDFStyle.COLOR_ACCENT_RED)
    c.setLineWidth(1)
    # Simple placeholder shape in the center (hands/clap icon approximation)
    c.circle(0, 0.2*cm, radius*0.4, stroke=1, fill=0)
    c.line(-radius*0.3, -0.1*cm, radius*0.3, -0.1*cm)
    c.line(-radius*0.2, -0.3*cm, radius*0.2, -0.3*cm)
    
    c.restoreState()

def draw_pause_badge(c, x, y, radius=0.4*cm):
    """Draws the 'Pause' badge icon (circle with Play + Pause bars)."""
    c.saveState()
    
    # Circle
    c.setStrokeColor(PDFStyle.COLOR_WHITE)
    c.setLineWidth(1.5)
    c.circle(x, y + 0.15*cm, radius, fill=0, stroke=1)
    
    # Pause bars
    bar_width = 0.08*cm
    bar_height = 0.3*cm
    c.setFillColor(PDFStyle.COLOR_WHITE)
    c.rect(x - 0.15*cm, y, bar_width, bar_height, fill=1, stroke=0)
    
    # Play triangle
    p = c.beginPath()
    p.moveTo(x + 0.02*cm, y)
    p.lineTo(x + 0.02*cm, y + bar_height)
    p.lineTo(x + 0.22*cm, y + bar_height/2)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    
    c.restoreState()

def create_standard_cover(c, subtitle, title="BILAN DE COMPÉTENCES & ALIGNEMENT"):
    """
    Standard Cover Page generator for Workbooks.
    """
    width, height = A4
    
    # 1. Background Nude + Grid
    c.setFillColor(PDFStyle.COLOR_BG_NUDE)
    c.rect(0, 0, width, height, fill=1, stroke=0)
    draw_dot_grid(c, width, height)

    # 1b. Blue Side Band (Left)
    band_width = 1.75*cm 
    c.setFillColor(PDFStyle.COLOR_ACCENT_BLUE)
    c.rect(0, 0, band_width, height, fill=1, stroke=0)

    # A. Illustration Principale (Cover)
    if os.path.exists(PDFStyle.PATH_ILLU_COVER):
        content_width = width - band_width
        img_width = content_width * 0.75 
        center_x = band_width + (content_width - img_width) / 2
        
        c.drawImage(PDFStyle.PATH_ILLU_COVER, center_x, height * 0.10, width=img_width, height=height*0.5, mask='auto', preserveAspectRatio=True, anchor='sw')
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
    c.drawRightString(width - 40, height - 210, title) 
    
    c.setFont(PDFStyle.FONT_TITLE, 18)
    c.setFillColor(PDFStyle.COLOR_ACCENT_RED)
    c.drawRightString(width - 40, height - 240, subtitle)
    
    c.showPage()

