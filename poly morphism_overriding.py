class Circle:
    def draw(self,a,b):
        return a+b
    
class Square:
    def draw(self,x,y,z):
        return x+y+z
    
circle = Circle()
square =Square()

print("sum of 2.no set: ",circle.draw(3,5))
print("sum of 3.no set: ",square.draw(6,7,5))