import random

global words
words = { 'good; fine':  ['hǎo'],
          'you':  ['nǐ'],
          'How are you?':  ['nǐ hǎo ma?'],
          'I':  ['wǒ'],
          'Very well':  ['hěn hǎo'],
          'I am fine.':  ['wǒ hěn hǎo'],
          'And you?':  ['nǐ ne?'],
          'Not bad':  [''],
          'question particle':  ['ma?'],
          'thanks': ['xièxie'],
          'you are welcome': ['bù kèqì'],
          'excuse me; I am sorry': ['duìbùqǐ'],
          'It is nothing; do not worry; no problem': ['méi shì'],
          'goodbye': ['zàijiàn']
          }


global word
word = random.sample(list(words),1)[0]

def reset():
    global word
    word = random.sample(list(words),1)[0]

def english(): # sample random word
    global word
    print(word)

def chinese(): # display pinyin word
    global word, words
    print(words[word][0])
