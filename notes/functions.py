# To define a function use def
# functions do not get executed when 
# the file is run. Instead when called it 
# is executed.
def func1():
    print("This is func 1")

# We do not need to specify type in python
def double(num):
    # Use return to return
    return num * 2

going = True
while(going):
    num = input("Give me a number: ")
    try:
        # Here we 'invoke' the function double
        print(num, "doubled is", str(double(int(num))))
    except:
        if(num.lower().strip() == "quit"):
            going = False
            print("Good bye")
            quit()
        else:
            print("You did not give me a number")