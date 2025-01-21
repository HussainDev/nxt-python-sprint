import random
number=random.randint(1,100) # number generated
print(number)
''''''
print('')
print('Welcome to number guessing game!')
print('')
attemps=int(input('how many attempts do you want -- '))
print('')
if attemps>10:
    attemps=10
    print('you have chosen too many attemps, we will provide you 10')
    print('')
print("game starts now, Guess the choice, so what's your first choice")
print('')
#attempts finalized here
for i in range(attemps):
    ip=int(input())
    if i==(attemps-1) and ip!=number:
        print('')
        print('your attemps have completed and you LOSE')
        print('')
    elif ip>number:
        print('')
        print('its higher try again')
        print('')
        
    elif ip<number:
        print('')
        print('its lower try again')
        print('')
        
    else:
        print('')
        print('congrats you are correct and you WON')
        break

