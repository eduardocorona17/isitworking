favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}")

alien_o = {'color': 'green', 'points':20}
speed_value = alien_o.get('speed', 'No speed value assigned')
print(speed_value)
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")