import random
options=["rock","paper","scissor"]
user=input("Enter your choice:").lower()
computer=random.choice(options)
print("computer choose",computer)
if user=='rock'and computer=='scissor':
    print("user wins!")
elif user=='paper'and computer=='scissor':
    print("computer wins!")
elif user=='scissor'and computer=='scissor':
    print("game is tie now!")
elif user=='rock' and computer=='paper':
    print("computer wins!")
elif user=='scissor' and computer=='paper':
    print("user wins!")
elif user=='paper' and computer=='paper':
    print("game is tie now!")
elif user=='scissor' and computer=='rock':
    print("computer wins!")
elif user=='paper' and computer=='rock':
    print("user wins!")
elif user=='rock' and computer=='rock':
    print("game is tie now!")
else:
    print("invalid choice")
again=input("play again(yes,no)").lower()
if again!="yes":
    print("Thanks for playing")
else:
    print("play again")
