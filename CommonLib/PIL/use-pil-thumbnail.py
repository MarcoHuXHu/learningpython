#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image

with Image.open('/Users/HXH/Documents/Ronaldo.png') as im:
    w, h = im.size
    print('Original image size: %s * %s', w, h)
    while (w > 720 or h > 360):
        w = w // 2
        h = h // 2
    print('Resize image size to: %s * %s', w, h)
    im.thumbnail((w, h))
    im.save('/Users/HXH/Documents/Ronaldo-thumbnail.png')