import random, time

print('This program will simulate 100 dice rolls. \n\n\n ')


for i in range(0, 100):
    n = i + 1
    rolls = random.randint(1, 6)
    #time.sleep(.25)
    print('roll number:' + str(n) + ': ' + str(rolls))
