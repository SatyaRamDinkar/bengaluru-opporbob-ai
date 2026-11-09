"""
OpportunityBob — Update PPT with Live Streamlit URL on closing slide
"""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
import os

IBM_BLUE       = RGBColor(0x05, 0x43, 0xCE)
IBM_DARK       = RGBColor(0x16, 0x16, 0x16)
IBM_LIGHT_BLUE = RGBColor(0x40, 0x8B, 0xFC)
GOLD           = RGBColor(0xFF, 0xC0, 0x00)
WHITE          = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_GREY     = RGBColor(0xF4, 0xF4, 0xF4)
MID_GREY       = RGBColor(0xE0, 0xE0, 0xE0)
DARK_GREY      = RGBColor(0x52, 0x52, 0x52)
GREEN          = RGBColor(0x24, 0xA1, 0x48)
TEAL           = RGBColor(0x00, 0x91, 0x9A)
ORANGE         = RGBColor(0xFF, 0x83, 0x2A)
PURPLE         = RGBColor(0x82, 0x1E, 0xDE)

BLANK = None

def add_rect(slide, l, t, w, h, fill_color):
    shape = slide.shapes.add_shape(1, Inches(l), Inches(t), Inches(w), Inches(h))
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    shape.line.fill.background()
    return shape

def add_text(slide, text, l, t, w, h, font_size, bold=False, color=WHITE,
             align=PP_ALIGN.LEFT, italic=False):
    txBox = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    txBox.word_wrap = True
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(font_size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    run.font.name = "Calibri"
    return txBox

ppt_path = r"D:\Projects & Internships\bengaluru-opporbob-ai\OpportunityBob_IBM_Bobathon_Submission.pptx"
prs = Presentation(ppt_path)

# ── Add NEW SLIDE 9 — LIVE DEMO slide ───────────────────────────────────────
blank_layout = prs.slide_layouts[6]
sl = prs.slides.add_slide(blank_layout)

# Background
add_rect(sl, 0, 0, 13.33, 7.5, IBM_DARK)
add_rect(sl, 0, 0, 0.5, 7.5, GREEN)
add_rect(sl, 0.5, 0, 12.83, 0.04, GREEN)

# Header
add_text(sl, "LIVE DEMO — TRY IT NOW", 0.75, 0.12, 8, 0.38, 12, bold=True, color=GREEN)
add_text(sl, "OpportunityBob is Deployed Live on Streamlit Cloud",
         0.75, 0.42, 11, 0.7, 28, bold=True, color=WHITE)

# URL box — prominent
add_rect(sl, 0.65, 1.3, 11.9, 1.4, RGBColor(0x03, 0x33, 0x1A))
add_rect(sl, 0.65, 1.3, 11.9, 0.08, GREEN)
add_text(sl, "LIVE APP URL", 0.9, 1.4, 5, 0.38, 11, bold=True, color=GREEN)
add_text(sl,
         "https://bengaluru-opporbob-ai.streamlit.app",
         0.75, 1.72, 11.5, 0.72, 26, bold=True, color=GOLD, align=PP_ALIGN.CENTER)

# 3 feature quick-access cards
features = [
    (IBM_BLUE, "Tab 1: Job Matching",
     "Search in English, Kannada, or Hindi.\nGet scored matches with XAI reasoning."),
    (ORANGE,   "Tab 2: Skill Gap",
     "Enter your skills. Get a 3-step\npersonalised learning roadmap."),
    (TEAL,     "Tab 3: Community Exchange",
     "Browse surplus food, tools, volunteers.\nPost for human-review publication."),
]
for i, (col, title, desc) in enumerate(features):
    x = 0.65 + i * 4.1
    add_rect(sl, x, 2.95, 3.8, 2.2, RGBColor(0x20, 0x20, 0x20))
    add_rect(sl, x, 2.95, 3.8, 0.08, col)
    add_text(sl, title, x+0.2, 3.1, 3.4, 0.45, 13, bold=True, color=col)
    add_text(sl, desc, x+0.2, 3.65, 3.4, 1.3, 11, color=MID_GREY)

# GitHub + QR placeholder
add_rect(sl, 0.65, 5.35, 11.9, 1.3, RGBColor(0x0C, 0x0C, 0x0C))
add_text(sl, "GitHub Repository:", 0.9, 5.45, 3.5, 0.38, 11, bold=True, color=DARK_GREY)
add_text(sl, "https://github.com/SatyaRamDinkar/bengaluru-opporbob-ai",
         0.9, 5.82, 7.5, 0.5, 14, bold=True, color=IBM_LIGHT_BLUE)
add_text(sl, "SCAN TO OPEN", 9.8, 5.45, 2.5, 0.38, 10, bold=True, color=DARK_GREY, align=PP_ALIGN.CENTER)

# Scan box placeholder
add_rect(sl, 9.9, 5.82, 2.1, 0.75, RGBColor(0x20, 0x20, 0x20))
add_text(sl, "share.streamlit.io", 9.95, 5.9, 2.0, 0.6, 9, color=DARK_GREY, align=PP_ALIGN.CENTER)

add_rect(sl, 0, 7.1, 13.33, 0.4, GREEN)
add_text(sl, "OpportunityBob | IBM Bobathon 2026 | Live on Streamlit Cloud",
         0.3, 7.12, 12, 0.35, 10, color=WHITE, align=PP_ALIGN.CENTER)

# ── Also update Slide 8 (closing) info boxes to show Streamlit URL ───────────
closing_slide = prs.slides[7]  # 0-indexed, slide 8

# Add a Streamlit URL strip on existing slide 8
url_box = closing_slide.shapes.add_textbox(
    Inches(0.75), Inches(5.4), Inches(11.5), Inches(0.5))
tf = url_box.text_frame
p = tf.paragraphs[0]
p.alignment = PP_ALIGN.CENTER
run = p.add_run()
run.text = "LIVE DEMO: https://bengaluru-opporbob-ai.streamlit.app"
run.font.size = Pt(15)
run.font.bold = True
run.font.color.rgb = GOLD
run.font.name = "Calibri"

# Save
prs.save(ppt_path)
print(f"PPT updated with Streamlit URL — Total slides: {len(prs.slides)}")
