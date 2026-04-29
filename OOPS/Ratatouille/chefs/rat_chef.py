from chefs.base_ import Chef

class Rat_Chef(Chef):

    def __init__(self):
        pass

    def cook(self,dish):
        print(f"Remy cooks {dish.name}")