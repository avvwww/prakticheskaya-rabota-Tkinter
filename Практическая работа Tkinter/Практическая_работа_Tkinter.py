from tkinter import *
im=['Леви Аккерман','Микаса Аккерман','Армин Арлерт','Конни Спрингер','Саша Браус','Хистория Рейсс','Эрвин Смит','Эрен Йегер','Ханджи Зоэ','']
win=Tk()

def list_to_txt(event):
    txt.delete(0.0,END)
    valik=lbox.curselection()
    txt.insert(END,lbox.get(valik[0]))

def txt_to_list(event):
    text=txt.get(0.0,END)
    text=text[-2:-1]
    if text=='\n':
        pass
    else:
        im.append(text)
        lbox.config(height=len(im))
        lbox.insert(END,text)
        txt.delete(0.0,END)

lbox=Listbox(win,width=20,height=len(im),selectmode=SINGLE)
for element in im:
    lbox.insert(END,element)
lbox.grid(row=0,column=0)
lbox.bind("<<ListboxSelect>>",list_to_txt)
txt=Text(win,height=1,width=15,wrap=WORD)
txt.grid(row=1,column=0)
txt.bind("<Return>",txt_to_list)


Button(text='Карнтинка:').grid(row=0,column=2)

gif=PhotoImage(file="Армин Арлерт.gif").subsample(2)




win.mainloop()
