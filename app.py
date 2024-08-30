from flask import Flask, request, jsonify
from producto import Producto
from categoria import Categoria
from proveedor import Proveedor
from bodega import Bodega
from gestion_inventario import GestionInventario

app = Flask(__name__)

# Instancias para manejar las entidades
productos = {}
categorias = {}
proveedores = {}
bodegas = {}
gestion_inventario = GestionInventario()

@app.route('/', methods=['GET'])
def home():
    return "<h1>Bienvenido al Sistema de Gestión de Inventario</h1>"

@app.route('/categoria', methods=['POST'])

def agregar_categoria():
    data = request.json
    categoria = Categoria(nombre=data['nombre'], descripcion=data['descripcion'])
    categorias[data['nombre']] = categoria
    return jsonify({"mensaje": "Categoría agregada exitosamente"})

@app.route('/categoria/<nombre>', methods=['GET'])
def consultar_categoria(nombre):
    categoria = categorias.get(nombre)
    if categoria:
        productos_asociados = [p.nombre for p in productos.values() if p.categoria == categoria]
        return jsonify({
            "nombre": categoria.nombre,
            "descripcion": categoria.descripcion,
            "productos": productos_asociados
        })
    return jsonify({"mensaje": "Categoría no encontrada"}), 404

@app.route('/producto', methods=['POST'])
def agregar_producto():
    data = request.json
    categoria = categorias.get(data['categoria'])
    if not categoria:
        return jsonify({"mensaje": "Categoría no encontrada"}), 404
    producto = Producto(
        nombre=data['nombre'],
        descripcion=data['descripcion'],
        precio=data['precio'],
        stock_inicial=data['stock_inicial'],
        categoria=categoria
    )
    productos[data['nombre']] = producto
    return jsonify({"mensaje": "Producto agregado exitosamente"})

@app.route('/producto/<nombre>', methods=['GET'])
def consultar_producto(nombre):
    producto = productos.get(nombre)
    if producto:
        return jsonify({
            "nombre": producto.nombre,
            "descripcion": producto.descripcion,
            "precio": producto.precio,
            "stock_inicial": producto.stock_inicial,
            "categoria": producto.categoria.nombre if producto.categoria else None
        })
    return jsonify({"mensaje": "Producto no encontrado"}), 404

@app.route('/proveedor', methods=['POST'])
def agregar_proveedor():
    data = request.json
    proveedor = Proveedor(
        nombre=data['nombre'],
        direccion=data['direccion'],
        telefono=data['telefono'],
        productos_suministrados=[]
    )
    proveedores[data['nombre']] = proveedor
    return jsonify({"mensaje": "Proveedor agregado exitosamente"})

@app.route('/proveedor/<nombre>', methods=['GET'])
def consultar_proveedor(nombre):
    proveedor = proveedores.get(nombre)
    if proveedor:
        productos_suministrados = [p.nombre for p in proveedor.productos_suministrados]
        return jsonify({
            "nombre": proveedor.nombre,
            "direccion": proveedor.direccion,
            "telefono": proveedor.telefono,
            "productos_suministrados": productos_suministrados
        })
    return jsonify({"mensaje": "Proveedor no encontrado"}), 404

@app.route('/bodega', methods=['POST'])
def agregar_bodega():
    data = request.json
    bodega = Bodega(
        nombre=data['nombre'],
        ubicacion=data['ubicacion'],
        capacidad_maxima=data['capacidad_maxima'],
        productos_almacenados={}
    )
    bodegas[data['nombre']] = bodega
    return jsonify({"mensaje": "Bodega agregada exitosamente"})

@app.route('/bodega/<nombre>', methods=['GET'])
def consultar_bodega(nombre):
    bodega = bodegas.get(nombre)
    if bodega:
        productos_almacenados = {p.nombre: cantidad for p, cantidad in bodega.productos_almacenados.items()}
        return jsonify({
            "nombre": bodega.nombre,
            "ubicacion": bodega.ubicacion,
            "capacidad_maxima": bodega.capacidad_maxima,
            "productos_almacenados": productos_almacenados
        })
    return jsonify({"mensaje": "Bodega no encontrada"}), 404

@app.route('/stock/agregar', methods=['POST'])
def agregar_stock():
    data = request.json
    producto = productos.get(data['nombre_producto'])
    if not producto:
        return jsonify({"mensaje": "Producto no encontrado"}), 404
    cantidad = data['cantidad']
    gestion_inventario.agregar_stock(producto, cantidad)
    return jsonify({"mensaje": "Stock agregado exitosamente"})

@app.route('/stock/retirar', methods=['POST'])
def retirar_stock():
    data = request.json
    producto = productos.get(data['nombre_producto'])
    if not producto:
        return jsonify({"mensaje": "Producto no encontrado"}), 404
    cantidad = data['cantidad']
    gestion_inventario.retirar_stock(producto, cantidad)
    return jsonify({"mensaje": "Stock retirado exitosamente"})

@app.route('/stock/valor_total', methods=['GET'])
def calcular_valor_total_stock():
    valor_total = gestion_inventario.calcular_valor_total_stock()
    return jsonify({"valor_total_stock": valor_total})

@app.route('/stock/informe', methods=['GET'])
def generar_informe_stock():
    informe = gestion_inventario.generar_informe_stock()
    return jsonify(informe)

if __name__ == '__main__':
    app.run(debug=True)

