class Pokemon:
    def __init__(self, idAttack, NameAttack, typeAttack, damageAttack):
        self._idAttack = idAttack
        self._NameAttack = NameAttack
        self._typeAttack = typeAttack
        self._damageAttack = damageAttack
        
    @property
    def idAttack(self): #Getter
        return self._idAttack   
    
    @idAttack.setter
    def idAttack(self, newIdAttack):
        if isinstance(newIdAttack, int):
            self._idAttack = newIdAttack
        else:
            raise ValueError("Not Number")
    
    
    @property
    def NameAttack(self): #Getter
        return self._NameAttack   
    
    @NameAttack.setter
    def NameAttack(self, newNameAttack):
        if isinstance(newNameAttack, str):
            self._NameAttack = newNameAttack
        else:
            raise ValueError("Name must be a string")    
            
    
    @property
    def typeAttack(self): #Getter
        return self._typeAttack   
    
    @typeAttack.setter
    def typeAttack(self, newtypeAttack):
        if isinstance(newtypeAttack, int):
            self._typeAttack = newtypeAttack
        else:
            raise ValueError("Not Number")  
    
    @property
    def damageAttack(self): #Getter
        return self._damageAttack
    
    @damageAttack.setter
    def damageAttack(self, damageAttack):
        if isinstance(damageAttack, int):
            self._damageAttack = damageAttack
        else:
            raise ValueError("Not Number")
            

    def __str__(self):
        return f"this Attack id{self._idAttack} \n has this name {self._NameAttack} \n is this type: {self._typeAttack} and this damage {self._damageAttack}"
