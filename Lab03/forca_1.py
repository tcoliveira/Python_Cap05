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
    def __init__(self,  file = (open('palavras.txt', 'r')).readlines()):
        self. file = file
        self.random = rd.choice(file)
    #    print('class creation process completed')

    def fPrint(self):
        print(Word.random)

    def Mask(self):
        print("-"*(len(Word.random)))

    '''def __str__():
        return Word.randomOpen(self)
'''
Word().fPrint()
Word().Mask()
