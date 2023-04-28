# -------------------------
# Desktop app No. 1
#--------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *

#----------------------
# funciones de la app
#----------------------

#------------------------------
# ventana principal de la app
#------------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de una objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("suiza")

# tamaño de la ventana
ventana_principal.geometry("500x500")

# desabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="red")

#---------------------------------
# frame blanco1
#---------------------------------
frame_blanco1 = Frame(ventana_principal)
frame_blanco1.config(bg="white", width=100, height=300)
frame_blanco1.place(x=200, y=100)

#---------------------------------
# frame blanco1
#---------------------------------
frame_blanco1 = Frame(ventana_principal)
frame_blanco1.config(bg="white", width=300, height=100)
frame_blanco1.place(x=100, y=200)
# run
# se ejecuta el metodo mainloop() de la clase Tk() a travez de la instancia ventana_principal. Este metodo despliega la ventana en pantalla y queda a la espera de lo que el usuario haga (click en un boton, escribir, etc). Cada accion del usuario se conoce como un evento. El metodo mainloop() es un bucle infinito.

ventana_principal.mainloop()
