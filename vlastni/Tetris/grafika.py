# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 20:55:43 2021

@author: jzahorec
"""

import tkinter as tk
import tetris as trs

# hraci_pole = [[1, 0, 0, 0, 0], [0, 0, 0, 1, 1], [
#     0, 1, 0, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [1, 1, 1, 1, 1]]

hra = trs.Hra([10, 10])

game = tk.Tk()
game.title("TETRIS")

length = 80

zobrazovaci_pole = tk.Canvas(
    game, width=length*len(hra.hraci_pole[0]), height=length*len(hra.hraci_pole))

zobrazovaci_pole.pack()

body_pole = [[None for j in range(len(hra.hraci_pole[0]))]
             for i in range(len(hra.hraci_pole))]

for i in range(len(body_pole)):
    for j in range(len(body_pole[0])):
        body_pole[i][j] = zobrazovaci_pole.create_rectangle(
            j*length, i*length, (j+1)*length, (i+1)*length, fill="white")


def obnov():
    vykreslitelne_pole = hra.vykresli()
    for i in range(len(vykreslitelne_pole)):
        for j in range(len(vykreslitelne_pole)):
            if vykreslitelne_pole[i][j]:
                zobrazovaci_pole.itemconfig(body_pole[i][j], fill="blue")
            else:
                zobrazovaci_pole.itemconfig(body_pole[i][j], fill="white")


def doleva(e):
    hra.posun([0, -1])
    obnov()


def doprava(e):
    hra.posun([0, 1])
    obnov()


def otoc_levo(e):
    hra.otoc(True)
    obnov()


def otoc_pravo(e):
    hra.otoc(False)
    obnov()


def tick():
    if not hra.tick():
        game.after(1000, tick)
    obnov()


game.bind("<Left>", doleva)
game.bind("<Right>", doprava)
game.bind("<Up>", otoc_levo)
game.bind("<Down>", otoc_pravo)

obnov()
game.after(1000, tick)
game.mainloop()
