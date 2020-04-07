#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
from PIL import ImageTk,Image
import sys
print(sys.version)
# ----- Colores -----
cl = "#35c3cc"
cf = "#090a23"
# ----- Dimensiones -----
vx="470"
vy="300"
# ----- Acceder a el tamaño de la pantalla -----
from win32api import GetSystemMetrics
width = str(GetSystemMetrics (0))
height = str(GetSystemMetrics (1)-85)
# ----- Tipos de Letra -----
f = "Impact"
      # SABER TIPOS DE LETRAS
# for font in font.families():
#     print(font)
#######Future, Impact#######

################ Constructor Ventana Principal ###################
class menuPrincipal:
    
    def __menuPrincipal__():
        # ----- Ventana Principal -----
        __ventanaPrincipal__= tk.Tk()
        __ventanaPrincipal__.iconphoto(False, 
                                      tk.PhotoImage(file='Recursos/store.png'))
        __ventanaPrincipal__.configure(bg=cf)
        __ventanaPrincipal__.geometry(width+"x"+height+'+0+0')
        __ventanaPrincipal__.resizable(width=0, height=0)
        __ventanaPrincipal__.title("It Curo Faciles")
        __ventanaPrincipal__.maxsize(width, height)
        __ventanaPrincipal__.state('zoomed')
        

        # ----- Opciones bar ------
        menuP = tk.Menu(__ventanaPrincipal__,
                        background=cf, 
                        foreground=cl,
                        activebackground=cf, 
                        activeforeground=cl,
                        font=(f, 16)
                        )
        
        # ----- subMenú Ventas -----
        ventas = tk.Menu(menuP,tearoff=0,
                     background=cl, 
                     foreground=cf,
                     font=(f, 16),
                        activebackground=cf, activeforeground=cl)
        ventas.add_command(label="v1")
        ventas.add_command(label="v2")
        
        # ----- subMenú Agragaciones -----
        agregaciones = tk.Menu(menuP,tearoff=0,
                     background=cl, 
                     foreground=cf,
                     font=(f, 16),
                        activebackground=cf, activeforeground=cl)
        agregaciones.add_command(label="a1",command=None)
        agregaciones.add_command(label="a2",command=None)

        # ----- subMenú actualiza -----
        actualiza = tk.Menu(menuP,tearoff=0,
                     background=cl, 
                     foreground=cf,
                     font=(f, 16),
                        activebackground=cf, activeforeground=cl)
        actualiza.add_command(label="ac1",command=None)
        actualiza.add_command(label="ac2",command=None)

        # ----- subMenú consultas ----- 
        consultas = tk.Menu(menuP,tearoff=0,
                     background=cl, 
                     foreground=cf,
                     font=(f, 16),
                        activebackground=cf, activeforeground=cl)
        consultas.add_command(label="c1",command=None)
        consultas.add_command(label="c2",command=None)
        consultas.add_command(label="c3",command=None)
        
        ayuda = tk.Menu(menuP,tearoff=0,
                     background=cl, 
                     foreground=cf,
                     font=(f, 16),
                        activebackground=cf, activeforeground=cl)
        ayuda.add_command(label="Contacto",command=None)
        
        # ----- Menú principal -----
        menuP.add_cascade(label="Ventas", menu=ventas)
        menuP.add_cascade(label="Agregaciones", menu=agregaciones)
        menuP.add_cascade(label="Actualizaciones", menu=actualiza)
        menuP.add_cascade(label="Consultas", menu=consultas)
        menuP.add_cascade(label="Ayuda", menu=ayuda)
        
        
        __ventanaPrincipal__.config(menu=menuP)

        
        __ventanaPrincipal__.mainloop()

############################# Ventana Login ################################
login = tk.Tk()
posicion = "+"+str(int(int(width)/3))+"+"+str(int(int(height)/3))
login.geometry(vx+"x"+vy+posicion)
login.title("Login")
login.overrideredirect(1)
login.wm_attributes("-topmost", True)

# ----- Imagen de Fondo -----
cargaF = Image.open('Recursos/Fondo.gif')
cargaF = cargaF.resize((int(vx), int(vy)), Image.ANTIALIAS)
photoFondo = ImageTk.PhotoImage(cargaF)
w = photoFondo.width()
h = photoFondo.height()
fondo = tk.Label(login, image=photoFondo)
fondo.place(x=0, y=0, relwidth=1, relheight=1)

# ----- Label Usuario -----
lu = tk.Label(login,
              text="Usuario:", 
              font=(f, 14),
              bg=cf, 
              fg=cl)
# lu.config(bg="systemTransparent")
lu.pack()
lu.place(x=50,y=150)

# ----- Entry Usuario -----
p1 = tk.Entry(login, 
                      width=20,
                      font=(f, 12), 
                      bg=cl, 
                      fg=cf)
p1.pack()
p1.place(x=180,y=155)

# -----Label Contraseña -----
lc = tk.Label(login,
              text="Contraseña:",
              font=(f, 13),
              bg=cf,
              fg=cl
              )
lc.pack()
lc.place(x=50,y=190)

# ----- Entry Contraseña -----
p1 = tk.Entry(login, 
                      width=20,
                      font=(f, 12), 
                      bg=cl, 
                      fg=cf,
                      show="*")
p1.pack()
p1.place(x=180,y=190)

# ----- Metodo Entrar ----- 
def __entrar__():
    login.destroy()
    menuPrincipal.__menuPrincipal__()

#   ----- Boton Entrar -----
entrar = tk.Button(login,
                   text="Entrar",
                   bg= cf,                           
                   fg= cl,
                   font=(f, 12),
                   command=__entrar__
                    )
entrar.pack()
entrar.place(x=200,y=230)

# ----- Imagen Login -----
image = tk.PhotoImage(file='Recursos/users.png')
smaller_image = image.subsample(11, 11)
imgLogin = tk.Label(login,image=smaller_image, bg = cf)
imgLogin.pack()
imgLogin.place(x=175,y=15)

#   ----- Boton Cerrar -----
def cerrarLogin():
    login.destroy()

cerrar = tk.Button(text="Cerrar",
                   bg= cf,                           
                   fg= cl,
                   font=(f, 12),
                   command=cerrarLogin)
cerrar.pack()
cerrar.place(x=403)

login.mainloop()

"""
Created on Fri Apr  3 09:34:48 2020
@author: Kevin Andrés Forero Guaitero
https://github.com/kevinandresforero/Sistema-De-Ventas
"""

