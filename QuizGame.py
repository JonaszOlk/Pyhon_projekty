def new_game(): #nasze funkcje ktorych bedziemy uzywac do twrzenia quizy
    
    guesses = [] #guesses are empty set
    correct_guesses = 0 #starting value
    question_num = 1 #first question

    for key in questions: #itwill take keys from dic
        print("---------------------")
        print(key)
        for i in options[question_num - 1]: #nested for loop for i in options[index], without it it will print lists 
            print(i)                        #of lists after every question
        guess = input("Enter (A, B, C or D): ") #input of player
        guess = guess.upper() #upper the input
        guesses.append(guess) #add guess to empty set of guesses

        correct_guesses += check_answer(questions.get(key), guess) #increse by the return value of funtion
        question_num += 1 #it will increse question num by 1 for every finished nested loop so we will have next list
    display_score(correct_guesses, guesses)

def check_answer(answer,guess): #function check answer with 2 arguments
    if answer == guess: #if answer(ABCD) == input
        print("CORRECT!")
        return 1
    else:
        print("WRONG!") #if answer is NOT == input
        return 0

def display_score(correct_guesses, guesses):
    print("-----------------------")#just for the looks
    print("RESULTS!") #output
    print("-----------------------")#just for the looks
    print("Answers: ", end="") #output keep in the same lane
    for i in questions: #for key in dict
        print(questions.get(i), end=" ") #print values in one line with answers from above
    print() #break line

    print("Guesses: ", end="") #print guesses without breaking line
    for i in guesses: #for index in guesses collection of inputs from player
        print(i, end=" ") #print inputs in the same line with guesses
    print() #break line

    score = int((correct_guesses/len(questions))*100) #score == integer of correct guesses divided by amount of que
    print("Your score is: " + str(score)+"%") #score changed to sting form int to make it print together

def play_again(): #funkcja play again dodana poza loopami funkcji new game
    response = input("Do you want to play again? (yes/no): ") #input
    response = response.upper() #input in upper case
    
    if response == "YES": #logic of comparing inputs
        return True
    else:
        return False

#Dictionary with our questions as keys and answers as values
questions = { 
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ":"C",
    "Is the earth round?: ": "A"
}
#Lists in list with our possible answers
options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Islnad", "B. Smosh", "C. Monthy Python", "D. SNL"],
           ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]]

new_game() #call function with functions inside

while play_again(): #if function play again return true call function new game again
    new_game() #function is called again

print("BYE!") #if function above is false it will end and output bye!