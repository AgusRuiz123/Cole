import openpyxl
from openpyxl.styles import Font
from datetime import datetime
import os



class Productos:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.codigo}: {self.nombre} - ${self.precio:.2f} (Stock: {self.stock})"
        
class venta:
    def __init__(self):
        self.productos_vendidos = []
        self.total = 0
        self.fecha = datetime.now()
    
    def agregar_productos(self, productos, cantidad):
        