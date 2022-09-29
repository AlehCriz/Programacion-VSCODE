vehiculo=0
velocidad=0
giro=0
print("Seleccione una opcion")
print("1. Registrarse")
print("2. Comenzar una carrera")
opcion=int(input("ingrese una opcion"))
latitud=0
longitud=0
if(opcion==1):
    print ("ingrese su nombre")
    nombre=input()
    print("ingrese patente de su vehiculo")
    patente=input()
if(opcion==2):
    print ("Inicio de carrera")
i=0
while(i<20):
    print ("1.- Ingresar ubicación GPS, LATITUD")
    print ("2.- Ingresar ubicacion GPS, LONGITUD")
    print ("3.- Encender el vehículo.")
    print ("4.- Acelerar vehículo")
    print ("5.- Apagar Vehículo")
    print ("6.- Girar Vehiculo")
    carrera=int(input())
    if (carrera==1) and (vehiculo==1):
        latitud=int(input())
    if (carrera==1) and (vehiculo==0):
        print("Debe encender el vehiculo")
    if (carrera==2) and (vehiculo==1):
       longitud=int(input())
    if (carrera==2) and (vehiculo==0):
        print("Debe encender el vehiculo")
    if (carrera==3):
        vehiculo=1
        print("vehiculo encendido")
    if (carrera==4) and (vehiculo==1):
        velocidad= velocidad+10
        print ("velocidad actual es: ", velocidad, ("Km/H"))
    if (carrera==4) and (vehiculo==0):
        print ("Debe encender el vehiculo")
    if (carrera==5):
        vehiculo=0
        velocidad=0
        print("vehiculo apagado")
        print ("ubicacion GPS",longitud,latitud)
        print (longitud,latitud)
        print ("Viaje finalizado")
        print ("nombre conductor: ",nombre )
        print ("Patente del vehiculo: ", patente)
    if (carrera==6):
        print ("Hacia donde gira el vehiculo")
        print ("1.- Derecha")
        print ("2.- Izquierda")
        opgiro=int(input())
        if (opgiro==1) and (giro==0): #neutro a derecha
            print ("El vehiculo va hacia la derecha")
        if (opgiro==2) and (giro==0): #neutro a izquierda
            print ("El vehiculo a girado a la izquierda")