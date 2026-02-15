from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
        
        
class BkashPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} taka using bKash")
        
class CardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} taka using Card")



p1 = BkashPayment()
p1.pay(1000)

p2 = CardPayment()
p2.pay(2000)




class Shape(ABC):

    @abstractmethod
    def area(self):
        pass 

class TriAngle(Shape):
    
    def area(self, height, base):
        self.h = height
        self.b = base 
        self.a = 0.5 * self.h * self.b 
        
        return self.a 
            
    
tri_obj = TriAngle()
print(tri_obj.area(6, 3))
    