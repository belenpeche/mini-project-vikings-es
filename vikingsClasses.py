import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        # your code here
    
    def attack(self):
        # your code here

    def receiveDamage(self, damage):
        # your code here
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here

    def battleCry(self):
        # your code here

    def receiveDamage(self, damage):
        # your code here

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super(). __init__(health, strength)
        

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health >0:
            return f"Un 'Saxon' ha recibido {damage} punto de daño"
        else:
            return f"Un 'Saxon' ha muerto en combate"

# Davicente

class War():
    def __init__(self):
        # your code here

    def addViking(self, viking):
        # your code here
    
    def addSaxon(self, saxon):
        # your code here
    
    def vikingAttack(self):
        # your code here
    
    def saxonAttack(self):
        # your code here

    def showStatus(self):
        # your code here
    pass

#yop
class War2:

    def __init__(self):
        # your code here

    def addViking(self, Viking):
        # your code here
    
    def addSaxon(self, Saxon):
        # your code here
    
    def vikingAttack(self):
        # your code here

    def saxonAttack(self):
        # your code here

    def showStatus(self):
        # your code here

    pass


