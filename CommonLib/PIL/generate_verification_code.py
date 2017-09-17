#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random

def random_character():
    return chr(random.randint(65, 90))

# random color for background
def rndColor1():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# random color for verification code
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

character_size = 60
character_number = 5
character_spacing = 10

width  = character_size * character_number
height = character_size
# create image object
image = Image.new('RGB', (width, height), (255, 255, 255))
# create font object
font = ImageFont.truetype('Arial.ttf', character_size // 2)
# create draw object
draw = ImageDraw.Draw(image)
# fill every pix for background
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor1())
# fill in text
for t in range(character_number):
    draw.text((character_size * t + random.randint(1, character_spacing), random.randint(1, character_spacing)),
              random_character(), font=font, fill=rndColor2())
image = image.filter(ImageFilter.BLUR)
image.save('/Users/HXH/Documents/verification_code.jpg', 'jpeg')