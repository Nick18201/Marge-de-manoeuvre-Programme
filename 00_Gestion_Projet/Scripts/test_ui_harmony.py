import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from workbook_generator.components import (
    create_standard_summary_page, 
    create_standard_engagement_page,
    create_standard_recap_page,
    ExercisePageLayout
)
from workbook_generator.utils import register_fonts

def run_tests():
    register_fonts()
    output_filename = "test_ui_harmony.pdf"
    c = canvas.Canvas(output_filename, pagesize=A4)
    
    # 1. Summary
    print("Testing summary page...")
    create_standard_summary_page(c, "1", "Concept", "Intro text", [
        ("1.", "Engagement"), ("2.", "Météo")
    ])
    
    # 2. Engagement
    print("Testing engagement page...")
    create_standard_engagement_page(c, "MON ENGAGEMENT")
    
    # 3. Recap
    print("Testing recap page...")
    create_standard_recap_page(c, "RÉCAPITULATIF", "Voici un récapitulatif test.", [
        "Qu'est-ce que vous avez appris ?",
        "Comment vous sentez-vous ?"
    ])
    
    # 4. Exercise Layout
    print("Testing exercise page layout...")
    layout = ExercisePageLayout(c, "Titre de l'exo", "1. MOTEURS")
    layout.add_intro_text("Consigne ou explication sur plusieurs lignes pour voir ce que ça donne avec le word wrap. " * 3)
    layout.add_question_block("Question 1 ?", "form_q1")
    layout.add_question_block("Question 2 avec un sous-titre ?", "form_q2", subtitle="Ceci est un sous-titre d'aide qui explique comment répondre à la question 2.")
    layout.render()
    
    c.save()
    print(f"Generated {output_filename} successfully.")

if __name__ == "__main__":
    run_tests()
