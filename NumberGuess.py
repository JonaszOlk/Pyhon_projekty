import random #używamy by móc generować losowe liczby

top_of_range = input("Type a number: ") #osoba wpisuje numer, który wyznaczy górną granice losową

if top_of_range.isdigit(): #sprawdzamy czy podane w string jest liczbą
    top_of_range = int(top_of_range) #jeżeli jest to string zmienia się w int, żeby użyć w górnej granicy zakresu
    if top_of_range <= 0: #jeżeli wybrana przez uczestnika jest mniejsza/równa zero wyświetli się wiadomość z dołu
        print("please type a number larger than 0 next time")
        quit() #restartuje po wyświetleniu wiadomości
else: 
    print("Please type a number next time")
    quit()
    
random_number = random.randint(0, top_of_range) #po przejściu przez sprawdzenie z góry generuje się nam range losowych liczb
guesses = 0 #początkowa liczba zgadnięć

while True: #początek loopa po przejściu początkowej regulacji
    guesses += 1 #pry każdym loopie zwiększa liczbę zgadnięć o 1
    user_guess = input("Make a guess: ") #osoba wpisuje swoją próbę
    if user_guess.isdigit(): #jeżeli string zawiera numbers to zmienia się str do int
        user_guess = int(user_guess)
    else: #jeżeli w stringu nie ma liczby dostaje komunikat by wpisać liczbę
        print("Please type a number.")
        continue #powtarzanie loopa

    if user_guess == random_number: #jeżeli zgadnie liczbę to dostaje komunikat o sukcesie i loop jest przerwany
        print("You got it!")
        break
    else:
        print("You got it wrong!") #komunikat gdy nie zgadnie

print("You got it in", guesses, "guesses") #informacja o tym ile zgadnięć zajęło użytkownikowi odgadnięcie



    

