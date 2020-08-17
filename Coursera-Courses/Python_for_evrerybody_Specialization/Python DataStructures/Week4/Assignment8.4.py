fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line_split = line.split()
    for i in line_split:
        if i not in lst:
            lst.append(i)
lst.sort()

#print(line_split)
print(lst)
