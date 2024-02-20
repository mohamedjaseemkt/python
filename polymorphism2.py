class addition:
   def calculation(self,a,b):
      return a+b

class subtract:
   def calculation(self,a,b,c):
      return a+b-c
   
class multiply:
   def calculation(self,a,b):
      return a*b 

class divition:
   def calculation(self,a,b):
      return a/b

add = addition()
sub = subtract()
product = multiply()
divide = divition()


print("sum of addition: ",add.calculation(9,5))
print("sum of subtract: ",sub.calculation(9,5,3))
print("poduct is: ",product.calculation(9,4))
print("sum of divition: ",divide.calculation(8,3))