class Dice:
    side=[0,0,0,0,0,0]
    roll=0
    iSides=6
    def __init__(self):
        pass
    def rollDice(self):
        result=random.randint(1,6)
        self.side[result-1]+=1
        self.roll+=1
        return result
    def sideCount(self,i):
        return self.side[i-1]
    def rollCount(self):
        return self.roll
    
import random
random.seed(0)   #设置随机数种子，以便让执行结果固定
d = Dice()
print("-----Roll dice for 100 times-----")
for x in range(100):
    r = d.rollDice()
    if x < 10:
        print(r,end=",") 
print("...")

print("-----Statistics of rolling the dice-----")
for i in range(1,d.iSides+1):
    sideCount = d.sideCount(i)
    rollCount = d.rollCount()
    print(f"Side {i}: {sideCount}/{rollCount} = "\
        f"{sideCount*100/rollCount:.1f}%")