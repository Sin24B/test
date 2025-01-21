import tkinter as tk 
from tkinter import messagebox

def deleni_nulou():
    while True:
      try:
         x=5/0
         print(x)
         break
      except ZeroDivisionError:
         messagebox.showerror("chyba", "Nulou dělit nelze")
         continue 
deleni_nulou()
"""
dalsi kod
"""
