from PIL import Image, ImageDraw, ImageFont
from math import ceil

def add_watermark(input_image_path, output_image_path, watermark_text):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    
    watermark = Image.new("RGBA", original_image.size)
    draw = ImageDraw.Draw(watermark, "RGBA")
    
    font_size=ceil(height/width*min(75,int(width/len(watermark_text))))
    print(height,width,font_size)
    text = watermark_text
    font = ImageFont.truetype("Mexaronzy.ttf", font_size)

    text_width, text_height = draw.textsize(text, font)
    x_pos = width - text_width - 10
    y_pos = height - text_height - 10

    draw.text((x_pos, y_pos), text, font=font, fill=(255, 255, 255, 128))
    
    watermarked_image = Image.alpha_composite(original_image.convert("RGBA"), watermark)
    watermarked_image.save(output_image_path, "PNG")
    
import sys


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Использование: python main.py <input_image_path> <output_image_path> <watermark_text>")
        print("Или использование: python main.py <input_and_output_image_path> <watermark_text>")
        sys.exit(1)
    
    if len(sys.argv) == 3:
        input_image_path = sys.argv[1]
        output_image_path = sys.argv[1]
        watermark_text = sys.argv[2]
    else:
        input_image_path = sys.argv[1]
        output_image_path = sys.argv[2]
        watermark_text = sys.argv[3]

    add_watermark(input_image_path, output_image_path, watermark_text)
