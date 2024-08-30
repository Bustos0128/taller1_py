from producto import Producto

class Proveedor:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.productos_suministrados = []

    def agregar_producto(self, producto):
        """ Agrega un producto a la lista de productos suministrados """
        if producto not in self.productos_suministrados:
            self.productos_suministrados.append(producto)

    def eliminar_producto(self, producto):
        """ Elimina un producto de la lista de productos suministrados """
        if producto in self.productos_suministrados:
            self.productos_suministrados.remove(producto)
