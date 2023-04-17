import json
filename = 'favorite_num.txt'
with open(filename) as f:
    filename = json.load(f)
    print(f"Your favorite number is {filename}")