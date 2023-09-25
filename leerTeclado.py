
from readchar import readkey,key

# Bucle infinito
while True:
    # Leer un caracter del teclado
    char = readkey()
    
    # Verificar si el caracter es la tecla '↑'
    # En la librería `readchar`, la tecla '↑' se representa como '\x1b[A'
    if char == key.UP:
        print("Tecla '↑' presionada. Terminando el programa.")
        break
    
    # Imprimir el caracter leído
    print(char) 



