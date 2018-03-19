text = "X-DSPAM-Confidence:    0.8475"
x = text.find(":")
slice1 = text[x+1:]
slice2 = slice1.strip()
print(float(slice2))
