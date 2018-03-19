# input section
fname = input("Input file name: ")
try:
    fhand = open(fname)
except:
    print('Incorrect file name')
    quit()

total = 0.0
counter = 0

for line in fhand :
    # searching for lines lik X-DSPAM-Confidence: 0.8475
    if not line.startswith("X-DSPAM-Confidence:") : continue
    strippedLine = line.rstrip()            # line without /n in the end
    pos = strippedLine.find(":")            # position of :
    subLine = strippedLine[pos + 1 : ]      # keep only the number
    valueStr = subLine.lstrip()             # without spaces in the beginning
    # update counters
    counter = counter + 1
    total = total + float(valueStr)

# desired output
print("Average spam confidence:", total / counter)
