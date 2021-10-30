#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functions import * 
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
    
    def __init__(self,nombrePokemon,identificadorPokemon,puntosVidaPokemon,puntoAtaquePokemon,tipoPokemon,debilidad,fortaleza):
        self.nombre=nombrePokemon  
        self.id=identificadorPokemon  
        self.pSalud=puntosVidaPokemon  
        self.pAtaque=puntoAtaquePokemon
        self.tipo=tipoPokemon  
        self.debilidad=debilidad 
        self.fortaleza=fortaleza
        
    def mostrarInfoPokemon(self):
        print (f"1: {self.nombre}2: {self.id} 3: {self.pSalud} 4:{self.pAtaque} 5: {self.tipo} 6: {self.debilidad}7: {self.fortaleza}")
        
        
primerPokemon=[]
def crearRegistros1(pokemon1_name):
    
    if len(primerPokemon)==0:
        for i in pokemon1_name:
            primerPokemon.append(i)
        print("Registro de Pokemon #1 agregado satisfactoriamente")
        time.sleep(1)
        #print(primerPokemon)
    else:
        print("No es posible sobreescribir datos de Pokemon #1")
        time.sleep(1)  
        #print("Lista primer pokemon: ",primerPokemon)

segundoPokemon=[]    
def crearRegistros2(pokemon1_name):
    
    if len(segundoPokemon)==0:
        for i in pokemon1_name:
            segundoPokemon.append(i)
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
        pass
    else:
        mostrarInfoPokemon()
        print(primerPokemon)
        print(segundoPokemon)
        
            
Pokemon(primerPokemon)
Pokemon(segundoPokemon)
    


    
        
while (True):
    print("Seleccione una de las tareas a realizar:")
    print("1) Pokedex")
    print("2) Duelo Pokemon")
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
            pass
            
        elif (opcMenu=="4"):
            #Eliminar Datos
            pass
        elif (opcMenu=="0"):
            #Salir
            pass
        else:
            pass
        
               

        
        
    elif(pokeMenu==2):
        print(primerPokemon)
        print(segundoPokemon)
        input()
            
    elif(pokeMenu==0):
        #Salir
        break





        


if __name__ == '__main__':
    get_pokemon_data1(url1)
    print(get_pokemon_data1(url1)) 
    get_pokemon_data1(url2)
    print(get_pokemon_data1(url2)) 
    

