import random
randNo = random.randint(1,100)
# print(randNo)
UserGuess = 0
guesses = 0
while(UserGuess!=randNo):
    UserGuess=int(input("Enter your Guess "))
    guesses+=1
    if(UserGuess==randNo):
        print("You guessed it right !!")
    else:
        if(UserGuess>randNo):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")

print(f"You guessed the number in {guesses} guesses ")
with open("hiscore.txt") as f:
    hiscore = int(f.read())
if(guesses<hiscore):
    print("You have just broken the high score!")
    with open("hiscore.txt",'w') as f:
        f.write(str(guesses))