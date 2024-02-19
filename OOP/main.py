"""this is the doc"""
# print(globals().values())



class CAR:
   name = "mercedis"
   model = 2024



car1 = CAR()
print(car1.name)
print(car1.model)

class_name = car1.__class__.__name__

car2 = CAR()

print(car2.name)
print(car2.model)

# class_name = CAR.__name__

print(class_name)

# print(globals())