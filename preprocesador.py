def traduce_codigo(codigo):
    traducciones = {
        "función": "def",
        "imprimir": "print",
    }
    for esp, py in traducciones.items():
        codigo = codigo.replace(esp, py)
    return codigo

codigo_usuario = """
función saluda(nombre):
    imprimir("Hola", nombre)
"""

exec(traduce_codigo(codigo_usuario))
saluda("Mundo")  # Imprime: Hola Mundo