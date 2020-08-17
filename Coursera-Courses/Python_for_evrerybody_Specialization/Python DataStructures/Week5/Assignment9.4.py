name = input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)
empty = {}
for line in handle:
    if line.startswith('From '):
        words = line.split()
        email = words[1]
        empty[email] = empty.get(email,0)+1


bigcount = None
bigmail = None

for mail,count in empty.items():
    if bigcount is None or count >bigcount:
        bigcount = count
        bigmail = mail

print(bigmail,bigcount)
