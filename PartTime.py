import random

def addPartTime(randomNumbers):
    if randomNumbers == 1:
        Emp_Wage=8*20
    elif randomNumbers == 0:
        Emp_Wage=4*20
    else:
        Emp_Wage=0

    return Emp_Wage

if __name__ == "__main__":
    random=random.randint(0,2)
    calculateEmpWage=addPartTime(random)
    print(calculateEmpWage)