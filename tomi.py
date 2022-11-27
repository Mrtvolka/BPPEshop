import tkinter as tk
from tkinter import ttk
import tkinter
from tkinter.ttk import *
from tkinter.messagebox import showinfo

subor=open('databaza/TOVAR.txt','r')

root = tk.Tk()
root.title('Treeview demo')
root.geometry('820x300')

# define columns
columns = ('KOD_tovaru', 'NAZOV_tovaru', 'OBRAZOK_tovaru')

tree = ttk.Treeview(root, columns=columns, show='headings')

# define headings
tree.heading('KOD_tovaru', text='kod tovaru')
tree.heading('NAZOV_tovaru', text='nazov tovaru')
tree.heading('OBRAZOK_tovaru', text='nazov obrazku')

#generate sample data
# produkty = []
# for n in range(1, 20):
#     produkty.append((f'first {n}', f'last {n}', f'email{n}@example.com'))


pocet_produktov = (subor.readline()).strip()
riadok=(subor.readline()).strip()
produkty = []
print(pocet_produktov)

while riadok !='':
    produkt=riadok.split(';')
    tree.insert('', tk.END, values=produkt)    
    riadok=(subor.readline()).strip()



tree.grid(padx=10,pady=10, sticky='nsew')
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')
root.mainloop()
