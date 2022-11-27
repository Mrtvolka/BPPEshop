import tkinter

subor=open('TOVAR.txt','r')

riadok=(subor.readline()).strip()


while riadok !='':
    #slovo=riadok.split()
    print(riadok)
    riadok=(subor.readline()).strip()
    

