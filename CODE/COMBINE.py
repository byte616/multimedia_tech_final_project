import tkinter as tk
from tkinter.constants import W
from PIL import Image, ImageOps, ImageFont, ImageDraw, Image, ImageTk, ImageFilter
import math

def add_border1(file_name):
    image = Image.open(file_name)
    image = ImageOps.expand(image, border=100, fill='white')
    image.save("../example_result/deal.jpg")
    return image.size

def add_border2():
    img = Image.open('../example_result/deal.jpg')
    [a,b]=img.size
    new_pic = Image.new('RGB', (img.size[0] , img.size[1] + int(a/2)), (255,255,255))
    new_pic.paste(img, (3, 3))
    return new_pic

def add_text(new_pic):
    title_font = ImageFont.truetype('../FONT/AA.ttf',100)
    title_text1="我不會去摘月亮"
    title_text2="我要月亮奔我而來"
    image_editable = ImageDraw.Draw(new_pic)
    [n,m]=new_pic.size
    x=(n-len(title_text1)*100)/2
    y=b+200
    image_editable.text((x,y), title_text1, (0,0,0),title_font)
    x=(n-len(title_text2)*100)/2
    image_editable.text((x,y+100), title_text2, (0,0,0),title_font)

# filter
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
    im.save("../example_result/result1.jpg")

def RGBtoGRAY(im):
    im_width, im_height = im.size
    pixels = im.load()
    for i in range(im_width):
        for j in range(im_height):
            r, g, b = pixels[i, j]
            gray = math.floor((r*30 + g*59 + b*11 + 50)/100)
            pixels[i,j] = (gray, gray, gray)
    im.save("../example_result/result2.jpg")

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
    im.save("../example_result/result3.jpg")

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
    im.save("../example_result/result4.jpg")

def edge(im):
    im=im.filter(ImageFilter.FIND_EDGES)
    im.save("../example_result/result5.jpg")

def Pimage(new_pic):
    ## add border
    [a,b]=add_border1(file_name)
    new_pic=add_border2()
    ## add text
    add_text(new_pic)
    ## save original pic
    new_pic.save('../example_result/result.jpg')
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


## file name
file_name="../image/42.jpg"
new_pic=Image.open(file_name)
[a,b]=new_pic.size
Pimage(new_pic)

#########################################################

window = tk.Tk()
window.title('GUI')
align_mode = 'nswe'
pad = 5

# 分割空間
div_size = 300
img_size = div_size * 2
div1 = tk.Frame(window,  width=img_size , height=img_size , bg='#ffcc66')
div2 = tk.Frame(window,  width=div_size , height=div_size , bg='black')
div3 = tk.Frame(window,  width=div_size , height=div_size , bg='#f5b2af')

div1.grid(column=0, row=0, padx=pad, pady=pad, rowspan=2, sticky=align_mode)
div2.grid(column=1, row=0, padx=pad, pady=pad, sticky=align_mode)
div3.grid(column=1, row=1, padx=pad, pady=pad, sticky=align_mode)

# TITLE

lbl_title1 = tk.Label(div2, text='文青句濾鏡', font= ('Helvetica 15 bold italic'), bg='black', fg='white')
lbl_title2 = tk.Label(div2, text="CHOOSE\nMODE", font= ('Helvetica 15 bold italic'), bg='black', fg='white')

lbl_title1.grid(column=0, row=0, sticky=align_mode)
lbl_title2.grid(column=0, row=2, sticky=align_mode)

# 視窗縮放
def define_layout(obj, cols=1, rows=1):
    def method(trg, col, row):
        for c in range(cols):    
            trg.columnconfigure(c, weight=1)
        for r in range(rows):
            trg.rowconfigure(r, weight=1)
    if type(obj)==list:        
        [ method(trg, cols, rows) for trg in obj ]
    else:
        trg = obj
        method(trg, cols, rows)

# BUTTON EVENT
def bt1_event():
    img_title = Image.open('../example_result/result2.jpg')
    open_img(img_title)

def bt2_event():
    img_title = Image.open('../example_result/result1.jpg')
    open_img(img_title)

def bt3_event():
    img_title = Image.open('../example_result/result3.jpg')
    open_img(img_title)

def bt4_event():
    img_title = Image.open('../example_result/result4.jpg')
    open_img(img_title)

def bt5_event():
    img_title = Image.open('../example_result/result5.jpg')
    open_img(img_title)

def bt6_event():
    img_title = Image.open('../example_result/result.jpg')
    open_img(img_title)

def open_img(im):
    [n,m]=im.size
    a = n / img_size
    b = m / img_size
    if a>b and a>1:
        n /= a
        m /= a
    elif b>a and b>1:
        n /= b
        m /= b
    imTK = ImageTk.PhotoImage( im.resize( (int(n),int(m)) ) )
    image_main = tk.Label(div1, image=imTK)
    image_main.configure(image=imTK) 
    image_main.image = imTK  
    image_main['height'] = img_size
    image_main['width'] = img_size
    image_main.grid(column=0, row=0, sticky=align_mode)

# BUTTON
bt1 = tk.Button(div3, text='# 舊時光 #', font= ('Helvetica 15 bold italic'), bg='#ffcc66', fg='white')
bt2 = tk.Button(div3, text='# 睡醒的午後 #', font= ('Helvetica 15 bold italic'), bg='#25dae9', fg='white')
bt3 = tk.Button(div3, text='# 褪去的愛 #', font= ('Helvetica 15 bold italic'), bg='#f86263', fg='white')
bt4 = tk.Button(div3, text='# 馬鹿 #', font= ('Helvetica 15 bold italic'), bg='#ffa157', fg='white')
bt5 = tk.Button(div3, text='# 鍊鋸人 #', font= ('Helvetica 15 bold italic'), bg='#f5b2af', fg='white')
bt6 = tk.Button(div3, text='# 一般 #', font= ('Helvetica 15 bold italic'), bg='#f56254', fg='white')

bt1.grid(column=0, row=0, sticky=align_mode)
bt2.grid(column=0, row=1, sticky=align_mode)
bt3.grid(column=0, row=2, sticky=align_mode)
bt4.grid(column=0, row=3, sticky=align_mode)
bt5.grid(column=0, row=4, sticky=align_mode)
bt6.grid(column=0, row=5, sticky=align_mode)

bt1['command'] = bt1_event
bt2['command'] = bt2_event
bt3['command'] = bt3_event
bt4['command'] = bt4_event
bt5['command'] = bt5_event
bt6['command'] = bt6_event

#origin img
im = Image.open(file_name)
open_img(im)

define_layout(window, cols=2, rows=2)
define_layout(div1)
define_layout(div2, rows=3)
define_layout(div3, rows=6)

window.mainloop()