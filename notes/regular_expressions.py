### Powerful way to look through text
### This imports regular expressions
import re

hand = open('mbox-short.txt', "r")
for line in hand:
    line = line.rstrip()
    ### Carrot character indiccates F at begining of line
    if re.search('^From:', line):
        print(line)
### . indicates any character
### * means zero or more times
### ^X.*: -> means a line started by X, followed
### by some number of characters, followed by a colon

### ^X-\S+: -> X- with \S non-white space charcter
### + means one or more times

### [] -> indicates one cahracter
### [0-9] -> anything from 0 to 9
### This finds all characters
x = "Fav numbers are 0, 3, and 23"
### + allows for numbers to go together
y = re.findall('[0-9]+', x)
print(y)

### findall is greedy
x = "From: the using :"
y = re.findall('F.+:', x)
print(y)
### We can use ? to eliminate the greediness
y = re.findall('F.+?:', x)
print(y)
hand.close()
hand = open('mbox-short.txt', "r")
file = hand.read()
y = re.findall("\S+@\S+", file)
print(y)
hand.close()

### We can use parenthesis to match
### This matches the From, but then only extracts
### the parenthesis
print("From:")
hand = open('mbox-short.txt', "r")
file = hand.read()
y = re.findall("From (\S+@\S+)", file)
print(y)
hand.close()

### [^ ] means nonblank characters
### To have special characters act normal,
### use \ i.e. \.