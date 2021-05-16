import random
import sys
import os


def calcbuilder():

    print("Hallo und willkommen zu meinem kleinen Rechenspiel.")
    print("Beantworte immer die Fragen und drück dann Enter.")
    print("Wenn du aufhören willst, antworte q bei der nächsten Frage, und schon hört das Spiel auf.")
    print("Viel Spaß! :)      Spiel wurde erstellt von Daris Kadic")
    while 1 == 1:
        x1 = 100
        x2 = 100
        while x1 + x2 >= 20 or x1 + x2 <= 10:
            x1 = random.randrange(0, 20)
            x2 = random.randrange(0, 20)
        true_result = str(x1 + x2)
        inptores = input("was ist " + str(x1) + " + " + str(x2) + "?   ")
        if inptores == "q":

            break
        if true_result == inptores:
            print("Yaaay richtig!!!")
        else:
            print("Falsch, nächstes mal schaffst du es richtig!")
        input("Drück Enter um weiter zu machen")
        # print(x1)
        # print(x2)
        # print(x1 + x2)

    def clear():
        os.system('cls')
    clear()
    raise SystemExit


calcbuilder()
