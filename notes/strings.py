### Strings can be indexed
### Strngs are objects in python
### This prints every char in a string
def charify(word):
    count = 0
    print("Charify", word)
    print("Left is indexed, right is through the word")
    for i in word:
        print(word[count] + ":" + i)
        count += 1

def len(word):
    count = 0
    for i in word:
        count += 1
    return count

def cut(word):
    length = len(word)
    half = int(length/2)
    ### Here we slice a string cutting a certain portion
    word = word[half:length]
    return word
### Helper to determine lowest word
def determine_lowest_word(words):
    word = None
    for w in words:
        if(word == None):
            word = w
        if(word > w):
            word = w
    return word
### sorts words by alphabetical order
def sort_alphabetical(words):
    length = len(words)
    sorted_words = []
    temp = None
    for i in range(length):
        temp = determine_lowest_word(words)
        words.remove(temp)
        sorted_words = sorted_words + [temp]
    return sorted_words

phrase = input("Give me a word: ")
charify(phrase)
print("It is", len(phrase), "letters long")
print("Slicing", phrase, "gives", cut(phrase))
### Finding word in a string
print("The letter", phrase[0], "is in index", phrase.find(phrase[0]))
print("The letter z is not in the word:", phrase.find("z"))

### Replace a word using replace(word in string, replacement)
### This will replace all the words
name = input("What is your name: ")
hello_message = "Hello, temporary"
print(hello_message)
print(hello_message.replace("temporary", name))

### Striping
white_space = "      HEllo     "
print(white_space.lstrip() + "end")
print(white_space.rstrip() + "end")
print(white_space.strip() + "end")

### Concat vs comma
print("No" + "space")
print("Yes", "space")

### Using in to know if a string exists in a string
if("car" in "racecar"):
    print("Car is in racecar")

### You can compare strings using < and ==
### Note that capitilization matters. Capital letters
### are all before lower case letters
arr1 = ["Cat", "mouse", "Alien", "bat"]
print("Sorted with mixed capitals", sort_alphabetical(arr1))
arr2 = ["cat", "mouse", "alien", "bat"]
print("Sorted with no capitals", sort_alphabetical(arr2))

### Using string functions
var = "CAT"
### This function will not change var. This makes a copy
var1 = var.lower()
print("String object functions dont change the real string:", var, var1)





