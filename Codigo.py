#Examen Tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox

ventana=tk.Tk()
ventana.title("Sistema Escolar")

texto=ttk.Label(tab1,text="Capital de Indonesia: ")
texto.grid(column=0,row=0)
nombre=tk.StringVar()
preguntar_nombre=ttk.Entry(tab1,width=20,textvariable=nombre)
preguntar_nombre.grid(column=1,row=0)

texto=ttk.Label(tab1,text="Apellido Paterno: ")
texto.grid(column=0,row=2)
apellido1=tk.StringVar()
preguntar_apellido1=ttk.Entry(tab1,width=20,textvariable=apellido1)
preguntar_apellido1.grid(column=1,row=2)

