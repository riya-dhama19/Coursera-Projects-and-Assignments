# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count= 0
z = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count = count+1
    n = line.find('0')
    x = float(line[n:])
    z = z + x
    avg = z/count
print("Average spam confidence:",avg)        
