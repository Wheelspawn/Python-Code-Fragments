import random

words = { 'good; fine': ['hǎo'],
          'you': ['nǐ'],
          'How are you?': ['nǐ hǎo ma?'],
          'I': ['wǒ'],
          'Very well': ['hěn hǎo'],
          'I am fine.': ['wǒ hěn hǎo'],
          'And you?': ['nǐ ne?'] }

global word
word = random.sample(list(words),1)[0]

def test(): # sample random word
    global word
    word = random.sample(list(words),1)[0]
    print(word)

def check(): # display pinyin word
    print(words[word])
