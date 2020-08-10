print("welcome to my game!")
name = input ("What is your name? " )
age = int(input("What is your age? "))

print("Hello", name , "you are", age, "years old")

friends = 10 

#nesting if statements 
if age >= 18: 
  print("you are old enough to play!")
  print("You have", friends ,"friends.")
# i used .lower so the user can input any case of yes
  wants_to_play= input("Do you want to play? ").lower()
  if wants_to_play == "yes":
    print("lets play!")

    pennstate_or_umd = input ("First choice... do you want to attend Penn State or University of Maryland? (Penn State/UMD) ")
    if pennstate_or_umd == "Penn State": 
      ans = input ("Nice choice! Now that you picked Penn State, you have to pick which campus.. Do you want to attend Altoona or Main Campus? (Altoona/Main) ")
      if ans == "Main":
        print("You made it to State College! Here we have the creamery and the football stadium ")
      elif ans == "Altoona":
        print("You made it to campus only to find out you are a few hours away from the football stadium. Your friends can't stay at your place for game days so you lost Five friends")
        friends -= 5
      ans = input ("Do you want to go to a football game or get a milkshake? (Game/shake) ")
      if ans == "Game":
        print("You went to a game with friends and PSU won...but it hailed the entire time. Five of your friends left at halftime and no longer want to hangout after.")
        friends -= 5
        if friends <=0 :
          print ("You have 0 friends. You transfer and lost the game!")
        else:
          print("You were able to stay close with a lot of friends! You win!")
      else: 
        print("Your friends are vegan. You lost them all!")
        
    else: 
      print("Wrong choice... Penn State rocks socks (We Are!)")
  else: 
    print("Cya next time!")
else: 
  print("Sorry, you can't play. Come back when you are older please!")


