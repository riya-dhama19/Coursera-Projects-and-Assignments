# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
fh1 = fh.read()
file1 = fh1.upper()
file1 = file1.rstrip()
print(file1)
