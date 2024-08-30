from producto import Producto

class Bodega:
    def __init__(self, nombre, ubicacion, capacidad_maxima):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.capacidad_maxima = capacidad_maxima
        self.productos_almacenados = {}

    def agregar_producto(self, producto, cantidad):
        if producto not in self.productos_almacenados:
            self.productos_almacenados[producto] = 0

        if self.consultar_disponibilidad(producto) + cantidad > self.capacidad_maxima:
            raise ValueError("No hay suficiente espacio en la bodega.")
        
        self.productos_almacenados[producto] += cantidad

    def retirar_producto(self, producto, cantidad):
        if producto in self.productos_almacenados:
            if cantidad > self.productos_almacenados[producto]:
                raise ValueError("No hay suficiente stock en la bodega.")
            self.productos_almacenados[producto] -= cantidad
        else:
            raise ValueError("El producto no está en la bodega.")

    def consultar_disponibilidad(self, producto):
        return self.productos_almacenados.get(producto, 0)
