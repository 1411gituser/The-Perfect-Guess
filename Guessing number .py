import random 
randnumber=random.randint(1,100)
userguess=None
guesses=0

while(userguess!=randnumber):
    userguess=int(input("enter a guess number"))
    guesses+=1

    if(userguess==randnumber):
        print("your guess is correct")

    else:
        if(userguess>randnumber):
            print("your guess is wrong. please enter a smaller number")

        else:
            if(userguess<randnumber):
                print("your guess is wrong. please enter a larger number")

            else:
                     print("none")

print(f"you guessed the number in {guesses} guesses")

with open("hiscore.txt", "r") as f:
    hiscore=(f.read())

if(guesses<hiscore):
    print("you have just broken the previous hiscore")

    with open("hiscore.txt","w") as f:
        f.write(str("guesses"))