import requests

#reponse 407 -> il faut custom un proxy
people = requests.get('http://api.open-notify.org/astros.json')

json = people.json()

print (json)

print("The people currently in space are:")
for p in json["people"]:
    print(p['name'])