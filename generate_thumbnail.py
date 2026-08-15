from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps
import math, os, random

W, H = 1280, 720
# Output path - this will be the thumbnail you upload in dashboard
OUT = r"C:\games\project\res\thumbnail_barrels_4v4.png"
OUT2 = r"C:\games\project\thumbnail_barrels_4v4.png"

# Colors
BG_TOP = (18, 22, 42)
BG_MID = (43, 58, 95)
BG_BOT = (20, 27, 50)
GROUND = (45, 36, 28)
GROUND2 = (58, 45, 35)

# Barrel colors
BARREL_WOOD = (139, 91, 43)
BARREL_WOOD_DARK = (92, 61, 29)
BARREL_WOOD_LIGHT = (183, 127, 66)
BARREL_BAND = (62, 62, 66)
BARREL_BAND_LIGHT = (95, 95, 102)

def lerp(a,b,t): return int(a + (b-a)*t)

# Create base image
img = Image.new("RGBA", (W, H), (0,0,0,255))
draw = ImageDraw.Draw(img)

# --- Gradient background ---
for y in range(H):
    t = y / H
    if t < 0.5:
        tt = t*2
        r = lerp(BG_TOP[0], BG_MID[0], tt)
        g = lerp(BG_TOP[1], BG_MID[1], tt)
        b = lerp(BG_TOP[2], BG_MID[2], tt)
    else:
        tt = (t-0.5)*2
        r = lerp(BG_MID[0], BG_BOT[0], tt)
        g = lerp(BG_MID[1], BG_BOT[1], tt)
        b = lerp(BG_MID[2], BG_BOT[2], tt)
    draw.line([(0,y),(W,y)], fill=(r,g,b))

# Add subtle vignette + spot light
overlay = Image.new("RGBA", (W,H), (0,0,0,0))
od = ImageDraw.Draw(overlay)
# Center glow
for i in range(300):
    alpha = int(30 * (1 - i/300)**1.5)
    od.ellipse([W//2-400+i, H//2-300+i, W//2+400-i, H//2+300-i], fill=(255,220,140, alpha))
# Top light streak
od.rectangle([0,0,W, 90], fill=(255,255,255, 18))
img = Image.alpha_composite(img.convert("RGBA"), overlay)

draw = ImageDraw.Draw(img)
# Ground
draw.rectangle([0, 540, W, H], fill=GROUND)
# ground planks detail
for x in range(0, W, 80):
    draw.line([(x, 540),(x, H)], fill=GROUND2, width=2)
for y in range(580, H, 45):
    draw.line([(0,y),(W,y)], fill=(35,28,22), width=2)
# ground perspective line
draw.rectangle([0, 535, W, 545], fill=(255,200,90, 90))

# --- Helpers ---
def draw_barrel(cx, cy, w, h, scale=1.0):
    # w,h base size
    w = int(w*scale); h = int(h*scale)
    x0 = cx - w//2; x1 = cx + w//2
    y0 = cy - h//2; y1 = cy + h//2
    # shadow
    draw.ellipse([x0-4, y1-10, x1+4, y1+14], fill=(0,0,0,70))
    # body rectangle with rounded
    # main wood
    draw.rectangle([x0, y0+12, x1, y1-12], fill=BARREL_WOOD)
    # top/bottom ellipse caps
    draw.ellipse([x0, y0, x1, y0+28], fill=BARREL_WOOD_LIGHT, outline=BARREL_WOOD_DARK, width=3)
    draw.ellipse([x0, y1-28, x1, y1], fill=BARREL_WOOD_DARK, outline=(0,0,0), width=2)
    # wood planks vertical lines
    for i in range(1,4):
        px = x0 + w*i//4
        draw.line([(px, y0+14),(px, y1-14)], fill=BARREL_WOOD_DARK, width=3)
        draw.line([(px+1, y0+14),(px+1, y1-14)], fill=BARREL_WOOD_LIGHT, width=1)
    # horizontal bands
    band_ys = [y0+32, y0+h//2-6, y0+h//2+6, y1-32]
    for by in band_ys:
        draw.rectangle([x0-3, by-7, x1+3, by+7], fill=BARREL_BAND, outline=BARREL_BAND_LIGHT, width=1)
        # rivets
        for rx in [x0+8, x0+w//2, x1-8]:
            draw.ellipse([rx-3, by-2, rx+3, by+2], fill=(180,180,185))
    # highlight
    draw.rectangle([x0+10, y0+34, x0+18, y1-34], fill=(255,255,255, 38))
    # outline
    draw.rectangle([x0, y0+12, x1, y1-12], outline=(0,0,0), width=3)
    draw.ellipse([x0, y0, x1, y0+28], outline=(0,0,0), width=3)
    draw.ellipse([x0, y1-28, x1, y1], outline=(0,0,0), width=2)

def draw_crate(cx, cy, w, h):
    x0=cx-w//2; x1=cx+w//2; y0=cy-h//2; y1=cy+h//2
    draw.rectangle([x0,y0,x1,y1], fill=(158,112,68), outline=(0,0,0), width=3)
    draw.rectangle([x0+6,y0+6,x1-6,y1-6], fill=(183,140,90), outline=(92,61,29), width=2)
    # planks
    for i in range(1,3):
        py = y0 + h*i//3
        draw.line([(x0,py),(x1,py)], fill=(92,61,29), width=2)
    for i in range(1,3):
        px = x0 + w*i//3
        draw.line([(px,y0),(px,y1)], fill=(92,61,29), width=2)
    # X brace
    draw.line([(x0+8,y0+8),(x1-8,y1-8)], fill=(0,0,0), width=2)
    draw.line([(x1-8,y0+8),(x0+8,y1-8)], fill=(0,0,0), width=2)
    draw.ellipse([x0-3,y1-4,x1+3,y1+8], fill=(0,0,0,50))

# Try load font
try:
    # Try to find a bold font
    font_bold_large = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 22)
    font_bold_med = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 18)
    font_bold_small = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 14)
    font_regular = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 13)
    font_title = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 52)
    font_subtitle = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 18)
except:
    font_bold_large = ImageFont.load_default()
    font_bold_med = ImageFont.load_default()
    font_bold_small = ImageFont.load_default()
    font_regular = ImageFont.load_default()
    font_title = ImageFont.load_default()
    font_subtitle = ImageFont.load_default()

def draw_character(cx, cy, palette, facing_right=True, weapon_color=(80,80,80), skin_tone=None, hair_color=None, accessory=None):
    # palette: dict with body, head, etc or simple color
    # Draw chibi character peeking behind barrel
    # cy is feet y
    # facing direction affects weapon hand
    body_w = 44; body_h = 48
    head_r = 28
    # shadow
    draw.ellipse([cx-22, cy-6, cx+22, cy+10], fill=(0,0,0,80))
    # legs
    leg_y0 = cy - 22; leg_y1 = cy - 2
    draw.rectangle([cx-14, leg_y0, cx-3, leg_y1], fill=palette["pants"], outline=(0,0,0), width=2)
    draw.rectangle([cx+3, leg_y0, cx+14, leg_y1], fill=palette["pants"], outline=(0,0,0), width=2)
    # shoes
    draw.ellipse([cx-15, leg_y1-3, cx-1, leg_y1+6], fill=(30,30,30), outline=(0,0,0), width=1)
    draw.ellipse([cx+1, leg_y1-3, cx+15, leg_y1+6], fill=(30,30,30), outline=(0,0,0), width=1)
    # body
    bx0 = cx - body_w//2; bx1 = cx + body_w//2
    by0 = cy - 22 - body_h; by1 = cy - 22
    draw.rectangle([bx0, by0, bx1, by1], fill=palette["shirt"], outline=(0,0,0), width=2)
    # shirt detail
    draw.rectangle([bx0+6, by0+10, bx0+12, by1-8], fill=(255,255,255,55))
    # collar
    draw.polygon([(cx-10, by0), (cx, by0+10), (cx+10, by0)], fill=(0,0,0,30))
    # arms
    # left arm (behind barrel side)
    # arm holding weapon
    arm_x = cx + (18 if facing_right else -18)
    arm_y = by0 + 18
    draw.ellipse([arm_x-10, arm_y-7, arm_x+10, arm_y+7], fill=palette["skin"], outline=(0,0,0), width=2)
    # weapon
    wx0 = arm_x + (12 if facing_right else -28)
    wy0 = arm_y -4; wy1 = arm_y+4
    wx1 = wx0 + (34 if facing_right else -34)
    # gun body
    if facing_right:
        draw.rectangle([wx0, wy0, wx0+30, wy1+6], fill=weapon_color, outline=(0,0,0), width=2)
        draw.rectangle([wx0+26, wy0-2, wx0+38, wy1+2], fill=(40,40,40), outline=(0,0,0), width=1)
        # muzzle
        draw.rectangle([wx0+36, wy0, wx0+40, wy1], fill=(60,60,60))
    else:
        draw.rectangle([wx0-30, wy0, wx0, wy1+6], fill=weapon_color, outline=(0,0,0), width=2)
        draw.rectangle([wx0-38, wy0-2, wx0-26, wy1+2], fill=(40,40,40), outline=(0,0,0), width=1)
        draw.rectangle([wx0-40, wy0, wx0-36, wy1], fill=(60,60,60))
    # other arm
    other_x = cx - (18 if facing_right else -18)
    draw.ellipse([other_x-8, arm_y-6, other_x+8, arm_y+6], fill=palette["skin"], outline=(0,0,0), width=2)

    # head
    hx, hy = cx, by0 - 2
    # neck
    draw.rectangle([cx-8, by0-4, cx+8, by0+6], fill=palette["skin"], outline=(0,0,0), width=1)
    # face base
    draw.ellipse([hx-head_r, hy-head_r, hx+head_r, hy+head_r], fill=palette["skin"], outline=(0,0,0), width=2)
    # hair
    if hair_color:
        # top hair cap
        draw.ellipse([hx-head_r+1, hy-head_r-2, hx+head_r-1, hy-2], fill=hair_color, outline=(0,0,0), width=1)
        # bangs
        draw.ellipse([hx-head_r+2, hy-head_r+6, hx+head_r-2, hy+2], fill=hair_color)

    # eyes
    eye_y = hy + 4
    # eye whites
    draw.ellipse([hx-14, eye_y-5, hx-4, eye_y+5], fill=(255,255,255), outline=(0,0,0), width=1)
    draw.ellipse([hx+4, eye_y-5, hx+14, eye_y+5], fill=(255,255,255), outline=(0,0,0), width=1)
    # pupils - look towards center (peek)
    look = 2 if facing_right else -2
    draw.ellipse([hx-11+look, eye_y-3, hx-6+look, eye_y+3], fill=(30,30,30))
    draw.ellipse([hx+7+look, eye_y-3, hx+12+look, eye_y+3], fill=(30,30,30))
    # eye shine
    draw.ellipse([hx-10+look, eye_y-2, hx-8+look, eye_y+0], fill=(255,255,255))
    draw.ellipse([hx+8+look, eye_y-2, hx+10+look, eye_y+0], fill=(255,255,255))
    # mouth
    draw.arc([hx-5, eye_y+6, hx+5, eye_y+14], 0, 180, fill=(0,0,0), width=2)
    # blush
    draw.ellipse([hx-20, eye_y+7, hx-14, eye_y+11], fill=(255,120,120, 120))
    draw.ellipse([hx+14, eye_y+7, hx+20, eye_y+11], fill=(255,120,120, 120))

    # accessory
    if accessory == "cap":
        draw.rectangle([hx-head_r+4, hy-head_r+4, hx+head_r-4, hy-8], fill=(200,30,30), outline=(0,0,0), width=1)
        draw.ellipse([hx-head_r+2, hy-12, hx+head_r-2, hy-2], fill=(200,30,30), outline=(0,0,0), width=1)
        draw.ellipse([hx-6, hy-14, hx+6, hy-8], fill=(255,255,255))
    elif accessory == "crown":
        draw.polygon([(hx-14, hy-head_r+8), (hx-8, hy-head_r-2), (hx, hy-head_r+6), (hx+8, hy-head_r-2), (hx+14, hy-head_r+8), (hx+10, hy-head_r+10), (hx-10, hy-head_r+10)], fill=(255,215,0), outline=(0,0,0), width=1)
        draw.ellipse([hx-2, hy-head_r+2, hx+2, hy-head_r+6], fill=(255,0,0))
    elif accessory == "ears":
        # mickey ears
        draw.ellipse([hx-22, hy-head_r-4, hx-6, hy-head_r+14], fill=(20,20,20), outline=(0,0,0), width=1)
        draw.ellipse([hx+6, hy-head_r-4, hx+22, hy-head_r+14], fill=(20,20,20), outline=(0,0,0), width=1)
    elif accessory == "fluff":
        # fluffy hair
        for dx, dy in [(-14,-8),(0,-12),(14,-8),(-10,-14),(10,-14)]:
            draw.ellipse([hx+dx-10, hy-head_r+dy, hx+dx+10, hy-head_r+dy+14], fill=(255,200,220), outline=(0,0,0), width=1)
    elif accessory == "kirby":
        draw.ellipse([hx-head_r+6, hy-head_r-6, hx+head_r-6, hy-4], fill=(255,120,180), outline=(0,0,0), width=1)
        draw.ellipse([hx-head_r+2, hy-8, hx-8, hy+2], fill=(255,120,180), outline=(0,0,0), width=1)
        draw.ellipse([hx+8, hy-8, hx+head_r-2, hy+2], fill=(255,120,180), outline=(0,0,0), width=1)

def draw_name_label(cx, y, name, align_center=True):
    # y is top of label
    # measure
    bbox = draw.textbbox((0,0), name, font=font_bold_med)
    tw = bbox[2]-bbox[0]; th = bbox[3]-bbox[1]
    pad_x = 8; pad_y = 4
    rw = tw + pad_x*2; rh = th + pad_y*2
    x0 = cx - rw//2; x1 = cx + rw//2
    y0 = y; y1 = y+rh
    # shadow
    draw.rectangle([x0+2, y0+2, x1+2, y1+2], fill=(0,0,0,100))
    # bg
    draw.rectangle([x0, y0, x1, y1], fill=(255,255,255), outline=(0,0,0), width=2)
    # text
    draw.text((cx - tw//2, y0 + pad_y -1), name, fill=(20,20,20), font=font_bold_med)

# --- Draw title at top center ---
# Title bg banner
banner_y0 = 18; banner_y1 = 76
banner_x0 = W//2 - 310; banner_x1 = W//2 + 310
# shadow
draw.rectangle([banner_x0+4, banner_y0+4, banner_x1+4, banner_y1+4], fill=(0,0,0,90))
draw.rectangle([banner_x0, banner_y0, banner_x1, banner_y1], fill=(255, 64, 64), outline=(0,0,0), width=3)
draw.rectangle([banner_x0, banner_y0, banner_x1, banner_y0+8], fill=(255,255,255,60))
# title text
title = "BARREL BATTLE  4  VS  4"
# center
bbox = draw.textbbox((0,0), title, font=font_title)
tw = bbox[2]-bbox[0]
# hack font_title size 52 might be large, adjust if needed
try:
    small_title_font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 32)
    bbox = draw.textbbox((0,0), title, font=small_title_font)
    tw = bbox[2]-bbox[0]
    draw.text((W//2 - tw//2, 26), title, fill=(255,255,255), font=small_title_font, stroke_width=3, stroke_fill=(0,0,0))
except:
    draw.text((W//2 - tw//2, 26), title, fill=(255,255,255), font=font_title, stroke_width=3, stroke_fill=(0,0,0))

subtitle = "HIDE  •  PEEK  •  SHOOT"
bbox2 = draw.textbbox((0,0), subtitle, font=font_subtitle)
tw2 = bbox2[2]-bbox2[0]
draw.text((W//2 - tw2//2, 62), subtitle, fill=(255,230,120), font=font_subtitle, stroke_width=2, stroke_fill=(0,0,0))

# --- Barrel stacks left and right ---
# Left stack positions (x,y) - vertical stack of 4 barrels with slight variation
left_cx = 178
right_cx = 1102
barrel_w, barrel_h = 110, 92

left_barrel_positions = [
    (left_cx, 165),
    (left_cx, 265),
    (left_cx, 380),
    (left_cx, 490),
]
right_barrel_positions = [
    (right_cx, 165),
    (right_cx, 265),
    (right_cx, 380),
    (right_cx, 490),
]

# Also add side crates for variety behind barrels (depth)
for (cx,cy) in left_barrel_positions:
    # back crate shadow behind
    draw_crate(cx+18, cy+10, 84, 84)
for (cx,cy) in right_barrel_positions:
    draw_crate(cx-18, cy+10, 84, 84)

# Draw actual barrels front
for (cx,cy) in left_barrel_positions:
    draw_barrel(cx, cy, barrel_w, barrel_h)
for (cx,cy) in right_barrel_positions:
    draw_barrel(cx, cy, barrel_w, barrel_h)

# --- Characters ---
# Left side 4 top to bottom: Ilikepaperclips, RodrigoM25613, Fluffpuff, Kirb0_EXE
# Right side 4: PileoHarse, Iilikepaperclips, M1cky_M0us3, Ell13b3ll13
# Palettes distinct per user

palettes = {
    "Ilikepaperclips": {"shirt": (220,50,50), "pants": (40,40,120), "skin": (255,220,180), "hair": (60,30,15)},
    "RodrigoM25613": {"shirt": (50,120,220), "pants": (30,30,30), "skin": (232,190,150), "hair": (25,25,25)},
    "Fluffpuff": {"shirt": (255,150,200), "pants": (255,230,240), "skin": (255,225,195), "hair": (255,210,230)},
    "Kirb0_EXE": {"shirt": (255,110,160), "pants": (250,80,120), "skin": (255,190,190), "hair": (255,120,180)},
    "PileoHarse": {"shirt": (110,180,70), "pants": (110,90,50), "skin": (235,200,165), "hair": (90,60,30)},
    "Iilikepaperclips": {"shirt": (180,40,40), "pants": (50,50,140), "skin": (255,215,170), "hair": (50,25,10)},
    "M1cky_M0us3": {"shirt": (20,20,20), "pants": (200,30,30), "skin": (255,220,180), "hair": (20,20,20)},
    "Ell13b3ll13": {"shirt": (160,80,220), "pants": (40,20,60), "skin": (255,220,195), "hair": (90,40,130)},
}

# weapon colors per player
weapon_colors = {
    "Ilikepaperclips": (230,70,70),
    "RodrigoM25613": (70,130,230),
    "Fluffpuff": (255,170,220),
    "Kirb0_EXE": (255,90,150),
    "PileoHarse": (120,190,80),
    "Iilikepaperclips": (190,50,50),
    "M1cky_M0us3": (50,50,50),
    "Ell13b3ll13": (150,70,210),
}
accessories = {
    "Ilikepaperclips": "crown",
    "RodrigoM25613": "cap",
    "Fluffpuff": "fluff",
    "Kirb0_EXE": "kirby",
    "PileoHarse": None,
    "Iilikepaperclips": "crown",
    "M1cky_M0us3": "ears",
    "Ell13b3ll13": None,
}

left_names = ["Ilikepaperclips","RodrigoM25613","Fluffpuff","Kirb0_EXE"]
right_names = ["PileoHarse","Iilikepaperclips","M1cky_M0us3","Ell13b3ll13"]

# Character Y positions: feet Y aligned near barrel middles but offset to peek
left_char_ys = [205, 315, 430, 538]
right_char_ys = [205, 315, 430, 538]
left_char_x = left_cx + 78  # peek to right of left barrels
right_char_x = right_cx - 78 # peek to left

for idx, name in enumerate(left_names):
    pal = palettes[name]
    # enhance palette with pants/skin keys
    palette = {
        "shirt": pal["shirt"],
        "pants": pal["pants"],
        "skin": pal["skin"],
    }
    cy = left_char_ys[idx]
    cx = left_char_x
    # add slight random offset for natural peek
    cx += [6, -2, 4, -4][idx]
    # draw character facing right (toward center)
    draw_character(cx, cy, palette, facing_right=True, weapon_color=weapon_colors[name], hair_color=pal["hair"], accessory=accessories[name])
    # name label above head
    # head top approx cy -22 -48 -28*2 ~ cy -126
    label_y = cy - 126 - 26
    draw_name_label(cx, label_y, name)

for idx, name in enumerate(right_names):
    pal = palettes[name]
    palette = {"shirt": pal["shirt"], "pants": pal["pants"], "skin": pal["skin"]}
    cy = right_char_ys[idx]
    cx = right_char_x
    cx += [-6, 2, -4, 4][idx]
    draw_character(cx, cy, palette, facing_right=False, weapon_color=weapon_colors[name], hair_color=pal["hair"], accessory=accessories[name])
    label_y = cy - 126 - 26
    draw_name_label(cx, label_y, name)

# --- Center VS ---
vs_cx, vs_y = W//2, 310
# VS burst
for r, col in [(62, (0,0,0,90)), (56, (255,210,60)), (50, (255,80,80)), (44, (255,255,255))]:
    draw.ellipse([vs_cx-r, vs_y-r, vs_cx+r, vs_y+r], fill=col, outline=(0,0,0) if r!=62 else None, width=3 if r<60 else 0)
# VS text
try:
    vs_font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 40)
    vs_text = "VS"
    bbox = draw.textbbox((0,0), vs_text, font=vs_font)
    tw = bbox[2]-bbox[0]; th = bbox[3]-bbox[1]
    draw.text((vs_cx - tw//2, vs_y - th//2 -2), vs_text, fill=(20,20,20), font=vs_font)
except:
    draw.text((vs_cx-18, vs_y-14), "VS", fill=(20,20,20), font=font_title)

# Crosshair in center slightly below VS
draw.ellipse([vs_cx-8, vs_y+52-8, vs_cx+8, vs_y+52+8], outline=(255,255,255), width=2)
draw.line([(vs_cx-14, vs_y+52),(vs_cx+14, vs_y+52)], fill=(255,255,255), width=2)
draw.line([(vs_cx, vs_y+52-14),(vs_cx, vs_y+52+14)], fill=(255,255,255), width=2)

# Side team labels
def draw_team_label(cx, y, text, color):
    bbox = draw.textbbox((0,0), text, font=font_bold_small)
    tw = bbox[2]-bbox[0]; th = bbox[3]-bbox[1]
    rw = tw+14; rh = th+8
    x0=cx-rw//2; x1=cx+rw//2; y0=y; y1=y+rh
    draw.rectangle([x0, y0, x1, y1], fill=color, outline=(0,0,0), width=2)
    draw.text((cx - tw//2, y0+3), text, fill=(255,255,255), font=font_bold_small, stroke_width=1, stroke_fill=(0,0,0))

draw_team_label(left_cx, 560, "BLUE  TEAM", (60,120,255))
draw_team_label(right_cx, 560, "RED  TEAM", (255,60,60))

# Bottom bar with game name
draw.rectangle([0, H-42, W, H], fill=(0,0,0, 180))
try:
    bottom_font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 18)
    draw.text((W//2 - 210, H-30), "Paperclip's Shooting Game!   •   4v4 Barrel Hideout", fill=(255,255,255), font=bottom_font)
except:
    draw.text((W//2 - 180, H-30), "Paperclip's Shooting Game! - 4v4 Barrel Hideout", fill=(255,255,255), font=font_bold_med)

# Border
draw.rectangle([0,0,W-1,H-1], outline=(255,255,255, 70), width=2)
draw.rectangle([2,2,W-3,H-3], outline=(0,0,0, 120), width=2)

# Save
img.convert("RGB").save(OUT, "PNG", optimize=True)
img.convert("RGB").save(OUT2, "PNG", optimize=True)
print(f"Saved to {OUT} size {img.size}")
print(f"Saved to {OUT2}")

# Also make icon versions (square 512, 1024)
for sz in [512, 1024]:
    thumb = img.convert("RGB").resize((sz, sz), Image.LANCZOS)
    # Actually need to crop center square from 1280x720 -> 720x720 then resize
    sq = img.convert("RGB").crop(( (W-720)//2, 0, (W+720)//2, 720 ))
    sq = sq.resize((sz,sz), Image.LANCZOS)
    sq.save(f"C:/games/project/res/thumbnail_icon_{sz}.png", "PNG", optimize=True)
    print(f"Icon {sz} saved")

# Also make a small preview for scene icon replacement
preview = img.convert("RGB").resize((256,144), Image.LANCZOS)
preview.save(r"C:\games\project\res\thumbnail_preview.png", "PNG")
print("Preview saved")
