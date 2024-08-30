
class Producto:
    def __init__(self, nombre, descripcion, precio, stock_inicial, categoria):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock_inicial = stock_inicial
        self.categoria = categoria

 
    def obtener_detalles(self):
        from categoria import Categoria #se importa en el metodo para dar solucion al error de importacion ciclica
        
        return {
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "stock_inicial": self.stock_inicial,
            "categoria": self.categoria.nombre
        }
