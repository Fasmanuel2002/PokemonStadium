import random
attacks = {
                "Surf ": 90,
                "Hydro Pump": 110,
                "Surf": 40,
                "Aqua Tail":90
            }

choice, damate = random.choice(list(attacks.items()))

print(choice)