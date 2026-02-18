from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from .config import PDFStyle

def draw_page_background(c, width, height):
    """Refactored: Standard background with Nude color, Dot Grid, and Marginal Signature."""
    c.setFillColor(PDFStyle.COLOR_BG_NUDE)
    c.rect(0, 0, width, height, fill=1, stroke=0)
    draw_dot_grid(c, width, height)
    draw_marginal_signature(c, height)

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
    c.setFillColor(PDFStyle.COLOR_TEXT_SECONDARY) 
    c.drawCentredString(0, 0, "m a r g e   d e   m a n œ u v r e")
    c.restoreState()

def draw_card(c, x, y, width, height):
    """Draws a white rounded card with shadow."""
    c.saveState()
    # Shadow
    c.setFillColor(colors.black, alpha=0.05)
    c.roundRect(x+3, y-3, width, height, PDFStyle.CARD_RADIUS, fill=1, stroke=0)
    # Card
    c.setFillColor(PDFStyle.COLOR_WHITE)
    c.roundRect(x, y, width, height, PDFStyle.CARD_RADIUS, fill=1, stroke=0)
    c.restoreState()

def draw_side_panel(c, x, page_width, page_height):
    """Draws a white panel extending to Top, Bottom, Right."""
    c.saveState() 
    # Shadow (Left side only)
    c.setFillColor(colors.black, alpha=0.05)
    c.rect(x-3, 0, page_width - x + 3, page_height, fill=1, stroke=0)
    
    # Main White Panel
    c.setFillColor(PDFStyle.COLOR_WHITE)
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

def draw_branding_logo(c, x, y, size=40):
    """
    Draws the 'marge de manœuvre' logo with underline.
    """
    c.saveState()
    c.setFont(PDFStyle.FONT_BRANDING, size)
    c.setFillColor(PDFStyle.COLOR_ACCENT_RED)
    
    line_height = size * 1.1 # Approx line height based on font size font
    
    c.drawString(x, y, "marge")
    c.drawString(x, y - line_height, "de manœuvre")
    
    # Underline
    underline_y = y - line_height - 0.3*cm
    # specific fix for the underline length adaptable to size
    # Base length 9cm for size 40. 
    # ratio = size / 40.
    # length = 9 * ratio
    length = 9 * cm * (size / 40.0)
    
    c.setLineWidth(3 * (size/40.0))
    c.setStrokeColor(PDFStyle.COLOR_ACCENT_RED)
    c.line(x, underline_y, x + length, underline_y)
    c.restoreState()

def create_closing_page(c):
    """
    Standard Closing Page.
    """
    width, height = A4
    draw_page_background(c, width, height)
    
    # 1. Logo Centered
    # Calculate approx center. 
    # "marge" is roughly 5 chars wide. "de manœuvre" is longer.
    # We'll just place it somewhat centrally visually.
    
    logo_x = width/2 - 4.5*cm # Centering approx based on 9cm width
    logo_y = height/2 + 2*cm
    
    draw_branding_logo(c, logo_x, logo_y, size=40)
    
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
