import re

# I/O section
name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_78960.txt"          # default file name for the empty input
handle = open(name)

# init section
sum = 0

# processing section
for line in handle :
    stLine = line.rstrip()                  # strip the line out of /n
    rexp = re.findall('[0-9]+', stLine)     # find all digit strings
    for digit in rexp :
        sum = sum + int(digit)              # sum all the converted numbers

# output section
print(sum)
