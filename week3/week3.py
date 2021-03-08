import urllib.request as req
import json
url = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json'

with req.urlopen(url) as response:
    data = json.load(response)
data = data['result']['results']

with open('data.txt', mode='w') as f:
    for attraction in data:
        f.write(attraction['stitle']+',')
        f.write(attraction['longitude']+',')
        f.write(attraction['latitude']+',')
        jpgUrl = attraction['file'].split('http:')
        f.write('http:' + jpgUrl[1] +'\n')