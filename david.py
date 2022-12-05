import tkinter as tk
import tkinter.messagebox
from PIL import Image, ImageTk
import customtkinter
import os

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

WIDTH = 1280
HEIGHT = 720    
BACKGROUND_BUTTON_CLR = "#43CD80"
BACKGROUND_BUTTON_ACTIVE_CLR = "#4EEE94"
TEXT_FONT = ("Helvetica", "15") 
PATH = os.path.dirname(os.path.realpath(__file__))

root = customtkinter.CTk()

cestaObrazky = r"C:/Users/tomin/Documents/GitHub/BPPEshop/images2/"
#cestaTxt = r"C:/Users/david/OneDrive/Desktop/Sklad_custom/txt/"




root.title("Module: Sklad")
root.geometry(f"{WIDTH}x{HEIGHT}")

canvas = customtkinter.CTkCanvas(root,width = WIDTH, height = HEIGHT)

# CREATING TWO FOR WORK FRAMES

root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

#=========================================================== LEFT =============================================================================#
root.frame_left = customtkinter.CTkFrame(master=root,width=WIDTH/5,corner_radius=10)
root.frame_left.grid(row=0, column=0, sticky="nswe", padx=20, pady=20)

root.frame_left.grid_rowconfigure(1, minsize=25)   # empty row with minsize as spacing
root.frame_left.grid_rowconfigure(3, weight=1)  # empty row as spacing
root.frame_left.grid_rowconfigure(8, weight=9)  # empty row as spacing
root.frame_left.grid_rowconfigure(11, minsize=25)




# ============> BUTTONS

#BUTTON BACK TO MENU + FUNCTION

def go_back_to_menu():
    print("Deleting sklad and going to the menu....")

def go_to_settings():
    print("Deleting sklad and going to the settings....")

home_image = tk.PhotoImage(file = cestaObrazky + "home_logo.png")
settings_image = tk.PhotoImage(file = cestaObrazky + "settings_logo.png")
purchase_image = tk.PhotoImage(file = cestaObrazky + "purchase_logo.png")

#rifle_image = tk.PhotoImage(file=r"C:/Users/david/OneDrive/Desktop/Sklad_custom/images/" + "rifle_logo.png")


menu = customtkinter.CTkButton(master=root.frame_left,image=home_image,text="", fg_color= BACKGROUND_BUTTON_CLR , hover_color= BACKGROUND_BUTTON_ACTIVE_CLR  , height=50,width=90,	
                                command=go_back_to_menu)  
menu.grid(row=2, column=0, pady=0, padx=15,sticky="w")

settings = customtkinter.CTkButton(master=root.frame_left,image=settings_image,text="", fg_color = BACKGROUND_BUTTON_CLR, hover_color= BACKGROUND_BUTTON_ACTIVE_CLR  , height=50,width=90,	
                                command=go_to_settings)  
settings.grid(row=2, column=0, pady=0, padx=15,sticky="e")

#RADIO BUTTONS
v = tk.IntVar()

root.manual = customtkinter.CTkRadioButton(master=root.frame_left,text="Manualne",variable=v,value=0)
root.manual.grid(row=4, column=0, pady=10, padx=20,  sticky = "nwes")

root.semimanual = customtkinter.CTkRadioButton(master=root.frame_left,text="Semimanualne",variable=v,value=1)
root.semimanual.grid(row=5, column=0, pady=15, padx=20, sticky = "nwes")

root.automatic = customtkinter.CTkRadioButton(master=root.frame_left,text="Automaticky",variable=v,value=2)
root.automatic.grid(row=6, column=0, pady=15, padx=20, sticky = "nwes")

#MISSING GOOD LABEL

#TITLE
root.missing_goods_title = customtkinter.CTkLabel(master=root.frame_left,
                                                        text="Chýbajúce predmety",
                                                        text_font=TEXT_FONT,
                                                        corner_radius=6,
                                                        fg_color=("white", "gray38"),
                                                        justify=tk.CENTER)
root.missing_goods_title.grid(column=0, row=7,sticky="n", padx = 20,pady = 20)

#MISSING
root.missing_item1 = customtkinter.CTkLabel(master=root.frame_left,text="ITEM: 1 | PIECES:1 ",corner_radius=6,fg_color=("white", "red"),justify=tk.LEFT)
root.missing_item1.grid(column=0, row=8,sticky="nw", padx = 20,pady = 10) # purchase_image

#item 1 
root.missing_item1_logo = customtkinter.CTkLabel(master=root.frame_left,image= purchase_image,corner_radius=6,fg_color=("white", None),justify=tk.LEFT,width=50)
root.missing_item1_logo.grid(column=0, row=8,sticky="ne", padx = 20,pady = 10) # purchase_image

root.missing_item2 = customtkinter.CTkLabel(master=root.frame_left,text="ITEM: 2 | PIECES:2 ",corner_radius=6,fg_color=("white", "red"),justify=tk.LEFT)
root.missing_item2.grid(column=0, row=8,sticky="nw", padx = 20,pady = 60) # purchase_image

#item2
root.missing_item2_logo = customtkinter.CTkLabel(master=root.frame_left,image= purchase_image,corner_radius=6,fg_color=("white", None),justify=tk.LEFT,width=50)
root.missing_item2_logo.grid(column=0, row=8,sticky="ne", padx = 20,pady = 60) # purchase_image

#item 3
root.missing_item3 = customtkinter.CTkLabel(master=root.frame_left,text="ITEM: 3 | PIECES: 3 ",corner_radius=6,fg_color=("white", "red"),justify=tk.LEFT)
root.missing_item3.grid(column=0, row=8,sticky="nw", padx = 20,pady = 110) # purchase_image 

root.missing_item3_logo = customtkinter.CTkLabel(master=root.frame_left,image= purchase_image,corner_radius=6,fg_color=("white", None),justify=tk.LEFT,width=50)
root.missing_item3_logo.grid(column=0, row=8,sticky="ne", padx = 20,pady = 110) # purchase_image

# OPTIONS MODE + FUNCTION
def change_appearance_mode(new_appearance_mode):
    customtkinter.set_appearance_mode(new_appearance_mode)


root.optionsmode = customtkinter.CTkOptionMenu(master=root.frame_left,values=["Light", "Dark", "System"],command=change_appearance_mode)
root.optionsmode.grid(row=10, column=0, pady=10, padx=20, sticky="sw")

# MISSING GOODS 





#============================================================= FRAME MIDDLE =============================================================================#
root.frame_middle = customtkinter.CTkFrame(master=root,width = WIDTH/5, corner_radius = 10 )
root.frame_middle.grid(row=0, column=1, sticky="wnes", padx=20, pady=20)


#root.frame_middle.grid_rowconfigure(1, weight=1)
root.frame_middle.grid_rowconfigure(5, weight=1)
#root.frame_middle.grid_rowconfigure(10, minsize=25)



picture_up,picture_down = "Non exist", "Non exist"

# SEARCHBAR + FUNCTION
def get_info_from_searchbar(e):
    global picture_up,picture_down

    info = e.widget.get()
    items_names,items_logo_names = give_items()
    check_item(info,items_names)
    create_picture(info)


def check_item(info,items_names):
    check_input = False

    for name in items_names:
        if name == info:
            check_input = True

    return check_input

def give_items():
    with open(cestaTxt + "TOVAR.txt", "r") as f:
        items_names = []
        items_logo_names = []
        for i,line in enumerate(f):
            if i == 0:  #pass first line  
                continue
            else:
                splited_line = line.split(";")
                items_names.append(splited_line[1])
                items_logo_names.append(splited_line[2].strip())
    return items_names,items_logo_names






def create_picture(info):
    global picture_up,picture_down

    if picture_up == "Non exist":
        root.item1 = customtkinter.CTkLabel(master=root.frame_middle,text=info,height=80,corner_radius=6,fg_color=("white", "gray38"),justify=tk.LEFT)
        root.item1.grid(column=1, row=2, rowspan=3, columnspan=2,sticky="nswe", padx = 20,pady = 20,ipadx = 65, ipady = 100) 

        root.pic1 = customtkinter.CTkLabel(master=root.frame_middle,text="OBRAZOK",height=80,corner_radius=6,fg_color=("RED",  "gray38"))
        root.pic1.grid(column=0, row=2, rowspan=3, columnspan=3,sticky="w", padx = 20,pady = 20,ipadx = 65, ipady = 120) 
        #button execute

        picture_up = "created"

    elif picture_down == "Non exist":
        root.item2 = customtkinter.CTkLabel(master=root.frame_middle,text=info,height=80,corner_radius=6,fg_color=("white", "gray38"),justify=tk.LEFT)
        root.item2.grid(column=1, row=4, rowspan=3, columnspan=3,sticky="wse", padx = 20,pady = 20,ipadx = 65, ipady = 120)

        root.pic2 = customtkinter.CTkLabel(master=root.frame_middle,text="OBRAZOK",height=80,corner_radius=6,fg_color=("white", "gray38"))
        root.pic2.grid(column=0, row=4, rowspan=3, columnspan=3,sticky="ws", padx = 20,pady = 20,ipadx = 65, ipady = 120) 

        #button execute



        picture_down = "created"

    else:
        print("Max count of images are created")

searchbar = customtkinter.CTkEntry(master=root.frame_middle,width=500,placeholder_text="Vyhľadaj")
searchbar.grid(row=0, column=0, columnspan=2, pady=20, padx=20, sticky="we")
searchbar.bind("<Return>", get_info_from_searchbar)





#============================================================= FRAME RIGHT =============================================================================#
root.frame_right = customtkinter.CTkFrame(master=root,corner_radius = 10 )
root.frame_right.grid(row=0, column=3, sticky="nwes", padx=20, pady=20)

root.missing_goods_title = customtkinter.CTkLabel(master=root.frame_right,
                                                        text="Tu vytvorte objednávku",
                                                        text_font=TEXT_FONT,
                                                        corner_radius=6,
                                                        fg_color=("white", "gray38"),
                                                        justify=tk.CENTER)


root.missing_goods_title.grid(column=0, row=0,sticky="wnes", padx = 10,pady = 20)



# DEFAULT OPTIONS

root.optionsmode.set("Dark")
root.automatic.select()




#keep it open
root.mainloop()   