import random
import string

def generar_contraseña(longitud=12, usar_mayus=True, usar_numeros=True, usar_simbolos=True):
    caracteres = string.ascii_lowercase
    if usar_mayus:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += "!@#$%^&*()-_"

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

if __name__ == "__main__":
    print("Generador de contraseñas seguras")
    longitud = int(input("¿Qué longitud querés? (mínimo 6): "))
    usar_mayus = input("¿Querés mayúsculas? (s/n): ").lower() == 's'
    usar_numeros = input("¿Querés números? (s/n): ").lower() == 's'
    usar_simbolos = input("¿Querés símbolos? (s/n): ").lower() == 's'

    if longitud < 6:
        print("La longitud mínima es 6. Usando 6.")
        longitud = 6

    contraseña = generar_contraseña(longitud, usar_mayus, usar_numeros, usar_simbolos)
    print(f"Tu contraseña generada es: {contraseña}")