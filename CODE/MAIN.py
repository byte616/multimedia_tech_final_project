# ecoding: utf-8
from PIL import Image, ImageOps, ImageFont, ImageDraw 
import math
from PIL import ImageFilter

def add_border1(file_name):
    image = Image.open(file_name)
    image = ImageOps.expand(image, border=100, fill='white')
    image.save("deal.jpg")
    return image.size

def add_border2():
    img = Image.open('deal.jpg')
    [a,b]=img.size
    new_pic = Image.new('RGB', (img.size[0] , img.size[1] + int(a/2)), (255,255,255))
    new_pic.paste(img, (3, 3))
    return new_pic

def add_text():
    title_font = ImageFont.truetype('./FONT/AA.ttf',100)
    title_text1="我不會去摘月亮"
    title_text2="我要月亮奔我而來"
    image_editable = ImageDraw.Draw(new_pic)
    [n,m]=new_pic.size
    x=(n-len(title_text1)*100)/2
    y=b+50
    image_editable.text((x,y), title_text1, (0,0,0),title_font)
    x=(n-len(title_text2)*100)/2
    image_editable.text((x,y+100), title_text2, (0,0,0),title_font)

def softlightFilter(im):
    [im_width, im_height] = im.size
    pixels = im.load()
    for i in range(im_width):
        for j in range(im_height):
            r, g, b = pixels[i, j]
            r = 250 if r+30>250 else r+45
            g = 250 if g+30>250 else g+45
            b = 250 if b+30>250 else b+45
            pixels[i,j] = (r, g, b)
    im.save("result1.jpg")

def RGBtoGRAY(im):
    im_width, im_height = im.size
    pixels = im.load()
    for i in range(im_width):
        for j in range(im_height):
            r, g, b = pixels[i, j]
            gray = math.floor((r*30 + g*59 + b*11 + 50)/100)
            pixels[i,j] = (gray, gray, gray)
    im.save("result2.jpg")

def rmRED(im):
    im_width, im_height = im.size
    pixels = im.load()
    for i in range(im_width):
        for j in range(im_height):
            r, g, b = pixels[i, j]
            r = 0 if (g < 60 and b < 60) else r
            g = 250 if g+30>250 else g+45
            b = 250 if b+30>250 else b+45
            pixels[i,j] = (r, g, b)
    im.save("result3.jpg")

def inverted(im):
    im_width, im_height = im.size
    pixels = im.load()
    for i in range(im_width):
        for j in range(im_height):
            r, g, b = pixels[i, j]
            r = 255-r
            g = 255-g
            b = 255-b
            pixels[i,j] = (r, g, b)
    im.save("result4.jpg")

def edge(im):
    im=im.filter(ImageFilter.FIND_EDGES)
    im.save("result5.jpg")

## file name
file_name="42.jpg"
## add border
[a,b]=add_border1(file_name)
new_pic=add_border2()
## add text
add_text()
## save original pic
new_pic.save('result.jpg')
print("SUCCESS #1")
## softlight
softlightFilter(new_pic)
print("SUCCESS #2")
## gray scale
RGBtoGRAY(new_pic)
print("SUCCESS #3")
## rmRED
rmRED(new_pic)
print("SUCCESS #4")
## invert
inverted(new_pic)
print("SUCCESS #5")
## edge detection
edge(new_pic)
print("SUCCESS #6")