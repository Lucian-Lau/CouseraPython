import json
import urllib.request

address = 'http://py4e-data.dr-chuck.net/comments_1270940.json'
uh = urllib.request.urlopen(address)

data = uh.read().decode()
# add .read().decode() to make it readable and decoded by python

info = json.loads(data)
count = 0
sum = 0

for item in info['comments']:
    x = item['count']
    count += 1
    sum += int(x)
print(count, sum)
