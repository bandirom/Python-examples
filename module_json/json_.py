import json

#  print(dir(json))
album_string = """{
    "album_title": "Yellow Submarine",
    "release_year": 1996,
    "won_grammy": false,
    "band": "The Beatles",
    "album_sale": null,
    "musicians": ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr"],
    "studio": {
        "studio_name": "Abbey Road Studios",
        "location": "London, England"
    }
}"""

album2 = {
    "album_title": "Yellow Submarine",
    "release_year": 1996,
    "won_grammy": False,
    "band": "The Beatles",
    "album_sale": None,
    "musicians": ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr"],
    "studio": {
        "studio_name": "Abbey Road Studios",
        "location": "London, England"
    }
}

album_json_file = open('album.txt', 'r')
album = json.load(album_json_file)

print('### Load: \n', album, type(album))
print("Album Title: ", album['album_title'])
print('Released year: ', album['release_year'])

album_s = json.loads(album_string)
print('### Loads: \n', album_s, type(album_s))

print('### Dumps: \n', json.dumps(album2), type(json.dumps(album2)))

file2 = open('album2.txt', 'w')
json.dump(album2, file2)
