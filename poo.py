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



def IngresarPersona():
    os.system("cls")   
    print("Modulo de ingreso de persona")
    nombrePersona=input("Favor de ingresar el nombre de la persona: ")
    rutPersona=int(input("Favor de ingresar el RUT de la persona: "))
    tipo=input("Favor de ingresar el Tipo de usuario : ")
    fono=int(input("Favor de ingresar el numero telefonico: "))
    correo=input("Favor de ingresar el correo: ")
    sueldo=int(input("Favor de ingresar el sueldo: "))

    p=Persona(rutPersona,nombrePersona,tipo,[],fono,correo,sueldo)
    listPersonas.append(p)
   
    input("Persona agregada con Exito")

def ListarPersonas(opcionView):
    if opcionView==1:
        os.system("cls")   
        print("Listado de personas:")
   
    for per in listPersonas:
        per.mostrarInformacioPersona()

    if (opcionView==1):   
        input()
    

def EliminarPersonas():
    os.system("cls")      
    print("Eliminar Persona:")
    ListarPersonas(0)
    rutELimina=int(input("Favor de ingresar el rut a eliminar: "))
    # listPersonasNoElimina=listPersonas
    # listPersonasNoElimina=filter(lambda p : p.rut!=rutELimina , listPersonas)
    # listPersonas=listPersonasNoElimina
    

    # for per in listPersonasNoElimina:
    #     print(per.nombreApellido)
    

    indice=0
    for per in listPersonas:
        if per.rut==rutELimina:
            listPersonas.pop(indice)  
            print("La persona que elmino es ",per.nombreApellido)
        indice+=1  

    input()

def ModificarPersonas():
    os.system("cls")      
    print("Modificar Persona:")

    ListarPersonas(0)

    rutModifica=int(input("Favor de ingresar el rut a modificar: "))

    indice=0
    for per in listPersonas:
        if per.rut==rutModifica:
            per.nombreApellido=input("Favor de ingresar el nombre de la persona: ")
            per.tipoUsuario=input("Favor de ingresar el Tipo de usuario : ")
            per.fono=int(input("Favor de ingresar el numero telefonico: "))
            per.correo=input("Favor de ingresar el correo: ")
            per.sueldo=int(input("Favor de ingresar el sueldo: "))
  
        indice+=1  

    input()

def HobiPersonas():
    os.system("cls")      
    print("Hobbis de Persona:")

    ListarPersonas(0)

    rutHobbi=int(input("Favor de ingresar el rut a ingresar los Hobbi's: "))

    indice=0
    for per in listPersonas:
        if per.rut==rutHobbi:
            
            while(True):
                hobbi=input("Ingrese el hobbi nº "+str(len(per.hobis)+1) +" de la persona (Presione enter para terminar): ")
                if hobbi!= "":
                    per.hobis.append(hobbi)
                else:
                    break
  
        indice+=1  

    input()



# p1=Persona(11111,"Carlos Alvarez","Admin",[],8712683712,"carlos@carlos.cl",50000)
# p2=Persona(22222,"Benjamin","Jefe",[],21372198,"benja@benja.cl",150000)
# p3=Persona(33333,"Lucho","Informatico",[],687123871,"lucho@lucho.cl",800000)

# listPersonas.append(p1)
# listPersonas.append(p2)
# listPersonas.append(p3)

listPersonas=[
    Persona(11111,"Carlos Alvarez","Admin",[],8712683712,"carlos@carlos.cl",50000),   
    Persona(22222,"Benjamin","Jefe",[],21372198,"benja@benja.cl",150000),
    Persona(33333,"Lucho","Informatico",[],687123871,"lucho@lucho.cl",800000)
]   

while(True):
    os.system("cls")
    print("Bienvenido a Sistema de mantención de usuarios")
    print("Seleccione una de las tareas a realizar:")
    print(" 1) Insertar personas")
    print(" 2) Listar personas")
    print(" 3) ELiminar personas")
    print(" 4) Modificar personas")
    print(" 5) Ingresar Hobi's")
    print(" 0) Salir\n")

    opcMenu=input() 

    if (opcMenu=="1"):
        IngresarPersona()
    elif (opcMenu=="2"):
        ListarPersonas(1)
    elif (opcMenu=="3"):
        EliminarPersonas()
    elif (opcMenu=="4"):
        ModificarPersonas()
    elif (opcMenu=="5"):
        HobiPersonas()
    elif (opcMenu=="0"):
        print ("Muchas Gracias")
        break
    else:
        os.system("cls")
        print("Opcion no valida.")
        input()
        


# Atributos (Datos asociados al objeto)
# Metodos (Funciones, o actos que realiza este objeto)
# Clase: Molde 

# PersonaCarlos=Carlos, 11111111-1,ADministrador,[ver peliculas,jugar, estudiar, leer],17239812,carlos@incap.cl
# PersonaBenjamin=Benjamin,222222,Jefe,[Jugar],187929831,benja@benja.cl

# CRUD de personas (Directorio de personas)::atributos(rut,nombreApellido,tipoUsuario,hobi's,fono,correo)
# Crear (formulario),listar, leer los datos en particular de la persona, eliminar y modificar
# Menu el cual me permita seleccionar una de las opciones descrita anteriormente.
# se almacena en listas 
