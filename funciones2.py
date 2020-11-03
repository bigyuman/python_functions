def descuento(precio,descuento):
    """Funcion que aplica un descuento a un precio
        Argumentos
            precio sobre el que aplicar el desuento
            descuento, que es un numero de 0 a 100
        Devuelve el precio con el descuento aplicado con una precisión de dos decimales
    """
    if is number(descuento):
        if (0 <= descuento <= 100):
            return (precio * descuento)/100

