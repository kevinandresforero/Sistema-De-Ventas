#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import font
from PIL import Image

# ----- Colores -----
cf = "#8BB2E4"
cl = "#00006a"
# ----- Tipos de Letra -----
f = "Future"
#       SABER TIPOS DE LETRAS
#for font in font.families():
#    print(font)
#######Future, Impact#######

login = tk.Tk()
login.geometry("470x300")
login.title("Login")
login.overrideredirect()
login.configure(bg = cf)


# ----- Label Usuario -----
lu = tk.Label(login,
              text="Usuario:", 
              font=(f, 20),
              bg=cf, 
              fg=cl)
lu.pack()
lu.place(x=60,y=150)

# ----- Entry Usuario -----
p1 = tk.Entry(login, 
                      width=25,
                      font=(f, 12), 
                      bg=cl, 
                      fg=cf)
p1.pack()
p1.place(x=190,y=160)

# -----Label Contraseña -----
lc = tk.Label(login,
              text="Contraseña:",
              font=(f, 18),
              bg=cf,
              fg=cl
              )
lc.pack()
lc.place(x=60,y=190)

# ----- Entry Contraseña -----########### Cambiar Entry normamal por "*******"
p1 = tk.Entry(login, 
                      width=25,
                      font=(f, 12), 
                      bg=cl, 
                      fg=cf,
                      show="*")
p1.pack()
p1.place(x=190,y=190)

#   ----- Boton Entrar -----
entrar = tk.Button(login,
                   text="Entrar",
                   bg= cl,                           
                   fg= cf,
                   font=(f, 15),
#                   command=
                    )
entrar.pack()
entrar.place(x=210,y=230)

#----- Label con Imagen -----
#img = Image.open("usuario.svg")
#img.resize((200,200), Image.ANTIALIAS)
#can = tk.Canvas(login)
#can.pack()
#can.place(x=10,y=10)
#can.create_image(20, 20, image=img)
#imgLogin.place()
image = tk.PhotoImage(file='usuario.gif')
smaller_image = image.subsample(4, 4)
imgLogin = tk.Label(login,image=smaller_image)
imgLogin.pack()
imgLogin.place(x=175,y=15)



login.mainloop()

"""
Created on Fri Apr  3 09:34:48 2020
@author: Kevin
"""

