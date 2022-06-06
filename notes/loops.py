# While loops
going = True
while(going):
    num = input("Give me a number between 1 and 10: ")
    try:
        num = int(num)
        while(num > 0):
            # Use break to break through the next loop
            if(num > 10):
                print("That is not between 1 and 10!")
                break;
            # Use continue to go to next iteration
            # This is like "filtering" only prints conditionally
            if((num%2) != 0):
                continue
            print(num)
            num -= 1
    except:
        if(num.lower().strip() == "quit"):
            going = False
            print("Good bye")
        else:
            print("You did not give me a number")
# For loops
### Using lists
arr = []
### Use 'in' range() to create a list from
### that i goes through. range() can have up to three arguments
### If just one arguments, arg is upper bound
### If two, lower and upper bound
### The third argument is how the range can be incremented
### Also python uses lists!
for i in range(5, 0, -1):
    arr = arr + [i]
print("Here is the array", arr)

arr = range(5, 0 , -1)
print("Here is the array", arr)

### Can also just itterate through a list
for i in arr:
    print((i))


### Finding largest num in an array
arr = [64, 50, 2, 10, 15, 8]
### Here we assume the numbers are greater than 0
temp = 0;
print("Here is the array", arr)
for i in arr:
    if (temp < i):
        temp = i
print("The largest number is", temp) 

### Find smallest num in an array
### None is kinda like null, temp just doesn't have a value
temp = None
arr = [64, 50, 2, 10, 15, 8]
print("Here is the array", arr)
for i in arr:
    # is basically saying is temp the same as None
    # Useful for objects, stronger than ==
    if ((temp is None) or (temp > i)):
        temp = i
print("The smallest number is", temp) 