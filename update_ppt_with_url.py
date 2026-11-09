"""
OpportunityBob — Update PPT with Exact Live Streamlit URL
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

# ── Add SLIDE 9: LIVE DEMO URL ──────────────────────────────────────────────
blank_layout = prs.slide_layouts[6]
sl = prs.slides.add_slide(blank_layout)

add_rect(sl, 0, 0, 13.33, 7.5, IBM_DARK)
add_rect(sl, 0, 0, 0.5, 7.5, GREEN)
add_rect(sl, 0.5, 0, 12.83, 0.04, GREEN)

add_text(sl, "LIVE CLOUD PROTOTYPE — STREAMLIT CLOUD", 0.75, 0.12, 8, 0.38, 12, bold=True, color=GREEN)
add_text(sl, "OpportunityBob is Deployed Live & Verified",
         0.75, 0.42, 11, 0.7, 28, bold=True, color=WHITE)

# Prominent URL Box
add_rect(sl, 0.65, 1.3, 11.9, 1.45, RGBColor(0x03, 0x33, 0x1A))
add_rect(sl, 0.65, 1.3, 11.9, 0.08, GREEN)
add_text(sl, "OFFICIAL LIVE APP URL", 0.9, 1.38, 5, 0.35, 11, bold=True, color=GREEN)
add_text(sl,
         "https://bengaluru-opporbob-ai-ud8igywajubnqmsmxn476f.streamlit.app/",
         0.75, 1.70, 11.7, 0.75, 20, bold=True, color=GOLD, align=PP_ALIGN.CENTER)

# 3 Feature highlights
features = [
    (IBM_BLUE, "Module 1: Multilingual Matching",
     "Instant semantic queries in English, Kannada (ಕನ್ನಡ), and Hindi (हिंदी). Calibrated fit score + XAI reasoning."),
    (ORANGE,   "Module 2: Skill Gap Roadmaps",
     "Automated identification of missing technical skills. Localized 3-step micro-learning paths via Karnataka ITIs."),
    (TEAL,     "Module 3: Surplus Food Exchange",
     "Redistributes event meals & community supplies. Built-in PII redaction and Human-in-the-Loop review."),
]
for i, (col, title, desc) in enumerate(features):
    x = 0.65 + i * 4.1
    add_rect(sl, x, 3.0, 3.8, 2.15, RGBColor(0x20, 0x20, 0x20))
    add_rect(sl, x, 3.0, 3.8, 0.08, col)
    add_text(sl, title, x+0.2, 3.15, 3.4, 0.45, 12.5, bold=True, color=col)
    add_text(sl, desc, x+0.2, 3.65, 3.4, 1.35, 10.5, color=MID_GREY)

# GitHub Repo footer box
add_rect(sl, 0.65, 5.35, 11.9, 1.3, RGBColor(0x0C, 0x0C, 0x0C))
add_text(sl, "GitHub Repository:", 0.9, 5.45, 3.5, 0.38, 11, bold=True, color=DARK_GREY)
add_text(sl, "https://github.com/SatyaRamDinkar/bengaluru-opporbob-ai",
         0.9, 5.82, 7.5, 0.5, 14, bold=True, color=IBM_LIGHT_BLUE)
add_text(sl, "STATUS: VERIFIED LIVE", 9.5, 5.75, 2.8, 0.38, 11, bold=True, color=GREEN, align=PP_ALIGN.CENTER)

add_rect(sl, 0, 7.1, 13.33, 0.4, GREEN)
add_text(sl, "OpportunityBob | IBM Bobathon 2026 | Verified Live Deployment",
         0.3, 7.12, 12, 0.35, 10, color=WHITE, align=PP_ALIGN.CENTER)

# ── Update Slide 8 with the exact URL ───────────────────────────────────────
closing_slide = prs.slides[7]
url_box = closing_slide.shapes.add_textbox(
    Inches(0.75), Inches(5.35), Inches(11.5), Inches(0.55))
tf = url_box.text_frame
p = tf.paragraphs[0]
p.alignment = PP_ALIGN.CENTER
run = p.add_run()
run.text = "LIVE APP: https://bengaluru-opporbob-ai-ud8igywajubnqmsmxn476f.streamlit.app/"
run.font.size = Pt(13.5)
run.font.bold = True
run.font.color.rgb = GOLD
run.font.name = "Calibri"

prs.save(ppt_path)
print(f"PPT updated with exact Streamlit Cloud URL! Total slides: {len(prs.slides)}")
