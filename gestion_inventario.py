from producto import Producto

class GestionInventario:
    def __init__(self):
        self.inventario = {}

    def agregar_stock(self, producto, cantidad):
        """ Agrega stock a un producto en el inventario """
        if producto in self.inventario:
            self.inventario[producto] += cantidad
        else:
            self.inventario[producto] = cantidad

    def retirar_stock(self, producto, cantidad):
        """ Retira stock de un producto en el inventario """
        if producto in self.inventario:
            if cantidad > self.inventario[producto]:
                raise ValueError("La cantidad a retirar no puede exceder el stock disponible.")
            self.inventario[producto] -= cantidad
        else:
            raise ValueError("El producto no está en el inventario.")

    def calcular_valor_total_stock(self):
        """ Calcula el valor total del stock """
        total_valor = 0.0
        for producto, cantidad in self.inventario.items():
            total_valor += producto.precio * cantidad
        return total_valor

    def generar_informe_stock(self):
        """ Genera un informe del stock """
        informe = {}
        for producto, cantidad in self.inventario.items():
            informe[producto.nombre] = {
                "descripcion": producto.descripcion,
                "precio": producto.precio,
                "stock": cantidad
            }
        return informe
