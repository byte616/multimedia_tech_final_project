import tkinter as tk
from PIL import Image, ImageTk

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
lbl_title2 = tk.Label(div2, text="CHOSE\nMODE", bg='black', fg='white')

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