#Examen Tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox

ventana=tk.Tk()
ventana.title("Examen de Guerras mundiales")

texto=ttk.Label(ventana,text="Quien inicio la primera guerra mundial: ")
texto.grid(column=0,row=0)
nombre1=tk.StringVar()
preguntar_nombre1=ttk.Entry(ventana,width=20,textvariable=nombre1)
preguntar_nombre1.grid(column=1,row=0)

texto=ttk.Label(ventana,text="Quien inicio la segunda guerra mundial: ")
texto.grid(column=0,row=2)
nombre2=tk.StringVar()
preguntar_nombre2=ttk.Entry(ventana,width=20,textvariable=nombre2)
preguntar_nombre2.grid(column=1,row=2)

#Radio 1.01
texto=ttk.Label(ventana,text="Quienes eran los aliados: ")
texto.grid(column=0,row=2)
opcion = tk.IntVar()
radio1 = tk.Radiobutton(ventana,text="Alemania, Estados unidos, Japon", variable=opcion,value=1)
radio1.grid(column=0,row=19,sticky=tk.W)

#Radio 1.02
radio2 = tk.Radiobutton(ventana,text="Alemania, Japon, URSS", variable=opcion,value=2)
radio2.grid(column=1,row=19,sticky=tk.W)

#Radio 1.03
radio3 = tk.Radiobutton(ventana,text="Reino Unido, Estados Unidos, Francia", variable=opcion,value=3)
radio3.grid(column=2,row=19,sticky=tk.W)

    #Segunda pregunta radio
texto=ttk.Label(ventana,text=": ")
texto.grid(column=0,row=2)
#Radio 1.1
opcion2 = tk.IntVar()
radio4 = tk.Radiobutton(ventana,text="", variable=opcion2,value=1)
radio4.grid(column=0,row=19,sticky=tk.W)

#Radio 1.2
radio4 = tk.Radiobutton(ventana,text="", variable=opcion2,value=2)
radio4.grid(column=1,row=19,sticky=tk.W)

#Radio 1.3
radio4 = tk.Radiobutton(ventana,text="", variable=opcion2,value=3)
radio4.grid(column=2,row=19,sticky=tk.W)

ventana.mainloop()