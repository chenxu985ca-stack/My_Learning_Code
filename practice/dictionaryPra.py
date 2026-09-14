# dictionary

favorite_language = {
    'jen': 'python',
    'alian': 'c#',
    'michle': 'java',
    'mark': 'python'
}

languages = ['python']

# for name, language in sorted(favorite_language.items()):
#   if language.lower() in languages:
#        print(f"{name.title()},Welcome,I heard you like {language.title()},mine too!!!")
#    else:
#        print(f'{name.title()},Welcome')

for language in favorite_language.values():
    print(language.title())
