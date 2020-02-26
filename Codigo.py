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


