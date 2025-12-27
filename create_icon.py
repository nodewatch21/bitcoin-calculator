"""
Bitcoin Icon Generator - PROFESSIONAL VERSION
Creates bitcoin_icon.ico with glow effects and round design
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import sys

def create_bitcoin_icon():
    """Create professional Bitcoin icon with glow effect"""
    
    sizes = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)]
    images = []
    
    for size in sizes:
        # Create transparent background
        img = Image.new('RGBA', size, (0, 0, 0, 0))
        
        # Calculate dimensions
        width, height = size
        center_x, center_y = width // 2, height // 2
        radius = int(width * 0.45)  # 90% of half width for padding
        
        # Create a temporary larger image for better glow effect
        temp_size = (width * 2, height * 2)
        temp_img = Image.new('RGBA', temp_size, (0, 0, 0, 0))
        temp_draw = ImageDraw.Draw(temp_img)
        temp_center = (temp_size[0] // 2, temp_size[1] // 2)
        temp_radius = radius * 2
        
        # Draw multiple circles for glow effect (outer glow)
        glow_layers = 8
        for i in range(glow_layers, 0, -1):
            alpha = int(30 * (1 - i/glow_layers))  # Fade out
            glow_radius = temp_radius + (i * 8)
            glow_color = (242, 169, 0, alpha)  # Bitcoin orange with alpha
            temp_draw.ellipse(
                [temp_center[0] - glow_radius, temp_center[1] - glow_radius,
                 temp_center[0] + glow_radius, temp_center[1] + glow_radius],
                fill=glow_color
            )
        
        # Draw main circle (solid Bitcoin orange)
        temp_draw.ellipse(
            [temp_center[0] - temp_radius, temp_center[1] - temp_radius,
             temp_center[0] + temp_radius, temp_center[1] + temp_radius],
            fill=(242, 169, 0, 255)  # #f2a900
        )
        
        # Resize back to original size (smooth anti-aliasing)
        temp_img = temp_img.resize(size, Image.LANCZOS)
        img = Image.alpha_composite(img, temp_img)
        
        # Now draw the Bitcoin symbol
        draw = ImageDraw.Draw(img)
        
        # Calculate font size
        font_size = int(width * 0.6)
        
        # Try to load a font
        font = None
        font_paths = [
            'arial.ttf',
            'arialbd.ttf',  # Arial Bold
            'segoeui.ttf',
            'segoeuib.ttf',  # Segoe UI Bold
            'C:\\Windows\\Fonts\\arial.ttf',
            'C:\\Windows\\Fonts\\arialbd.ttf',
        ]
        
        for font_path in font_paths:
            try:
                font = ImageFont.truetype(font_path, font_size)
                break
            except:
                continue
        
        if font is None:
            font = ImageFont.load_default()
        
        # Draw Bitcoin symbol
        # Using 'Ƀ' (Latin Capital Letter B with Stroke) - close to Bitcoin symbol
        # Or '₿' if available, with fallback
        bitcoin_symbols = ['₿', 'Ƀ', 'Ƀ', 'B']
        text = None
        
        for symbol in bitcoin_symbols:
            try:
                bbox = draw.textbbox((0, 0), symbol, font=font)
                text = symbol
                break
            except:
                continue
        
        if text is None:
            text = 'B'
        
        # Get text dimensions
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        # Center the text
        x = center_x - text_width // 2 - bbox[0]
        y = center_y - text_height // 2 - bbox[1]
        
        # Draw text shadow for depth (multiple layers)
        shadow_offset = max(2, width // 80)
        for offset in range(shadow_offset, 0, -1):
            shadow_alpha = int(100 * (offset / shadow_offset))
            draw.text(
                (x + offset, y + offset),
                text,
                fill=(0, 0, 0, shadow_alpha),
                font=font
            )
        
        # Draw main text in dark color
        draw.text((x, y), text, fill=(10, 10, 10, 255), font=font)
        
        # Keep transparency - don't convert to RGB!
        # This preserves the transparent background
        images.append(img)
    
    # Save as ICO
    images[0].save('bitcoin_icon.ico', format='ICO', sizes=[(s[0], s[1]) for s in sizes], append_images=images[1:])
    print('[OK] bitcoin_icon.ico created with GLOW EFFECT!')
    return True

if __name__ == '__main__':
    try:
        create_bitcoin_icon()
    except Exception as e:
        print(f'[ERROR] Icon creation failed: {e}')
        sys.exit(1)
