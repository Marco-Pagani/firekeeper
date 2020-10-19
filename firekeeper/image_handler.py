from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import os, random

datapath = 'firekeeper/data/'
srcpath =  datapath + 'source_images/'
destpath = datapath + 'output_images/'
font = ImageFont.truetype(datapath + 'fonts/OptimusPrinceps.ttf', 114)
overlay = Image.open(srcpath + 'overlay.png')

def get_base_image():
    images = os.listdir(srcpath)
    return random.choice(images)

def generate_meme(image_path, text, color):
    im = Image.open(image_path)
    # scale the image to 1080 on the short edge
    aspect_ratio = im.size[0] / im.size[1]
    im = im.resize((int(1080 * aspect_ratio), 1080))
    # add the text backing overlay
    im.paste(overlay, (0,0), overlay)
    # draw the text
    d = ImageDraw.Draw(im)
    d.text((im.size[0] / 2, im.size[1] / 2), text, fill=color, anchor="ms", font=font)
    # save the image to a jpeg
    filename = ''.join(e for e in text if e.isalnum()) + str(random.randint(100, 999)) + '.jpg'
    im.save(destpath + filename)
    # return the filepath
    return destpath + filename

def make_death_meme(text):
    return generate_meme(srcpath + get_base_image(), text, (201,64,31))
    
def make_humanity_meme(text):
    return generate_meme(srcpath + get_base_image(), text, (135,175,148))
    
def make_bonfire_meme(text):
    return generate_meme(srcpath + get_base_image(), text, (253,188,96))
