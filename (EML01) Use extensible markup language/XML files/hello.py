class Dog:
    
    def __init__(self, name:str, age: int, breed: str, weight: float):
        self.name = name
        self.age = age
        self.breed = breed
        self.weight = weight

    def bark(self):
        return f"{self.name} goes bark!"

    def ispuppy(self):
        if self.age<= 1:
            return f"{self.name} is a puppy!"
        else:
            return f"{self.name} is not a puppy!"
        
    def size(self):
        if self.weight <= 30:
            return f"{self.name} is a small dog!"
        elif self.weight >30 and self.weight <=60:
            return f"{self.name} is a medium dog!"
        else:
            return f"{self.name} is a big dog!"
charlie = Dog("Charlie",1,"poodle",30)
    
    




