import tkinter as tk
from PIL import Image, ImageTk

from PIL import Image, ImageOps, ImageFont, ImageDraw 
import math
from PIL import ImageFilter

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

def add_text():
    title_font = ImageFont.truetype('../FONT/AA.ttf',100)
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

## file name
file_name="../image/42.jpg"
## add border
[a,b]=add_border1(file_name)
new_pic=add_border2()
## add text
add_text()
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

#########################################################3

window = tk.Tk()
window.title('Window')
align_mode = 'nswe'
pad = 5

# FUCNTION
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

def get_size(self, event, obj=''):

    trg_obj = self.window if obj == '' else obj
    self.w, self.h = trg_obj.winfo_width(), trg_obj.winfo_height()
    print(f'\r{(self.w, self.h)}', end='')

def toggle_fullScreen(self, event):
    is_windows = lambda : 1 if platform.system() == 'Windows' else 0

    self.isFullScreen = not self.isFullScreen
    self.window.attributes("-fullscreen" if is_windows() else "-zoomed", self.isFullScreen)
# 分割空間
div_size = 200
img_size = div_size * 2
div1 = tk.Frame(window,  width=img_size , height=img_size , bg='#ffcc66')
div2 = tk.Frame(window,  width=div_size , height=div_size-100 , bg='black')
div3 = tk.Frame(window,  width=div_size , height=div_size+100 , bg='#f5b2af')

window.update()
win_size = min( window.winfo_width(), window.winfo_height())
print(win_size)

div1.grid(column=0, row=0, padx=pad, pady=pad, rowspan=2, sticky=align_mode)
div2.grid(column=1, row=0, padx=pad, pady=pad, sticky=align_mode)
div3.grid(column=1, row=1, padx=pad, pady=pad, sticky=align_mode)

# 視窗縮放
define_layout(window, cols=2, rows=2)
define_layout([div1, div2, div3])

# 照片
im = Image.open('../image/42.jpg')
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
image_main['height'] = img_size
image_main['width'] = img_size

image_main.grid(column=0, row=0, sticky=align_mode)

# TITLE

lbl_title1 = tk.Label(div2, text='假文青濾鏡', bg='black', fg='white')
lbl_title2 = tk.Label(div2, text="CHOOSE\nMODE", bg='black', fg='white')

lbl_title1.grid(column=0, row=0, sticky=align_mode)
lbl_title2.grid(column=0, row=1, sticky=align_mode)

# BUTTON EVENT

def bt1_event():
    im = Image.open('../example_result/result2.jpg')
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

def bt2_event():
    im = Image.open('../example_result/result1.jpg')
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

def bt3_event():
    im = Image.open('../example_result/result3.jpg')
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

def bt4_event():
    im = Image.open('../example_result/result4.jpg')
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

def bt5_event():
    im = Image.open('../example_result/result5.jpg')
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

def bt6_event():
    im = Image.open('../example_result/result.jpg')
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
bt1 = tk.Button(div3, text='# 舊時光 #', bg='#ffcc66', fg='white')
bt2 = tk.Button(div3, text='# 睡醒的午後 #', bg='#25dae9', fg='white')
bt3 = tk.Button(div3, text='# 褪去的愛 #', bg='#f86263', fg='white')
bt4 = tk.Button(div3, text='# 馬鹿 #', bg='#ffa157', fg='white')
bt5 = tk.Button(div3, text='# 鍊鋸人 #', bg='#f5b2af', fg='white')
bt6 = tk.Button(div3, text='# 一般 #', bg='#f56254', fg='white')

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



define_layout(window, cols=2, rows=2)
define_layout(div1)
define_layout(div2, rows=2)
define_layout(div3, rows=4)
window.mainloop()