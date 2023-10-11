from tkinter import *
import math
import numpy
from scipy import stats
win=Tk()
win.title('科学计算器')
win.geometry('800x480')
ans=0.0
flag=0
falg=0
def er_yuan():
    num=str(en.get())
    for i in range(0,len(num)):
        if (str.isdigit(num[i]) or num[i] == '.') == 0:
            number=eval(num[0:i])
            print(number)
            en.delete(0,END)
            if num[i]=='^':
                en.insert(0,str(number**(eval(num[i+1:]))))
            else:
                en.insert(0,str(number*(10**eval(num[i+3:]))))
            return
def numinput(number):
    global flag
    if (flag):
        en.delete(0,END)
        flag=0
    first_num=en.get()
    en.delete(0,END)
    en.insert(0,str(first_num)+str(number))
def end1():
    global ans
    global flag
    global falg
    if falg:
        er_yuan()
        falg=0
        return
    num=eval(str(en.get()))
    en.delete(0,END)
    en.insert(0,str(num))
    ans=num
    flag=1

def add_char(x):
    global falg
    num = en.get()
    en.delete(0,END)
    global flag
    if(flag):
        en.insert(0,str(ans)+x)
        flag=0
    else:
        en.insert(0, str(num) +x)

def clear():
    en.delete(0,END)
def delete_n():
    en.delete(len(str(en.get()))-1,END)
def sqrt_():
    num = str(en.get())
    for i in range(len(num) - 1, 0, -1):
        if  (str.isdigit(num[i]) or num[i]=='.')==0:
            en.delete(0, END)
            en.insert(0, num[0:i+1] + str(math.sqrt(eval(num[i+1:]))))
            return
    en.delete(0, END)
    en.insert(0, str(math.sqrt(eval(num))))
def jiechen():
    num = str(en.get())
    en.delete(0, END)
    sum=1
    k=abs(eval(num))
    for i in range(2,k+1,1):
        sum*=i
    en.insert(0, str(sum))
def tentotwo():
    num = str(en.get())
    en.delete(0, END)
    en.insert(0, str(bin(eval(num))))
def sin_():
    num = str(en.get())
    for i in range(len(num) - 1, 0, -1):
        if (str.isdigit(num[i]) or num[i] == '.') == 0:
            en.delete(0, END)
            en.insert(0, num[0:i + 1] + str(math.sin(math.radians(eval(num[i + 1:])))))
            return
    en.delete(0, END)
    en.insert(0, str(math.sin(math.radians(eval(num[0:])))))
def cos_():
    num = str(en.get())
    for i in range(len(num) - 1, 0, -1):
        if (str.isdigit(num[i]) or num[i] == '.') == 0:
            en.delete(0, END)
            en.insert(0, num[0:i + 1] + str(math.cos(math.radians(eval(num[i + 1:])))))
            return
    en.delete(0, END)
    en.insert(0, str(math.cos(math.radians(eval(num[0:])))))

def ans_():
    global ans
    num=en.get()
    en.delete(0, END)
    en.insert(0, str(num)+str(ans))

def pingjun():
    num = ans
    en.delete(0, END)
    en.insert(0, str(numpy.mean(num)))

def zhongwei():
    num = ans
    en.delete(0, END)
    en.insert(0, str(numpy.median(num)))

def zhongshu():
    num = ans
    en.delete(0, END)
    en.insert(0, str(stats.mode(num)))

def fangcha():
    num = ans
    en.delete(0, END)
    en.insert(0, str(numpy.var(num)))

def ln_():
    num = str(en.get())
    for i in range(len(num) - 1, 0, -1):
        if (str.isdigit(num[i]) or num[i] == '.') == 0:
            en.delete(0, END)
            en.insert(0, num[0:i + 1] + str(math.log(eval(num[i + 1:]))))
            return
    en.delete(0, END)
    if eval(num[0:]) <= 0:
        en.insert(0, 'error')
        return
    en.insert(0, str(math.log(eval(num[0:]))))

but7=Button(win,text=7,width=3,font=('Arial',31),command=lambda :numinput(7))
but8=Button(win,text=8,width=3,font=('Arial',31),command=lambda :numinput(8))
but9=Button(win,text=9,width=3,font=('Arial',31),command=lambda :numinput(9))
but4=Button(win,text=4,width=3,font=('Arial',31),command=lambda :numinput(4))
but5=Button(win,text=5,width=3,font=('Arial',31),command=lambda :numinput(5))
but6=Button(win,text=6,width=3,font=('Arial',31),command=lambda :numinput(6))
but1=Button(win,text=1,width=3,font=('Arial',31),command=lambda :numinput(1))
but2=Button(win,text=2,width=3,font=('Arial',31),command=lambda :numinput(2))
but3=Button(win,text=3,width=3,font=('Arial',31),command=lambda :numinput(3))
but0=Button(win,text=0,width=3,font=('Arial',31),command=lambda :numinput(0))
b1=Button(win,text='.',width=3,font=('Arial',31),command=lambda:add_char('.'))
b2=Button(win,text='=',width=3,font=('Arial',31),command=end1)
b3=Button(win,text='+',width=3,font=('Arial',31),command=lambda:add_char('+'))
b4=Button(win,text='-',width=3,font=('Arial',31),command=lambda:add_char('-'))
b5=Button(win,text='*',width=3,font=('Arial',31),command=lambda:add_char('*'))
b6=Button(win,text='/',width=3,font=('Arial',31),command=lambda:add_char('/'))
b7=Button(win,text='CE',width=3,font=('Arial',31),command=clear)
b8=Button(win,text='del',width=3,font=('Arial',31),command=delete_n)
b9=Button(win,text='(',width=3,font=('Arial',31),command=lambda:add_char('('))
b10=Button(win,text=')',width=3,font=('Arial',31),command=lambda:add_char(')'))
b11=Button(win,text='n!',width=4,font=('Arial',31),command=jiechen)
b12=Button(win,text='mod',width=4,font=('Arial',31),command=lambda:add_char('%'))
b13=Button(win,text='sqrt()',width=4,font=('Arial',31),command=sqrt_)
b14=Button(win,text='Bin',width=4,font=('Arial',31),command=tentotwo)
b15=Button(win,text='sin',width=3,font=('Arial',31),command=sin_)
b16=Button(win,text='cos',width=3,font=('Arial',31),command=cos_)
b17=Button(win,text=',',width=3,font=('Arial',31),command=lambda:add_char(','))
b18=Button(win,text='平均值',width=5,font=('Arial',31),command=pingjun)
b19=Button(win,text='中位数',width=5,font=('Arial',31),command=zhongwei)
b20=Button(win,text='众数',width=5,font=('Arial',31),command=zhongshu)
b21=Button(win,text='方差',width=5,font=('Arial',31),command=fangcha)
b22=Button(win,text='ln',width=3,font=('Arial',31),command=ln_)
but7.place(x=10,y=100)
but8.place(x=100,y=100)
but9.place(x=190,y=100)
but4.place(x=10,y=190)
but5.place(x=100,y=190)
but6.place(x=190,y=190)
but1.place(x=10,y=280)
but2.place(x=100,y=280)
but3.place(x=190,y=280)
but0.place(x=10,y=370)
b1.place(x=100,y=370)
b2.place(x=190,y=370)
b3.place(x=280,y=100)
b4.place(x=280,y=190)
b5.place(x=280,y=280)
b6.place(x=280,y=370)
b7.place(x=370,y=100)
b8.place(x=370,y=190)
b9.place(x=370,y=280)
b10.place(x=370,y=370)
b11.place(x=460,y=100)
b12.place(x=460,y=190)
b13.place(x=460,y=280)
b14.place(x=460,y=370)
b15.place(x=570,y=100)
b16.place(x=570,y=190)
b22.place(x=570,y=280)
b17.place(x=570,y=370)
b18.place(x=660,y=100)
b19.place(x=660,y=190)
b20.place(x=660,y=280)
b21.place(x=660,y=370)
en=Entry(win,width=45,font=('Arial',40))
en.place(x=0,y=0)
mainloop()
