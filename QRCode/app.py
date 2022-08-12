from tkinter import *

root = Tk()
root.title("QRCode Generetor")
canvas =Canvas(root,width=400,height=500)
canvas.pack()

#ชื่อโปรแกรม
app_label = Label(root,text="QRCode Generator",font=('Arial',20,'bold'))
canvas.create_window(200,50,window=app_label)
#ระบุชื่อพร้อมกับลิงค์ -> QRCode
name_label =Label(root,text="QRCode Name")
canvas.create_window(200,100,window=name_label)

link_label =Label(root,text="URL")
canvas.create_window(200,160,window=link_label)

#สร้างtextbox
name_entry =Entry(root)
canvas.create_window(200,130,window=name_entry)
link_entry =Entry(root)
canvas.create_window(200,180,window=link_entry)

#create Button
button = Button(text="Create QRCode")
canvas.create_window(200,230,window=button)

root.mainloop()