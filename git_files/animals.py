class Cat:
    
    def __init__(self):
        self.mood = "neutral"     

    def speak(self):
        if self.mood == "happy":
            print("Purrr")
        elif self.mood == "angry":
            print("Hiss!!")
        else:
            print("Meow!")


class Dog:
    
    scientific_name = "Canis lupus familiaris"

    def __init__(self, name,):
        self.name = name
        self.woof = 0
        
    def count(self):
        self.woof += 1
        for bark in range(self.woof):
            self.speak()   
    
    def speak(self):
        print("Woof!")

    def hear(self, words):
        if self.name in words:
            self.speak()
            
class Husky(Dog):
    
    def speak(self):
        print("Bark")
        