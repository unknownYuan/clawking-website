#!/usr/bin/env python3
"""Generate ClawKing logo v2 - Royal Blue/Purple theme"""

from PIL import Image, ImageDraw, ImageFont
import os

# 创建 512x512 图片
img = Image.new('RGB', (512, 512), color='#4A00E0')
draw = ImageDraw.Draw(img)

# 身体 - 紫色渐变效果
draw.ellipse([156, 280, 356, 430], fill='#8E2DE2')

# 尾巴
draw.polygon([(180, 430), (140, 512), (220, 480)], fill='#4A00E0')
draw.polygon([(332, 430), (372, 512), (292, 480)], fill='#4A00E0')

# 头部
draw.ellipse([186, 150, 326, 270], fill='#8E2DE2')

# 眼睛
draw.ellipse([226, 180, 266, 220], fill='white')
draw.ellipse([286, 180, 326, 220], fill='white')
draw.ellipse([236, 190, 256, 210], fill='#FFD700')
draw.ellipse([296, 190, 316, 210], fill='#FFD700')

# 嘴巴 - 微笑
draw.arc([246, 230, 306, 260], 0, 180, fill='white', width=3)

# 左钳子
draw.ellipse([80, 200, 180, 300], fill='#6A3093')
draw.ellipse([50, 160, 130, 220], fill='#8E2DE2')
draw.ellipse([40, 180, 100, 240], fill='#6A3093')

# 右钳子
draw.ellipse([332, 200, 432, 300], fill='#6A3093')
draw.ellipse([382, 160, 462, 220], fill='#8E2DE2')
draw.ellipse([412, 180, 472, 240], fill='#6A3093')

# 皇冠 - 金色
crown_points = [
    (180, 100),
    (220, 40),
    (245, 80),
    (280, 30),
    (315, 80),
    (340, 40),
    (380, 100),
]
draw.polygon(crown_points, fill='#FFD700')

# 宝石 - 彩色
draw.ellipse([215, 40, 235, 60], fill='#FF6B6B')
draw.ellipse([300, 40, 320, 60], fill='#4ECDC4')
draw.ellipse([260, 70, 280, 90], fill='#C44DFF')

# 皇冠底边
draw.rectangle([180, 95, 380, 115], fill='#FFA500')

# 文字 KING - 金色
try:
    font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 80)
except:
    font = ImageFont.load_default()
    
draw.text((256, 420), "KING", fill='#FFD700', anchor='mm', font=font)

# 保存
output_dir = os.path.dirname(__file__) or '.'
img.save(os.path.join(output_dir, 'logo_v2.jpg'), 'JPEG', quality=95)
print(f"✅ Logo v2 saved!")
print(f"📐 Size: 512x512")
