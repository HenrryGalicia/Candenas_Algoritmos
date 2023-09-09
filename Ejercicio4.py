numero_telefono = input("Introduce un número de teléfono con el formato +34-XXXXXXXXX-XX: ")

partes = numero_telefono.split("-")

if len(partes) == 3 and partes[0] == "+34" and len(partes[1]) == 9 and len(partes[2]) == 2 and partes[1].isdigit() and partes[2].isdigit():
    numero_principal = partes[1] 
    print("Número principal:", numero_principal)
else:
    print("El número de teléfono no tiene el formato válido.")
