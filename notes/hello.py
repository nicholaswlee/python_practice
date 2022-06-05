# Print statements in python
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
print("98.6 casted to an int is", str(int(98.6)))

### Concatenation and Input ###
# Here we use input() to get input
num_one = input("Give me a number: ")
num_two = input("Give me another number: ")
num_three = num_one + num_two
num_sum = int(num_one) + int(num_two) + int (num_three)
# When listing things, we can use commas to implicityly
# add spaces between our variables
print("Your numbers are ", num_one, num_two, num_three, "\nThe sum is:", str(num_sum))