import time
print("---------1")
answer = int(input("What is 2+2?: "))
while answer < 4 or answer > 4:
    print("Wrong!")
    answer = int(input("What is 2+2?: "))
if answer == 4:
    print("Good Job!")
    time.sleep(1)
    print("---------2")
    time.sleep(1)
answer2 = int(input("What is 2 Times 3?: "))
time.sleep(1)
while answer2 < 6 or answer2 > 6:
    print("You'll get em next time!")
    answer2 = int(input("What is 2 Times 3?: "))
if answer2 == 6:
    print("Wow your a Natural!!")
    time.sleep(1)
    print("---------3")
    time.sleep(1)
answer3 = int(input("What is 3 divided by 3?: "))
time.sleep(1)
while answer3 < 1 or answer3 > 1:
    print("Wow you suck!")
    answer3 = int(input("What is 3 divided by 3?: "))
if answer3 == 1:
    print("Genius! absolute Genius!")
    time.sleep(1)
    print("---------4")
    time.sleep(1)
answer4 = int(input("What is 20 times 4?: "))
time.sleep(1)
while answer4 < 80 or answer4 > 80:
    print("Fucking Moron!")
    answer4 = int(input("What is 20 times 4?: "))
if answer4 == 80:
    print("Breathtakingly Intelligent!")
    time.sleep(1)
    print("---------5")
    time.sleep(1)
answer5 = int(input("What is 100 divided by 4?: "))
time.sleep(1)
while answer5 < 25 or answer5 > 25:
    print("Your a Real Bloody Genius You know that? ")
    answer5 = int(input("What is 100 divided by 4?: "))
if answer5 == 25:
    print("Brilliant, just Brilliant!")
    time.sleep(1)
    print("---------6")
    time.sleep(1)
answer6 = int(input("What is 250 divided by 10?: "))
time.sleep(1)
while answer6 < 25 or answer6 > 25:
    print("lost cause!!")
    answer6 = int(input("What is 250 times 10?: "))
if answer6 == 25:
    print("A God! A GOD I SAY!")
    time.sleep(1)
    print("---------7")
    time.sleep(1)
answer7 = int(input("What is 10000 times 2?: "))
time.sleep(1)
while answer7 < 20000 or answer7 > 20000:
    print("i wish i had never met you!")
    answer7 = int(input("What is 10000 times 2?: "))
if answer7 == 20000:
    print("Truly you have changed my life mate, Thank you!")
    time.sleep(1)
    print("---------8")
    time.sleep(1)
answer8 = int(input("What is 123 times 10?:"))
time.sleep(1)
while answer8 < 1230 or answer8 > 1230:
    print("Damn it! its like your trying to be a fucking Idiot!")
    answer8 = int(input("What is 123 times 10?:"))
if answer8 == 1230:
    print("Almost there mate! Just a couple more!")
    time.sleep(1)
    print("---------9")
    time.sleep(1)
answer9 = int(input("What is 4 squared?: "))
time.sleep(1)
while answer9 < 16 or answer9 > 16:
    print("Well i guess this is it.........you have chosen Death")
    time.sleep(1)
    answer9 = int(input("What is 4 squared?: "))
if answer9 == 16:
    print("time for the final Boss.......")
    time.sleep(1)
    print("---------10")
    time.sleep(1)
answer10 = int(input("What is 223444 times 23?: "))
while answer10 < 5139212 or answer10 > 5139212:
    print("Ha! SUFFER VILE HUMAN!.....Die!")
    answer10 = int(input("what is 223444 times 23?: "))
if answer10 == 5139212:
    print("wow.........y-you actually did it!")
    time.sleep(1)
    print("i have been defeated, Goodbye")
    time.sleep(1)
    print(".........")
    time.sleep(1)
question = str(input("How did you like the game?"))
time.sleep(1)
if question == "good":
    print(" ")
    print("im glad you enjoyed it! now let the countdown begin!")
elif question == "bad":
    print("im sorry to hear that! here's a fun little for loop countdown")
elif question == "great":
    print("Thanks! i had a Great time making it!")
else:
    print("Thanks for playing! now let the countdown begin!")
for i in range(11):
    print(i)
    time.sleep(1)
if 1 == 1:
    print("Happy New Year!")
    time.sleep(1)
quit()