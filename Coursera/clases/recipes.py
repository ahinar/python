class Recipe():
    
    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time

    def content(self):
        print( f"El plato {self.dish} tiene como ingredientes {str(self.items)} "\
              f"y se prepara en {str(self.time)}")
        
pizza = Recipe("pizza", ["Harina", "Queso", "Salami"], 45)

print(pizza.items)

print(pizza.content())