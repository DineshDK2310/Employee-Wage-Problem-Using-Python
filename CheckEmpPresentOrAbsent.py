import random


def attendance(randomNumbers):
    if randomNumbers == 1:
        return "Employee is present"
    else:
        return "Employee is Absent"

if __name__ =="__main__":
    random=random.randint(0,1)
    attendance=attendance(random)
    print(attendance)

