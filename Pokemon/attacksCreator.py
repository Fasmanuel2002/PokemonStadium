from .PokemonType import Type

attacks = [
    # FIRE type moves (IDs 1-8)
    (1,  "Ember",           Type.FIRE,  40, 100, 25),
    (2,  "Flamethrower",     Type.FIRE,  90, 100, 15),
    (3,  "Fire Blast",       Type.FIRE, 110,  85,  5),
    (4,  "Heat Wave",        Type.FIRE,  95,  90, 10),
    (5,  "Inferno",          Type.FIRE, 100,  75,  5),
    (6,  "Fire Punch",       Type.FIRE,  75, 100, 15),
    (7,  "Blaze Kick",       Type.FIRE,  85,  90, 10),
    (8,  "Flame Charge",     Type.FIRE,  50, 100, 20),

    # WATER type moves (IDs 9-16)
    (9,  "Water Gun",        Type.WATER,  40, 100, 25),
    (10, "Bubble Beam",      Type.WATER,  65, 100, 20),
    (11, "Hydro Pump",       Type.WATER, 110,  80,  5),
    (12, "Surf",             Type.WATER,  90, 100, 15),
    (13, "Aqua Tail",        Type.WATER,  90,  90, 10),
    (14, "Waterfall",        Type.WATER,  80, 100, 15),
    (15, "Muddy Water",      Type.WATER,  90,  90, 10),
    (16, "Scald",            Type.WATER,  80, 100, 15),

    # PLANT type moves (IDs 17-24)
    (17, "Vine Whip",        Type.PLANT,  45, 100, 25),
    (18, "Razor Leaf",       Type.PLANT,  55,  95, 25),
    (19, "Solar Beam",       Type.PLANT, 120, 100, 10),
    (20, "Leaf Blade",       Type.PLANT,  70, 100, 15),
    (21, "Seed Bomb",        Type.PLANT,  80, 100, 15),
    (22, "Petal Dance",      Type.PLANT, 120, 100, 10),
    (23, "Bullet Seed",      Type.PLANT,  25, 100, 30),
    (24, "Giga Drain",       Type.PLANT,  75, 100, 10),

    # ELECTRIC type moves (IDs 25-32)
    (25, "Thunder Shock",    Type.ELECTRIC, 40, 100, 30),
    (26, "Thunderbolt",      Type.ELECTRIC, 90, 100, 15),
    (27, "Thunder",          Type.ELECTRIC,110,  70, 10),
    (28, "Spark",            Type.ELECTRIC, 65, 100, 20),
    (29, "Volt Tackle",      Type.ELECTRIC,120, 100, 15),
    (30, "Discharge",        Type.ELECTRIC, 80, 100, 15),
    (31, "Charge Beam",      Type.ELECTRIC, 50,  90, 10),
    (32, "Electro Ball",     Type.ELECTRIC, 60, 100, 10),

    # AIR type moves (IDs 33-40)
    (33, "Gust",             Type.AIR,  40, 100, 35),
    (34, "Wing Attack",      Type.AIR,  60, 100, 35),
    (35, "Air Cutter",       Type.AIR,  60,  95, 25),
    (36, "Air Slash",        Type.AIR,  75,  95, 15),
    (37, "Sky Attack",       Type.AIR, 140,  90,  5),
    (38, "Feather Dance",    Type.AIR,   0, 100, 15),
    (39, "Tailwind",         Type.AIR,   0, 100, 20),
    (40, "Aeroblast",        Type.AIR, 100,  95,  5),

    # FIGHTING type moves (IDs 41-48)
    (41, "Karate Chop",      Type.FIGHTING, 50, 100, 25),
    (42, "Double Kick",      Type.FIGHTING, 30, 100, 30),
    (43, "Low Kick",         Type.FIGHTING, 50, 100, 20),
    (44, "Mega Kick",        Type.FIGHTING,120,  75,  5),
    (45, "Brick Break",      Type.FIGHTING, 75, 100, 15),
    (46, "Close Combat",     Type.FIGHTING,120, 100,  5),
    (47, "Focus Punch",      Type.FIGHTING,150, 100, 20),
    (48, "Dynamic Punch",    Type.FIGHTING,100,  50,  5),

    # POISON type moves (IDs 49-56)
    (49, "Poison Sting",     Type.POISON, 15, 100, 35),
    (50, "Acid",             Type.POISON, 40, 100, 30),
    (51, "Sludge",           Type.POISON, 65, 100, 20),
    (52, "Poison Gas",       Type.POISON,  0,  90, 40),
    (53, "Gunk Shot",        Type.POISON, 80,  80, 10),
    (54, "Toxic",            Type.POISON,  0,  90, 10),
    (55, "Venoshock",        Type.POISON, 65, 100, 20),
    (56, "Acid Spray",       Type.POISON, 40, 100, 20),

    # GROUND type moves (IDs 57-64)
    (57, "Mud-Slap",         Type.GROUND, 20, 100, 10),
    (58, "Dig",              Type.GROUND, 80, 100, 10),
    (59, "Earthquake",       Type.GROUND,100, 100, 10),
    (60, "Magnitude",        Type.GROUND, 80, 100, 30),
    (61, "Bulldoze",         Type.GROUND, 60, 100, 20),
    (62, "Sand Tomb",        Type.GROUND, 35,  85, 15),
    (63, "Fissure",          Type.GROUND,  0,  30,  5),  # One-hit KO style
    (64, "Mud Bomb",         Type.GROUND, 65,  85, 10),

    # FLYING type moves (IDs 65-72)
    (65, "Gust",             Type.FLYING, 40, 100, 35),
    (66, "Wing Attack",      Type.FLYING, 60, 100, 35),
    (67, "Air Cutter",       Type.FLYING, 60,  95, 25),
    (68, "Air Slash",        Type.FLYING, 75,  95, 15),
    (69, "Sky Attack",       Type.FLYING,140,  90,  5),
    (70, "Brave Bird",       Type.FLYING,120, 100, 15),
    (71, "Peck",             Type.FLYING, 35, 100, 35),
    (72, "Aerial Ace",       Type.FLYING, 60, 100, 20),

    # PSYCHIC type moves (IDs 73-80)
    (73, "Confusion",        Type.PSYCHIC, 50, 100, 25),
    (74, "Psychic",          Type.PSYCHIC, 90, 100, 10),
    (75, "Psybeam",          Type.PSYCHIC, 65, 100, 20),
    (76, "Zen Headbutt",     Type.PSYCHIC, 80,  90, 15),
    (77, "Future Sight",     Type.PSYCHIC,120, 100, 10),
    (78, "Psyshock",         Type.PSYCHIC, 80, 100, 15),
    (79, "Extrasensory",     Type.PSYCHIC, 80, 100, 20),
    (80, "Mind Bend",        Type.PSYCHIC, 70,  95, 15),

    # #BUG type moves (IDs 81-88)
    (81, "Bug Bite",         Type.BUG,  40, 100, 20),
    (82, "String Shot",      Type.BUG,   0,  95, 40),
    (83, "Leech Life",       Type.BUG,  80, 100, 10),
    (84, "Silver Wind",      Type.BUG,  60, 100,  5),
    (85, "X-Scissor",        Type.BUG,  80, 100, 15),
    (86, "Bug Buzz",         Type.BUG,  90, 100, 10),
    (87, "Signal Beam",      Type.BUG,  75, 100, 15),
    (88, "Fury Cutter",      Type.BUG,  40,  95, 20),

    # ROCK type moves (IDs 89-96)
    (89, "Rock Throw",       Type.ROCK,  50,  90, 15),
    (90, "Rock Slide",       Type.ROCK,  75,  90, 10),
    (91, "Stone Edge",       Type.ROCK, 100,  80,  5),
    (92, "Rock Blast",       Type.ROCK,  25,  90, 10),
    (93, "Rock Tomb",        Type.ROCK,  60,  95, 15),
    (94, "Smack Down",       Type.ROCK,  50, 100, 15),
    (95, "Head Smash",       Type.ROCK, 150,  80,  5),
    (96, "Rollout",          Type.ROCK,  30,  90, 20),

    # GHOST type moves (IDs 97-104)
    (97, "Lick",             Type.GHOST,  30, 100, 30),
    (98, "Night Shade",       Type.GHOST,  80, 100, 15),
    (99, "Shadow Ball",       Type.GHOST,  80, 100, 15),
    (100,"Shadow Punch",      Type.GHOST,  60, 100, 20),
    (101,"Hex",               Type.GHOST,  65, 100, 10),
    (102,"Phantom Force",     Type.GHOST,  90, 100, 10),
    (103,"Curse",             Type.GHOST,   0,  90, 10),
    (104,"Astonish",          Type.GHOST,  30, 100, 15),

    # NORMAL type moves (IDs 105-112)
    (105,"Tackle",            Type.NORMAL, 40, 100, 35),
    (106,"Scratch",           Type.NORMAL, 40, 100, 35),
    (107,"Quick Attack",      Type.NORMAL, 40, 100, 30),
    (108,"Hyper Beam",        Type.NORMAL,150,  90,  5),
    (109,"Body Slam",         Type.NORMAL, 85, 100, 15),
    (110,"Take Down",         Type.NORMAL, 90,  85, 20),
    (111,"Double-Edge",       Type.NORMAL,120, 100, 15),
    (112,"Struggle",          Type.NORMAL, 50, 100,  1),

    # FAIRY type moves (IDs 113-120)
    (113,"Fairy Wind",        Type.FAIRY, 40, 100, 35),
    (114,"Moonblast",         Type.FAIRY, 95, 100, 15),
    (115,"Dazzling Gleam",    Type.FAIRY, 80, 100, 10),
    (116,"Draining Kiss",     Type.FAIRY, 50, 100, 10),
    (117,"Play Rough",        Type.FAIRY, 90,  90, 10),
    (118,"Mystical Fire",     Type.FAIRY, 75, 100, 15),
    (119,"Sparkle Strike",    Type.FAIRY, 65, 100, 15),
    (120,"Charm",             Type.FAIRY,  0, 100, 20)
]
