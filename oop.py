

# def calculate():
#   print("Nalu is a carton boy")

# calculate()

#attribute, properties.
#    # class attribute
#    state = "flying-car"
#    color = "silver"
#    tyre = "six-tyres"
#    mode_of_movement = "water"

    # constructor Method
#    def __init__(self) -> None:
#     print("hello world")

#    def __book__(self):
#      print("GOD is the greatest")

from uuid import uuid4

class Car:
    def __init__(self, state, color, tyre) -> None:
        self.state = state
        self.color = color
        self.tyre = tyre
        self.uuids = str(uuid4())

    # key == mercedis.909f95b2-27f6-4f6d-8c9b-0b14eb70a5fe

    
    def __str__(self) -> str:
        return f"Tobi's Car is a {self.state}\nand it has a {self.color}color\nwith {self.tyre} and its uuid is {self.uuids}"
    
    def to_dict(self) -> dict:
        return self.__dict__
        

mercedis = Car("flying-car", "black", "4-tyres")
print(mercedis)

dictionary = mercedis.to_dict()
print(dictionary)






# print(mercedis.state)
# print(mercedis.state)
# print(mercedis.color)
# print(mercedis.tyre)
# print(mercedis.mode_of_movement)

# mercedis414 = Car()
# print(mercedis414.color)
