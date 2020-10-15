from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('font/OptimusPrinceps.ttf', 108)
overlay = Image.open('overlay.png')


def generate_meme(image_path, text, color):
    im = Image.open(image_path)
    aspect_ratio = im.size[0] / im.size[1]
    im = im.resize((1080 * aspect_ratio, 1080))
    im.paste(overlay, (0,0), overlay)
    d = ImageDraw.Draw(im)
    d.text((im.size[0] / 2, im.size[1] / 2), text, fill=color, anchor="ms", font=font)
    # print(im.format, im.size, im.mode)
    im.show()

generate_meme('test.webp', "h- hewwo?", "red")