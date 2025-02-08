import string as str

with open("diccionario-rae-completo.txt", "r", encoding="utf-8") as file:
    palabras = [line.strip() for line in file]

print(f"Total de palabras: {len(palabras)}")


def convertidor_ascii(letra):
    x=letra.encode()
    return int.from_bytes(x, byteorder="big")

for letra1 in "aáeéiíoóuú":
    print(f"Letra {letra1} = {convertidor_ascii(letra1)}")



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


        

    
