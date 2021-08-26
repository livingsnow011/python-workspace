from tkinter import *

root = Tk()
root.geometry("640x480")

# 라디오 버튼 = 여러 개 중 택 1 

label1= Label(root,text =" 메뉴를 선택하세요. ").pack()

burger_var = IntVar()
btn_burger1 = Radiobutton(root,text="햄버거",value=1,
variable=burger_var)
btn_burger1.select()

btn_burger2 = Radiobutton(root,text="치즈버거",value=2,
variable=burger_var)

btn_burger3 = Radiobutton(root,text="치킨버거",value=3,
variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

# 그룹핑 , variable로 
drink_var=StringVar()
btn_drink1 = Radiobutton(root,text="콜라",value="콜라",
variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root,text="사이다",value="사이다",
variable=drink_var)
btn_drink3 = Radiobutton(root,text="환타",value="환타",
variable=drink_var)
lable2 = Label(root,text="음료를 선택하세요.")
lable2.pack()

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()

def btncmd():
    print(burger_var.get())
    print(drink_var.get())
btn = Button(root,text="클릭",command=btncmd)
btn.pack()

root.mainloop()