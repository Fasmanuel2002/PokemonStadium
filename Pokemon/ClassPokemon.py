from CreatePokemons import PokemonType
from CreatePokemons.PokemonType import Type

class Pokemon:
    def __init__(self, NumPokedex, NamePokemon, Hp, attack,defense, speed, pokemonType):
        self._NumPokedex = NumPokedex
        self._NamePokemon = NamePokemon
        self._Hp = Hp
        self._attack = attack
        self._defense = defense
        self._speed = speed
        self._pokemonType = pokemonType
        
        
        
    @property
    def NumPokedex(self): #Getter
        return self._NumPokedex   
    
    @NumPokedex.setter
    def NumPokedex(self, newPokedexNumber):
        if isinstance(newPokedexNumber, int):
            self._NumPokedex = newPokedexNumber
        else:
            raise ValueError("Not Number")
    
    
    @property
    def NamePokemon(self): #Getter
        return self._NamePokemon   
    
    @NamePokemon.setter
    def NamePokemon(self, newPokemonName):
        if isinstance(newPokemonName, str):
            self._NamePokemon = newPokemonName
        else:
            raise ValueError("Name must be a string")    
            
    
    @property
    def Hp(self): #Getter
        return self._Hp   
    
    @Hp.setter
    def Hp(self, newHP):
        if isinstance(newHP, int):
            self._Hp = newHP
        else:
            raise ValueError("Not Number")
            
    
    @property
    def attack(self): #Getter
        return self._attack   
    
    @attack.setter
    def attack(self, newAttack):
        if isinstance(newAttack, int):
            self._attack = newAttack
        else:
            raise ValueError("Not Number")
        
    
    @property
    def defense(self): #Getter
        return self._defense   
    
    @defense.setter
    def defense(self, newDefense):
        if isinstance(newDefense, int):
            self._defense = newDefense
        else:
            raise ValueError("Not Number")
    
    @property
    def speed(self): #Getter
        return self._speed   
    
    @speed.setter
    def speed(self, newSpeed):
        if isinstance(newSpeed, int):
            self._speed = newSpeed
        else:
            raise ValueError("Not Number")
            
    @property
    def pokemonType(self): #Getter
        return self._pokemonType   
    
    @pokemonType.setter
    def pokemonType(self, newPokemonType):
        if isinstance(newPokemonType, str):
            self._pokemonType = newPokemonType
        else:
            raise ValueError("Name must be a string")    
            
    
   
    def get_damage(self, other):
        return float((((2*50)/5 + 2) * (other.attack/self.defense)) / 50)
    
    def attacks(self):
        if self.pokemonType == "🔥":
            attacks = {
                "Flamethrower ": 90,
                "Fire Blast ": 110,
                "Ember ": 40,
                "Fire Punch ": 75
            }
            return attacks
        elif self.pokemonType == "💧":
            attacks = {
                "Surf ": 90,
                "Hydro Pump": 110,
                "Surf": 40,
                "Aqua Tail":90
            }
            return attacks
        elif self.pokemonType == "🏃":
            attacks = {
                "Body Slam": 85,
                "Hyper Beam": 150,
                "Quick Attack": 40,
                "Double-Edge":120
            }
            return attacks
        elif self.pokemonType == "⚡":
            attacks = {
                "Thunderbolt ": 90,
                "Thunder": 110,
                "Spark ": 65,
                "Shock Wave":60
            }
            return attacks
        elif self.pokemonType == "🌿":
            attacks = {
                "Tackle": 15,
                "Razor Leaf": 25,
                "Magical Leaf": 28,   
            }
            return attacks
        elif self.pokemonType == "🌪️":
            attacks = {
                "Aerial Ace": 60,
                "Wing Attack":60,
                "Air Slash": 75,
                "Drill Peck":80   
            }
            return attacks
        elif self.pokemonType == "🌍":
            attacks = {
                "Earthquake ":100,
                "Magnitude":80,
                "Mud Shot":55,
                "Bulldoze":60   
            }
            return attacks
        elif self.pokemonType == "☠️":
            attacks = {
                "Sludge Bomb": 90,
                "Poison Jab": 80,
                "Acid": 40,
                "Toxic": 90
            }
            return attacks
        elif self.pokemonType == "🔮":
            attacks = {
                "Psychic ": 90,
                "Psybeam ": 65,
                "Confusion": 50,
                "Future Sight": 120
            }
            return attacks
        elif self.pokemonType == "🐛":
            attacks = {
                "X-Scissor": 80,
                "Signal Beam": 75,
                "Bug Buzz": 90,
                "Silver Wind": 60
            }
            return attacks
        elif self.pokemonType == "💎":
            attacks = {
                "Rock Slide": 75,
                "Stone Edge": 100,
                "Rock Tomb": 60,
                "Ancient Power": 60
            }
            return attacks
        elif self.pokemonType == "🧚":
            attacks = {
                "Moonblast": 95,
                "Dazzling Gleam": 80 ,
                "Play Rough": 90,
                "Fairy Wind": 40
            }
            return attacks
        elif self.pokemonType == "👊🏻":
            attacks = {
                "Brick Break": 75 ,
                "Focus Punch": 150 ,
                "Low Kick": 75,
                "Mach Punch": 40
            }
            return attacks
        
            
        else: return f"Error Pokemon doesnt have type"
                

    def __str__(self):
        return f"Pokedex No: {self.NumPokedex}\t Name: {self.NamePokemon}\n Hp: {self.Hp}\t \t Attack: {self.attack}\n Defense: {self.defense}\t Speed: {self.speed}\n Type: {self.pokemonType}"

    def __repr__(self):
        return self.__str__()