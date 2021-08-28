

def checksum(num):
    sum = 0
    length = len(num)
    switch = True
    for index in range(length, 0, -1):

        if switch:
            sum += int(num[index - 1])
            switch = False
        else:
            tempnum = int(num[index - 1]) * 2
            if tempnum >= 10:
                sum += tempnum % 10
                tempnum /= 10
                sum += int(tempnum)
            else:
                sum += tempnum
            switch = True

    if sum % 10 != 0:
        return False
    else:
        return True


def cardtype(num):
    print("this is cardtype")


ccnum = input("Enter Credit Card number:")
if checksum(ccnum):
    cardtype(ccnum)
