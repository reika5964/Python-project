from tkinter import * 
from googletrans import Translator

def translate():
    message = text1.get('1.0','end-1c') #ดึงข้อความจากtext1
    translator =Translator()
    output= translator.translate(text=message,src='th',dest='en')
    text2.insert('end',output.text)
def reset():
    text1.delete(1.0,'end')  
    text2.delete(1.0,'end')    

#ออกแบบหน้าจอ
root = Tk()
root.title("Google Tranlater (TH-EN)")
root.geometry('530x300')
root.maxsize(530,300)
root.minsize(530,300)

#widget
label = Label(text="Thai - English",font=('Arial',25,'bold'))
label.place(x=150,y=20)

#เก็บข้อความภาษาอังกฤษ
text1 = Text(root,width=30,height=10)
text1.place(x=10,y=70)

#เก็บข้อความภาษาไทย
text2= Text(root,width=30,height=10)
text2.place(x=260,y=70)

#ปุ่ม
translateBtn = Button(root,text="Tranlate",command=translate)
translateBtn.place(x=180,y=250)

clearBtn = Button(root,text="Clear",command=reset)
clearBtn.place(x=280,y=250)



root.mainloop()
