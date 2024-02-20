x = [12,"jaseem",6.5,False]
x.insert(2,"basitrh")
print(x)

y=[2541,36,125]
x.extend(y)
print(x)

x.append("python")
print(x)

x[4] = True
print(x)

x.remove("basitrh")
print(x)

x.pop()
print(x)

x.pop(4)
print(x)

del x[5]
print(x)

#print joint
a=[12,65,85,1,22,3]
b=[25,63,98,52,5]
print(a+b)

#list copy
x = ["apple","banana","cherry"]
y = x.copy()
print(y)
