# ==========================================
# PROBLEMA 2 - MENÚ DE RESTAURANTE
# FUNDAMENTOS DE PROGRAMACIÓN
# ==========================================

# Función para calcular el precio final
def calcular_precio_final(categoria, precio_base,
                          categoria_objetivo,
                          umbral):

    # Condición para aplicar descuento
    if categoria == categoria_objetivo and precio_base > umbral:

        descuento = precio_base * 0.15
        precio_final = precio_base - descuento

    else:
        precio_final = precio_base

    return precio_final


# Matriz de productos
menu = [

    ["Hamburguesa", "Plato Fuerte", 25000],
    ["Pizza", "Plato Fuerte", 30000],
    ["Perro Caliente", "Comida Rápida", 18000],
    ["Gaseosa", "Bebida", 5000],
    ["Café", "Bebida", 4000],
    ["Lasaña", "Plato Fuerte", 28000]

]

# Variables de promoción
categoria_objetivo = "Plato Fuerte"
umbral = 20000

# Mostrar resultados
print("========== MENÚ CON PROMOCIÓN ==========\n")

for producto in menu:

    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]

    precio_final = calcular_precio_final(
        categoria,
        precio_base,
        categoria_objetivo,
        umbral
    )

    print("Producto:", nombre)
    print("Categoría:", categoria)
    print("Precio Base: $", precio_base)
    print("Precio Final: $", round(precio_final))
    print("--------------------------------")