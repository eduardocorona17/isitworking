players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:4])
# print(players[0:2])
# print(players[2:])
print(players[-3]) # Prints 3rd item from end of list (working backwards)
print(players[-3:]) # Prints items starting from back of list in this case, the last 3 items. 

print("Here are my first three players: ")
for player in players[:3]:
    print(player.title())
