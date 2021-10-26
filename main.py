import random
isRight = 0
playerPick = 0
firstLoop = 1
print ("Hello welcome to my number guessing game.\nYou'll guess first then I'll guess.\nWe'll see who guessed in fewer tries.")
while isRight == 0:
  if firstLoop == 1:
    computerNumber = random.randint(1,10)
    playerPick = int(input("I have selected a random number, guess from 1-10\n"))
    firstLoop = 0
  elif firstLoop == 0:
    playerPick = int(input("Try again, the number is the same, pick 1-10\n"))
  if playerPick == computerNumber:
   isRight = 1
