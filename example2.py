x = open("text2.txt","w")
x.write("hai ")
x.close()
x = open("text2.txt","rt")
print(x.read())
x.close()
x = open("text2.txt","a")
x.write("how are you")
x.close()
x = open("text2.txt","rt")
print(x.read())
x.close()
