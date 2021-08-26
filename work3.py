
def thesaurus(*args):
    new_dict = {}
    for i in args:
        key = i[0].capitalize()
        if key not in new_dict:
            new_dict[key] = []
        new_dict[key].append(i)
    return new_dict

print(thesaurus("Иван", "Мария", "Петр", "Илья"))