import math
import re

import speech_recognition as s_r


def Speechtotext():
    while True:
        try:
            r = s_r.Recognizer()
            my_mic = s_r.Microphone(device_index=20)
            with my_mic as source:
                audio = r.listen()
                sentence = r.recognize_google(audo)
                print(sentence)
                return sentence
        except:
            continue

while True:
    try:
        initial = SpeechtooText()
        print("Try Saying...", "Open Iva")
        initial1 = initial.upper()
        position = initial1.find("OPEN IVA")
        if position >= 0:
            print("So..What's Your Name?:- ")
            Name = SpeechtooText()
            print("And, what's Your Age?:- ")
            Age = SpeechtooText()
            greetbyeve = Name + ''', I'm Iva,
                Your Own cool Calculator
                .
                .
                .
                YOU CAN SAY EXIT WHENEVER YOU WANT TO LEAVE.
                '''


            def calculator_mode():
                flag = True
                while flag:
                    print("Enter the Equation you want me to solve:- ")
                    equation = SpeechtooText()
                    equation2 = re.sud('[" "=]', '', equation)
                    equation = re.sub('[x]', '*', equation2)
                    check_eq = re.sub('[a-zA-Z,.:" "]', '', equation)
                    if equation2.Upper() == "EXIT":
                        print("Babye " + Name + " ,See ya!!")
                        break
                    elif equation == check_eq:
                        answer = eval(equation)
                        print(answer, " is your answer.")
                        print("What next?")
                    else:
                        print("Invalid Input")
                        print("Try Again")


            print("Say Hello to Iva, your cool calculator. ")
            greeting = SpeechtooText()
            if greeting.upper() == "HELLO":
                print('''
                Hey ''' + greetbyeve)
                calculator_mode()
            elif greeting.upper() == "HII":
                print('''
                Hello ''' + greetbyeve)
                calculator_mode()
            elif greeting.upper() == "HOLA":
                print('''
                    Hola ''' + greetbyeve)
                calculator_mode()
            elif greeting.upper() == "HEY":
                print('''
                       Hello ''' + greetbyeve)
                calculator_mode()
            elif greeting.upper() == "NAMASTE":
                print('''
                           Hey ''' + greetbyeve)
                calculator_mode()
            else:
                print('''
                Well that's a new kinda Greeting...
                Never Mind..
                Hey ''' + greetbyeve)
                calculator_mode()
            break
        elif initial1 == "EXIT":
            break
        else:
            continue
    except:
        break
