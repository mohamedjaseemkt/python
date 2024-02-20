from array import array
my_array = array("i",[23,52,45,15,251,252,255,5545,99,55])
print("array",my_array)

my_list =[12,36,63,"jaseem","basith",65,55.5,63.9]
print("my list:",my_list)

my_tuple = (23,36,25,15,25.5,"jasz","mathew",50)
print("my tuple:",my_tuple)

my_set = {63,85,69,74,95,99,47,15,52}
print("set: ",my_set)

my_dict = {"name":"M4",
           "Brand":"BMW","Model":2024}
print("dict: ",my_dict)

a = set(my_list)
b = set(my_tuple)
intersection_set = a.intersection(b)
print(list(intersection_set))


set1 = {'oranege','mango','apple','pinapple','banana'}
set2 = {'cherry','melon'}
set1.update(set2)
print("updated set: ",set1)

fruits = ('oranege','mango','apple','pinapple','banana',)
x,*y,z= fruits
print(x)
print(y)
