import random,math

def gambleOnce():
    return random.randint(0,1)

def gambleDay(money):
    if money<1:
        return money
    wager=1
    money -= wager

    while not gambleOnce():
        wager *=2
        money -= wager
        if money <=0:
            return money
        
    money = money + wager*2
    return money

moneyHold = 1024
moneyHolds = []
dayNumber = 3650
for x in range(dayNumber):
    moneyHold=gambleDay(moneyHold)
    moneyHolds.append(moneyHold)
from matplotlib import pyplot as plt
plt.scatter(list(range(1,dayNumber+1)),moneyHolds,s=1)
plt.title(f'Every Day\'s money during {dayNumber} days')
plt.show()