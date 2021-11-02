"""
        - Listado de todos los tipos de POKEMON de acuerdo a la colección POKEDEX de BULBAGARDEN 
        - Creditos:
    
                https://bulbagarden.net/  
                        &
                  https://pokeapi.co/
    
    
        ** 18 TIPOS DE POKEMON  + ESTRUCTURADOR MAESTRO (POKEMON) **
"""

import random as rd

# Contrincante #1

dueloNombreMaestro1=[]
dueloNombrePokemon1=[]
dueloMovimientos1=[]
dueloVariacionVida1=[]
dueloCoinWiner1=0 

# Contrincante #2
dueloNombreMaestro2=[]
dueloNombrePokemon2=[]
dueloMovimientos2=[]
dueloVariacionVida2=[]
dueloCoinWiner2=0 

class Pokemon:
    
    def __init__(self,identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza):
        
        #Atributos del objeto "Pokemon"
        self.id=identificadorPokemon #ID de Pokemon
        self.nombre=nombrePokemon  # Nombre
        self.abilities=abilities #Habilidades
        self.tipo=tipoPokemon  #Tipo de Pokemon
        self.health=int(100)
        self.pAtaque=pAtaque
        self.debilidad=debilidad
        self.fortaleza=fortaleza
        
        #Métodos
        
    def mostrarInfoPokemon(self):
        print (f"1) Pokedex ID: {str(self.id [0][0])} \n2) Nombre: {str(self.nombre [0][0])} \n3) Habilidad:  {str(self.abilities [0][0])} \n4) Tipo:  {str(self.tipo [0][0])}\n5) Puntos de vida: {self.health} \n6) Puntos de ataque: {self.pAtaque}\n\n")
        
    def mostrarInfoDuelo(self):
        print (f"1) Pokedex ID: {str(self.id [0][0])} \n2) Nombre: {str(self.nombre [0][0])} \n3) Habilidad:  {str(self.abilities [0][0])} \n4) Tipo:  {str(self.tipo [0][0])}\n5) Puntos de vida: {self.health} \n6) Puntos de ataque: {self.pAtaque} \n\n")
        
    def mostrarNombrePokemon(self):
        print(f"Nombre: {str(self.nombre[0][0])}")

    
            
class datosDuelo:
    
    def __init__(self, nombreEntrenador, nombrePokemonDuelo):
        
        self.nombreEntrenador=nombreEntrenador
        self.nombrePokemonduelo=nombrePokemonDuelo
 
        
    def mostrarDatosDuelo(self):
        print(f"1) Nombre Entrenador: {self.nombreEntrenador} \n 2) Pokemon seleccionado: {self.nombrePokemonduelo}")
                     
                   
                            
            
class tipoNormal(Pokemon): #1
    def __init__(self,identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza, MegaGolpe):
        super().__init__(identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza)
        self.ataqueNormal=MegaGolpe
    def esquivarGhost(self):
        if self.tipo == "ghost":
            print("Tipo1: ",self.tipo)
            print(f"El pokemon {self.nombre} del tipo {self.tipo} ha esquivado GHOST")
    
        

class tipoLucha(Pokemon): #2
    def __init__(self,identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza, TriplePatada):
        super().__init__(identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza)
        self.ataqueFighting=TriplePatada
    def esquivarRock(self):
        if self.tipo == "rock":

            print(f"El pokemon {self.nombre} del tipo {self.tipo} ha esquivado ROCK")

        
class tipoVolador(Pokemon): #3
    def __init__(self,identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza, AeroBlast):
        super().__init__(identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza)
        self.ataqueFlying=AeroBlast
    def esquivarBug(self):
        if self.tipo == "bug":
            
            print(f"El pokemon {self.nombre} del tipo {self.tipo} ha esquivado INSECTO")


class tipoVeneno(Pokemon): #4
    def __init__(self,identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza, PoisonSting):
        super().__init__(identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza)
        self.ataquePoison=PoisonSting
    def esquivarFlying(self):
        if self.tipo == "flying" :
            
            print(f"El pokemon {self.nombre} del tipo {self.tipo} ha esquivado VOLADOR")
 
        
class tipoTierra(Pokemon): #5
    def __init__(self,identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza, EarthQuake):
        super().__init__(identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza)
        self.ataqueTierra=EarthQuake
    def esquivarElectric(self):
        if self.tipo == "electric":
            
            print(f"El pokemon {self.nombre} del tipo {self.tipo} ha esquivado ELECTRIC")
  
        
class tipoRoca(Pokemon): #6
    def __init__(self,identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza, DiamondStorm):
        super().__init__(identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza)
        self.ataqueRoca=DiamondStorm
    def esquivarFighting(self):
        if self.tipo == "fighting":
            
            print(f"El pokemon {self.nombre} del tipo {self.tipo} ha esquivado FIGHTING")
 
        
class tipoBicho(Pokemon): #7
    def __init__(self,identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza, SpiderWeb):
        super().__init__(identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza)
        self.ataqueBicho=SpiderWeb
    def esquivarGround(self):
        if self.tipo == "ground":
            
            print(f"El pokemon {self.nombre} del tipo {self.tipo} ha esquivado GROUND")
  
        
class tipoFantasma(Pokemon): #8
    def __init__(self,identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza, Nightmare):
        super().__init__(identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza)
        self.ataqueFantasma=Nightmare
    def esquivarNormal(self):
        if self.tipo == "normal":
            
            print(f"El pokemon {self.nombre} del tipo {self.tipo} ha esquivado NORMAL")

        
class tipoHierro(Pokemon): #9
    def __init__(self,identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza, MetalClaw):
        super().__init__(identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza)
        self.ataqueHierro=MetalClaw
    def esquivarVeneno(self):
        if self.tipo == "poison":
            
            print(f"El pokemon {self.nombre} del tipo {self.tipo} ha esquivado POISON")
 

class tipoFuego(Pokemon): #10
    def __init__(self,identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza, RafagaFuego):
        super().__init__(identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza)
        self.ataqueFuego=RafagaFuego
    def esquivarfairy(self):
        if self.tipo == "fairy":
            
            print(f"El pokemon {self.nombre} del tipo {self.tipo} ha esquivado FAIRY")


class tipoAgua(Pokemon): #11
    def __init__(self,identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza, hidroBomba):
        super().__init__(identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza)
        self.ataqueAgua=hidroBomba
    def esquivarFuego(self):
        if self.tipo == "fire":
            
            print(f"El pokemon {self.nombre} del tipo {self.tipo} ha esquivado FUEGO")
 
        

class tipoHierva(Pokemon): #12
    def __init__(self,identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza, AtaqueSolar):
        super().__init__(identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza)
        self.ataqueHierba=AtaqueSolar
    def esquivarAgua(self):
        if self.tipo == "water":
            
            print(f"El pokemon {self.nombre} del tipo {self.tipo} ha esquivado AGUA")
        
                
class tipoElectrico(Pokemon): #13
    def __init__(self,identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza, Thunderbolt):
        super().__init__(identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza)
        self.ataqueElectrico=Thunderbolt
    def esquivarSteel(self):
        if self.tipo == "steel":
            
            print(f"El pokemon {self.nombre} del tipo {self.tipo} ha esquivado HIERRO")
   
        
class tipoPsiquico(Pokemon): #14
    def __init__(self,identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza, Hypnosis):
        super().__init__(identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza)
        self.ataquePsiquico=Hypnosis
    def esquivarDark(self):
        if self.tipo == "dark":
            
            print(f"El pokemon {self.nombre} del tipo {self.tipo} ha esquivado DARK")
   
        
class tipoHielo(Pokemon): #15
    def __init__(self,identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza, Avalanche):
        super().__init__(identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza)
        self.ataqueHielo=Avalanche
    def esquivarHielo(self):
        if self.tipo == "ice":
            
            print(f"El pokemon {self.nombre} del tipo {self.tipo} ha esquivado HIELO")
    
class tipoDragon(Pokemon): #16
    def __init__(self,identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza, Twister):
        super().__init__(identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza)
        self.ataqueDragon=Twister
    def esquivarHierba(self):
        if self.tipo == "grass":
            
            print(f"El pokemon {self.nombre} del tipo {self.tipo} ha esquivado HIERBA")
   
        
class tipoDark(Pokemon): #17
    def __init__(self,identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza, NightSlash):
        super().__init__(identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza)
        self.ataqueDark=NightSlash
    def esquivarPsiquico(self):
        if self.tipo == "dark":
            
            print(f"El pokemon {self.nombre} del tipo {self.tipo} ha esquivado DARK")
   
        
class tipoHada(Pokemon): #18
    def __init__(self,identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza, Moonlight):
        super().__init__(identificadorPokemon,nombrePokemon,abilities,tipoPokemon,pAtaque,debilidad,fortaleza)
        self.ataqueHada=Moonlight
    def esquivarDragon(self):
        if self.tipo == "dragon":
            
            print(f"El pokemon {self.nombre} del tipo {self.tipo} ha esquivado DRAGON")

