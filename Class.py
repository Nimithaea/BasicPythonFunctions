class num:
    num1 = 20
    def n(self):
        print('Nimitha')

obj = num()
print(obj.num1)
obj.n()


class car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color

    def show(self):
        print(self.brand,self.color)

car1 = car('BMW','Black')
car2 = car('AUDI', 'White')
car3 = car('Volvo', 'Grey')

# print(car1.brand, car1.color)
# print(car2.brand, car2.color)
# print(car3.brand, car3.color)

car1.show()
car2.show()
car3.show()