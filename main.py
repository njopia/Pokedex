#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from functions import * 
import requests
import os
import time

clear=os.system("cls")
import random as rd

rand1=rd.randint(1,400)
varia1=str(rand1)
rand2=rd.randint(1,400)
varia2=str(rand2)

url1 ='https://pokeapi.co/api/v2/pokemon/'+varia1
url2 ='https://pokeapi.co/api/v2/pokemon/'+varia2

#Variables separadas de Pokemon 1
id1=[]
name1=[]
abilitie1=[]
type1=[]

#Variables separadas de Pokemon 2
id2=[]
name2=[]
abilitie2=[]
type2=[]

 
#def get_pokemon_data1(url='https://pokeapi.co/api/v2/pokemon/'+varia):
def get_pokemon_data1(url):
    pokemon1_id=[]
    pokemon1_name=[]
    pokemon1_abilities=[]
    pokemon1_type=[]
    
    response = requests.get(url)
    if response.status_code == 200:
        payload = response.json()
        
    #Obtener ID de pokemon
        getID = payload.get('id', [])
        pokemon1_id.append(getID)
            

    #Obtener nombre de pokemon
        results = payload.get('forms', [])
        if results:
            for pokemon in results:
                name = pokemon['name']
                pokemon1_name.append(name)
            #print(pokemon1_name)

            
                        
    #Obtener habilidad del pokemon
        results = payload.get('abilities', [])
        if results:
            for abilities_nest in results:
                skills = abilities_nest['ability']
                habilidades=skills.get('name')
                pokemon1_abilities.append(habilidades)    
             
            #print(pokemon1_abilities)

            
    #Obtener tipo del pokemon
        results = payload.get('types', [])
        #print(results)
        for type_nest1 in results:
            type_nest1_1 = type_nest1['type']
            type_pokemon=type_nest1_1.get('name')
            pokemon1_type.append(type_pokemon)  
            return pokemon1_id, pokemon1_name,pokemon1_abilities,pokemon1_type 
                
      
class Pokemon:
    
    def __init__(self,identificadorPokemon,nombrePokemon,abilities,tipoPokemon):
        
        self.id=identificadorPokemon
        self.nombre=nombrePokemon  
        self.abilities=abilities
        self.tipo=tipoPokemon  
        

    def mostrarInfoPokemon(self):
        print (f"1) Pokedex ID: {str(self.id [0][0])} \n2) Nombre: {str(self.nombre [0][0])} \n3) Habilidad:  {str(self.abilities [0][0])} \n4) Tipo:  {str(self.tipo [0][0])} \n \n")


    
        
primerPokemon=[]
def crearRegistros1(pokemon1_name):
    if len(primerPokemon)==0:
        for i in pokemon1_name:
            primerPokemon.append(i)
            id1.append(i)
            name1.append(i)
            abilitie1.append(i)
            type1.append(i)
        for i in range(3):    
            id1.pop()
        for i in range(2):    
            name1.pop()
        abilitie1.pop()
        del name1[0]
        del abilitie1[0:2]
        del type1[0:3]

        print("Registro de Pokemon #1 agregado satisfactoriamente")
        time.sleep(1)
        #print(primerPokemon)
    else:
        print("No es posible sobreescribir datos de Pokemon #1")
        time.sleep(1)  
        #print("Lista primer pokemon: ",primerPokemon)

segundoPokemon=[] 
def crearRegistros2(pokemon1_name):
    
    """ No vean estas proximas lineas . NO EXISTEN """
    if len(segundoPokemon)==0:
        for i in pokemon1_name:
            segundoPokemon.append(i)
            id2.append(i)
            name2.append(i)
            abilitie2.append(i)
            type2.append(i)
        for i in range(3):    
            id2.pop()
        for i in range(2):    
            name2.pop()
        abilitie2.pop()
        del name2[0]
        del abilitie2[0:2]
        del type2[0:3]
        """ Listo ahora pueden seguir viendo """
        
        print("Registro de Pokemon #2 agregado satisfactoriamente")
        time.sleep(1)
        #print(segundoPokemon)
    else:
        print("No es posible sobreescribir datos de Pokemon #2")
        time.sleep(1)    

    
    #print("Lista segundo pokemon: ",segundoPokemon)

def crearRegistros():
    crearRegistros1(get_pokemon_data1(url1))
    #print("Lista primer pokemon: ")
    
        
    crearRegistros2(get_pokemon_data1(url2))
    #print("Lista segundo pokemon: ")
    
def leerRegistros():
    if len(primerPokemon)== 0:
        print("Registros de Pokemones vacío. Ingrese datos primero.")
        time.sleep(3)
    else:
        for i in lista:
            i.mostrarInfoPokemon()           

        
lista=[
    Pokemon(id1, name1, abilitie1,type1),
    Pokemon(id2, name2, abilitie2,type2)
    ]

while (True):
    print("====MENU PRINCIPAL====")
    print("\nSeleccione una de las tareas a realizar:")
    print("1) Pokedex")
    print("0) Salir \n")
    
    pokeMenu=int(input())
    
    if(pokeMenu==1):
        
        print("Seleccione una de las tareas a realizar:\n")
        print(" 1) Crear registros")
        print(" 2) Listar datos")
        print(" 3) Modificar registros")
        print(" 4) Eliminar datos")
        print(" 0) SALIR\n")
        
        opcMenu=input()
        
        if (opcMenu=="1"):
            crearRegistros()
            
        elif (opcMenu=="2"):
            #Listar Datos
            leerRegistros()

                    
        elif (opcMenu=="3"):
            #Modificar Datos
            
            modificarDatos=int(input("Ingrese id a actualizar"))
            indice=0
            for per in lista:
                if per.id[0][0]==modificarDatos:
                    per.nombre[0][0]=input("Favor de ingresar el nombre: ")
                    per.abilities[0][0]=input("Favor de ingresar abilities : ")
                    per.tipo[0][0]=input("Favor de ingresar tipo ")
                    indice+=1  
            
        elif (opcMenu=="4"):
            #Eliminar Datos    
            print("Eliminar Persona:")

            rutELimina=int(input("Favor de ingresar el rut a eliminar: "))

            indice=0
            for per in lista:
                if per.id[0][0]==rutELimina:
                    lista.pop(indice)  
                    print(f"Los datos de {per.nombre[0][0]} han sido eliminados satisfactoriamente !!")
                indice+=1
                

            input()

        elif (opcMenu=="0"):
            #Salir
            pass
        else:
            pass
        
               

        
        
    elif(pokeMenu==2):
        pass
    elif(pokeMenu==0):
        #Salir
        break





        


if __name__ == '__main__':
    get_pokemon_data1(url1)
    print(get_pokemon_data1(url1)) 
    get_pokemon_data1(url2)
    print(get_pokemon_data1(url2)) 
    

