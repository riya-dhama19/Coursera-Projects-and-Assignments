name = input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)

hr = {}
for line in handle:
    line.rstrip()
    if not line.startswith('From '):
        continue
    word = line.split()

    hrs = word[5].split(':')
    hr[hrs[0]] = hr.get(hrs[0],0) + 1

lst = []

for a,b in hr.items():
    lst.append((a,b))

lst.sort()

for a,b in lst:
    print (a,b)
