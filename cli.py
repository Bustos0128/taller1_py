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
    console.print("5. Salir")
    return Prompt.ask("Selecciona una opción", choices=["1", "2", "3", "4", "5"])

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
            console.print("Saliendo del programa...", style="bold yellow")
            break

if __name__ == "__main__":
    main()
