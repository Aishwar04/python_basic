phrase = "Giraffe\ Academy"
print(phrase)

phrase = "\"Giraffe\" Academy"
print(phrase)

phrase = "Giraffe Academy\"\\\\"
print(phrase + " is cool.")


print(phrase.islower())


print(phrase.lower().islower())

print(len(phrase))


##########  Indexing Strings ##########

print(phrase[0])  # indexing in python strings starts from 0


print(phrase.index("Academy")) # returns the index of a character or substring 


#print(phrase.index("mine")) # retrusn error if substring not found

print(phrase.replace("Giraffe","Elephant"))

print(type(phrase))