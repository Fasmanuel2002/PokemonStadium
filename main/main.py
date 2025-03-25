import sys
import os
import random
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Pokemon import ClassPokemon as cls
from CreatePokemons.PokemonType import Type
from AIpokemon.PokemonTrainer import *


def main():
    AIPlayer = pokemons()[0]
    Pokemons = pokemons()[1]
    pokemons_player = []
    pokemons_AI = []
    player = Trainer()
    AI = TrainerAI()
    print("Selects 3 Pokemons of the list")
    for poke in Pokemons:
        print(f"{poke} \n")
    
    for i in range(3):
        selection = int(input(f"{i+1}Pokemon: "))
        Single_Pokemon = choosePokemon(Pokemons, selection)
        pokemons_player.append(Single_Pokemon)
    
    player.team = pokemons_player
    print("Player Team")
    for poke in player.team:
        print(f"{poke}\n")

    
    #Selection for Pokemons for Ai
    for i in range(3):
        selectIA = random.randrange(1,80)
        SinlePokemon = choosePokemon(AIPlayer, selectIA)
        pokemons_AI.append(SinlePokemon)
    
    AI.team = pokemons_AI
    print("AI team")    
    for poke in AI.team:
        print(f"{poke}\n")
   
   
     
    """
    print("\n\n\nPokemons that you Selected")
    for poke in pokemons_player:
        print(f"{poke}\n")
    
    print("\n\n\nThese is the first Pokemon of the AI")    
    #for pokeIA in pokemons_AI:
    #   print(f"{pokeIA}\n")
    selectIAfirst = random.choice(pokemons_AI)
    print(selectIAfirst.NamePokemon)
    
    
    pokemon_to_use = int(input("Select First pokemon"))
    print(f"{pokemons_player[pokemon_to_use]}")
    
    #First Fight
    fightPokemons(selectIAfirst, pokemons_player,pokemon_to_use)
    AIPlayer.remove(selectIAfirst)
    print(f"This pokemon has fainted {selectIAfirst.NamePokemon}")
    
    
    print("\n\n\nThese is the second Pokemon of the AI")
    selectIASecond = random.choice(pokemons_AI)
    print(selectIASecond.NamePokemon)
    
    #Second Fight
    fightPokemons(selectIASecond, pokemons_player,pokemon_to_use)
    AIPlayer.remove(selectIASecond)
    print(f"This pokemon has fainted {selectIASecond.NamePokemon}")
    
    
    #Third Fight
    print("\n\n\nThese is the Third Pokemon of the AI")
    selectIAThird = random.choice(pokemons_AI)
    print(selectIAThird.NamePokemon)
    
    
    fightPokemons(selectIAThird, pokemons_player,pokemon_to_use)
    print(f"This pokemon has fainted {selectIAThird.NamePokemon}")
    
    print("PLAYERS WINS")
    
"""   
    
    

def pokemons():
    pokemons = [
    cls.Pokemon(1, "Pikachu", 35, 55, 40, 90, Type.ELECTRIC.value),
    cls.Pokemon(2, "Eevee", 55, 50, 50, 55, Type.FIRE.value),
    cls.Pokemon(3, "Charmander", 39, 52, 43, 65, Type.FIRE.value),
    cls.Pokemon(4, "Bulbasaur", 45, 49, 49, 45, Type.PLANT.value),
    cls.Pokemon(5, "Squirtle", 44, 48, 65, 43, Type.WATER.value),
    cls.Pokemon(6, "Wartortle", 59, 63, 80, 58, Type.WATER.value),
    cls.Pokemon(7, "Blastoise", 79, 83, 100, 78, Type.WATER.value),
    cls.Pokemon(8, "Caterpie", 45, 30, 35, 45, Type.BUG.value),
    cls.Pokemon(9, "Metapod", 50, 20, 55, 30, Type.BUG.value),
    cls.Pokemon(10, "Butterfree", 60, 45, 50, 70, Type.BUG.value),
    cls.Pokemon(11, "Weedle", 40, 35, 30, 50, Type.POISON.value),
    cls.Pokemon(12, "Kakuna", 45, 25, 50, 35, Type.POISON.value),
    cls.Pokemon(13, "Beedrill", 65, 90, 40, 75, Type.POISON.value),
    cls.Pokemon(14, "Pidgey", 40, 45, 40, 56, Type.AIR.value),
    cls.Pokemon(15, "Pidgeotto", 63, 60, 55, 71, Type.AIR.value),
    cls.Pokemon(16, "Pidgeot", 83, 80, 75, 101, Type.AIR.value),
    cls.Pokemon(17, "Rattata", 30, 56, 35, 72, Type.NORMAL.value),
    cls.Pokemon(18, "Raticate", 55, 81, 60, 97, Type.NORMAL.value),
    cls.Pokemon(19, "Spearow", 40, 60, 30, 70, Type.AIR.value),
    cls.Pokemon(20, "Fearow", 65, 90, 65, 100, Type.AIR.value),
    cls.Pokemon(21, "Ekans", 35, 60, 44, 55, Type.POISON.value),
    cls.Pokemon(22, "Arbok", 60, 85, 69, 80, Type.POISON.value),
    cls.Pokemon(23, "Pikachu", 35, 55, 40, 90, Type.ELECTRIC.value),
    cls.Pokemon(24, "Sandshrew", 50, 75, 85, 40, Type.GROUND.value),
    cls.Pokemon(25, "Sandslash", 75, 100, 110, 65, Type.GROUND.value),
    cls.Pokemon(26, "Nidoran♀", 55, 47, 52, 41, Type.POISON.value),
    cls.Pokemon(27, "Nidorina", 70, 62, 67, 56, Type.POISON.value),
    cls.Pokemon(28, "Nidoqueen", 90, 82, 87, 76, Type.POISON.value),
    cls.Pokemon(29, "Nidoran♂", 46, 57, 40, 50, Type.POISON.value),
    cls.Pokemon(30, "Nidorino", 61, 62, 55, 65, Type.POISON.value),
    cls.Pokemon(31, "Nidoking", 81, 102, 77, 85, Type.POISON.value),
    cls.Pokemon(32, "Clefairy", 70, 45, 48, 35, Type.FAIRY.value),
    cls.Pokemon(33, "Clefable", 95, 70, 73, 60, Type.FAIRY.value),
    cls.Pokemon(34, "Vulpix", 38, 41, 40, 65, Type.FIRE.value),
    cls.Pokemon(35, "Ninetales", 73, 76, 75, 100, Type.FIRE.value),
    cls.Pokemon(36, "Jigglypuff", 115, 45, 20, 20, Type.FAIRY.value),
    cls.Pokemon(37, "Wigglytuff", 140, 70, 45, 45, Type.FAIRY.value),
    cls.Pokemon(38, "Zubat", 40, 45, 35, 50, Type.POISON.value),
    cls.Pokemon(39, "Golbat", 75, 80, 70, 90, Type.POISON.value),
    cls.Pokemon(40, "Oddish", 45, 50, 55, 30, Type.PLANT.value),
    cls.Pokemon(41, "Gloom", 60, 65, 70, 40, Type.PLANT.value),
    cls.Pokemon(42, "Vileplume", 75, 80, 85, 50, Type.PLANT.value),
    cls.Pokemon(43, "Paras", 35, 70, 55, 25, Type.BUG.value),
    cls.Pokemon(44, "Parasect", 60, 95, 80, 30, Type.BUG.value),
    cls.Pokemon(45, "Venonat", 60, 55, 50, 45, Type.BUG.value),
    cls.Pokemon(46, "Venomoth", 70, 65, 60, 90, Type.BUG.value),
    cls.Pokemon(47, "Diglett", 10, 55, 25, 95, Type.GROUND.value),
    cls.Pokemon(48, "Dugtrio", 35, 80, 50, 120, Type.GROUND.value),
    cls.Pokemon(49, "Meowth", 40, 45, 35, 90, Type.NORMAL.value),
    cls.Pokemon(50, "Persian", 65, 70, 60, 115, Type.NORMAL.value),
    cls.Pokemon(51, "Psyduck", 50, 52, 48, 55, Type.PSYCHIC.value),
    cls.Pokemon(52, "Golduck", 80, 82, 78, 85, Type.PSYCHIC.value),
    cls.Pokemon(53, "Mankey", 40, 80, 35, 70, Type.FIGHTING.value),
    cls.Pokemon(54, "Primeape", 65, 105, 60, 95, Type.FIGHTING.value),
    cls.Pokemon(55, "Growlithe", 55, 70, 45, 60, Type.FIRE.value),
    cls.Pokemon(56, "Arcanine", 90, 110, 80, 95, Type.FIRE.value),
    cls.Pokemon(57, "Poliwag", 40, 50, 40, 90, Type.WATER.value),
    cls.Pokemon(58, "Poliwhirl", 65, 65, 50, 90, Type.WATER.value),
    cls.Pokemon(59, "Politoed", 90, 75, 75, 70, Type.WATER.value),
    cls.Pokemon(60, "Abra", 25, 20, 15, 90, Type.PSYCHIC.value),
    cls.Pokemon(61, "Kadabra", 40, 35, 30, 105, Type.PSYCHIC.value),
    cls.Pokemon(62, "Alakazam", 55, 50, 45, 150, Type.PSYCHIC.value),
    cls.Pokemon(63, "Machop", 70, 80, 50, 35, Type.FIGHTING.value),
    cls.Pokemon(64, "Machoke", 80, 100, 70, 45, Type.FIGHTING.value),
    cls.Pokemon(65, "Machamp", 90, 130, 80, 55, Type.FIGHTING.value),
    cls.Pokemon(66, "Bellsprout", 50, 75, 35, 40, Type.PLANT.value),
    cls.Pokemon(67, "Weepinbell", 65, 90, 50, 55, Type.PLANT.value),
    cls.Pokemon(68, "Victreebel", 80, 105, 65, 70, Type.PLANT.value),
    cls.Pokemon(69, "Tentacool", 40, 40, 35, 70, Type.WATER.value),
    cls.Pokemon(70, "Tentacruel", 80, 70, 65, 100, Type.WATER.value),
    cls.Pokemon(71, "Geodude", 40, 80, 100, 20, Type.ROCK.value),
    cls.Pokemon(72, "Graveler", 55, 95, 115, 35, Type.ROCK.value),
    cls.Pokemon(73, "Golem", 80, 110, 130, 45, Type.ROCK.value),
    cls.Pokemon(74, "Ponyta", 50, 65, 40, 60, Type.FIRE.value),
    cls.Pokemon(75, "Rapidash", 65, 100, 70, 105, Type.FIRE.value),
    cls.Pokemon(76, "Slowpoke", 90, 65, 65, 15, Type.PSYCHIC.value),
    cls.Pokemon(77, "Slowbro", 95, 75, 110, 30, Type.PSYCHIC.value),
    cls.Pokemon(78, "Magnemite", 25, 35, 70, 45, Type.ELECTRIC.value),
    cls.Pokemon(79, "Magneton", 50, 60, 95, 70, Type.ELECTRIC.value),
    cls.Pokemon(80, "Farfetch'd", 52, 65, 55, 60, Type.NORMAL.value),
    
    ]
    pokemons_random1 = pokemons
    pokemon_random2 = random.sample(pokemons, 6)
    return (pokemons_random1, pokemon_random2)

def choosePokemon(List_Pokemons,number):
    for pokemon in List_Pokemons:
        if number == pokemon.NumPokedex:
            return pokemon


def actions():
    #The four attacks that it has
    ...

def fightPokemons(selectIAfirst, pokemons_player,pokemon_to_use):
    
    #Create iF and While, if the IA is more Rapid or not
    while(selectIAfirst.Hp > 0):
        print(pokemons_player[pokemon_to_use].attacks())
        choice = input("Attacks chose:")
        if choice in pokemons_player[pokemon_to_use].attacks():
            pokemon_attack = pokemons_player[pokemon_to_use].attacks()
            for attack, damage in pokemon_attack.items():
                if choice in attack:
                    damage_from = selectIAfirst.get_damage(pokemons_player[pokemon_to_use])
                    hp = (damage * damage_from)
                    selectIAfirst._Hp -= hp
                    print(selectIAfirst.Hp)
if __name__ == "__main__":
    main()