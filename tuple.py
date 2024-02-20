tuple1 = (12,65,58,74,45)
tuple2 = (11,22,33,55)
x = list(tuple1)
y = list(tuple2)
x.append(y)
print(tuple(x))


a=(25,63,41,85,74,62,7,5,33,54,3)
print(type(a))
b=list(a)
print(type(b))
print(b)

print(len(b))

b[1:3] = [25,88,55,77]

b.append(2)
print(b)

b.insert(3,"jaseem")
print(b)

c=(31,71,51)
d=list(c)
b.extend(d)
print(b)

b.remove("jaseem")
print(b)

b.sort()
print(b)

b.pop()
print(b)

i = 0
while(i<len(b)):
    print(b[i])
    i=i+1
