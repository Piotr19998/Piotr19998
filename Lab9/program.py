# -*- coding: utf-8 -*-
"""
Created on Sun May  1 19:01:15 2022

@author: piotr
"""

import mojeklasy

def testy():
    pass

print("zadanie 1")
pkt1 = mojeklasy.Punkt2D(3,4)
pkt1.drukuj()
pkt1.zeruj()
pkt1.drukuj()
print()

print("zadanie 2")
pkt2 = mojeklasy.Punkt3D(3,4,5)
pkt2.drukuj()
pkt2.zeruj()
pkt2.drukuj()
print()

print("zadanie 3")
dluOdc = mojeklasy.Odcinek(3,4,4,6)
dluOdc.drukuj()
print()

if __name__ == "__main__":
    testy()