import random as rd

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
    def __init__(self,  file = (open('palavras.txt', 'r')).readlines()):
        self. file = file
        self.random = rd.choice(file)
    #    print('class creation process completed')

    def fPrint(self):
        print(Word.random)

    #Masking random word
    def Mask(self):
        print("-"*(len(Word.random)-1))

    '''def __str__():
        return Word.randomOpen(self)
        
'''
    def wordinput(self):
        if Word.x == Word.random:
            print(1)
        else:
            print(2)

class Compareword(Word):
    x = Word.random
    def __init__(self):
        pass
    def Teste():
        print(Compareword.x)



Word().fPrint()
Word().Mask()
Word.wordinput()
