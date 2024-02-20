a = {"brand":"ford", "model":"mustang","year":1964}
print(a)

x=a.get("model")
print(x)

y=a.keys()
print(y)

z=a.values()
print(z)

a.update({"model":"ferrari"})
print(a)

a["type"]="racing"
print(a)

a["colour"] = ["matte navy blue","matte black","dark blue"]
print(a)