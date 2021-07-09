import random
import unittest

class program():

    def start_game(self):
        antwort = input(" Type easy, hard or quit: ")
        if antwort == "easy":
            easy()
        if antwort == "hard":
            hard()
        else: play_again()

    def easy(self):
        secret = int(random.randint(1,5))
        antwort2 = int(input("Choose a number between 1 and 5: "))
        print(antwort2)

        if antwort2 == secret:
            antwort3 = input('Congratulations! You have won! Type P-A to play again: ')

        if antwort3 == "P-A":
            play_again()
        else:
            antwort3 = input("You have lost! Type P-A to play again: ")

        if antwort3 == "P-A":
            play_again()


    def hard(self):
        secret = int(random.randint(1, 50))
        antwort2 = int(input("Choose a number between 1 and 50: "))
        print(antwort2)

        if antwort2 == secret:
            antwort3 = input('Congratulations! You have won! Type P-A to play again: ')

        if antwort3 == "P-A":
            play_again()

        else:
            antwort3 = input("You have lost! Type P-A to play again: ")

        if antwort3 == "P-A":
            play_again()


    def play_again(self):
        start_game(self)


start_game()

if __name__ == '__main__':
    unittest.main()
