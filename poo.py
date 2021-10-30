import os
listPersonas=[]

class Persona:
    def __init__(self,rut,nombreApellido,tipoUsuario,hobis,fono,correo,sueldo): #Tambien conocido como constructor
        self.rut=rut  
        self.nombreApellido=nombreApellido  
        self.tipoUsuario=tipoUsuario  
        self.hobis=hobis  
        self.fono=fono  
        self.correo=correo  
        self.sueldo=sueldo

    def mostrarInformacioPersona(self):
        print (f"Nombre: {self.nombreApellido} ##### Rut: {self.rut} ##### Tipo de usuario: {self.tipoUsuario} ##### Hobi's: {self.hobis} ##### Fono: {self.fono} ##### Correo: {self.correo}##### Sueldo: {self.sueldo}")
        
    def aumentoSueldo(self):
        self.sueldo=self.sueldo*1.15            

def ListarPersonas(opcionView):
    if opcionView==1:
        os.system("cls")   
        print("Listado de personas:")
   
    for per in listPersonas:
        per.mostrarInformacioPersona()

    if (opcionView==1):   
        input()
      
    
listPersonas=[
    Persona([11111],["Carlos Alvarez"],"Admin",[],8712683712,"carlos@carlos.cl",50000),   
    Persona(22222,"Benjamin","Jefe",[],21372198,"benja@benja.cl",150000),
    Persona(33333,"Lucho","Informatico",[],687123871,"lucho@lucho.cl",800000)
]

while(True):
    os.system("cls")
    print("Bienvenido a Sistema de mantención de usuarios")
    print("Seleccione una de las tareas a realizar:")
    print(" 1) Listar personas")
    print(" 0) Salir\n")

    opcMenu=input() 

    if (opcMenu=="1"):
        ListarPersonas(1)

    elif (opcMenu=="0"):
        print ("Muchas Gracias")
        break
    else:
        os.system("cls")
        print("Opcion no valida.")
        input()
        