favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}")

for name in favorite_languages.keys():
    print(f"{name.title()}")

for lang in set(favorite_languages.values()): # set returns python 1s instead of twice.
    print(f"{lang.title()}")

friends = ['sarah', 'phil']

for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"Hi {name.title()}, I see you like {language.title()}!")
if 'erin' not in favorite_languages.keys():
    print("Erin, take our poll dude! What language do you like or write in?")

# alien_o = {'color': 'green', 'points':20}
# speed_value = alien_o.get('speed', 'No speed value assigned')
# print(speed_value)
# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}")
