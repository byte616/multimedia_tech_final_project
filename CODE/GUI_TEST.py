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
# 分割空間
div_size = 200
img_size = div_size * 2
div1 = tk.Frame(window,  width=img_size , height=img_size , bg='#ffcc66')
div2 = tk.Frame(window,  width=div_size , height=div_size , bg='')
div3 = tk.Frame(window,  width=div_size , height=div_size , bg='#f5b2af')

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
im = Image.open('42.jpg')
imTK = ImageTk.PhotoImage( im.resize( (img_size, img_size) ) )

image_main = tk.Label(div1, image=imTK)
image_main['height'] = img_size
image_main['width'] = img_size

image_main.grid(column=0, row=0, sticky=align_mode)

# TITLE

lbl_title1 = tk.Label(div2, text='假文青濾鏡', bg='black', fg='white')
lbl_title2 = tk.Label(div2, text="CHOSE\nMODE", bg='black', fg='white')

lbl_title1.grid(column=0, row=0, sticky=align_mode)
lbl_title2.grid(column=0, row=1, sticky=align_mode)

# BUTTON
bt1 = tk.Button(div3, text='# 舊時光 #', bg='#ffcc66', fg='white')
bt2 = tk.Button(div3, text='# 睡醒的午後 #', bg='#25dae9', fg='white')
bt3 = tk.Button(div3, text='# 褪去的愛 #', bg='#f86263', fg='white')
bt4 = tk.Button(div3, text='# 馬鹿 #', bg='#ffa157', fg='white')
bt5 = tk.Button(div3, text='# 鍊鋸人 #', bg='#f5b2af', fg='white')

bt1.grid(column=0, row=0, sticky=align_mode)
bt2.grid(column=0, row=1, sticky=align_mode)
bt3.grid(column=0, row=2, sticky=align_mode)
bt4.grid(column=0, row=3, sticky=align_mode)
bt5.grid(column=0, row=4, sticky=align_mode)
#bt1['command'] = lambda : get_size(window, image_main, im)



define_layout(window, cols=2, rows=2)
define_layout(div1)
define_layout(div2, rows=2)
define_layout(div3, rows=4)
window.mainloop()