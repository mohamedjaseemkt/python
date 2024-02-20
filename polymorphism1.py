class animal:
    def speak(self):
        pass

class Dog(animal):
    def speak(self):
        return "woof!"
    
class Cat(animal):
    def speak(self):
        return "meow!"
    
class Duck(animal):
    def speak(self):
        return "quack!"
    
def animal_sound(animal):
    return animal.speak()

dog = Dog()
cat = Cat()
duck = Duck()

print(animal_sound(dog))
print(animal_sound(cat))
print(animal_sound(duck))
