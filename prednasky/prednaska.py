# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 12:18:07 2021

@author: jzahorec
"""

# import sys


# =============================================================================
# class clovek:
#     def __init__(self):
#         self.__ockovany = False
#
#
# class dite:
#     def __init__(self):
#         self.hracky = ["Panda"]
#
#
# class student(clovek, dite):
#     @staticmethod
#     def f():
#         print("ano")
#
#     def __init__(self, jmeno, prijmeni, co_studuje, schopnosti):
#         super(clovek, self).__init__()
#         self.jmeno = jmeno
#         self.prijmeni = prijmeni
#         self.co_studuje = co_studuje
#         self.jak_umi = schopnosti
#
#     def studuj(self, co):
#         print("Studuju", co, "az se ze me kouri!")
#         self.schopnosti = input("Jak dobre umim ? ")
#         print("A uz umim", self.schopnosti)
#
#     def jak_jsem_studoval(self):
#         print("Minule jsem umel na", self.schopnosti)
#
#
# s = student("Jan", "Zahorec", "Bioinf", 4)
# # s.studuj("Nic")
# =============================================================================
# s.jak_jsem_studoval()

# sys.stdin.read()


class spojak:
    def __init__(self, hodnota, next=None):
        self.hodnota = hodnota
        self.next = next


hlava = None
hlava = spojak(1, hlava)
hlava = spojak(2, hlava)
hlava = spojak(3, hlava)
hlava = spojak(4, hlava)
hlava = spojak(5, hlava)
