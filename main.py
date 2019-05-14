import os

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
