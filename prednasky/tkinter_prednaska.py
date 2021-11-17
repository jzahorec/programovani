"""
Tkinter prednaska
"""

from tkinter import *

formular = Tk() # udelej novy formular
formular.geometry("800x600+50+10")
hlaseni = Label(formular, text="Nazdarek!") #velikost/umisteni
hlaseni.pack() #Prilep hlaseni na formular
b = Button(formular, text="Cudlik")
b.pack(fill=Y, side = LEFT)
formular.mainloop() # a jedeme!

 """
#Překreslení: formular.update()
implicitn9 parametry .pack(fill=, expand=, side=), fill X, Y, BOTH, expand = 0 nenatahuje, cokoliv jinak natahuje, side TOP LEFT BOTTOM RIGHT

 existuje .grid() misto .pack(), nekombinovat grid(row=0, column=0), pripadne rowspan, columnspan

pak existuje .place() - x, y, width, height, relx, rely, relheight, relwidth (relativni vzhledem k velikosti okna )

 spole4n0 metody - .config(), .cget()


zpracovani udalosti: mainloop, quit, , wail_variable(var), wait_visibility(window), wait_window(window), update, update_idletasks...
likvidaci okna provede destroy


funkce s udalostmi: bind(udalost, funkce), unbind(udalost), udalosti se predavaji jako string
<Button-1>, <B1-Motion>, <ButtonRelease-1>, <Double-Button-1>,

casovace: after(cas, funkce), after_idle(funkce), after_cancel(id)

sprava oken: lift, lower (posunou okno nahoru/dolu)
"""
