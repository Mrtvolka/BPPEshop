import tkinter as tk
from tkinter import ttk
import tkinter
from tkinter.ttk import *
from tkinter.messagebox import showinfo
import os

root = tk.Tk()
root.title('Treeview demo')
root.geometry('850x300')

db_tovar_url = 'databaza/TOVAR.txt'
# define columns
columns = ('KOD_tovaru', 'NAZOV_tovaru', 'OBRAZOK_tovaru')
tree = ttk.Treeview(root, columns=columns, show='headings')

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

def edit():
    kod = kod_entry.get()
    nazov = nazov_entry.get()
    obrazok = obrazok_entry.get()

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



viewProducts()

kod_entry = tkinter.Entry()
kod_entry.insert(0, 'kod')
kod_entry.grid(row=1, column=2)

nazov_entry = tkinter.Entry()
nazov_entry.insert(0, 'nazov')
nazov_entry.grid(row=2, column=2)

obrazok_entry = tkinter.Entry()
obrazok_entry.insert(0, 'obrazok')
obrazok_entry.grid(row=3, column=2)

add_button = tk.Button(text="PRIDAT TOVAR",command=add) 
add_button.grid(row=4, column=2)

delete_button = tk.Button(text="VYMAZAT TOVAR",command=delete) 
delete_button.grid(row=5, column=2)

edit_button = tk.Button(text="UPRAVIT TOVAR",command=edit) 
edit_button.grid(row=6, column=2)

tree.grid(padx=10,pady=10, sticky='nsew')
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=2, column=1, sticky='ns')
root.mainloop()
