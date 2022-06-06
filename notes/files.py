### Use open() to open the file
### Recall that the second argument 
### in the open() function is the mode
### fhandle is not the data, but something
### we can manipulte
### Open will fail if the file doesn't exist
fhandle = open("mbox-short.txt", 'r')
x = 0

def len(string):
    i = 0
    for char in string:
        i += 1;
    return i
def find_received(file):
    for line in file:
        line = line.rstrip()
        if(line.startswith("Received:")):
            start =len("Received: ")
            end = line.find("(")
            if(end == -1):
                continue
            print("Name: ", line[start:end])

### This counts through 5 lines
for line in fhandle:
    if(x == 5):
        break
    print(line, end="")
    x += 1
find_received(fhandle)
### At this point the enitre file has been read
entire_file = fhandle.read()
print("Our file is ", len(entire_file), "characters long")
### Don't forget to close!
fhandle.close()
fhandle = open("mbox-short.txt", 'r')
entire_file = fhandle.read()
print("Our file is ", len(entire_file), "characters long")


