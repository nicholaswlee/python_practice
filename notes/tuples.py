### Tuples are unmodifiable list
x = ('Glenn', 'Sally', 'Joseph')
print(x[2])
y = (1, 9, 2)
print(max(y))

### Tuples are immutable, we cannot alter
### its contents
### x[2] = 6 will not work
### Cannot append to a tuple

### Can also assign tuples on the left hand side
(x, y) = (4, "Fred")
z = (x,y)
print(z)
print(y)
y = 5
print((x,y))
print(z)

### Recall that items() returns tuples
name_count = dict()
name_count["nicholas"] = 5
name_count["nathan"] = 3
### k,v act as a tuple 
for (k,v) in name_count.items():
    print(k,v)

### Tuples are also comparable
### The first element is compared, and then so on
### if there is equality
if((0,1,2) < (5, 1, 2)):
    print((5,1,2), "is greater than", (0,1,2))

### Tuples can be sorted
d = {'a': 10, 'b':1, 'c' : 22}
### Sorted will sort by key order
sorted_names = sorted(d.items())
print(sorted_names)
### To sort by value order
tmp = []
for (k,v) in d.items():
    ### Notice reverse order
    tmp.append((v,k))
### This revereses the sortation by value
tmp = sorted(tmp, reverse=True)
print(tmp)

### Another way this works is using get
def count_names_get(names):
    name_counter = dict()
    for name in names:
        ### get takes in the key and the default value
        name_counter[name] = name_counter.get(name, 0)
        name_counter[name] += 1
    return name_counter
### Opening a file but now lets reverse by value
fd = open("words.txt", "r")
words = []
for line in fd:
    words += line.split()
word_count = count_names_get(words)
words_max_val = []
### sort by make value
for (k,v) in word_count.items():
    words_max_val.append((v, k))
words_max_val = sorted(words_max_val, reverse = True)
print(words_max_val)
fd.close()

### Using list comprehension
print(sorted([(v,k) for k,v in word_count.items()]))