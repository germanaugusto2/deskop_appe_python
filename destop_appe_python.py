#-----------------------------
# Desktop app No. 1
#-----------------------------

# se importa la libreria tkinter con todas sus funciones 
from tkinter import *

#-------------------------
# funciones de la app
#-------------------------

#-----------------------------
# ventana principal de la app
#-----------------------------

# se declara una variable llamada ventana_principal, que adquiere caracteristicas de un objeto Tk()
ventana_principal = Tk()

# Titul de la ventana 
ventana_principal.title("Bandera de Colombia")

# Tamaño de la ventana
ventana_principal.geometry("500x500")

#Desabilitar boton de maximisar
ventana_principal.resizable(False,False)

# Color de fondo de la ventana
ventana_principal.config(bg="black")

#---------------------
# frame amarillo 
#---------------------
frame_amarillo = Frame(ventana_principal)
frame_amarillo.config(bg="yellow", width=500, height=250)
frame_amarillo.place(x= 0, y=0)

#---------------------
# frame azul
#---------------------
frame_azul = Frame(ventana_principal)
frame_azul.config(bg="blue", width=500, height=125)
frame_azul.place(x= 0, y=250)

#---------------------
# frame rojo 
#---------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="red", width=500, height=125)
frame_rojo.place(x= 0, y=375)


#run
# se ejecuta el metodo mainloop() de la clase Tk() a traves de la instancia ventana_principal.ste metodo despliega la ventana en pantalla y queda en espera de lo que el usuario haga (click en un boton,escribir,etc). Cada accion del usuario se conoce como un evento. El metodo mainloop()es un bucle infinito.
ventana_principal.mainloop()