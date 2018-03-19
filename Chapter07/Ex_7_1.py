# Use words.txt as the file name

# input section
fname = input("Enter file name: ")

# check the filename
try:
    fh = open(fname)
except:
    print("File doesn't exist")
    quit()

# processing
for line in fh :
    slice1 = line.rstrip()
    print(slice1.upper())
