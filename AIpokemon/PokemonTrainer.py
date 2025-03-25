from Pokemon import ClassPokemon as Pokemon


class Trainer:
    def __init__(self):
        self.team = [None, None, None]
        self.token = None #what is turn
        self.isIA = False
        
        
        
    










class TrainerAI:
    def __init__(self):
        self.teamIA = [None,None,None]
        self.token = None
        self.isIA = True


class RandomAI(TrainerAI):
    ...



class MinimaxAI(TrainerAI):
    ...


class MMAlphaBetaAI(MinimaxAI):
    ...
    


class ExpectiMaxAI(MinimaxAI):
    ...