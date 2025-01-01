from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox


GUI = Tk()#นี่คือหน้าจอหลักของโปรเเกรม
GUI.title('โปรเเกรมบันทึกข้อมููล')#นี่คือชื่อโปรเเกรม
GUI.geometry('500x400')#นี่คือขนาดโปรเเกรม

B1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท')
B1.pack(ipadx=20,ipady=20)
###############################

L1 = Label(GUI,text='โปรเเกรมบันทึกความรู้',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)

###############################
def Button2():
    text = 'ตอนนี่มีเงินในบัญชีอยู่ 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)

FB1 = Frame(GUI)#คล้ายกระดาน
FB1.place(x=100,y=300)
B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)
B2.pack(ipadx=20,ipady=20)
###############################

GUI.mainloop()
