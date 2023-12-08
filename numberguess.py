import random
import math

def rand_num():
    global mul
    global prob
    global x,y
    mul=random.randint(1,3)
    prob=random.randint(4,10)
    y=random.randint(1,10**mul)
    x=y
    if mul>=2:
        if prob <=5:
            pass
        else:
            x=random.randint(int(0.4*(10**mul)),10**mul)
    else:
        pass
def min_guess():
    return int(math.log(10**mul,1.4))
def is_equal(num):
    if num==x:
        return 0
    elif num>x:
        return 1
    else:
        return -1 

def game():
    rand_num()
    count=0
    print(f"You have {min_guess()} chances to guess")
    while(True):
        num=int(input(f"Enter guessed number between[{1,10**mul}]:\n"))
        count+=1
        print(f"\nyou have {min_guess()-count} chances left")
        if is_equal(num)==0:
            print("\nPrecise!")
            print("You Guessed in",count,"times")
            break
        if(count==min_guess()):
            print("\nGame Over!")
            break
        if is_equal(num)==1:
            print("\nHot!")
        if is_equal(num)==-1:
            print("\nCold!")
game()