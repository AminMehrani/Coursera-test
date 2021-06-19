name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
emails = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue

    lines = line.split()
    email = lines[1]
    email = email.split()
    for sender in email:
        emails[sender]= emails.get(sender,0) + 1

Maximum = -1
Maxsender = None
for k,v in emails.items():
        if  v > Maximum:
            Maximum = v
            Maxsender = k
print (Maxsender, Maximum, )

    #print(email)
