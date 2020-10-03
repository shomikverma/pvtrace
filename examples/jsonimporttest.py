import json
from sys import argv

with open(argv[1]) as json_file:
    data = json.load(json_file)
    print(data)
