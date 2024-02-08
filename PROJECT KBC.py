import random
import os
from termcolor import colored
questions = [
        ["What is the capital of France?", "Paris", "Berlin", "Rome", "London", 1],
        ["What is the largest planet in the solar system?", "Earth", "Jupiter", "Saturn", "Neptune", 2],
        ["Who wrote the novel '1984'?", "George Orwell", "Aldous Huxley", "Ray Bradbury", "J.R.R. Tolkien", 1],
        ["What is the name of the longest river in the world?", "Amazon", "Nile", "Yangtze", "Mississippi", 2],
        ["What is the name of the smallest bone in the human body?", "Stapes", "Hammer", "Anvil", "Cochlea", 1],
        ["What is the name of the largest bone in the human body?", "Femur", "Humerus", "Tibia", "Fibula", 1],
        ["What is the name of the process by which plants make their own food?", "Photosynthesis", "Respiration", "Transpiration", "Fermentation", 1],
        ["What is the name of the largest animal in the world?", "Blue whale", "Elephant", "Giraffe", "Dinosaur", 1],
        ["What is the name of the smallest country in the world?", "Vatican City", "Monaco", "Maldives", "Singapore", 1],
        ["What is the name of the currency used in Japan?", "Yen", "Dollar", "Euro", "Pound", 2],
        ["What is the name of the sport that involves hitting a shuttlecock over a net?", "Badminton", "Tennis", "Squash", "Volleyball", 1],
        ["What is the name of the instrument that measures atmospheric pressure?", "Barometer", "Thermometer", "Hygrometer", "Anemometer", 1],
        ["What is the name of the art of folding paper into various shapes?", "Origami", "Kirigami", "Calligraphy", "Pottery", 1],
        ["What is the name of the branch of mathematics that deals with shapes and angles?", "Geometry", "Algebra", "Calculus", "Trigonometry", 1],
        ["What is the name of the imaginary line that divides the earth into two hemispheres?", "Equator", "Prime meridian", "Tropic of Cancer", "Tropic of Capricorn", 1]
    ]

option ={"a":1, "b":2, "c":3, "d":4, "quit":"quit"}

won=[0,100,200,400,800,1600,3200,6400,12800,25600,51200,102400,204800,409600,819200,1638400]

final_questions=[]
for x in range(len(questions)):
    q = random.choice(questions)
    questions.remove(q)
    final_questions.append(q)

print("There'll be 15 questions also there's a safe spot after every 5 questions. But, first 5 questions and Question # 13 are safe.\nYou'll not lose your previous money if you are at safe spot.")
print("(~) Means Safe Spot. List of Money Prizes:-")

prize=100
for j in range (1,16):
    if (j<=5 or j%5==0 or j==13):
        print(f"~ {j}) {prize}$")
        j=j+1
        prize=prize*2
    else:
        print(f"  {j}) {prize}$")
        j=j+1
        prize=prize*2

print("You'll only recieve price 409600$ if you gave wrong answer at Question # 14. If you don't want to loss your amount you can quit whenever you want. BEST OF LUCK!!!!")

yes_quit=input("Are you Ready to start? Enter \"y\" to enter or \"quit\" to exit: ")
yes_quit=yes_quit.lower()
try:
    if(yes_quit=="quit"):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Thanks for Coming.")
    elif(yes_quit=="y"):
        for i in range(0,15):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Total amount won Before this question: {won[i]}$")
            question=final_questions[i]
            print(f"Question # {i+1}:")
            print(question[0])
            print(f"a) {question[1]}             b) {question[2]}")
            print(f"c) {question[3]}             d) {question[4]}")
            if(4<i<9 or 9<i<12 or i==13):
                print(colored("Disclaimer: ","red", attrs=["bold"]),"You are not at safe spot. You'll loose your money to previous safe spot if you answered this question wrong.If you don't wanna lose it quit to exit.")
            while True:
                try:
                    reply=input("Enter Your Answer (a,b,c,d or quit to exit): ")
                    reply=reply.lower()
                    if(reply=="a" or reply=="b" or reply=="c" or reply=="d"):
                        reply_int=option[reply]
                    if (reply == "quit"):
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f"Thanks For Coming. Your Total Amount won : {won[i]}$")
                        break
                    elif (reply == "a" or reply == "b" or reply == "c" or reply == "d"):
                        if(reply_int==question[-1]):
                            print("Correct Answer!")
                            print(f"Total amount won after this question : {won[i+1]}$")
                            won=won*2
                            if (i<14):
                                continue_or_not=input("You want to continue or Exit (y/quit): ")
                            continue_or_not=continue_or_not.lower()
                            if(continue_or_not=="quit"):
                                print(f"Thanks For Coming. Total amount won : {won[i+1]}$")
                                break
                            break
                        elif (reply == "a" or reply == "b" or reply == "c" or reply == "d"):
                            if(reply_int!=question[-1]):
                                print("Hard Luck Wrong Answer :(")
                                if(i==0):
                                    print(f"Total amount won : {won[0]}$")
                                    break
                                elif (i<4 or (i+1)%5==0 or i==12):
                                    print(f"Total amount won : {won[i+1]}$")
                                    break
                                elif(i==10 or i==11 or i==13):
                                    print(f"Total amount won : {won[10]}$")
                                    break
                                elif(i==5 or i==6 or i==7 or i==8):
                                    print(f"Total amount won : {won[5]}$")
                                    break
                    else:
                        raise ValueError
                except ValueError:
                    print("\033[A\033[A")
            if (reply=="quit"):
                break     
            elif(reply_int!=question[-1] and i==0):
                break
            elif (continue_or_not=="quit"):
                break   
            elif (reply == "a" or reply == "b" or reply == "c" or reply == "d"):
                if(reply_int!=question[-1]):
                    break  
        if(i==14 and reply_int==question[-1]):
            print(colored("Congratulation You have answered all the questions correct!!!!!!","green",attrs=["bold"]))
    else:
        raise ValueError
except ValueError:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Your Input Must be Quit or Y only")