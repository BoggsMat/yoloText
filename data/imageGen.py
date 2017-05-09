import PIL
import os, random
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from random import randint

def genIm(num, word): 
	# Random ints 
	size = randint(40, 150)
	r = randint(0, 255)
	g = randint(0, 255)
	b = randint(0, 255)
	x = randint(0, 380 - 2*size)
	y = randint(0, 400 - size)

	# Choose a random font 
	#fontName = random.choice(os.listdir("fonts/"))
	fontName = "BrookeS8.ttf"
	print(str(num) + fontName)
	# Fetch font
	font = ImageFont.truetype("fonts/" + fontName, size)

	# Gen image 
	img=Image.new("RGBA", (448,448),(r,g,b))
	draw = ImageDraw.Draw(img)

	# Gen text 
	w, h = draw.textsize(word, font)
	draw.text((x, y),word,(255-r,255-g,255-b),font=font)
	draw = ImageDraw.Draw(img)

	img.show(title = str(num))

if __name__ == "__main__":
	words = ["apple", "bike", "car", "drive", "end", "fail", "grad", "hope", "item", "jump"]

	for x in range(10): 
		w = randint(0,9)
		genIm(x, words[w])


