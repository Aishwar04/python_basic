# tuples are immutable i.e cannot be changed

coordinates = (4,5)

print(coordinates[0]) # access tuple element
print(coordinates[1])

#coordinates[1] = 10  # throws error as cannot modify a tuple 

coordinates1 = [(8,2),(9,4),(18,4),(5,2)] # allows item modification

print(coordinates1[2])

coordinates1.append(10)
print(coordinates1)

coordinates1[4] = 21
print(coordinates1)

coordinates1[1] = (9,5)
print(coordinates1)


