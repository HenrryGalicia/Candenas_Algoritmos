precio = input("Introduce el precio del producto en euros (con dos decimales): ")
try:
    precio_decimal = float(precio)
except ValueError:
    print("El precio introducido no es válido.")
else:
    euros = int(precio_decimal)
    centimos = int((precio_decimal - euros) * 100)

    print("Euros:", euros)
    print("Céntimos:", centimos)
