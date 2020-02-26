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
texto.grid(column=0,row=3)
opcion = tk.IntVar()
radio1 = tk.Radiobutton(ventana,text="Alemania, Estados unidos, Japon", variable=opcion,value=1)
radio1.grid(column=0,row=4,sticky=tk.W)

#Radio 1.02
radio2 = tk.Radiobutton(ventana,text="Alemania, Japon, URSS", variable=opcion,value=2)
radio2.grid(column=1,row=4,sticky=tk.W)

#Radio 1.03
radio3 = tk.Radiobutton(ventana,text="Reino Unido, Estados Unidos, Francia", variable=opcion,value=3)
radio3.grid(column=2,row=4,sticky=tk.W)

    #Segunda pregunta radio
texto=ttk.Label(ventana,text=": ")
texto.grid(column=0,row=5)
#Radio 1.1
opcion2 = tk.IntVar()
radio4 = tk.Radiobutton(ventana,text="", variable=opcion2,value=1)
radio4.grid(column=0,row=6,sticky=tk.W)

#Radio 1.2
radio4 = tk.Radiobutton(ventana,text="", variable=opcion2,value=2)
radio4.grid(column=1,row=6,sticky=tk.W)

#Radio 1.3
radio4 = tk.Radiobutton(ventana,text="", variable=opcion2,value=3)
radio4.grid(column=2,row=6,sticky=tk.W)

    #Siguiente pregunta
texto=ttk.Label(ventana,text="QUE APOS")
texto.grid(column=0,row=8)

#Botón de control
opcion_1= tk.IntVar()
casilla_1=tk.Checkbutton(ventana,text="CORRECTA",variable=opcion_1)
casilla_1.select()
casilla_1.grid(column=1,row=9,sticky=tk.W)

#Botón de control 2
opcion_2= tk.IntVar()
casilla_2=tk.Checkbutton(ventana,text="WRONG",variable=opcion_2)
casilla_2.select()
casilla_2.grid(column=0,row=9,sticky=tk.W)

#Botón de control 3
opcion_3= tk.IntVar()
casilla_3=tk.Checkbutton(ventana,text="WRONG",variable=opcion_3)
casilla_3.select()
casilla_3.grid(column=2,row=9,sticky=tk.W)

#Botón de control 4
opcion_4= tk.IntVar()
casilla_4=tk.Checkbutton(ventana,text="CORRECTA",variable=opcion_4)
casilla_4.select()
casilla_4.grid(column=3,row=9,sticky=tk.W)

#Botón de control 5
opcion_5= tk.IntVar()
casilla_5=tk.Checkbutton(ventana,text="WRONG",variable=opcion_5)
casilla_5.select()
casilla_5.grid(column=4,row=9,sticky=tk.W)



#BOTON CALIFICAR


ventana.mainloop()