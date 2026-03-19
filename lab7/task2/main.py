from models import Animal, Dog, Cat

animals = [
    Animal("Animal", 5, "gray"),
    Dog("Garry", 3, "black/white"),
    Cat("Maxwel", 2, "orange")
]

for animal in animals:
    print(animal)
    print(animal.speak())
    print(animal.move())
