# import json
# # some JSON:
# x =  '[ "Glenn", "Sally", "Jen" ]'

# # parse x:
# y = json.load(x)

# # the result is a Python dictionary:
# print(y)

import urllib.request as ur
import json
# json_url = 'http://py4e-data.dr-chuck.net/comments_875544.json'
json_url = input("Enter location: ")
print("Retrieving ", json_url)
retrieved_info = ur.urlopen(json_url).read().decode('utf-8')
print('Retrieved', len(retrieved_info), 'characters')
json_obj = json.loads(retrieved_info)
sum = 0
total = 0
for comment in json_obj["comments"]:
    sum += int(comment["count"])
    total += 1
print('Count:', total)
print('Sum:', sum)