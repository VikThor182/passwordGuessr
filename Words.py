import unidecode


class Words:
    data = ["test", "word", "monzbi", "coucou", "youhou", "incroyable", "oskour"]


def wordToLower(data):
    for x in data:
        print(x.lower())


def wordToCaps(data):
    for x in data:
        print(x.upper())


def firstLetterToUpper(data):
    for x in data:
        print(x.capitalize())


def removeAccent(data):
    for x in data:
        print(unidecode.unidecode(x))


