import random

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

def test(): # sample random word
    global word
    word = random.sample(list(words),1)[0]
    print(word)

def check(): # display pinyin word
    print(words[word][0])
