### Lists are collection variables
### List constants are surrounded by square brackets
### In python lists can have different types of elements
random_list = ["apple", 5, ["list", "inside", "list"]]
print(random_list)

### Lists in definite loops are in sync
for elem in random_list:
    print(elem)

### Lists are mutable
random_list[2] = "List has changed"
for elem in random_list:
    print(elem)

### Range basically creates a list
print(range(4))

### This is a counted loop
for i in range(len(random_list)):
    print(i)

### Lists can concat
random_list_two = ["pear", 10, "list is same"]
random_list_combo = random_list + random_list_two
print(random_list_combo)

### Lists can slice
print(random_list_combo[0:2])

### Since lists are mutable, it edits the actual list
random_list_combo.append("carrot")
print(random_list_combo)

### Again can use not in and in for lists
if(5 in random_list_combo):
    print("5 is in the list")

### Other functioms
num_list = [55, 20, 96, 21]
summation = sum(num_list)
minimum = min(num_list)
maximum = max(num_list)
print("Of the list", num_list, "\nMax:", maximum,
    "\nMin:", minimum, "\nSum:", summation)

### Turning a sentence into a list of strings
sentence = "This is a sentence"
### By default split strings by strings
strings = sentence.split()
print(strings)
for string in strings:
    print(string)
    
### Split can take arguments to know what to split by
phone_number = "206-519-2002"
numbers = phone_number.split("-")
for number in numbers:
    print(number)