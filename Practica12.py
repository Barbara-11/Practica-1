#Programa para tomar captura de pantalla

import pyautogui
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog

print("Pasos para la captura de pantalla\n"
      "1:De click en navegar y ubiquese en el lugar donde desee guardar la imagen, "
      "ingrese el nombre con el que desee guardar su captura y de click en guardar\n"
      "2:Dirijase a la pantalla donde desea tomar la captura y de click en captura\n"
      "Listo su imagen se ha guardado en la carpeta que usted especifico\n")

def Widgets():
    etiqueta = Label(vn, text = "Guardar como: ", font = ("", 10, "bold"))
    etiqueta.grid(row=1, column=0, pady=5, padx=5)

    vn.texto = Entry(vn, width = 30)
    vn.texto.grid(row=1, column=1, pady=5, padx=5)

    botonGuardar = Button(vn, text="Navegar", width=10, command = navegar)
    botonGuardar.grid(row=1, column=2, pady=5, padx=5)

    botonCaptura = Button(vn, text="Captura", width=10, command = captura)
    botonCaptura.grid(row=2, column=1, pady=5, padx=5)

def navegar():
    vn.archivo = filedialog.asksaveasfilename(title = "Guardar como",
                                                    defaultextension = ".png",
                                                    filetypes =(("Archivo Png", "*.png"),("Todos los Archivos","*.*")))
    vn.texto.insert("1", vn.archivo)

def captura():
    captura = pyautogui.screenshot()

    captura.save(vn.archivo)
    messagebox.showinfo("Practica 11","Captura Guardada")

vn=tk.Tk()
vn.title("Captura de Pantalla")
Widgets()
vn.mainloop()


