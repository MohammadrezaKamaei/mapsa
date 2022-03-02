import random
count = 1
num = (random.randint(1,20))
guess = int(input("Guess a number:- "))
if guess == num:
  print("You Win")
while guess != num:
  guess = int(input("Guess a number:- "))
  count += 1
  if count == 5:
    print(num)
    print ("Game Over")
    break