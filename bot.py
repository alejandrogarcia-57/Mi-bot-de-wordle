import string as str
import re

with open("diccionario-rae-completo.txt", "r", encoding="utf-8") as file:
    palabras = [line.strip() for line in file]

print(f"Total de palabras: {len(palabras)}")


def eliminar_tilde(palabra):
    print(f"PALABRA INICIAL: {palabra}")
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
    
    print(f"PALABRA FINAL: {palabra_nueva}")

print(eliminar_tilde(palabras[14]))

def tamano_palabra(size, palabras_actual):
    nueva_array_palabras = [palabra for palabra in palabras_actual if len(palabra) == size]
    return nueva_array_palabras
     

def resultado_elecc(resultado, palabra_eleg):
    res_intento = []
    for p in resultado:
        if p == "B":
            res_intento.append(palabra_eleg[p])
        if p == "M" and "C":
            res_intento.append("_")

    return res_intento

def filtrar_palabras(res_intento, palabras_actual):
    cont = 0
    for let in res_intento:
        if let != "_":
            cont += 1
    
    if cont == 0:
        return palabras_actual
    else:
        res_intento_regex = "^" + res_intento.replace("_", ".") + "$"

        palabras_filtradas = [palabra for palabra in palabras_actual if re.match(res_intento_regex, palabra)]
        return palabras_filtradas

        


        

def main():

    print("#############################################")
    print("#                                           #")
    print("#               BOT DE WORDLE               #")
    print("#                                           #")
    print("#############################################")



        

    
