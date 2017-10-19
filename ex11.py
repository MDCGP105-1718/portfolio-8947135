from random import randint

guess =int(input("Guess the number : "))
attempts = 0
y = randint (1,100)
def Ghici(x):
 if x < y :
    print("The number is higher,guess again .")
 elif x > y :
    print("The number is lower,guess again .")

while guess != y  :
     Ghici(guess)
     attempts += 1
     guess = int(input("Guess again : "))

if  guess == y :
    print(f"Correct! The number was {y},and the number of {attempts}  ")
