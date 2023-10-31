print("Welcome to my quiz about me!")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("okay let's play")
score = 0

answer = input("What is my first name? ")
if answer.lower() == "jonasz":
    print("correct")
    score += 1
else:
    print("incorrect!")

answer = input("What is my last name? ")
if answer.lower() == "olkowski":
    print("correct")
    score += 1
else:
    print("incorrect!")

answer = input("When is my birthday? ")
if answer == "28.12":
    print("correct")
    score += 1
else:
    print("incorrect!")

answer = input("What is my dog name? ")
if answer.lower() == "alma":
    print("correct")
    score += 1
else:
    print("incorrect!")

print("You got " + str(score) + " points!")
print("You got " + str((score / 4) * 100) + "%.")