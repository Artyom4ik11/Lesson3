import random

def get_jokes(count, flag =False):
    nouns = ["цветок", "стул", "лес", "мужчина", "магазин"]
    adverbs = ["вчера", "сегодня", "завтра", "позавчера", "послезавтра"]
    adjectives = ["смешной", "добрый", "яркий", "обычный", "лучший"]
    for i in range(count):
        noun = random.choice(nouns)
        adverb = random.choice(adverbs)
        adjective = random.choice(adjectives)
        joke = (f'{noun} {adverb} {adjective}')
        not_repeat_jokes = []
        print(joke)
        if flag == True:
            not_repeat_jokes = joke.split()
            for noun in nouns:
                for i in not_repeat_jokes:
                    if noun == i:
                        nouns.remove(noun)
            for adverb in adverbs:
                for i in not_repeat_jokes:
                    if i == adverb:
                        adverbs.remove(adverb)
            for adjective in adjectives:
                for i in not_repeat_jokes:
                    if i == adjective:
                        adjectives.remove(adjective)


print(get_jokes(3, flag=False))