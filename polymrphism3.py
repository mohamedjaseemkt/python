class addition:
   def calculation(self,a,b):
      print("sum of addition: ",(a+b))
   

class subtract:
   def calculation(self,a,b,c):
       
       print("sum of subtract: ",(a+b-c))  

class multiply:
   def calculation(self,a,b):
      #return a*b
      print("poduct is: ",(a*b)) 

class divition:
   def calculation(self,a,b):
     # return a/b
      print("sum of divition: ",(a/b))

add = addition()
sub = subtract()
product = multiply()
divide = divition()

add.calculation(9,5)
sub.calculation(9,5,3)
product.calculation(5,8)
divide.calculation(8,3)