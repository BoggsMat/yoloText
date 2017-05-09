import PIL
import os, random
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from random import randint

def genIm(): 
	# Random ints 
	size = randint(40, 150)
	r = randint(0, 255)
	g = randint(0, 255)
	b = randint(0, 255)
	x = randint(0, 150)
	y = randint(0, 400)

	# Choose a random font 
	fontName = random.choice(os.listdir("fonts/"))

	# Fetch font
	font = ImageFont.truetype("fonts/" + fontName, size)

	# Gen image 
	img=Image.new("RGBA", (448,448),(r,g,b))
	draw = ImageDraw.Draw(img)

	# Gen text 
	draw.text((x, y),"test",(255-r,255-g,255-b),font=font)
	draw = ImageDraw.Draw(img)

	img.show("test.png")

if __name__ == "__main__":

	genIm()