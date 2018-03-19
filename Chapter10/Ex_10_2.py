# I/O initialization
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"          # default file name for the empty input
handle = open(name)

# init
hours = {}                                          # key = hours string, value = occurencies

# string processing block
for line in handle :
    stLine = line.rstrip()                          # get rid of the /n in the strings
    if not stLine.startswith("From ") : continue    # skip unneccessary lines
    spLine = stLine.split()                         # split line to get
    time = spLine[5]                                # time in the fifth position
    hr = time.split(":")[0]                         # split time strig to get hours
    hours[hr] = hours.get(hr, 0) + 1                # and add update key/value pairs for hrs

# sorting results
stat = hours.items()                                # get tuples out of dict
stat = sorted(stat)                                 # to sort by key (hours string)

# output block
for item in stat :
    print(item[0], item[1])
