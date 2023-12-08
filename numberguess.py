import random as r

def rand_num():
    global mul
    global prob
    global x,y
    mul=r.randint(1,3)
    prob=r.randint(4,10)
    y=r.randint(1,10**mul)
    x=y
    if mul>=2:
        if prob <=5:
            pass
        else:
            x=r.randint(int(0.4*(10**mul)),10**mul)
    else:
        pass
    
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
    while(True):
        num=int(input(f"Enter guessed number between[{1,10**mul}]:\n"))
        count+=1
        if is_equal(num)==0:
            print("\nPrecise!")
            print("You Guessed in",count,"times")
            break
        elif is_equal(num)==1:
            print("Hot!")
        else:
            print("Cold!")

game()