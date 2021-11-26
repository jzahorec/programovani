#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.messagebox
import tetris

"""
Konstanty
"""
length = 80
tick_delay = 750
rozmery = [10, 10]

"""
Inicializace hry
"""
hra = tetris.Hra(rozmery)

grafika = tk.Tk()
grafika.title("TETRIS")

# grafika.geometry(str(length*len(hra.hraci_pole[0]))+"x"+str(length*len(hra.hraci_pole)))

# grafika.wm_attributes('-transparentcolor', grafika['bg']) #dela prusvitne pozadi

zobrazovaci_pole = tk.Canvas(
    grafika, width=length*len(hra.hraci_pole[0]), height=length*len(hra.hraci_pole))

zobrazovaci_pole.grid(row=0, column=0)

label_bodu = tk.Label(grafika, text="Skóre: " +
                      str(hra.skore), font="Arial 40")
label_bodu.grid(row=0, column=1)


body_pole = [[zobrazovaci_pole.create_rectangle(j*length, i*length, (j+1)*length, (i+1)*length, fill="white") for j in range(len(hra.hraci_pole[0]))]
             for i in range(len(hra.hraci_pole))]  # pole s odkazy na jednotlive ctverecky zobrazovaciho pole

barvy = ["blue", "black", "yellow", "orange", "green", "grey", "pink", "purple"]

def obnov():
    vykreslitelne_pole = hra.vykresli()
    for i in range(len(vykreslitelne_pole)):
        for j in range(len(vykreslitelne_pole)):
            if vykreslitelne_pole[i][j]:
                zobrazovaci_pole.itemconfig(body_pole[i][j], fill=barvy[vykreslitelne_pole[i][j]-1])
            else:
                zobrazovaci_pole.itemconfig(body_pole[i][j], fill="white")

    label_bodu.config(text="Skóre: " + str(hra.skore))


def obnov_zvyraznene():
    for i in range(len(hra.hraci_pole)):
        for j in range(len(hra.hraci_pole[0])):
            if hra.hraci_pole[i][j]:
                print(hra.hraci_pole[i][j])
                zobrazovaci_pole.itemconfig(body_pole[i][j], fill=barvy[hra.hraci_pole[i][j]-1])
            else:
                zobrazovaci_pole.itemconfig(body_pole[i][j], fill="white")

    for i in range(len(hra.dilek.rozmery)):
        for j in range(len(hra.dilek.rozmery[0])):
            if hra.dilek.rozmery[i][j]:
                zobrazovaci_pole.itemconfig(
                    body_pole[hra.dilek.i + i][hra.dilek.j + j], fill="red")

    label_bodu.config(text="Skóre: " + str(hra.skore))


def doleva(e):
    hra.posun([0, -1])
    # obnov()
    obnov_zvyraznene()


def doprava(e):
    hra.posun([0, 1])
    # obnov()
    obnov_zvyraznene()


def otoc_levo(e):
    hra.otoc(True)
    # obnov()
    obnov_zvyraznene()


def otoc_pravo(e):
    hra.otoc(False)
    # obnov()
    obnov_zvyraznene()


def nova_hra():
    hra.__init__(rozmery)
    # obnov()
    obnov_zvyraznene()
    grafika.after(tick_delay, tick)


def prohra():
    # proherni_okenko = tk.Label(
    #     zobrazovaci_pole, text="Prohrál jsi: " + str(hra.skore) + " bodů", font="Arial 60")
    # proherni_okenko.place(x=0, y=length*len(body_pole) //
    #                       2 - 50, width=length*len(body_pole[0]), height=100)

    if tkinter.messagebox.askquestion(
            title="Prohra", message="Prohrál jsi: " + str(hra.skore) + " bodů" + ", chceš další hru?") == "yes":
        nova_hra()
    else:
        grafika.destroy()


def tick():
    if not hra.tick():
        grafika.after(tick_delay, tick)
    else:
        prohra()
        return 0  # escape aby neprobehla obnova niceho pri konci aplikace
    # obnov()

    obnov_zvyraznene()


grafika.bind("<Left>", doleva)
grafika.bind("<Right>", doprava)
grafika.bind("<Up>", otoc_levo)
grafika.bind("<Down>", otoc_pravo)

# obnov()

obnov_zvyraznene()

grafika.after(tick_delay, tick)

grafika.mainloop()
