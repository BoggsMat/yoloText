import PIL
import os, random
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from random import randint
from pascal import PascalVocWriter
import cv2 
import argparse

def genIm(num, word): 
	# Random ints 
	size = randint(40, 150)
	r = randint(0, 255)
	g = randint(0, 255)
	b = randint(0, 255)
	x = randint(0, 380 - 2*size)
	y = randint(0, 400 - size)

	# Choose a random font 
	fontName = random.choice(os.listdir("fonts/"))

	# Fetch font
	font = ImageFont.truetype("fonts/" + fontName, size)

	# Gen image 
	img=Image.new("RGBA", (448,448),(r,g,b))
	draw = ImageDraw.Draw(img)

	# Gen text 
	w, h = draw.textsize(word, font)
	draw.text((x, y),word,(255-r,255-g,255-b),font=font)
	draw = ImageDraw.Draw(img)

	img.save('training/' + str("%04d"%num) + '.png')

	return (x,y,w,h)

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--num', default=45, type=int)
	args = parser.parse_args()

	words = ["apple", "bike", "car", "drive", "end", "fail", "grad", "hope", "item", "job"]

	for i in range(args.num): 
		wd = randint(0,9)
		(x, y, w, h) = genIm(i, words[wd])
		writer = PascalVocWriter('training/', str("%04d"%i)+ ".xml", (448,448))
		writer.addBndBox(x-2, y-2, x+w+2, y+h+2, words[wd])
		writer.save('training/'+str("%04d"%i)+ ".xml")



