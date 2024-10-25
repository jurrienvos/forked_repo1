

fruits = ['apple', 'banana', 'cherry']
enumerateFruits = enumerate(fruits)
print(enumerateFruits)
print(type(enumerateFruits))
for index, fruit in enumerate(fruits):
    print(index, fruit)
only_index_fruits=[index for index, fruit in enumerate(fruits)]
print(only_index_fruits)

x=[]
for a,b in enumerate(fruits):
    x.append((a,b))
print(x)
