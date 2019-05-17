import os
paso = input("Encriptar o Desencriptar:")
if paso == "Encriptar":
    nombre = input()
    contrasena  = int(input())
    lineas = int(input())

    archivo = open(str(os.getcwd())+"\\"+nombre+".txt","r+")
    frase = archivo.readline()
    nuevo = open(str(os.getcwd())+"\\"+nombre+"_Encriptado"+".txt","w")
    escribir = 1
    for x in range(lineas):
        for letra in frase:
            if letra == ' ':
                nuevo.write(" ")
            else: 
                escribir = (ord(letra)*contrasena)
                nuevo.write(str(escribir)+"/")
        frase = archivo.readline()
    archivo.close()
    os.remove(str(os.getcwd())+"\\"+nombre+".txt")

elif paso == "Desencriptar":
    nombre = input()
    lineas = input()
    clave = int(input())
    archivo = open(str(os.getcwd())+"\\"+nombre+".txt","r+")
    nuevo = open(str(os.getcwd())+"\\"+nombre+"_Desencriptado"+".txt","w")
    frase = archivo.readline()

        
else:
    print("Ingresar opción plausible")
