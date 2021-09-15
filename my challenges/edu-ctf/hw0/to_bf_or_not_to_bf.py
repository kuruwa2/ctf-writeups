#!/usr/bin/env python3
import cv2      #https://pypi.org/project/opencv-python/
import random
import string

charset = string.ascii_letters + string.digits + '+='
fire, water, earth, air = [random.choice(charset) for _ in range(4)]

def combine(a, b):
    return ''.join([a,b])

def encrypt(arr):
    swamp  = combine(water, earth)
    energy = combine(fire, air)
    lava   = combine(fire, earth)
    life   = combine(swamp, energy)
    stone  = combine(lava, air)
    sand   = combine(stone, water)
    seed   = combine(sand, life)
    random.seed(seed)
    
    h, w = arr.shape
    for i in range(h):
        for j in range(w):
            arr[i][j] ^= random.randint(0,255)


for i in ['flag', 'golem']:
    msg = cv2.imread(i+'.png', cv2.IMREAD_GRAYSCALE)
    encrypt(msg)
    cv2.imwrite(i+'_enc.png', msg)
