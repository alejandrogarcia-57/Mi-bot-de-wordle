import string as str
import re
import random as rdm
import sys

with open("diccionario-rae-completo.txt", "r", encoding="utf-8-sig") as file:
    palabras = [line.strip() for line in file]

print(f"Total de palabras: {len(palabras)}")


def eliminar_tilde(palabra):
    
    con_sin_tilde = {
        "á" : "a",
        "é" : "e",
        "í" : "i",
        "ó" : "o",
        "ú" : "u",
        "Á" : "A",
        "É" : "E",
        "Í" : "I",
        "Ó" : "O",
        "Ú" : "U"
    }

    palabra_nueva = "".join(con_sin_tilde.get(letra, letra) for letra in palabra)
    
    
    return palabra_nueva


def tamano_palabra(size, palabras_actual):
    nueva_array_palabras = [palabra for palabra in palabras_actual if len(palabra) == size]
    return nueva_array_palabras
     

def resultado_elecc(resultado, palabra_eleg):
    res_intento = []
    
    for i, p in enumerate(resultado):
        if p == "B":
            res_intento.append(palabra_eleg[i])  # Letra correcta en su lugar
        elif p in ["M", "C"]:  
            res_intento.append("_")  # Letra incorrecta o en mala posición
    print(res_intento)
    return res_intento



def filtrar_palabras(res_intento, palabras_actual, resultado, palabra_anterior):
    # 1️⃣ Obtener las letras descartadas (letras incorrectas que no deben aparecer en la palabra)
    letras_descartadas = {palabra_anterior[i] for i, p in enumerate(resultado) if p == "M"}  # Letras incorrectas

    # 2️⃣ Obtener las letras mal posicionadas (letras correctas pero en la posición incorrecta)
    letras_mal_posicionadas = {palabra_anterior[i]: i for i, p in enumerate(resultado) if p == "C"}  # Letras mal ubicadas

    # 3️⃣ Crear la expresión regular para la estructura de la palabra (sin considerar las letras incorrectas)
    regex = "^" + "".join(res_intento).replace("_", ".") + "$"

    palabras_filtradas = []
    
    for palabra in palabras_actual:
        # 4️⃣ Verificar que cumple con la estructura base (palabra válida según los intentos previos)
        if not re.fullmatch(regex, palabra):
            continue
        
        # 5️⃣ Evitar palabras con letras descartadas (M) en cualquier posición
        if any(letra in palabra for letra in letras_descartadas):
            continue
        
        # 6️⃣ Evitar palabras que tengan letras en la posición incorrecta (C)
        if any(palabra[idx] == letra for letra, idx in letras_mal_posicionadas.items()):
            continue
        
        palabras_filtradas.append(palabra)
    
    return palabras_filtradas




        

def main():
    global palabras
    print("#############################################")
    print("#                                           #")
    print("#             BOT DE WORDLE 1.0             #")
    print("#                                           #")
    print("#############################################")

    intentos = 0
    solucion = []
    acierto = False

    print("Este programa será utilizado para poder resolver correctamente el juego de la palabra del dia ")
    print("VAMOS A EMPEZAAAAR")
    
    try:
        size = int(input("Escribe el tamanyo de la palabra a adivinar: "))
    except ValueError:
        print("Por favor ingrese un número")
    palabras_actual = tamano_palabra(size, palabras)
    while intentos < 6 and not acierto:
        if intentos == 0:
            if len(palabras_actual) > 0:
                num = rdm.randint(0, len(palabras_actual)-1)
                palabra = eliminar_tilde(palabras_actual[num])
                palabra_MAY = palabra.upper()
            else:
                print("Error: No hay palabras disponibles")
            print(f"Para empezar con el primer intento probaremos con: " + palabra_MAY)
            res = input(f"¿Cual es el resultado del intento??: SIMBOLOGIA => 'B' = Posicion correcta, 'C' = Posición incorrecta, 'M' = Letra incorrecta: ")

        elif intentos < 5:
            if len(palabras_actual) > 0:
                num = rdm.randint(0, len(palabras_actual)-1)
                palabra = eliminar_tilde(palabras_actual[num])
                palabra_MAY = palabra.upper()
            else:
                print("Error: No hay palabras disponibles")
            print(f"Intento número {intentos + 1}, ahora probaremos con: " + palabra_MAY)
            res = input(f"¿Cual es el resultado del intento??: SIMBOLOGIA => 'B' = Posicion correcta, 'C' = Posición incorrecta, 'M' = Letra incorrecta: ")
        else:
            if len(palabras_actual) > 0:
                num = rdm.randint(0, len(palabras_actual)-1)
                palabra = eliminar_tilde(palabras_actual[num])
                palabra_MAY = palabra.upper()
            else:
                print("Error: No hay palabras disponibles")
            print(f"Vaya!!! Parece que esta es mi última oportunidad!! De acuerdo, prueba con: " + palabra_MAY)
            res = input(f"¿Cual es el resultado del intento??: SIMBOLOGIA => 'B' = Posicion correcta, 'C' = Posición incorrecta, 'M' = Letra incorrecta: ")
        
        solucion = resultado_elecc(res, palabra_MAY)
        cont = 0
        for i, x in enumerate(solucion):
            if solucion[i] == "_":
                cont = cont + 1

        if cont != 0:
            palabras_actual = filtrar_palabras(solucion, palabras_actual, res, palabra_MAY)
            intentos = intentos + 1
        else:
            acierto = True
        
    if acierto:
        print(f"ENHORABUENA, HEMOS COMPLETADO SATISFACTORIAMENTE EL JUEGO DIARIO DE LA PALABRA DEL DIA!!")
        print(f"LA PALABRA CORRECTA ERA: " + solucion + " y hemos necesitado " + (intentos + 1) + "intento/s para resolverlo")
    else:
        print(f"OOOOoooh, que lástima, no pudimos dar con la palabra del día en esta ocasión, mala suerte :/")
        

if __name__ == "__main__":
    main()        

    
        

    
