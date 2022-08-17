import random

def dailyWage(randomNumbers):
    if randomNumbers ==   1:
        Emp_Wage=8*20
    else:
        Emp_Wage=0

    return Emp_Wage

if __name__ == "__main__":
    random=random.randint(0,1)
    calculateWage=dailyWage(random)
    print(calculateWage)