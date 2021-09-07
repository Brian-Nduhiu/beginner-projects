

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
        print("Invalid")
        return False

    else:
        return True


def cardtype(num):

    if len(num) == 15 and (int(num) >= 340000000000000 and int(num) < 350000000000000) or (int(num) >= 370000000000000 and int(num) < 380000000000000):
        print("American Express")

    elif len(num) == 16 and (int(num) >= 5100000000000000 and int(num) < 5600000000000000):
        print("Mastercard")
    elif (len(num) == 13 or len(num) == 16) and (int(num) >= 4000000000000 and int(num) < 5000000000000) or (int(num) >= 4000000000000000 and int(num) < 5000000000000000):
        print("Visa")
    else:
        print("Invalid")


ccnum = input("Enter Credit Card number:")
if checksum(ccnum):
    cardtype(ccnum)
