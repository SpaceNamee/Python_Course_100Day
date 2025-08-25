from PIL import Image, ImageDraw, ImageFont

def add_watermark_overlay(input_image_path, output_image_path, watermark_text):
    input_image = Image.open(input_image_path)
    input_image = input_image.convert("RGBA")
    width, height = input_image.size

    overlay = Image.new("RGBA", input_image.size, (255,255,255,0))
    
    draw =  ImageDraw.Draw(overlay)

    watermark_color_pattern = (255,255,255,50)
    step = 50
    # size = 10
    # for size in [1,25]:
    #     for n in range(step,width,step):
    #         for x in range(step,height-step,step):
    #             draw.ellipse([n-size/2,x-size/2,n+size//2,x+size//2], fill="yellow")


    for i in range(0, width+height, step):
        draw.line([(0, height - i), (i, height)], fill=watermark_color_pattern, width=5)

    font_size = 80
    font = ImageFont.truetype("arial.ttf", font_size)

    # text_width, text_height = draw.textsize(watermark_text, font=font)
    text_width = draw.textlength(watermark_text, font=font)
    text_height = font_size * 1
    x = (width  - text_width) // 2
    y = (height - text_height) // 2

    watermark_color_text = (255,255,255,80)

    draw.text((x,y), watermark_text, fill=watermark_color_text, font=font)

    watermark_image = Image.alpha_composite(input_image, overlay)

    watermark_image.save(output_image_path)

input_image_path = r"D:\MyPython\Python_Course_100Day\Day85\361883.jpg"
output_image_path = r"D:\MyPython\Python_Course_100Day\Day85\361883_watermarked.png"
watermark_text = "Sample Watermark"

add_watermark_overlay(input_image_path, output_image_path, watermark_text)