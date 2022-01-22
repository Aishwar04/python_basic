from operator import index


friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends)

print(friends[0:2])  # excludes end element

print(friends[-1]) # access list elements in reverse

print(friends[1:]) # acess all the elemnts from 1

friends[1] = "Mike"  # update a list

print(friends)

########### List Funstions ##############

lucky_numbers = [4,8,15,16,23,21,42]

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

#friends.extend(lucky_numbers)  # extend adds one list to another

#print(friends)

friends.append("Creed")  # append adds an element to the end of the list
print(friends)

friends.insert(1,"Kelly")  #insert adds an elemnt to a list at the specified index
print(friends)

friends.remove("Jim")  # removes an elemnt from a list
print(friends)

friends.pop()  # pop by default removes the last element of an index
print(friends)

friends.pop(1)  # pop removes the element from the specified index
print(friends)

friends.clear()  # clear removes all the elements from a list
print(friends)



friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends.index("Karen")) # index returns the index of the elemnt being searches, if not present throws error
#print(friends.index("Mike"))


friends = ["Kevin", "Karen", "Jim","Jim", "Oscar", "Toby"]
print("index is " + str(friends.index("Jim")))  # index returns the first index if the same elemnt is present multiple times

print(friends.count("Jim"))  # count returns the count of an element in a list 

friends.sort()  # sort sorts a list

lucky_numbers.sort()
print(lucky_numbers)

print(friends)

(lucky_numbers.reverse())
print(lucky_numbers)

friends2 = friends.copy()  # make a copy of a list
print(friends2)


