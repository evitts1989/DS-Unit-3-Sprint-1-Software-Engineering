import random as r

# Product class
class Product:
    def __init__(self, name = None, price = 10, weight = 20,
                flammability = 0.5, identifier = r.randint(
                1000000,9999999)):
        
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier
    
    def stealability(self):
        ratio = self.price/self.weight
        if ratio < 0.5:
            return "Not so stealable..."
        elif ratio >= 0.5 and ratio < 1:
            return "Kinda stealable"
        else:
            return "Very stealable!"

    def explode(self):
        product = self.flammability * self.weight
        if product < 10:
            return "...fizzle"
        elif product >= 10 and product < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"

class BoxingGlove(Product):

    def __init__(self, name = None, price = 10, weight = 10,
                flammability = 0.5, identifier = r.randint(
                1000000,9999999)):
        super().__init__(name = name, price = price,
                         weight = weight,
                        flammability = flammability,
                        identifier=identifier)

    def explode(self):
        print("...it's a glove")

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif self.weight >= 5 and self.weight < 15:
            return "Hey that hurt" 
        else :
            return "OUCH!"
            
