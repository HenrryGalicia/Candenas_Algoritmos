fecha_nacimiento = input("Introduce tu fecha de nacimiento en formato dd/mm/aaaa: ")
try:
    dia, mes, anio = map(int, fecha_nacimiento.split('/'))
    print("Día:", dia)
    print("Mes:", mes)
    print("Año:", anio)
except ValueError:
    print("La fecha agregada no es válida.")
