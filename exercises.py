# ex 1

userInput = input("").lower()
print(userInput)


# ex 2

print("...".join(input("").split()))


#  ex 3

def convert(str):
    inputList = str.split()

    for i in inputList:
        if i == ':)':
            index = inputList.index(i)
            inputList.pop(index)
            inputList.insert(index, '🙂')
        elif i == ':(':
            index = inputList.index(i)
            inputList.pop(index)
            inputList.insert(index, '🙁')

    return ' '.join(inputList)

def main():
    print(convert(input("")))


main()


#  ex 4

print(f'E: {int(input("m:")) * 300000000 ** 2}')


#  ex 5



def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    arr = list(d)
    arr.remove('$')
    return float(''.join(arr))

def percent_to_float(p):
    arr = list(p)
    arr.remove('%')
    return float(''.join(arr)) * 0.01

main()
