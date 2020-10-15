from PIL import Image, ImageDraw, ImageFont
import os
import random

font = ImageFont.truetype('font/OptimusPrinceps.ttf', 114)
overlay = Image.open('overlay.png')
srcpath = 'images/'
destpath = 'send/'

def get_base_image():
    images = os.listdir(srcpath)
    return random.choice(images)


def generate_meme(image_path, text, color):
    im = Image.open(image_path)
    aspect_ratio = im.size[0] / im.size[1]
    im = im.resize((int(1080 * aspect_ratio), 1080))
    im.paste(overlay, (0,0), overlay)
    d = ImageDraw.Draw(im)
    d.text((im.size[0] / 2, im.size[1] / 2), text, fill=color, anchor="ms", font=font)
    # print(im.format, im.size, im.mode)
    # im.show()
    filename = ''.join(e for e in text if e.isalnum()) + str(random.randint(100, 999)) + '.jpg'
    im.save(destpath + filename)
    return destpath + filename

def make_death_meme(text):
    return generate_meme(srcpath + get_base_image(), text, (201,64,31))
    
def make_humanity_meme(text):
    return generate_meme(srcpath + get_base_image(), text, (135,175,148))
    
def make_bonfire_meme(text):
    return generate_meme(srcpath + get_base_image(), text, (253,188,96))
