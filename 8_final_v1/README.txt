文青句濾鏡專案 使用說明

A.安裝環境需求：

  1.執行環境： python3.8 or python3.9

  2.python 套件需求：
    a. torch (pytorch)
    b. torchvision
    c. tkinter
    d. PIL (pillow)

    ***ubuntu環境：
	   tkinter的安裝:
	           (sudo) apt-get install python3-tk

           PIL.image.imageTK 需要額外安裝套件:
	           (sudo) apt-get install python3-pil python3-pil.imagetk

B.如何執行程式:
    1."必須"將要加工的照片放入pic/pic/ 資料夾下面 
      (支援 .jpg, .jpeg, .png檔)
      (可以使用的類別有：飛機、貓、狗、西裝、車、咖啡、情侶、樹、船、月亮)


    2.執行DEMO_CODE資料夾裡面的main.py (python3 main.py)

