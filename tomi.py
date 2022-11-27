import tkinter as tk
from tkinter import ttk
import tkinter
from tkinter.ttk import *
from tkinter.messagebox import showinfo
import os

root = tk.Tk()
root.title('Treeview demo')
root.geometry('850x300')

# define columns
columns = ('KOD_tovaru', 'NAZOV_tovaru', 'OBRAZOK_tovaru')

tree = ttk.Treeview(root, columns=columns, show='headings')

# define headings
tree.heading('KOD_tovaru', text='kod tovaru')
tree.heading('NAZOV_tovaru', text='nazov tovaru')
tree.heading('OBRAZOK_tovaru', text='nazov obrazku')

db_tovar_url = 'databaza/TOVAR.txt'
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
    subor.write('\n' + kod +';'+ nazov +';'+ obrazok +';')
    subor.close()
    

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

tree.grid(padx=10,pady=10, sticky='nsew')
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=2, column=1, sticky='ns')
root.mainloop()
