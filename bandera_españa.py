# se declara una variable llamada ventana_pricipal,que aquiere las carateristicas de un objeto TK[]
from tkinter import Frame, Tk
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title ("bandera de españa ")
# ventana tamaño
ventana_principal.geometry("600x400")
# desabilitar boton de maximizar
ventana_principal.resizable(False,False)
# color de fondo de la ventana
ventana_principal.config(bg="salmon1")
#---------------
# frama roja
#---------------
frame_roja = Frame(ventana_principal)
frame_roja.config(bg="red", width=250, height=125)
frame_roja.place(x=0, y=125)

#---------------
# frama amarillo
#---------------
frame_amarilla = Frame(ventana_principal)
frame_amarilla.config(bg="yellow", width=500, height=250)
frame_amarilla.place(x=0, y=250)

#---------------
# frama roja
#---------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="red", width=250, height=125)
frame_rojo.place(x=0, y=250 )
# run
# se ejecuta el emtodo mainloop()de la clase Tk() a travez de la ventana_principal. este metodo despliega la ventana en pantalla y queda ala espera de lo que el usuario haga (click en un boton,escribir,etc). cada accion del usuario se conoce como un evento. El metodo mainloop() es un bucle infventana_principal.mainloop()es un bucle infinito.
ventana_principal.mainloop()