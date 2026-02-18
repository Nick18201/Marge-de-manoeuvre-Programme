from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from workbook_generator.utils import register_fonts
from workbook_generator.chapters.chap1 import (
    create_chap1_cover,
    create_engagement_page,
    create_concept_page,
    create_meteo_page,
    create_vision_page,
    create_boussole_page,
    create_sac_a_dos_page
)
from workbook_generator.components import create_closing_page

def build_chap1_pdf(output_filename):
    # Register fonts first
    register_fonts()
    
    c = canvas.Canvas(output_filename, pagesize=A4)
    c.setTitle("Marge de Manœuvre - Chapitre 1")
    
    create_chap1_cover(c)
    create_engagement_page(c)
    create_concept_page(c)
    create_meteo_page(c)
    create_vision_page(c)
    create_boussole_page(c)
    create_sac_a_dos_page(c)
    create_closing_page(c)
    
    c.save()
    print(f"PDF 'Workbook Chapitre 1' Generated: {output_filename}")

if __name__ == "__main__":
    final_output = "Workbook_Chap1.pdf"
    build_chap1_pdf(final_output)
