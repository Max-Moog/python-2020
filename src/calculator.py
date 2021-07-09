# 1) Schreibe eine Funktion für subtraction, multiplication, division, modulo mit Integer Zahlen
# 5 % 2 =  1
# def calc_run():
# op = input('add, subtract, multiply, divide, or modulo?')
# if elif
class Calc:

    def addition(self):
        number_1 = float(input("Gebe die erste zahl ein: "))
        number_2 = float(input("Gebe die zweite zahl ein: "))
        print(number_1 + number_2)


    def subtract(self):
        number_1 = float(input("Gebe die erste zahl ein: "))
        number_2 = float(input("Gebe die zweite zahl ein: "))
        print(number_1 - number_2)


    def multiply(self):
        number_1 = float(input("Gebe die erste zahl ein: "))
        number_2 = float(input("Gebe die zweite zahl ein: "))
        print(number_1 * number_2)


    def divide(self):
        number_1 = float(input("Gebe die erste zahl ein: "))
        number_2 = float(input("Gebe die zweite zahl ein: "))
        print(number_1 + number_2)


    def modulo(self):
        number_1 = float(input("Gebe die erste zahl ein: "))
        number_2 = float(input("Gebe die zweite zahl ein: "))
        print(number_1 % number_2)


    def sum(self, von, bis):
        summe = 0
        for i in range(von, bis):
            summe += i
        return summe


    def stop(self):
        quit()

