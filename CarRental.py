class CarRental:
    def __init__(self,customer_name,car_modal,days,price_per_day):
        self.customer_name=customer_name
        self.car_modal=car_modal
        self.days=days
        self.price_per_day=price_per_day

    def show(self):
        print(f'Customer Name: {self.customer_name}')
        print(f'Car Modal: {self.car_modal}')
        print(f'Number of Days: {self.days}')
        print(f'Price per day: {self.price_per_day}')

    def total(self):
        total_amt = self.days * self.price_per_day   
        print(f'The total amount is :', total_amt)

    def discount(self):
        #Days >= 7 AND total >= 400 → 15% discount
        #Days >= 5 OR total >= 300 → 10% discount
        #self.total_amt = self.days * self.price_per_day  
        self.discount_amt=0 
        if self.days >= 7 and self.total_amt >= 400:
            self.discount_amt = self.total_amt * 0.15
            #self.total_amt = self.total_amt - discount
            print('15% Discount is applied')
            #print(f'The total amount after discount is : {self.total_amt}')
        elif self.days >= 5 or self.total_amt >= 300: 
            self.discount_amt = self.total_amt * 0.10
            #self.total_amt = self.total_amt - discount
            print('10% Discount is applied')
           # print(f'The total amount after discount is : {self.total_amt}')
        else: 
            print('No discount')
    def final_amount(self):
        self.final_amt=self.total_amt - self.discount_amt
        print(f'The final price is : {self.final_amt}')

car_rental=CarRental('Nimitha', 'Audi-Q4', 5,1000)
car_rental.show()
car_rental.total()
car_rental.discount()
car_rental.final_amount()

