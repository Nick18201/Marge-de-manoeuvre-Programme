from reportlab.lib import colors
from .config import PDFStyle

def create_input_field(form, name, x, y, width, height, tooltip='', multiline=False, value=''):
    """Helper to create consistent input fields."""
    bg_color = PDFStyle.COLOR_WHITE
    border_color = colors.lightgrey
    
    # Flags: 'multiline' allows multiple lines. 
    # 'doNotScroll' is NOT set, so it should scroll if text exceeds area.
    flags = 'multiline' if multiline else ''
    
    # Font Size: Use a fixed size to ensure it doesn't auto-scale to huge if empty, 
    # but small enough to fit lines. 
    # For multiline, 10 or 11 is good. 
    font_size = 11
    
    form.textfield(
        name=name,
        tooltip=tooltip,
        value=value,
        x=x, y=y,
        width=width, height=height,
        borderStyle='solid',
        borderColor=border_color,
        borderWidth=0.5,
        forceBorder=True,
        fillColor=bg_color,
        fieldFlags=flags,
        fontSize=font_size,
        maxlen=0
    )
