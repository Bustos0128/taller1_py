from categoria import Categoria

class Producto:
    def __init__(self, nombre, descripcion, precio, stock_inicial, categoria):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock_inicial = stock_inicial
        self.categoria = categoria

 
    def obtener_detalles(self):
        """ Retorna un diccionario con los detalles del producto """
        return {
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "stock_inicial": self.stock_inicial,
            "categoria": self.categoria.nombre
        }
