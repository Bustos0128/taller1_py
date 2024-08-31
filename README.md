# Sistema de Gestión de Inventario

Este proyecto es un sistema de gestión de inventario que permite registrar y gestionar productos, categorías, proveedores y bodegas. Está desarrollado en Python y utiliza la biblioteca [Rich](https://rich.readthedocs.io/en/stable/) para la interfaz de texto.

## Características

- Registrar un **Producto** con atributos como nombre, descripción, precio, stock inicial y categoría.
- Registrar una **Categoría** con atributos como nombre y descripción.
- Registrar un **Proveedor** con atributos como nombre, dirección, teléfono y la lista de productos que suministra.
- Registrar una **Bodega** con atributos como nombre, ubicación, capacidad máxima y la lista de productos almacenados.
- Consultar información de productos, categorías, proveedores y bodegas.

## Requisitos

- Python 3.6 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/Bustos0128/taller1_py
   cd taller1
   ```
   ejecutar el script 
   ```bash
   python3 cli.py
  
## Uso

Una vez ejecutado el script `cli.py`, se mostrará un menú con las opciones disponibles:

```plaintext
Sistema de Gestión de Inventario
1. Agregar Producto
2. Consultar Producto
3. Agregar Categoría
4. Consultar Categoría
5. Agregar Proveedor
6. Consultar Proveedor
7. Agregar Bodega
8. Consultar Bodega
9. Salir
```

### Ejemplos

#### Agregar un Producto

1. Selecciona la opción **1. Agregar Producto**.
2. Ingresa el nombre del producto cuando se solicite.
3. Ingresa la descripción del producto.
4. Ingresa el precio del producto.
5. Ingresa el stock inicial del producto.
6. Ingresa el nombre de la categoría a la que pertenece el producto.

#### Consultar un Producto

1. Selecciona la opción **2. Consultar Producto**.
2. Ingresa el nombre del producto que deseas consultar.

#### pendiente por terminar el readme, app.py y finalizar cli.py