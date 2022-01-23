""" def sayhi():
    print("Hello User")

print("Top")
sayhi()
print("Bottom") """


def sayhi(name):
    print("Hello " + name)


sayhi("Mike")
sayhi("Steve")



def sayhi(name,age):
    print("Hello " + name + ", you are " + str(age))


sayhi("Mike",25)
sayhi("Steve",26)

sayhi("Mike", 26)

def cube(num):
    return num*num*num  # returns breaks the function

result = cube(4)

print(result)