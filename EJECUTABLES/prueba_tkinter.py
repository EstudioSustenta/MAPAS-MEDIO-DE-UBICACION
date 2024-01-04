import Tkinter as tk

def seleccion(boton_presionado):
    print("Selección: {}".format(boton_presionado))

# Crear una ventana principal
ventana = tk.Tk()
ventana.title("Selección")

# Funciones que se ejecutan al hacer clic en los botones
def clic_si():
    seleccion("Sí")
    ventana.destroy()  # Cierra la ventana al hacer clic en "Sí"

def clic_no():
    seleccion("No")
    ventana.destroy()  # Cierra la ventana al hacer clic en "No"

# Crear botones
boton_si = tk.Button(ventana, text="Sí", command=clic_si)
boton_no = tk.Button(ventana, text="No", command=clic_no)

# Colocar los botones en la ventana
boton_si.pack(pady=10)
boton_no.pack(pady=10)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
