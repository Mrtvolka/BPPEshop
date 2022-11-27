import tkinter

subor=open('databaza/TOVAR.txt','r')

pocet_produktov = (subor.readline()).strip()
riadok=(subor.readline()).strip()

print(pocet_produktov)
while riadok !='':
    #slovo=riadok.split()
    print(riadok)
    riadok=(subor.readline()).strip()

    

