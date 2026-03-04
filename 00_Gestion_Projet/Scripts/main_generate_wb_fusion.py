from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from workbook_generator.utils import register_fonts
from workbook_generator.components import create_standard_cover, create_closing_page
from workbook_generator.chapters.chap1 import (
    create_engagement_page,
    create_concept_page,
    create_meteo_page,
    create_vision_page,
    create_boussole_page,
    create_sac_a_dos_page
)
from workbook_generator.chapters.chap2 import (
    create_heritage_page,
    create_work_image_page,
    create_mentors_page,
    create_analysis_parcours_pages,
    create_skills_transfer_page,
    create_tree_of_life_page,
    create_interview_page
)

def create_fusion_cover(c):
    create_standard_cover(c, "WORKBOOK : SÉANCES 1 À 3")

def build_wb_fusion_pdf(output_filename):
    # Register fonts first
    register_fonts()
    
    c = canvas.Canvas(output_filename, pagesize=A4)
    c.setTitle("Marge de Manœuvre - Fusion Séances 1 à 3")
    
    # --- COVER ---
    create_fusion_cover(c)
    
    # --- SÉANCE 1 : RESTITUTION (from chap1) ---
    create_engagement_page(c)
    create_concept_page(c)
    create_meteo_page(c)
    create_vision_page(c)
    create_boussole_page(c)
    create_sac_a_dos_page(c)
    
    # --- SÉANCE 2 : HÉRITAGES ---
    create_heritage_page(c)
    create_work_image_page(c)
    create_mentors_page(c)
    
    # --- SÉANCE 3 : PARCOURS ---
    # We will modify create_analysis_parcours_pages in chap2.py to use blocks instead of tables
    create_analysis_parcours_pages(c)
    create_skills_transfer_page(c)
    
    # --- BONUS ---
    create_tree_of_life_page(c)
    create_interview_page(c)
    
    create_closing_page(c)
    
    c.save()
    print(f"PDF 'Workbook Fusion Séances 1-3' Generated: {output_filename}")

if __name__ == "__main__":
    final_output = "Workbook_Fusion_S1_S3.pdf"
    build_wb_fusion_pdf(final_output)
