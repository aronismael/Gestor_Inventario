from tkinter import *
from Ui.Components import Productos

root=Tk()

root.config(background="blue")

root.resizable(0,0)

def addPageProductos(root: Tk):

    ventanaProdcutos=Productos.VentanaProductos()

    ventanaProdcutos.CreatePage(root)    

addPageProductos(root)

root.mainloop()
