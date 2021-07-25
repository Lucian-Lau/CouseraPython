#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
tmp = []
a = []
for line in fh:
    lst = line.rstrip()
    lst = lst.split()
    tmp = tmp + lst
    tmp = sorted(tmp)
for word in tmp:
    if word not in a:
        a.append(word)
print(a)
