import random as rd
import re

# Tabuleiro

Board = ['''
>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# print(Board[6])

class Word():
    file = (open('palavras.txt', 'r'))
    file = file.readlines()
    random = rd.choice(file)
    x = input('Digite uma letra: ')
    def __init__(self,  file = (open('palavras.txt', 'r')).readlines()-1):
        self. file = file
        self.random = rd.choice(file)
    #    print('class creation process completed')

    def fPrint(self):
        z=list(Word.random)
        print(z)

    #Masking random word
    def Mask(self):
        print("-"*(len(Word.random)-1))

    '''def __str__():
        return Word.randomOpen(self)
        
'''
class Compareword(Word):
    x = Word.random
    def __init__(self):
        pass
    def Teste():
        print(Compareword.x)

def wordinput():
    y = list(Word.random)
    w=[z for z in y ]
    for i in range(len(y)):
        if re.search(Word.x, y):
            print(Word.x)
        elif not re.search(Word.x, Word.random):
            for x in range(len(Board)):
                print(Board[x])
                x += 1




Word().fPrint()
Word().Mask()
