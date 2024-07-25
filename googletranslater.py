from tkinter import *
from tkinter import ttk #ttk for combo box
from googletrans import Translator,LANGUAGES
from deep_translator import GoogleTranslator

"""def change(text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1=trans.translate(text,src=src1,dest=dest1)
    return trans1.text
"""

def change(text="type", src="english", dest="hindi"):
    trans1 = GoogleTranslator(source=src, target=dest).translate(text)
    return trans1

def data():
    s=comb_sor.get()
    d=comb_dest.get()
    mesg=sor_txt.get(1.0,END)
    textget=change(text=mesg,src=s,dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)





root=Tk()
root.title("Google Translator😎")
root.geometry("500x800")
root.config(bg="aqua")
lab_txt=Label(root,text="Translator",font=("Time New Roman",40,"italic"))
lab_txt.place(x=100,y=40,height=50,width=300)

frame=Frame(root).pack(side=BOTTOM) #pack for placement

lab_txt=Label(root,text="Source Text",font=("Time New Roman",20,"italic"))
lab_txt.place(x=100,y=100,height=20,width=300)

sor_txt=Text(frame,font=("Time New Roman",20,"italic"),wrap=WORD)
sor_txt.place(x=10,y=130,height=150,width=480)

list_text=list(LANGUAGES.values())

comb_sor=ttk.Combobox(frame,value=list_text)
comb_sor.place(x=10,y=300,height=40,width=150)
comb_sor.set("english")

button_change=Button(frame,text="Translate",relief=RAISED,command=data)
button_change.place(x=170,y=300,height=40,width=150)

comb_dest=ttk.Combobox(frame,value=list_text)
comb_dest.place(x=330,y=300,height=40,width=150)
comb_dest.set("english")

lab_txt=Label(root,text="Destination Text",font=("Time New Roman",20,"italic"))
lab_txt.place(x=100,y=360,height=20,width=300)

dest_txt=Text(frame,font=("Time New Roman",20,"italic"),wrap=WORD)
dest_txt.place(x=10,y=400,height=150,width=480)

root.mainloop()
