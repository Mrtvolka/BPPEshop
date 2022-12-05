import tkinter as tk
from tkinter import ttk
import tkinter
from tkinter.ttk import *
from tkinter.messagebox import showinfo
import os
import re
import PIL
from PIL import ImageTk,Image
import customtkinter

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.title('INTERNA DATABAZA')
root.geometry('1280x720')

db_tovar_url = 'C:/Users/tomin/Documents/GitHub/BPPEshop/databaza/TOVAR.txt'

columns = ('KOD_tovaru', 'NAZOV_tovaru', 'OBRAZOK_tovaru')
tree = ttk.Treeview(root, columns=columns, show='headings',)

def viewProducts():

    # define headings
    tree.heading('KOD_tovaru', text='kod tovaru')
    tree.heading('NAZOV_tovaru', text='nazov tovaru')
    tree.heading('OBRAZOK_tovaru', text='nazov obrazku')

    subor = open(db_tovar_url,'r+')
    pocet_produktov = (subor.readline()).strip()
    riadok=(subor.readline()).strip()

    produkty = []
    print(pocet_produktov)
    while riadok !='':
        produkt=riadok.split(';')
        tree.insert('', tk.END, values=produkt)    
        riadok=(subor.readline()).strip()
    subor.close()

def add():

    kod = kod_entry.get()
    nazov = nazov_entry.get()
    obrazok = obrazok_entry.get()

    kontrolny_riadok=kod +';'+ nazov +';'+ obrazok
    print(kontrolny_riadok)

    subor = open(db_tovar_url,'r+')
    for line in subor:
        if kontrolny_riadok in line:
            showinfo(title='INFO', message='Tovar uz existuje')
            return 

    pattern = re.compile("^[a-zA-Z ]+$")
    pattern2 = re.compile("^[a-zA-Z._]+$")
    pattern3 = re.compile("^[0-9]+$")

    if pattern.match(nazov) and pattern2.match(obrazok) and pattern3.match(kod):  

        tree.insert('', 'end',values=([kod, nazov, obrazok]))  

        subor = open(db_tovar_url,'r+')
        pocet_produktov = int((subor.readline()).strip()) + 1
        print(pocet_produktov)
        # FIRST ROW
        subor.seek(0, os.SEEK_SET)
        subor.write(str(pocet_produktov))
        # END of the file
        subor.seek(0, os.SEEK_END)
        subor.write('\n' + kod +';'+ nazov +';'+ obrazok)
        subor.close()
        
        kod_entry.delete(0,'end')
        nazov_entry.delete(0,'end')
        obrazok_entry.delete(0,'end')

    else:
        showinfo(title='INFO', message='zle zadane hodnoty')
 
def delete():
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        oznaceny = item['values']
        print(oznaceny)
        zmaz=';'.join(map(str,oznaceny))
        print(zmaz)
        
    with open(db_tovar_url, "r") as input:
        with open("temp.txt", "w") as output:
            for line in input:
                if line.strip("\n") != zmaz:
                    output.write(line)

    os.replace('temp.txt', db_tovar_url)

    selected_item = tree.selection()[0]
    tree.delete(selected_item)

    subor = open(db_tovar_url,'r+')
    pocet_produktov = int((subor.readline()).strip()) - 1
    print(pocet_produktov)
    # FIRST ROW
    subor.seek(0, os.SEEK_SET)
    subor.write(str(pocet_produktov))
    subor.close()

def fillEntries(event):
    kod_entry.delete(0,'end')
    nazov_entry.delete(0,'end')
    obrazok_entry.delete(0,'end')

    for selected_item3 in tree.selection():
        item1 = tree.item(selected_item3)
        #print(item1)
        oznaceny1 = item1['values']
        #print(oznaceny)
        riadok=';'.join(map(str,oznaceny1))
        #print(riadok)

        poz=riadok.find(';')
        nazov_kodu=riadok[:poz]
        #print(nazov_kodu)
        
        poz1=riadok.find(';')
        nazov_obrazku_cesta=riadok[poz1+1:]
        #print(nazov_obrazku_cesta)
        poz2=nazov_obrazku_cesta.find(';')
        nazov_obrazku=nazov_obrazku_cesta[poz2+1:]
        #print(nazov_obrazku)

        nazov_tovaru_cesta=riadok[poz+1:]
        #print(nazov_tovaru_cesta)
        poz3=nazov_tovaru_cesta.find(';')
        nazov_tovaru=nazov_tovaru_cesta[:poz3]
        #print(nazov_tovaru)

        kod_entry.insert(0,nazov_kodu)
        nazov_entry.insert(0,nazov_tovaru)
        obrazok_entry.insert(0,nazov_obrazku)

def edit():
    
    kod = kod_entry.get()
    nazov = nazov_entry.get()
    obrazok = obrazok_entry.get()

    kontrolny_riadok=kod +';'+ nazov +';'+ obrazok
    print(kontrolny_riadok)

    subor = open(db_tovar_url,'r+')
    for line in subor:
        if kontrolny_riadok in line:
            showinfo(title='INFO', message='Tovar uz existuje')
            return 

    pattern = re.compile("^[a-zA-Z ]+$")
    pattern2 = re.compile("^[a-zA-Z._]+$")
    pattern3 = re.compile("^[0-9]+$")

    if pattern.match(nazov) and pattern2.match(obrazok) and pattern3.match(kod):

        for selected_item1 in tree.selection():
            item = tree.item(selected_item1)
            oznaceny = item['values']
            print(oznaceny)
            riadok=';'.join(map(str,oznaceny))
            print(riadok)

        subor = open(db_tovar_url,'r+')
        for line in subor:
            if riadok in line:
                new_line = line.replace(line, kod+';'+nazov+';'+obrazok)
                print(new_line)
        subor.close()

        with open(db_tovar_url, "r") as input:
            with open("temp1.txt", "w") as output:
                for line in input:
                    if line.strip("\n") != riadok:
                        output.write(line)
                    if line.strip("\n") == riadok:
                        output.write(new_line+'\n')
                    
        os.replace('temp1.txt', db_tovar_url)

        selected_item = tree.selection()[0]
        tree.item(selected_item,values=([kod, nazov, obrazok]))

    else:
        showinfo(title='INFO', message='zle zadane hodnoty')

def search():
    search = search_entry.get()
    print(search)
        
    idx = []
    for id in tree.get_children():
        item = tree.item(id)['values']
        nazov = item[1]
        if search in nazov:
            idx.append(id)

    tree.selection_set(idx)

def showImage():
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        oznaceny = item['values']
        #print(oznaceny)
        zmaz=';'.join(map(str,oznaceny))

    poz=zmaz.find(';')
    nazov_obrazku_cesta=zmaz[poz+1:]
    #print(nazov_obrazku_cesta)
    poz2=nazov_obrazku_cesta.find(';')
    nazov_obrazku=nazov_obrazku_cesta[poz2+1:]
    print(nazov_obrazku)

    img=Image.open('C:/Users/tomin/Documents/GitHub/BPPEshop/images/'+nazov_obrazku)
    img.show()

    #my_image = ImageTk.PhotoImage(light_image=img,size=(30, 30))
                                  
    #img = tkinter.PhotoImage(file ='C:/Users/tomin/Documents/GitHub/BPPEshop/images/'+nazov_obrazku)
    
    #obrazok = customtkinter.CTkButton(frame1,image=img,command=None)  
                            
    #my_image.grid(row=1, column=0, pady=0, padx=50,sticky="e")

tree.bind('<<TreeviewSelect>>',fillEntries)
viewProducts()

#____________________________DESIGN_____________________________________________
cestaObrazky = r"C:/Users/tomin/Documents/GitHub/BPPEshop/images2/"
WIDTH=1280
HEIGHT=720
TEXT_FONT = ("Helvetica", "15")

#____________________________FRAME0______________________________________________
frame = customtkinter.CTkFrame(master=root,
                               width=WIDTH/5,
                               height=HEIGHT,
                               corner_radius=10)
frame.grid(padx=20,pady=20,ipady=110,rowspan=10)

frame.grid_rowconfigure(1, minsize=25)   # empty row with minsize as spacing
frame.grid_rowconfigure(3, weight=1)  # empty row as spacing
frame.grid_rowconfigure(8, weight=9)  # empty row as spacing
frame.grid_rowconfigure(11, minsize=25)

label_frame = customtkinter.CTkLabel(master=frame,
                                                        text="Funkcie s tovarom v databaze",
                                                        text_font=TEXT_FONT,
                                                        corner_radius=6,
                                                        fg_color=("white", "gray38"),
                                                        justify=tk.CENTER)
label_frame.grid(row=1,pady=50)

kod_entry = customtkinter.CTkEntry(master=frame)
kod_entry.insert(0, 'kod')
kod_entry.grid(row=2,padx=90,pady=10)

nazov_entry = customtkinter.CTkEntry(master=frame)
nazov_entry.insert(0, 'nazov')
nazov_entry.grid()

obrazok_entry = customtkinter.CTkEntry(master=frame)
obrazok_entry.insert(0, 'obrazok')
obrazok_entry.grid(pady=10)

add_button = customtkinter.CTkButton(master=frame,text="PRIDAT TOVAR",command=add) 
add_button.grid()

delete_button = customtkinter.CTkButton(master=frame,text="VYMAZAT TOVAR",command=delete) 
delete_button.grid()

edit_button = customtkinter.CTkButton(master=frame,text="UPRAVIT TOVAR",command=edit) 
edit_button.grid() 

def change_appearance_mode(new_appearance_mode):
    customtkinter.set_appearance_mode(new_appearance_mode)

root.optionsmode = customtkinter.CTkOptionMenu(master=frame,values=["Light", "Dark", "System"],command=change_appearance_mode)
root.optionsmode.grid(row=10, column=0, pady=10, padx=20, sticky="sw")

#FRAME1____________________________________________________________________________
frame1 = customtkinter.CTkFrame(master=root,
                               width=WIDTH/5,
                               height=HEIGHT,
                               corner_radius=10)
frame1.grid(row=0, column=3, sticky="nsew",padx = 20,pady= 20,rowspan=10)

frame1.grid_rowconfigure(1, minsize=25)   # empty row with minsize as spacing
frame1.grid_rowconfigure(3, weight=1)  # empty row as spacing
frame1.grid_rowconfigure(8, weight=9)  # empty row as spacing
frame1.grid_rowconfigure(11, minsize=25)


label_frame1 = customtkinter.CTkLabel(master=frame1,
                                                        text='↓obrazok oznaceneho tovaru↓',
                                                        text_font=TEXT_FONT,
                                                        corner_radius=6,
                                                        fg_color=("white", "gray38"),
                                                        justify=tk.CENTER)
label_frame1.grid(pady=50)

image_button =customtkinter.CTkButton(frame1,fg_color= 'orange', text="ZOBRAZ OBRAZOK",command=showImage) 
image_button.grid(row=10, column=0, pady=10, padx=90, sticky="s")



#__________________DAVID_BUTTONS____________________________________________________________________________

home_image = tk.PhotoImage(file = cestaObrazky + "home_logo.png")
settings_image = tk.PhotoImage(file = cestaObrazky + "settings_logo.png")

settings = customtkinter.CTkButton(master=frame,image=settings_image,text="", height=50,width=90,	
                                command=None)  
settings.grid(row=0, column=0, pady=0, padx=50,sticky="e")

menu = customtkinter.CTkButton(master=frame,image=home_image,text="", height=50,width=90,	
                                command=None)  
menu.grid(row=0, column=0, pady=20, padx=50,sticky="w")

#________________________TREE_STYLE_________________________________________________________________________
style=ttk.Style()
style.theme_use('clam')
style.configure('Treeview',background='silver',foreground='black',rowheight=50,fieldbackground='silver')
style.map('Treeview')
#__________________MIDDLE_PLACE____________________________________________________________________________
search_entry = customtkinter.CTkEntry()
search_entry.insert(0, 'vyhladat podla nazvu')
search_entry.grid(column=1,row=0,ipadx=150,ipady=0,padx=30,pady=20)

seacrh_button = customtkinter.CTkButton(text="VYHLADAT TOVAR",command=search) 
seacrh_button.grid(column=1,row=9,sticky='e')

#search()
#root.bind('<Enter>', search)
tree.grid(row=1, column=1,padx=50,pady=0,columnspan=2,rowspan=8,sticky='nsw')#
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=1,padx=50,pady=0,rowspan=8, column=2, sticky='nse')

root.optionsmode.set("Dark")

root.mainloop()