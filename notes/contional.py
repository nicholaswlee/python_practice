# Conditional Statements
going = True
possible = True
while(going):
    num = input("Give me a number between 1 and 10: ")
    # try and except prevents the code from failing
    try:
        num = int(num)
        possible = True
    # 
    except:
        possible = False
        if(num.lower().strip() == "quit"):
            going = False
            quit()
        else:
            print("YOU GAVE ME BAD INPUT")
        # continue goes through the next iteration
        continue
    # USE 'and', 'or', and 'not' instead of
    # &&, ||, !
    if(possible):
        if((num > 10) or (num < 1)):
            print(str(num), "is not between 1 and 10")
        elif((num % 2) == 0):
            print(str(num), "is even")
        # else statements aren't required
        else:
            print(str(num), "is odd")