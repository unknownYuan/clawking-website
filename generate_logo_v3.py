#!/usr/bin/env python3
"""Generate ClawKing logo v3 - Cute Lobster Edition"""

from PIL import Image, ImageDraw, ImageFont
import os

# 创建 512x512 图片 - 渐变背景
img = Image.new('RGB', (512, 512), color='#FFE5E5')
draw = ImageDraw.Draw(img)

# 身体 - 圆润可爱
draw.ellipse([156, 300, 356, 460], fill='#FF7B7B')

# 尾巴 - 卷曲可爱
draw.ellipse([196, 440, 316, 512], fill='#FF5252')

# 头部 - 大大圆圆的
draw.ellipse([156, 160, 356, 320], fill='#FF7B7B')

# 腮红
draw.ellipse([176, 250, 220, 290], fill='#FFB3B3', outline=None)
draw.ellipse([292, 250, 336, 290], fill='#FFB3B3', outline=None)

# 眼睛 - 大大可爱，带高光
draw.ellipse([206, 180, 256, 240], fill='white')
draw.ellipse([256, 180, 306, 240], fill='white')

# 瞳孔 - 大大的
draw.ellipse([221, 200, 251, 230], fill='#4A4A4A')
draw.ellipse([271, 200, 301, 230], fill='#4A4A4A')

# 眼神高光 - 可爱关键！
draw.ellipse([228, 208, 238, 218], fill='white')
draw.ellipse([278, 208, 288, 218], fill='white')

# 嘴巴 - 小小微笑
draw.arc([246, 255, 286, 275], 0, 180, fill='#FF5252', width=4)

# 触须 - 龙虾特征！
draw.line([186, 160, 120, 100], fill='#FF7B7B', width=8)
draw.line([326, 160, 392, 100], fill='#FF7B7B', width=8)

# 触须末端球球
draw.ellipse([110, 90, 130, 110], fill='#FF5252')
draw.ellipse([382, 90, 402, 110], fill='#FF5252')

# 左钳子 - 大大突出
draw.ellipse([60, 260, 180, 380], fill='#FF7B7B')
draw.ellipse([40, 280, 120, 360], fill='#FF5252')

# 钳子内部
draw.ellipse([70, 300, 130, 360], fill='#FF9999')

# 右钳子
draw.ellipse([332, 260, 452, 380], fill='#FF7B7B')
draw.ellipse([392, 280, 472, 360], fill='#FF5252')

# 钳子内部
draw.ellipse([382, 300, 442, 360], fill='#FF9999')

# 小脚脚 - 可爱加分
for i in range(5):
    x = 180 + i * 30
    draw.ellipse([x, 460, x+15, 475], fill='#FF5252')

# 皇冠 - 小小皇冠，更可爱
crown_points = [
    (206, 100),
    (226, 60),
    (246, 90),
    (266, 50),
    (286, 90),
    (306, 60),
    (326, 100),
]
draw.polygon(crown_points, fill='#FFD700')

# 小宝石
draw.ellipse([226, 60, 246, 80], fill='#FF69B4')
draw.ellipse([266, 50, 286, 70], fill='#00CED1')
draw.ellipse([306, 60, 326, 80], fill='#98FB98')

# 皇冠底边
draw.rectangle([206, 95, 326, 110], fill='#FFA500')

# 文字 KING - 圆润字体
try:
    font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 90)
except:
    font = ImageFont.load_default()
    
draw.text((256, 450), "KING", fill='#FF5252', anchor='mm', font=font)

# 保存
output_dir = os.path.dirname(__file__) or '.'
img.save(os.path.join(output_dir, 'logo_v3.jpg'), 'JPEG', quality=95)
print(f"✅ Cute Lobster Logo saved!")
print(f"📐 Size: 512x512")
