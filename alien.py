alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print(f"You just shot down a {alien_0['color']} alien and earned {new_points} points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
alien_0['color'] = 'yellow'
print(f"This alien's color is now {alien_0['color']}.")
# print(alien_0)
alien_0['speed'] = 'fast'
print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else: x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"The new position of this alien is: {alien_0['x_position']}.")
del alien_0['points']
print(alien_0)