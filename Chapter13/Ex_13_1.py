import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')



# url =  "http://py4e-data.dr-chuck.net/comments_42.xml"
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)


results = tree.findall('comments/comment')
# print(results)
counter = 0
total = 0
for result in results :
    #print(result.find('count').text)
    counter = counter + 1
    total = total + int(result.find('count').text)

print('Count:', counter)
print('Sum:', total)
