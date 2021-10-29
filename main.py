#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functions import * 
import requests
import os

clear=os.system("cls")
import random as rd

rand=rd.randint(1,400)
varia=str(rand)


     
def get_pokemon_data1(url='https://pokeapi.co/api/v2/pokemon/'+varia):
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



def crearRegistros(pokemon1_name):
    primerPokemon=[]
    segundoPokemon=[]
    
    for i in pokemon1_name:
        primerPokemon.append(i)
    print("Lista primer pokemon: ",primerPokemon)
    
    get_pokemon_data1(url='https://pokeapi.co/api/v2/pokemon/'+varia)

    for i in pokemon1_name:
        segundoPokemon.append(i)
    print("Lista segundo pokemon: ",segundoPokemon)
    
    
while (True):
    print("Seleccione una de las tareas a realizar:")
    print("1) Pokedex")
    print("2) Duelo Pokemon")
    print("0) Salir \n")
    
    pokeMenu=int(input())
    
    if(pokeMenu==1):
        crearRegistros(get_pokemon_data1())

        
        
        
    elif(pokeMenu==2):

        input()
        
    elif(pokeMenu==0):
        #Salir
        break









if __name__ == '__main__':
    url ='https://pokeapi.co/api/v2/pokemon/'+varia
    get_pokemon_data1()
    
    
    

