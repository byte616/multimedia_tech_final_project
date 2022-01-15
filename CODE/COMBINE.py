# ecoding: utf-8
import tkinter as tk
from tkinter.constants import W
from PIL import Image, ImageOps, ImageFont, ImageDraw, Image, ImageTk, ImageFilter
import math
import random

#########文青句##########
moon=[["月光所至","皆是思念"],["月亮在販售快樂","我與星輝一同為你沉淪"],["月亮是我拋的硬幣","兩面都是夢見你"],["思君如滿月","夜夜減清輝"],["我不會試圖摘月","我要月亮奔我而來"],["我在月影下望著遠方","那是有你的遠方"],["天上只有一個月亮","世間只有一個你"],["月亮是一個隱喻","所有的本體都是你"],["我只想在花好月圓下","陪你說一世情話"],["天上只有一個月亮","就像我心裡也只有一個你"],["我望著天空上的月亮","在手心寫著你的名字"],["若有人給你一盞燈","我給你月亮"],["在這個月圓之夜","深深地想你"],["月光是海的夢境","而你是我的遠行"],["你要一直做我的月亮","做那個照亮我的人"],["江畔何人初見月","江月何年初照人"],["踏月而來","這繁星便是贈禮"],["月光如水","思念如潮"],["我愛三樣東西","太陽，月亮，和你"],["你是藏在雲層里的月亮","也是我窮極一生尋找的寶藏"]]
success=[["世界上那些最容易的事情中","拖延時間最不費力"],["積極者相信只有推動自己","才能推動世界"],["忍別人所不能忍的痛","吃別人所不能吃的苦"],["有志者，事竟成"],["破釜沉舟","百二秦關終歸楚"],["苦心人，天不負"],["臥薪嘗膽","三千越甲可吞吳"],["即使爬到最高的山上","一次也隻能腳踏實地地邁一步"],["即使是不成熟的嘗試","也勝於胎死腹中的策略"],["世上沒有絕望的處境","只有對處境絕望的人"],["智者一切求自己","愚者一切求他人"],["回避現實的人","未來將更不理想"],["別想一下造出大海","必須先由小河川開始"],["苦想沒盼頭","苦幹有奔頭"],["自己打敗自己的","遠遠多於比別人打敗的"],["成功需要成本","時間也是一種成本","對時間珍惜就是對成本節約"],["以誠感人者","人亦誠而應"],["動是治愈恐懼的良藥","而猶豫拖延將不斷滋養恐懼"],["凡真心嘗試助人者","沒有不幫到自己的"],["每一個成功者都有一個開始","勇於開始，才能找到成功的路"]]
car=[["走自己的路","讓別人也有路可走"],["練好武功","你才能在江湖上活得更久","練好忍功","你才能在道路上開得更久"],["車跟貓一樣","多摸才能聽話"],["守住自己的道","看清自己的路","無論開車還是處世都用得著"],["車跟女人都是有脾氣的","獨立駕駛前一定要熟悉"],["感情就像跟車","稍不留意就有別的車插進來","再不用心就可能跟丟了"],["小人最好別交","大車最好別跟","小人開的大車那是絕對要躲遠點"],["別人的愛人和愛車都不要輕易去碰","出事的後果都很嚴重"],["愛人和愛車","選擇時都一定要慎重"],["不要花光你所有的錢去買車","買車只是花錢的開始"],["新車如同少女","還是少進美容店最好"],["如果你不願意醫生來修理你","那麼最好經常修理好你的車"],["哥收藏的不是車","是寂寞"],["如果你沒有翻過車","就說明你開的不夠快"],["無論你到哪裡","家都是你最終的目的地"],["女人開車是為了享受","男人開車是為了征服"],["不要開車吃東西","因為你很可能沒有消化它的機會了"],["從車型未必能看出車主身份","但從開車卻能看出車主素質"],["學好交通規則","生命也許就葬送在你忘記它的那一瞬間"],["風花雪月天談情是一種浪漫","風花雪月天行車可是一種危險"]]
ship=[["我的船上沒有手下，只有夥伴"],["人生是汪洋中一條船","你才是它的船長"],["野徑雲俱黑","江船火獨明"],["社會猶如一條船","每個人都要有掌舵的準備"],["雖然船在上面，水在下面","然而水仍然是主人翁"],["人生是海，金錢是船夫","如無船伕，度世維艱"],["願變成一塊石頭","守望著我們已經看不見的小船"],["每個人的生命都是一隻小船","理想是小船的風帆"],["晚風吹行舟","花路入溪口"],["船上管弦江面綠","滿城飛絮滾輕塵"],["乘風破浪會有時","直掛雲帆濟滄海"],["船動湖光灩灩秋","貪看年少信船流"],["窗含西嶺千秋雪","門泊東吳萬里船"],["破帽遮顏過鬧市","漏船載酒泛中流"],["欲渡黃河冰塞川","將登太行雪滿山"],["移舟泊煙渚","日暮客愁新"],["君看一葉舟","出沒風波里"],["看海天一色","聽風起雨落"],["颱風天就是要泛舟阿","不然要幹嘛"],["對於一艘盲目航行的船來說","所有的風都是逆風"]]
airplane=[["我不是在旅行",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""]]
couple=[["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""]]
coffee=[["真正的咖啡","是一種心情，一種品味"],["愛情就像是一杯美味香濃的咖啡","婚姻則是剩餘咖啡渣的咖啡杯"],["咖啡似人生","有苦有甜"],["有時候喜歡喝苦咖啡","因為它像生活","日子苦，回憶甜"],["咖啡又香又濃","可有一些人卻無法入口","愛情亦是如此！"],["咖啡的美是短暫的","時間一長就感覺不好了"],["咖啡有冷有熱","心情亦是","感情亦是"],["喝一杯苦咖啡","為了和生活相遇"],["咖啡飄散過的香味","剩下苦澀陪著我"],["如果咖啡廳裡有童話","一杯咖啡讓我遇見了她"],["咖啡就是咖啡","不管放了多少糖","還是有淡淡的苦味"],["放棄喝咖啡","這種痛苦就好比失去最珍貴的感情"],["生活就像咖啡","自信如同沸騰的熱水","兩者融合就能香濃四溢"],["咖啡的苦與甜","完全在於喝的人"],["愛情，是種誤解","比咖啡因危險一點"],["給我一杯能燙死人的咖啡","讓我的心隨著咖啡","慢慢地冷靜下來"],["咖啡苦與甜","不在於怎麼攪拌","而在於是否放糖"],["你會不會忽然的出現","在街角的咖啡店"],["今天，我的生活從一杯咖啡開始"]]
cat=[["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""]]
dog=[["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""]]
#########################
label=3

def get_text():
    x=random.randint(0,19)
    if label == 1:
        text=moon[x]
    if label == 2:
        text=success[x]
    if label == 3:
        text=car[x]
    if label == 4:
        text=ship[x]
    if label == 5:
        text=airplane[x]
    if label == 6:
        text=couple[x]
    if label == 7:
        text=coffee[x]
    if label == 8:
        text=cat[x]
    if label == 9:
        text=dog[x]
    return text

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

def add_text(new_pic,a,b):
    text=get_text()
    image_editable = ImageDraw.Draw(new_pic)
    [n,m]=new_pic.size
    alpha_size=100
    ma_size=0
    for string in text:
        ma_size=max(len(string),ma_size)
    if ma_size*100>=n:
        alpha_size=n/ma_size-10
    title_font = ImageFont.truetype('../FONT/AA.ttf',int(alpha_size))
    i=0
    y=b+50
    for string in text:
        x=(n-len(string)*alpha_size)/2
        image_editable.text((x,y+i*100), string, (0,0,0),title_font)
        i+=1

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

def Pimage(new_pic,file_name,a,b):
    ## add border
    [a,b]=add_border1(file_name)
    new_pic=add_border2()
    ## add text
    add_text(new_pic,a,b)
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

def main():
    ## file name
    file_name="../image/46.jpg"
    new_pic=Image.open(file_name)
    [a,b]=new_pic.size
    Pimage(new_pic,file_name,a,b)


    window = tk.Tk()
    window.title('GUI')
    align_mode = 'nswe'
    pad = 0

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

    # lbl_title1 = tk.Label(div2, text='文青句濾鏡', font= ('Helvetica 15 bold italic'), bg='black', fg='white')
    # lbl_title2 = tk.Label(div2, text="CHOOSE\nMODE", font= ('Helvetica 15 bold italic'), bg='black', fg='white')

    # lbl_title1.grid(column=0, row=0, sticky=align_mode)
    # lbl_title2.grid(column=0, row=2, sticky=align_mode)

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
    def bt01_event():
        open_img(new_pic)

    def bt00_event():
        image_main = tk.Label(div1, text="文青句濾鏡 製作名單\n\n408410016  葉一廷\n408410098  蔡嘉祥\n408410102  楊力行\n409410027  王鴻鈞\n409410041  陳柏仲", font= ('Helvetica 25 bold italic'), bg='black', fg='white')
        image_main.grid(column=0, row=0, sticky=align_mode)

    def bt0_event():
        Pimage(new_pic,file_name,a,b)
        pic = Image.open(file_name)
        open_img(pic)

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
    bt00 = tk.Button(div2, text='# 文青句濾鏡 #\n\n# 製作團隊 #', font= ('Helvetica 13 bold italic'), bg='black', fg='white')
    bt01 = tk.Button(div2, text='# 原圖 #', font= ('Helvetica 13 bold italic'), bg='black', fg='white')
    bt0 = tk.Button(div2, text='# 重新生成文青句 #', font= ('Helvetica 13 bold italic'), bg='black', fg='white')
    bt1 = tk.Button(div3, text='# 舊時光 #', font= ('Helvetica 15 bold italic'), bg='#ffcc66', fg='white')
    bt2 = tk.Button(div3, text='# 睡醒的午後 #', font= ('Helvetica 15 bold italic'), bg='#25dae9', fg='white')
    bt3 = tk.Button(div3, text='# 褪去的愛 #', font= ('Helvetica 15 bold italic'), bg='#f86263', fg='white')
    bt4 = tk.Button(div3, text='# 馬鹿 #', font= ('Helvetica 15 bold italic'), bg='#ffa157', fg='white')
    bt5 = tk.Button(div3, text='# 鍊鋸人 #', font= ('Helvetica 15 bold italic'), bg='#f5b2af', fg='white')
    bt6 = tk.Button(div3, text='# 一般 #', font= ('Helvetica 15 bold italic'), bg='#f56254', fg='white')

    bt00.grid(column=0, row=0, sticky=align_mode)
    bt01.grid(column=0, row=2, sticky=align_mode)
    bt0.grid(column=0, row=1, sticky=align_mode)
    bt1.grid(column=0, row=0, sticky=align_mode)
    bt2.grid(column=0, row=1, sticky=align_mode)
    bt3.grid(column=0, row=2, sticky=align_mode)
    bt4.grid(column=0, row=3, sticky=align_mode)
    bt5.grid(column=0, row=4, sticky=align_mode)
    bt6.grid(column=0, row=5, sticky=align_mode)

    bt00['command'] = bt00_event
    bt01['command'] = bt01_event
    bt0['command'] = bt0_event
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

if __name__ == '__main__':
    main()