print("Hello World")


# Conditionals in Python
x = 5
if (x == 5):
    print(5)
else:
    print("Not 5")

# Loops in python
while(x > 0):
    print(x)
    # Python does not have direct increment ++
    # or decrement --, 
    x -= 1

### Math in python ###
# Notice ** is power 
x = 2 
x = x**4
if(x == 16):
    print("x is 16")
    # USE type() to determine type
    print(type(x))
    # This also does concetanation
    # WE MUST CAST TO DO CONCATENATION
    print("x mod 1 is " + str(x%5))

# Division is different in python. There is no integer division
# division automatically converts to floats
print("x divided by 5 is " + str(x/5))
print("x divided by 4 is " + str(x/4))

