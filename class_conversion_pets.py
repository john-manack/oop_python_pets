class Pet:
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness
    
    def eat_food(self):
        self.fullness += 30
    
    def get_love(self):
        self.happiness += 30
    
    def be_alive(self):
        self.fullness -= self.hunger
        self.happines -= self.mopiness
    
    def __str__(self):
        return """
        %s:
        Fullness: %d
        Happiness: %d
        """ % (self.name, self.fullness, self.happiness)
        
class CuddlyPet(Pet):
    def __init__(self, name, fullness=50, hunger=5, cuddle_level=1):
        super().__init__(name, fullness, 100, hunger, 1)
        self.cuddle_level = cuddle_level
        
    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness/2
        
    def cuddle(self, other_pet):
        for i in range(self.cuddle_level):
            other_pet.get_love()

benji = Pet("Benji", 50, 20, 20, 1)
lassie = Pet("Lassie", 50, 20, 20, 1)
clifford = Pet("Old Yeller", 50, 20, 20, 1)

print(benji.mopiness)

nora = CuddlyPet("Nora", 50, 20, 20, 1)
cujo = Pet("Cujo", 50, 10, 30, 10)
print(cujo.happiness)
nora.cuddle(cujo)
print(cujo.happiness)
print(cujo)