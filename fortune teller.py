import random

def fortune():
    userNum = int(len(name))+age
    randomNum = random.randint(1,200)
    fortuneNum = randomNum-userNum

    if fortuneNum < 0 and fortuneNum > -50:
        print('Your future looks negative.')
    elif fortuneNum <= -50:
        print('Your future is hopless.')
    elif fortuneNum == 0:
        print("You're a rare person.")
    elif fortuneNum >= 50:
        print('I wish I was you.')
    else:
        print('Your future is too chaotic to forsee.')
    


print('Let me see your future.')
print('What is your first name?')
name = str(input())
while name =='':
    print('What is your first name?')
    name = str(input())

print('What is your age?')
try:
    age = int(input())
except ValueError:
    print('Error: You tried to type a word instead of number.')
    print("Try again.")
    print("What is your age?")
    age = int(input())
fortune()



    
