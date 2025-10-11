




# list comprehensions 

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)


nameWith = [item for item in names if "o" in item]
print(nameWith)


print(len(names))