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
    temp=[]
    caracteres=[]
    s=[]
    res=[]
    for i in frase:
        while i != "/":
            temp.append(int(i))
            if (i=="/"):
                s=[str(i) for i in temp]
                res=int("". join(s))
                caracteres.append(res)
        for o in range(len(caracteres)):
            caracteres[o]=caracteres[o]/
            caracteres[o]=chr
            archivo.write(caracteres[o])
    print(caracteres)
else:
    print("Ingresar opción plausible")
