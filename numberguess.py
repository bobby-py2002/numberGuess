import random
import math
def user_input():
    global interval
    interval=input("Enter Range[a,b]:\n").split()
    for i in range(len(interval)):
        interval[i]=int(interval[i])
    
   
def rand_num():
    global mul
    global prob
    global x,y
    #mul=random.randint(1,3)
    #prob=random.randint(4,10)
    x=random.randint(interval[0],interval[1])
   # x=y
    
def min_guess():
    return int(math.log(interval[1]-interval[0]+1,1.7))
def is_equal(num):
    if num==x:
        return 0
    elif num>x:
        return 1
    else:
        return -1 

def game():
    user_input()
    rand_num()
    count=0
    print(f"You have {min_guess()} chances to guess")
    while(True):
        num=int(input(f"Enter guessed number between[{interval[0],interval[1]}:\n"))
        count+=1
        if is_equal(num)==0:
            print("\nPrecise!")
            print("You Guessed in",count,"times")
            break
        if(count==min_guess()):
            print("\nGame Over!\nNumber was:",x)
            break
        if is_equal(num)==1:
            print("\nHot!")
        if is_equal(num)==-1:
            print("\nCold!")
        print(f"\nyou have {min_guess()-count} chances left")
game()