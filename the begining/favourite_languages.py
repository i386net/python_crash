favourite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favourite_languages.items():
    if len(languages) == 1:
        print("• " + name.title() + "'s favourite language is " + languages[0].title())
    else:
        print("• " + name.title() + "'s favourite languages are: ")
        for lang in languages:
            print('\t◊ ' + lang.title())