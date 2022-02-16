import random
def rand(x, y, cnt, name):
    if y != x:
        print("Your guess is too low.")
        print("Take a guess.")
    else:
        print("Good job, " + name + "! You guessed my number in " + str(cnt) + " guesses!")
    
print("Hello! What is your name?")
name = input()
print("Well" + ", " + name + ", " + "I am thinking of a number between 1 and 20.")
print("Take a guess.")
x = random.randint(1, 20)
y = random.randint(1, 20)
cnt = 1
while True:
    y = random.randint(1,20)
    print(y)
    rand(x,y,cnt, name)
    cnt += 1
    if y == x:
        break