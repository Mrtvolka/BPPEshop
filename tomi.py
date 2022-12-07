import tkinter as tk
from tkinter import ttk
import tkinter
from tkinter.ttk import *
from tkinter.messagebox import showinfo,askyesno
import os
import re
import PIL
from PIL import ImageTk,Image
import customtkinter
from custom_hovertip import CustomTooltipLabel

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.title('INTERNA DATABAZA')
root.geometry('1280x720')

rootPath = 'C:/Users/tomin/Documents/GitHub/BPPEshop/'
#rootPath = 'C:/Users/Ivan/Documents/Sites/BPPEshop/'

db_tovar_url = rootPath + 'databaza/TOVAR.txt'
db_sklad_url = rootPath + 'databaza/SKLAD.txt'
db_cennik_url = rootPath + 'databaza/CENNIK.txt'

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
    #kontola duplicitneho tovaru
    kontrolny_riadok=kod +';'+ nazov +';'+ obrazok
    print(kontrolny_riadok)

    subor = open(db_tovar_url,'r+')
    for line in subor:
        if kontrolny_riadok in line:
            showinfo(title='INFO', message='Tovar uz existuje')
            return
    subor.close()
    #kontola duplicitneho kodu
    kontrolny_riadok2=kod
    print(kontrolny_riadok2)

    subor = open(db_tovar_url,'r+')
    for line in subor:
        print(line)
        if kontrolny_riadok2 in line:
            showinfo(title='INFO', message='kod uz existuje')
            return 
    subor.close()

    pattern = re.compile("^[a-zA-Z ]+$")
    pattern2 = re.compile("^[a-zA-Z._]+$")
    pattern3 = re.compile("^[0-9]+$")

    if pattern.match(nazov) and pattern2.match(obrazok) and pattern3.match(kod):  
        #zapisovanie do tabulky a suboru TOVAR.txt
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
    #potvrdzovacia tabulka
    answer = askyesno(title='POTVRDENIE',
                    message='Naozaj chcete vymazať tovar?')
    if answer:
        #deletovanie v TOVAR.txt
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
        pocet_produktov = int((subor.readline()).strip())
        print(pocet_produktov)
        subor.close()
        
        subor = open(db_tovar_url,'r+')
        pocet_produktov1 = int((subor.readline()).strip()) - 1
        print(pocet_produktov1)
        subor.close()

        with open(db_tovar_url, "r") as input:
            with open("temp2.txt", "w") as output:
                for line in input:
                    if line.strip("\n") != str(pocet_produktov) :
                        output.write(line)
                    if line.strip("\n") == str(pocet_produktov) :
                        output.write(str(pocet_produktov1)+'\n')

        os.replace('temp2.txt', db_tovar_url)

        #deletovanie v SKLAD.txt
        poz=zmaz.find(';')
        kodik=zmaz[:poz]
        print(kodik)

        with open(db_sklad_url, "r") as input:
            with open("temp.txt", "w") as output:
                for line in input:
                    if kodik not in line:
                        output.write(line)

        os.replace('temp.txt', db_sklad_url)

        subor = open(db_sklad_url,'r+')
        pocet_produktov = int((subor.readline()).strip())
        print(pocet_produktov)
        subor.close()
        
        subor = open(db_sklad_url,'r+')
        pocet_produktov1 = int((subor.readline()).strip()) - 1
        print(pocet_produktov1)
        subor.close()

        with open(db_sklad_url, "r") as input:
            with open("temp2.txt", "w") as output:
                for line in input:
                    if line.strip("\n") != str(pocet_produktov) :
                        output.write(line)
                    if line.strip("\n") == str(pocet_produktov) :
                        output.write(str(pocet_produktov1)+'\n')

        os.replace('temp2.txt', db_sklad_url)

        #deletovanie v CENNIK.txt
        poz=zmaz.find(';')
        kodik=zmaz[:poz]
        print(kodik)

        with open(db_cennik_url, "r") as input:
            with open("temp.txt", "w") as output:
                for line in input:
                    if kodik not in line:
                        output.write(line)

        os.replace('temp.txt', db_cennik_url)

        subor = open(db_cennik_url,'r+')
        pocet_produktov = int((subor.readline()).strip())
        print(pocet_produktov)
        subor.close()
        
        subor = open(db_cennik_url,'r+')
        pocet_produktov1 = int((subor.readline()).strip()) - 1
        print(pocet_produktov1)
        subor.close()

        with open(db_cennik_url, "r") as input:
            with open("temp2.txt", "w") as output:
                for line in input:
                    if line.strip("\n") != str(pocet_produktov) :
                        output.write(line)
                    if line.strip("\n") == str(pocet_produktov) :
                        output.write(str(pocet_produktov1)+'\n')

        os.replace('temp2.txt', db_cennik_url)

def fillEntries(event):
    kod_entry.delete(0,'end')
    nazov_entry.delete(0,'end')
    obrazok_entry.delete(0,'end')

    for selected_item3 in tree.selection():
        dlzka=tree.selection().__len__()
        #print(dlzka)
        if dlzka>1:
            return
        item1 = tree.item(selected_item3)
        oznaceny1 = item1['values']
        #print(oznaceny1)
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

        img=Image.open(rootPath + 'images/' + nazov_obrazku)
        produkt_img = customtkinter.CTkImage(light_image=img,dark_image=img,size=(280, 400))

        place_for_Image = customtkinter.CTkButton(master=frame1,image=produkt_img, text="",fg_color ="transparent",hover_color=('grey85','grey17'), height=200,width=200, corner_radius=0, border_spacing=0)
        place_for_Image.grid(row=7, column=0, pady=0, padx=0)

def edit():
    
    kod = kod_entry.get()
    nazov = nazov_entry.get()
    obrazok = obrazok_entry.get()
    #kontrola duplicitneho tovaru
    kontrolny_riadok=kod +';'+ nazov +';'+ obrazok

    subor = open(db_tovar_url,'r+')
    for line in subor:
        if kontrolny_riadok in line:
            showinfo(title='INFO', message='Tovar uz existuje')
            return 
    subor.close()
    #kontrola duplicitneho kodu
    kontrolny_riadok2=kod
    print(kontrolny_riadok2)

    subor = open(db_tovar_url,'r+')
    for line in subor:
        if kontrolny_riadok2 in line:
            showinfo(title='INFO', message='kod uz existuje')
            return 
    subor.close()
    #osetrenie vstupnych poli
    pattern = re.compile("^[a-zA-Z ]+$")
    pattern2 = re.compile("^[a-zA-Z._]+$")
    pattern3 = re.compile("^[0-9]+$")

    if pattern.match(nazov) and pattern2.match(obrazok) and pattern3.match(kod):
        #upravovanie v TOVAR.txt
        for selected_item1 in tree.selection():
            item = tree.item(selected_item1)
            oznaceny = item['values']
            #print(oznaceny)
            riadok=';'.join(map(str,oznaceny))
            #print(riadok)

        subor = open(db_tovar_url,'r+')
        for line in subor:
            if riadok in line:
                new_line = line.replace(line, kod+';'+nazov+';'+obrazok)
                print(new_line)
        subor.close()

        with open(db_tovar_url, "r") as input:
            with open("temp1.txt", "w") as output:
                for line in input:
                    if riadok not in line:
                        output.write(line)
                    if riadok in line:
                        output.write(new_line)
                    
        os.replace('temp1.txt', db_tovar_url)

        selected_item = tree.selection()[0]
        tree.item(selected_item,values=([kod, nazov, obrazok]))

        #upravovanie v SKLAD.txt
        poz=riadok.find(';')
        kodik=riadok[:poz]
        print(kodik)
        
        subor = open(db_sklad_url,'r+')
        for line in subor:
            if kodik in line:
                new_line = line.replace(kodik, kod)
                print(new_line)
        subor.close()

        with open(db_sklad_url, "r") as input:
            with open("temp1.txt", "w") as output:
                for line in input:
                    if kodik not in line:
                        output.write(line)
                    if kodik in line:
                        output.write(new_line)

        os.replace('temp1.txt', db_sklad_url)
        #upravovanie v CENNIK.txt
        poz=riadok.find(';')
        kodik=riadok[:poz]
        print(kodik)
        
        subor = open(db_cennik_url,'r+')
        for line in subor:
            if kodik in line:
                new_line = line.replace(kodik, kod)
                print(new_line)
        subor.close()

        with open(db_cennik_url, "r") as input:
            with open("temp1.txt", "w") as output:
                for line in input:
                    if kodik not in line:
                        output.write(line)
                    if kodik in line:
                        output.write(new_line)

        os.replace('temp1.txt', db_cennik_url)

    else:
        showinfo(title='INFO', message='zle zadane hodnoty')

def search(e):
    search = search_entry.get()
    print(search)
                
    idx = []
    for id in tree.get_children():
        item = tree.item(id)['values']
        nazov = item[1]
        if search in nazov:
            idx.append(id)

    tree.selection_set(idx)

def search2():
    search = search_entry.get()
    print(search)
                
    idx = []
    for id in tree.get_children():
        item = tree.item(id)['values']
        nazov = item[1]
        if search in nazov:
            idx.append(id)

    tree.selection_set(idx)

tree.bind('<<TreeviewSelect>>',fillEntries)
viewProducts()

#____________________________DESIGN_____________________________________________
cestaObrazky = rootPath + "images2/"
WIDTH=1280
HEIGHT=720

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

label_frame = customtkinter.CTkLabel(master=frame,width=260,height=40,text="Funkcie s tovarom v databaze",corner_radius=6,fg_color=("white", "gray38"),justify=tk.CENTER)
label_frame.grid(row=1,pady=50)

kod_entry = customtkinter.CTkEntry(master=frame,placeholder_text= "kod")
kod_entry.grid(row=2,padx=90,pady=10)

nazov_entry = customtkinter.CTkEntry(master=frame,placeholder_text= "nazov")
nazov_entry.grid()

obrazok_entry = customtkinter.CTkEntry(master=frame,placeholder_text= "obrazok")
obrazok_entry.grid(pady=10)

add_button = customtkinter.CTkButton(master=frame,text="PRIDAT TOVAR",command=add) 
add_button.grid()
#CustomTooltipLabel(anchor_widget=add_button,text="Add more items!")

edit_button = customtkinter.CTkButton(master=frame,text="UPRAVIT TOVAR",command=edit) 
edit_button.grid() 

delete_button = customtkinter.CTkButton(master=frame,text="VYMAZAT TOVAR",command=delete,fg_color='firebrick1',hover_color='firebrick3') 
delete_button.grid()

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


label_frame1 = customtkinter.CTkLabel(master=frame1,width=180,height=40,text='↓obrazok oznaceneho tovaru↓',corner_radius=6,fg_color=("white", "gray38"),justify=tk.CENTER)
label_frame1.grid(pady=50,padx=65)


#__________________DAVID_BUTTONS____________________________________________________________________________

home_image = customtkinter.CTkImage(light_image=Image.open(cestaObrazky + "home_logo.png"),
                                  dark_image=Image.open(cestaObrazky + "home_logo.png"),
                                  size=(30, 30))

settings_image = customtkinter.CTkImage(light_image=Image.open(cestaObrazky + "settings_logo.png"),
dark_image=Image.open(cestaObrazky + "settings_logo.png"),
size=(30, 30))

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
search_entry = customtkinter.CTkEntry(root,placeholder_text= "Vyhladaj podla nazvu")
search_entry.grid(column=1,row=0,ipadx=150,ipady=0,padx=30,pady=20)

search_image = customtkinter.CTkImage(light_image=Image.open(cestaObrazky + "lupa.png"),
                                  dark_image=Image.open(cestaObrazky + "lupa.png"),
                                  size=(30, 30))

seacrh_button = customtkinter.CTkButton(root,image=search_image, text="",fg_color ="transparent",hover_color=('grey92','grey14'), width=0,height=0,command=search2) 
seacrh_button.grid(column=1,row=0,sticky='e')

root.bind('<Return>', search)

tree.grid(row=1, column=1,padx=50,pady=0,columnspan=2,rowspan=8,sticky='nsw')#
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=1,padx=50,pady=0,rowspan=8, column=2, sticky='nse')

root.optionsmode.set("Dark")

root.mainloop()