#!/usr/bin/env python3
"""Generate ClawKing logo"""

from PIL import Image, ImageDraw, ImageFont
import os

# 创建 512x512 图片
img = Image.new('RGB', (512, 512), color='#FF6B35')
draw = ImageDraw.Draw(img)

# 身体
draw.ellipse([156, 280, 356, 430], fill='#FF8C42')

# 尾巴
draw.polygon([(180, 430), (140, 512), (220, 480)], fill='#FF6B35')
draw.polygon([(332, 430), (372, 512), (292, 480)], fill='#FF6B35')

# 头部
draw.ellipse([186, 150, 326, 270], fill='#FF8C42')

# 眼睛
draw.ellipse([226, 180, 266, 220], fill='white')
draw.ellipse([286, 180, 326, 220], fill='white')
draw.ellipse([236, 190, 256, 210], fill='black')
draw.ellipse([296, 190, 316, 210], fill='black')

# 嘴巴
draw.arc([246, 230, 306, 260], 0, 180, fill='black', width=3)

# 左钳子
draw.ellipse([80, 200, 180, 300], fill='#FF6B35')
draw.ellipse([50, 160, 130, 220], fill='#FF8C42')
draw.ellipse([40, 180, 100, 240], fill='#FF6B35')

# 右钳子
draw.ellipse([332, 200, 432, 300], fill='#FF6B35')
draw.ellipse([382, 160, 462, 220], fill='#FF8C42')
draw.ellipse([412, 180, 472, 240], fill='#FF6B35')

# 皇冠
crown_points = [
    (180, 100),  # 左下
    (220, 40),   # 左尖
    (245, 80),   # 凹槽
    (280, 30),   # 中尖（最高）
    (315, 80),   # 凹槽
    (340, 40),   # 右尖
    (380, 100),  # 右下
]
draw.polygon(crown_points, fill='#FFD700')

# 宝石
draw.ellipse([215, 40, 235, 60], fill='#FF4444')
draw.ellipse([300, 40, 320, 60], fill='#4444FF')
draw.ellipse([260, 70, 280, 90], fill='#44FF44')

# 皇冠底边
draw.rectangle([180, 95, 380, 115], fill='#FFA500')

# 文字 KING
try:
    font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 80)
except:
    font = ImageFont.load_default()
    
draw.text((256, 420), "KING", fill='white', anchor='mm', font=font)

# 保存
output_path = os.path.join(os.path.dirname(__file__), 'logo.png')
img.save(output_path, 'PNG')
print(f"✅ Logo saved to: {output_path}")
print(f"📐 Size: 512x512")
