a={25,63,55,33,88,99,53,31,48,49}
print(a)

[print(x) for x in a]

a.add(77)
print(a)

b= {5,6,7,77}
a.update(b)
print(a)

a.remove(7)
print(a)

a.discard(63)
print(a)

c={99,63,22,1}
d=a.union(c)
print(d)

e={11,62,46,35,20,7,88,77}
f=a.intersection(e)
print(f)

x ={1,2,3,4,5,6}
y ={5,6,7,8,9}
z=x.symmetric_difference(y)
print(z)