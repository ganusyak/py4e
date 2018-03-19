fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh :
    stLine = line.rstrip()
    if not stLine.startswith("From:") : continue
    splittedLine = stLine.split()
    mail = splittedLine[1]
    print(mail)
    count = count + 1

print("There were", count, "lines in the file with From as the first word")
