# class Cars:
#     wheel=4
#     def __init__(self,brand,modal,color):
#         self.brand=brand
#         self.modal=modal
#         self.color=color

#     def display_info(self):
#         print(f'{self.brand} {self.modal} has {self.wheel} wheels')
#         print(f'My car is {self.brand} {self.modal}, {self.color} color')


# car_obj=Cars('Audi','Q4','white')
# car_obj.display_info()


# class A:
#     num1=1000
# class B(A):
#     num2=2000
# class C(B):
#     num3=3000
# obj=C()
# print(obj.num1)
# print(obj.num2)
# print(obj.num3)

class Cat:
    def speak(self):
        print('Meow')

class Dog:
    def speak(self):
        print('Woof')

animals=[Cat(),Dog()]

for animal in animals:
 animal.speak()