alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

more_aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    more_aliens.append(new_alien)
for new_alien in more_aliens[:5]:
    print(new_alien)
print("...")  

print(f"Total aliens: {len(more_aliens)}") # check out how you can use the len() func in an f str format
for alien in more_aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
for alien in more_aliens[:5]:
    print(alien)