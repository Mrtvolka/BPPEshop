import tkinter as tk
from tkinter import ttk
import tkinter
from tkinter.ttk import *
from tkinter.messagebox import showinfo
canvas = tkinter.Canvas(width=820,height=200)
canvas.pack()


root = tk.Tk()
root.title('Treeview demo')
root.geometry('820x300')

# define columns
columns = ('first_name', 'last_name', 'email')

tree = ttk.Treeview(root, columns=columns, show='headings')

# define headings
tree.heading('first_name', text='First Name')
tree.heading('last_name', text='Last Name')
tree.heading('email', text='Email')

# generate sample data
contacts = []
for n in range(1, 20):
    contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))



def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))

def edit():
   # Get selected item to Edit
   selected_item = tree.selection()[0]
   tree.item(selected_item, values=(entry1.get()))


def delete():
   # Get selected item to Delete
   selected_item = tree.selection()[0]
   tree.delete(selected_item)

def add():
    tree.insert('', 'end', text="6",values=(entry1.get()))

entry1 = tkinter.Entry()
entry1.insert(0, 'NAZOV TOVARU')
entry1.pack()

edit_btn = tk.Button(text="Edit", command=edit)
edit_btn.pack()

del_btn = tk.Button( text="Delete", command=delete)
del_btn.pack()
##tree.bind('<<TreeviewSelect>>', item_selected)

menu_button = tk.Button(text="PRIDAT TOVAR",command=add) 
menu_button.place(x=700,anchor=tk.NW)

canvas.create_text(100,100,text='lol')


tree.grid(padx=10,pady=10, sticky='nsew')
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')
root.mainloop()
