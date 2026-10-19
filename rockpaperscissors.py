#S P,P S, R S,S R ,
import random
choices=["rock","paper","scissors"]
while True:
  num1=random.choice(choices)
  wish=input("Do you want to play with me, Υ for yes and N for no\n").upper()
  if wish=="N":
   print("Bye")
   break
  elif wish=="Y":
    move=input("Insert your choice\n").lower()
    if move not in choices:
      print("move not in choices")
      continue
    if move==num1:
      print("It is a draw")
    elif move=="scissors" and num1=="paper":
      print("You win")
    elif move=="paper" and num1=="scissors":
      print("I win")
    elif move=="rock" and num1=="paper":
      print("I win")
    elif move=="paper" and num1== "rock":
      print("You win")
    elif move=="scissors" and num1=="rock":
      print("I win")
    elif move=="rock" and num1=="scissors":
      print("You win")
  else:
      print("Invalid choice,enter Y or N")
   


      
