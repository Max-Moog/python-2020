from calculator import Calc

def calc_run():
    global antwort
    c = Calc()
    antwort = input('add, subtract, multiply, divide, sum, modulo or stop? ')
    if antwort == "add":
        c.addition()
    elif antwort == "subtract":
        c.subtract()
    elif antwort == "multiply":
        c.multiply()
    elif antwort == "divide":
        c.divide()
    elif antwort == "modulo":
        c.modulo()
    elif antwort == "sum":
        s = c.sum(von, bis)
        print(s)
    elif antwort == "stop":
        c.stop()
    else:
        print("eingabe ist ungültig")

calc_run()
