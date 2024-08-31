from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from producto import Producto
from categoria import Categoria
from proveedor import Proveedor
from bodega import Bodega
from gestion_inventario import GestionInventario

console = Console()

# Instancias para manejar las entidades
productos = {}
categorias = {}
proveedores = {}
bodegas = {}
gestion_inventario = GestionInventario()

def mostrar_menu():
    console.print("[bold blue]Sistema de Gestión de Inventario[/bold blue]")
    console.print("1. Agregar Producto")
    console.print("2. Consultar Producto")
    console.print("3. Agregar Categoría")
    console.print("4. Consultar Categoría")
    console.print("5. Agregar proveedor")
    console.print("6. Consultar proveedor")
    console.print("7. Agregar bodega")
    console.print("8. consultar bodega")
    
    console.print("9. Salir")
    return Prompt.ask("Selecciona una opción", choices=["1", "2", "3", "4", "5","6","7","8","9"])

def agregar_producto():
    nombre = Prompt.ask("Nombre del producto")
    descripcion = Prompt.ask("Descripción del producto")
    precio = float(Prompt.ask("Precio del producto"))
    stock_inicial = int(Prompt.ask("Stock inicial del producto"))
    categoria_nombre = Prompt.ask("Nombre de la categoría")
    
    categoria = categorias.get(categoria_nombre)
    if not categoria:
        console.print("Categoría no encontrada", style="bold red")
        return
    
    producto = Producto(nombre, descripcion, precio, stock_inicial, categoria)
    productos[nombre] = producto
    console.print("Producto agregado exitosamente", style="bold green")

def consultar_producto():
    nombre = Prompt.ask("Nombre del producto")
    producto = productos.get(nombre)
    if producto:
        console.print(f"Nombre: {producto.nombre}")
        console.print(f"Descripción: {producto.descripcion}")
        console.print(f"Precio: {producto.precio}")
        console.print(f"Stock Inicial: {producto.stock_inicial}")
        console.print(f"Categoría: {producto.categoria.nombre}")
    else:
        console.print("Producto no encontrado", style="bold red")

def agregar_categoria():
    nombre = Prompt.ask("Nombre de la categoría")
    descripcion = Prompt.ask("Descripción de la categoría")
    
    categoria = Categoria(nombre, descripcion)
    categorias[nombre] = categoria
    console.print("Categoría agregada exitosamente", style="bold green")

def consultar_categoria():
    nombre = Prompt.ask("Nombre de la categoría")
    categoria = categorias.get(nombre)
    if categoria:
        productos_asociados = [p.nombre for p in productos.values() if p.categoria == categoria]
        console.print(f"Nombre: {categoria.nombre}")
        console.print(f"Descripción: {categoria.descripcion}")
        console.print(f"Productos Asociados: {', '.join(productos_asociados)}")
    else:
        console.print("Categoría no encontrada", style="bold red")
def agregar_proveedor():
    nombre = Prompt.ask("Nombre del proveedor")
    direccion = Prompt.ask("Direccion del proveedor")
    telefono = Prompt.ask("Telefono del proveedor")
    
    proveedor = Proveedor(nombre,direccion,telefono)
    proveedores[nombre] = proveedor
    console.print("proveedor agregado exitosamente", style="bold green")

def consultar_proveedor():
    nombre = Prompt.ask("Nombre del proveedor")
    proveedor = proveedores.get(nombre)
    if proveedor:
        productos_suministrados = [p.nombre for p in proveedor.productos_suministrados]
        console.print(f"Nombre: {proveedor.nombre}")
        console.print(f"Dirección: {proveedor.direccion}")
        console.print(f"Teléfono: {proveedor.telefono}")
        console.print(f"Productos Suministrados: {', '.join(productos_suministrados) if productos_suministrados else 'Ninguno'}")
    else:
        console.print("Proveedor no encontrado", style="bold red")
 
def agregar_bodega():
    nombre = Prompt.ask("Nombre de la bodega")
    ubicacion = Prompt.ask("Ubicación de la bodega")
    capacidad_maxima = int(Prompt.ask("Capacidad máxima de la bodega"))
    
    bodega = Bodega(nombre, ubicacion, capacidad_maxima, {})
    bodegas[nombre] = bodega
    console.print("Bodega agregada exitosamente", style="bold green")

def consultar_bodega():
    nombre = Prompt.ask("Nombre de la bodega")
    bodega = bodegas.get(nombre)
    if bodega:
        productos_almacenados = {p.nombre: cantidad for p, cantidad in bodega.productos_almacenados.items()}
        console.print(f"Nombre: {bodega.nombre}")
        console.print(f"Ubicación: {bodega.ubicacion}")
        console.print(f"Capacidad Máxima: {bodega.capacidad_maxima}")
        console.print(f"Productos Almacenados: {productos_almacenados if productos_almacenados else 'Ninguno'}")
    else:
        console.print("Bodega no encontrada", style="bold red")   
    

def main():
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            consultar_producto()
        elif opcion == "3":
            agregar_categoria()
        elif opcion == "4":
            consultar_categoria()
        elif opcion == "5":
            agregar_proveedor()
        elif opcion == "6":
            consultar_proveedor()
        elif opcion == "7":
            agregar_bodega()
        elif opcion == "8":
            consultar_bodega()
        elif opcion == "9":
            console.print("Saliendo del programa...", style="bold yellow")
            break

if __name__ == "__main__":
    main()
