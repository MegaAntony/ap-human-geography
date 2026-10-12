import os
from PIL import Image, ImageDraw, ImageFont

# Canvas setup for 8.5 x 11 inch paper at 200 DPI = 1700 x 2200 pixels
W, H = 1700, 2200
img = Image.new('RGB', (W, H), color='#0B1120') # Deep slate background
draw = ImageDraw.Draw(img)

# Fonts
font_dir = '/System/Library/Fonts/Supplemental'
font_title = ImageFont.truetype(os.path.join(font_dir, 'Arial Bold.ttf'), 42)
font_subtitle = ImageFont.truetype(os.path.join(font_dir, 'Arial.ttf'), 24)
font_sec_title = ImageFont.truetype(os.path.join(font_dir, 'Arial Bold.ttf'), 26)
font_body = ImageFont.truetype(os.path.join(font_dir, 'Arial.ttf'), 20)
font_body_bold = ImageFont.truetype(os.path.join(font_dir, 'Arial Bold.ttf'), 20)
font_small = ImageFont.truetype(os.path.join(font_dir, 'Arial.ttf'), 17)
font_small_bold = ImageFont.truetype(os.path.join(font_dir, 'Arial Bold.ttf'), 17)
font_border = ImageFont.truetype(os.path.join(font_dir, 'Arial Bold.ttf'), 18)

# Paper coordinates (leaves 50px margin around canvas)
px1, py1 = 50, 50
px2, py2 = W - 50, H - 50

# Draw crisp white paper with rounded corners
draw.rounded_rectangle([px1, py1, px2, py2], radius=24, fill='#FFFFFF', outline='#38BDF8', width=4)

# Draw Inner Thematic Border (1/2 inch = 100px inset)
bx1, by1 = px1 + 50, py1 + 50
bx2, by2 = px2 - 50, py2 - 50
draw.rounded_rectangle([bx1, by1, bx2, by2], radius=16, outline='#D97706', width=5)

# Outer Border Banner Texts (Thematic Quotes around the border)
# Top Border Quote
quote_top = "★ THEMATIC BORDER: \"Most migrants move short distances for economic reasons (Ravenstein, 1885)\" ★"
draw.text((W // 2, py1 + 25), quote_top, fill='#92400E', font=font_border, anchor='mm')

# Bottom Border Quote
quote_bot = "★ \"Refugees cross international borders (UN 1951); Internally Displaced Persons (IDPs) remain within borders\" ★"
draw.text((W // 2, py2 - 25), quote_bot, fill='#92400E', font=font_border, anchor='mm')

# Header inside paper
hy = by1 + 45
draw.text((W // 2, hy), "AP® HUMAN GEOGRAPHY • UNIT 2 (TOPICS 2.10 – 2.12)", fill='#0369A1', font=font_subtitle, anchor='mm')
draw.text((W // 2, hy + 42), "PHYSICAL PAPER LAYOUT GRID (8.5\" × 11\" UNLINED SHEET)", fill='#0F172A', font=font_title, anchor='mm')
sub_header = "Organize your unlined paper into these 6 structural zones • Colored & Hand-Drawn • Due: Tuesday, Oct 13"
draw.text((W // 2, hy + 85), sub_header, fill='#475569', font=font_subtitle, anchor='mm')

# Usable content area inside the border and below header
cx1 = bx1 + 25
cy1 = hy + 115
cx2 = bx2 - 25
cy2 = by2 - 45

card_w = (cx2 - cx1 - 40) // 3
row1_h = 620
gap_y = 25
row2_y = cy1 + row1_h + gap_y
row2_h = cy2 - row2_y

def draw_card(x, y, w, h, bg_color, border_color, tag_text, tag_color, title_text, title_color):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=16, fill=bg_color, outline=border_color, width=3)
    # Tag
    draw.rounded_rectangle([x + 16, y + 14, x + 16 + len(tag_text) * 11 + 16, y + 42], radius=8, fill=tag_color)
    draw.text((x + 24, y + 28), tag_text, fill='#FFFFFF', font=font_small_bold, anchor='lm')
    # Title
    draw.text((x + 16, y + 68), title_text, fill=title_color, font=font_sec_title)
    # Horizontal separator
    draw.line([x + 16, y + 96, x + w - 16, y + 96], fill=border_color, width=2)

# ==========================================
# ROW 1 (TOP)
# ==========================================

# 1. ZONE 2: TOP-LEFT (RAVENSTEIN'S LAWS)
z2_x, z2_y = cx1, cy1
draw_card(z2_x, z2_y, card_w, row1_h, '#F0F9FF', '#0284C7', "ZONE 2 • TOP-LEFT", '#0284C7', "Ravenstein's Laws", '#0369A1')
ty = z2_y + 112
lines_z2 = [
    ("1. Distance Decay Principle:", True),
    ("   Most migrants travel short distances.", False),
    ("   Interaction fades with distance.", False),
    ("2. Urban Gravitation (Gravity Model):", True),
    ("   Long-distance migrants head to big cities.", False),
    ("3. Step Migration:", True),
    ("   Moves occur in stages (farm ➔ town ➔ city).", False),
    ("4. Rural to Urban Shift:", True),
    ("   Rural residents are more mobile.", False),
    ("5. Counter-Streams:", True),
    ("   Every major flow has a counter-stream.", False),
    ("6. Demographic Traits:", True),
    ("   Historically young single adult males for labor.", False),
    ("7. Economic Primacy:", True),
    ("   Economic opportunity is the #1 driver.", False)
]
for text, bold in lines_z2:
    draw.text((z2_x + 16, ty), text, fill='#0F172A' if bold else '#334155', font=font_body_bold if bold else font_body)
    ty += 28

# Draw small formula badge
draw.rounded_rectangle([z2_x + 16, z2_y + row1_h - 65, z2_x + card_w - 16, z2_y + row1_h - 16], radius=10, fill='#E0F2FE', outline='#38BDF8', width=2)
draw.text((z2_x + card_w // 2, z2_y + row1_h - 40), "Gravity: Interaction = (Pop A × Pop B) ÷ (Dist)²", fill='#0369A1', font=font_small_bold, anchor='mm')


# 2. ZONE 1: TOP-CENTER (TITLE & SYMBOLIC GRAPHIC)
z1_x, z1_y = cx1 + card_w + 20, cy1
draw_card(z1_x, z1_y, card_w, row1_h, '#FFFBEB', '#D97706', "ZONE 1 • CENTER CORE", '#D97706', "Central Title & Symbol", '#92400E')
# Central big title text
draw.text((z1_x + card_w // 2, z1_y + 130), "GLOBAL MIGRATION", fill='#B45309', font=font_sec_title, anchor='mm')
draw.text((z1_x + card_w // 2, z1_y + 162), "PUSH, PULL & IMPACT", fill='#78350F', font=font_title, anchor='mm')

# Symbolic Illustration Box
sym_x1, sym_y1 = z1_x + 25, z1_y + 195
sym_x2, sym_y2 = z1_x + card_w - 25, z1_y + 440
draw.rounded_rectangle([sym_x1, sym_y1, sym_x2, sym_y2], radius=16, fill='#FEF3C7', outline='#F59E0B', width=3)

# Inside illustration box: Passport & Globe icon drawing
draw.ellipse([sym_x1 + 80, sym_y1 + 25, sym_x2 - 80, sym_y2 - 75], outline='#D97706', width=5)
# Latitude & Longitude lines on globe
draw.arc([sym_x1 + 80, sym_y1 + 25, sym_x2 - 80, sym_y2 - 75], 0, 360, fill='#F59E0B', width=2)
draw.line([sym_x1 + 80, sym_y1 + 97, sym_x2 - 80, sym_y1 + 97], fill='#F59E0B', width=3) # Equator
draw.ellipse([sym_x1 + 135, sym_y1 + 25, sym_x2 - 135, sym_y2 - 75], outline='#F59E0B', width=3) # Meridian

# Flow Arrow across the globe
draw.line([sym_x1 + 50, sym_y2 - 45, sym_x2 - 50, sym_y1 + 45], fill='#DC2626', width=6)
# Arrow head
draw.polygon([(sym_x2 - 40, sym_y1 + 35), (sym_x2 - 50, sym_y1 + 75), (sym_x2 - 80, sym_y1 + 50)], fill='#DC2626')

draw.text((z1_x + card_w // 2, sym_y2 - 32), "[ LARGE CENTRAL HAND-DRAWN SYMBOL ]", fill='#92400E', font=font_small_bold, anchor='mm')
draw.text((z1_x + card_w // 2, sym_y2 - 12), "(Passport with visas, border trail, or divided globe)", fill='#78350F', font=font_small, anchor='mm')

# Guidelines note
draw.text((z1_x + card_w // 2, z1_y + 465), "• Must be large, colored, and prominent", fill='#1E293B', font=font_body_bold, anchor='mm')
draw.text((z1_x + card_w // 2, z1_y + 495), "• No empty white space left uncolored", fill='#1E293B', font=font_body, anchor='mm')
draw.text((z1_x + card_w // 2, z1_y + 525), "• Anchor quote ribbons connecting zones", fill='#1E293B', font=font_body, anchor='mm')

# Rubric highlight badge
draw.rounded_rectangle([z1_x + 16, z1_y + row1_h - 65, z1_x + card_w - 16, z1_y + row1_h - 16], radius=10, fill='#FEF3C7', outline='#F59E0B', width=2)
draw.text((z1_x + card_w // 2, z1_y + row1_h - 40), "Rubric Focus: Bold Visual Appeal & Thematic Cohesion", fill='#92400E', font=font_small_bold, anchor='mm')


# 3. ZONE 3: TOP-RIGHT (PUSH VS PULL MATRIX)
z3_x, z3_y = cx1 + 2 * (card_w + 20), cy1
draw_card(z3_x, z3_y, card_w, row1_h, '#ECFDF5', '#059669', "ZONE 3 • TOP-RIGHT", '#059669', "Push vs. Pull Factors", '#065F46')
ty = z3_y + 112
lines_z3 = [
    ("1. Economic (#1 Driver Globally):", True),
    ("   • Push: Job scarcity, inflation, poverty.", False),
    ("   • Pull: Factory wages, labor shortages.", False),
    ("2. Political Drivers:", True),
    ("   • Push: Civil war, dictatorship, persecution.", False),
    ("   • Pull: Democracy, civil liberties, asylum.", False),
    ("3. Social & Cultural Factors:", True),
    ("   • Push: Religious intolerance, discrimination.", False),
    ("   • Pull: Family ties (Chain Migration), colleges.", False),
    ("4. Environmental Conditions:", True),
    ("   • Push: Drought, crop blights, rising sea levels.", False),
    ("   • Pull: Warm Sunbelt climate, clean water.", False),
]
for text, bold in lines_z3:
    draw.text((z3_x + 16, ty), text, fill='#0F172A' if bold else '#334155', font=font_body_bold if bold else font_body)
    ty += 28

# Intervening Obstacles vs Opportunities callout
obs_box = [z3_x + 16, z3_y + row1_h - 120, z3_x + card_w - 16, z3_y + row1_h - 16]
draw.rounded_rectangle(obs_box, radius=10, fill='#D1FAE5', outline='#10B981', width=2)
draw.text((z3_x + 24, z3_y + row1_h - 100), "Intervening Obstacle vs. Opportunity:", fill='#065F46', font=font_small_bold)
draw.text((z3_x + 24, z3_y + row1_h - 75), "• Obstacle: Mountains, deserts, visa quotas, walls.", fill='#065F46', font=font_small)
draw.text((z3_x + 24, z3_y + row1_h - 50), "• Opportunity: Finding a great job midway & staying.", fill='#065F46', font=font_small)


# ==========================================
# ROW 2 (BOTTOM)
# ==========================================

# 4. ZONE 4: BOTTOM-LEFT (ESSENTIAL VOCABULARY)
z4_x, z4_y = cx1, row2_y
draw_card(z4_x, z4_y, card_w, row2_h, '#FAF5FF', '#9333EA', "ZONE 4 • BOTTOM-LEFT", '#9333EA', "Essential Vocab Corner", '#6B21A8')
ty = z4_y + 112
lines_z4 = [
    ("Refugee (UN 1951 Convention):", True),
    ("   Crosses INTERNATIONAL border to escape", False),
    ("   armed conflict or persecution. Has UN rights.", False),
    ("Internally Displaced Person (IDP):", True),
    ("   Fled home but REMAINS INSIDE own", False),
    ("   national borders. Lacks UN legal treaties.", False),
    ("Asylum Seeker:", True),
    ("   Crossed border and formally petitioned", False),
    ("   for legal recognition as a refugee.", False),
    ("Chain Migration:", True),
    ("   Moving because relatives/friends moved first.", False),
    ("Step Migration:", True),
    ("   Moving in stages (Farm ➔ Village ➔ City).", False),
    ("Transhumance:", True),
    ("   Seasonal pastoral movement (mountains/valleys).", False),
]
for text, bold in lines_z4:
    draw.text((z4_x + 16, ty), text, fill='#0F172A' if bold else '#334155', font=font_body_bold if bold else font_body)
    ty += 28

# Key distinction badge
draw.rounded_rectangle([z4_x + 16, z4_y + row2_h - 65, z4_x + card_w - 16, z4_y + row2_h - 16], radius=10, fill='#F3E8FF', outline='#A855F7', width=2)
draw.text((z4_x + card_w // 2, z4_y + row2_h - 40), "AP Trap: Refugee = International | IDP = Internal", fill='#6B21A8', font=font_small_bold, anchor='mm')


# 5. ZONE 5: BOTTOM-CENTER (CASE STUDY SKETCH MAP)
z5_x, z5_y = cx1 + card_w + 20, row2_y
draw_card(z5_x, z5_y, card_w, row2_h, '#FFF1F2', '#E11D48', "ZONE 5 • BOTTOM-CENTER", '#E11D48', "Corridor & Sketch Map", '#9F1239')

# Sketch Map Box
map_x1, map_y1 = z5_x + 20, z5_y + 112
map_x2, map_y2 = z5_x + card_w - 20, z5_y + 350
draw.rounded_rectangle([map_x1, map_y1, map_x2, map_y2], radius=14, fill='#FFE4E6', outline='#FB7185', width=3)

# Sketch map placeholder elements
draw.text((z5_x + card_w // 2, map_y1 + 25), "[ HAND-DRAWN SKETCH MAP AREA ]", fill='#9F1239', font=font_small_bold, anchor='mm')
# Draw map vectors
draw.ellipse([map_x1 + 40, map_y1 + 70, map_x1 + 100, map_y1 + 130], fill='#F43F5E') # Origin
draw.text((map_x1 + 70, map_y1 + 100), "ORIGIN", fill='#FFFFFF', font=font_small_bold, anchor='mm')

draw.ellipse([map_x2 - 130, map_y2 - 90, map_x2 - 40, map_y2 - 30], fill='#10B981') # Destination
draw.text((map_x2 - 85, map_y2 - 60), "DESTINATION", fill='#FFFFFF', font=font_small_bold, anchor='mm')

# Curving arrow
draw.line([map_x1 + 110, map_y1 + 105, map_x2 - 140, map_y2 - 65], fill='#BE123C', width=5)
draw.polygon([(map_x2 - 135, map_y2 - 80), (map_x2 - 125, map_y2 - 50), (map_x2 - 155, map_y2 - 60)], fill='#BE123C')
draw.text((z5_x + card_w // 2, map_y1 + 130), "MIGRATION CORRIDOR VECTOR", fill='#881337', font=font_small_bold, anchor='mm')
draw.text((z5_x + card_w // 2, map_y1 + 160), "Obstacles (Oceans, Borders, Deserts)", fill='#9F1239', font=font_small, anchor='mm')

# 3 Case study options text
draw.text((z5_x + 20, z5_y + 370), "Pick 1 Case Study to Illustrate:", fill='#0F172A', font=font_body_bold)
draw.text((z5_x + 20, z5_y + 400), "• Syria Civil War ➔ Turkey & Germany (6.6M forced)", fill='#334155', font=font_small)
draw.text((z5_x + 20, z5_y + 428), "• US Great Migration (Rural South ➔ Chicago/Detroit)", fill='#334155', font=font_small)
draw.text((z5_x + 20, z5_y + 456), "• Clarkston, GA: 'Ellis Island of the South' (50+ nations)", fill='#047857', font=font_small_bold)

draw.rounded_rectangle([z5_x + 16, z5_y + row2_h - 65, z5_x + card_w - 16, z5_y + row2_h - 16], radius=10, fill='#FFE4E6', outline='#F43F5E', width=2)
draw.text((z5_x + card_w // 2, z5_y + row2_h - 40), "Clarkston GA = Direct Georgia SSWG4.c Alignment", fill='#9F1239', font=font_small_bold, anchor='mm')


# 6. ZONE 6: BOTTOM-RIGHT (DUAL CONSEQUENCES MATRIX)
z6_x, z6_y = cx1 + 2 * (card_w + 20), row2_y
draw_card(z6_x, z6_y, card_w, row2_h, '#F0FDFA', '#0D9488', "ZONE 6 • BOTTOM-RIGHT", '#0D9488', "Consequences Matrix", '#115E59')
ty = z6_y + 112
lines_z6 = [
    ("Origin Country (Sending Societies):", True),
    ("  (+) Remittances:", True),
    ("      Cash sent home fuels domestic family", False),
    ("      survival and village GDP growth.", False),
    ("  (-) Brain Drain:", True),
    ("      Loss of doctors, scientists, engineers,", False),
    ("      and talented youth to wealthy states.", False),
    ("  (-) Demographics:", True),
    ("      Aging population and skewed sex ratios.", False),
    ("Destination Country (Receiving Societies):", True),
    ("  (+) Labor Supply Influx:", True),
    ("      Solves agricultural and STEM deficits.", False),
    ("  (+) Cultural Diffusion & Tax Revenues.", False),
    ("  (-) Social Friction & Xenophobia risks.", False),
]
for text, bold in lines_z6:
    draw.text((z6_x + 16, ty), text, fill='#0F172A' if bold else '#334155', font=font_body_bold if bold else font_body)
    ty += 28

draw.rounded_rectangle([z6_x + 16, z6_y + row2_h - 65, z6_x + card_w - 16, z6_y + row2_h - 16], radius=10, fill='#CCFBF1', outline='#14B8A6', width=2)
draw.text((z6_x + card_w // 2, z6_y + row2_h - 40), "Key Dualism: Remittances (+) vs. Brain Drain (-)", fill='#115E59', font=font_small_bold, anchor='mm')

# Save Image
output_path = '/Volumes/Backup/Antony/HighSchool/Grade9/HumanGeography/StudyMaterials/ExamsMaterials/01-set/studyGuide/migration-one-pager/migration_one_pager_layout_grid.png'
img.save(output_path, 'PNG', quality=95)
print(f"Generated successfully: {output_path} ({os.path.getsize(output_path):,} bytes)")
