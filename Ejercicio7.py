correo_original = input("Introduce tu correo electrónico: ")
nombre_usuario, dominio = correo_original.split('@')
correo_modificado = f"{nombre_usuario}@ceu.es"
print("Nuevo correo electrónico:", correo_modificado)
