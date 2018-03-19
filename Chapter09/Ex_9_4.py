# open file for reading
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

# list for all email occurencies
emailHist = {}

# counting all keys in all strings
for line in handle :
    stLine = line.rstrip()
    if not stLine.startswith("From ") : continue
    # splitting an email form the line
    splitLine = stLine.split()
    email = splitLine[1]
    emailHist[email] = emailHist.get(email, 0) + 1                 # and adding it to the list

                          # diction : email, occurencies

# top email counters
topMail = None                           # address
topCount = None                          # number of occurencies

# looping through the dictionary to find the key with the most value
for mail, count in emailHist.items() :
    if (topCount is None) or (topCount < count) :
        topMail = mail
        topCount = count

print(topMail, topCount)
