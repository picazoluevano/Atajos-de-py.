def saluda(nombre):
    return f"¡Hola, {nombre}!"

def es_par(numero):
    return numero % 2 == 0

def promedio(*args):
    return sum(args) / len(args) if args else 0