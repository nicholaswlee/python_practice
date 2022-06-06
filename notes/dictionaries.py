### Another type of data structure
### Dictionary is a "bag" of values
### Associative array, most powerful data collection
### Like a hashmap in java, memory based key value stores

### Makes an empty dictionary
purse = dict()
### Use bracket notation to create the key
### and then store the value at a certain key
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75

### We can print dictionaries as well
### the order of dictionaries are not predictable
print(purse)
print(purse['candy'])

### Can reassign value
purse['money'] = 9

### Creating dictionary constant
### Use curly bracket and :
dictionary_two = {'drugs': 5, 'alcohol' : 10, 'food' : 7}
print(dictionary_two)

### We can count values using dictionaries
names = ["marquard", "zhen", "csev", "zhen", "cwen", "csev",
        "cwen", "marquad", "csev", "zhen", "zhen"]
### If we try to access a key in the dictonary is does
### not work. Instead use in
ccc = dict()
print("zhen" in ccc)
def count_names(names):
    name_counter = dict()
    for name in names:
        ### Check to see if the name is in dict
        if(name not in name_counter):
            name_counter[name] = 1
        else:
            name_counter[name] += 1
    return name_counter
ccc = count_names(names)
print(ccc)

### Another way this works is using get
def count_names_get(names):
    name_counter = dict()
    for name in names:
        ### get takes in the key and the default value
        name_counter[name] = name_counter.get(name, 0)
        name_counter[name] += 1
    return name_counter
ddd = count_names_get(names)
print(ddd)

### Opening a file
fd = open("words.txt", "r")
words = []
for line in fd:
    words += line.split()
word_count = count_names_get(words)
print(word_count)
fd.close()

### Can iterate through dictionary
for key in word_count:
    print(key, ":", word_count[key])
### Can extract values, returns a list
print(word_count.values())
### Can extract keys, returns a list
print(word_count.keys())

### Can use two variables to iterate
### Items essntially is like a tuple
for key, val in word_count.items():
    print(key, val)
        