usuarios={}

def ingresar():
    while True:
        nombre=input("Ingrese el Nombre del usuario: ")
        if nombre.isalpha():
            if nombre in usuarios:
                print("Ya hay un usuario con ese nombre")
            else:
                break
        else:
            print("Solo ponga letras")
    while True:
        genero=input("ingrese su genero (H para hombre y M para mujer): ")
        if genero in ["H","h","M","m"]:
            break
        else:
            print("ponga H o M tambien pueden ser minusculas")
    while True:
        contraseña=input("ingrese su contraseña: ")
        if not contraseña:
            print("Contraseña no puede estar en blanco")
            return
        elif len(contraseña)<8:
            print("la contraseña debe minimo 8 digitos sin espacios en blanco")
        elif " "in contraseña:
            print("la contraseña no puede tener espacios en blanco")
        else:
            break
    usuarios[nombre]=[genero.upper(),contraseña]
print("usuario ingresado exitosamente")

def buscar():
    nombre=input("Ingrese el Nombre del usuario: ")
    if nombre in usuarios:
        genero,contraseña=usuarios[nombre]
        print(f"El ususario {nombre}")
        print(f"Es del genero {genero} y su contraseña es {contraseña}")
    else:
        print("El Ususario no se a encontrado")

def eliminar():
    nombre=input("Ingrese el Nombre del usuario: ")
    if nombre in usuarios:
        del usuarios[nombre]
        print("Se a eliminado al usuario exitosamente")
    else:
        print("No se a encontrado a un usuario con ese nombre")


opciones =0
while opciones!= 4:
    print("Menu de ususario")
    print("1.- Ingresar ususario")
    print("2.- Buscar usuario")
    print("3.- Eliminar usuario")
    print("4.- Salir")
    opciones=input("Elija una opcion del 1 al 4: ")
    match opciones:
        case "1":
            ingresar()
        case "2":
            buscar()
        case "3":
            eliminar()
        case "4":
            print("Terminando Programa...")
            break
        case _:
            print("ingrese una de las opciones")
