Calculating = True

while Calculating:
    print("Start")
    calculator= input("Select your operation\nSelect['+','-','*','/']: ")

    try:
        no1 =float(input('first number: '))
        no2 =float(input('second number: '))

    except:
        print('invalid input')
        continue

    
    if calculator == "+":
        print(no1 + no2)

    elif calculator == "-":
        print(no1 - no2)

    elif calculator == '*':
        print(no1 * no2)

    elif calculator == '/':
        print(no1 / no2)

    else:
        print('invalid operation')
     

    choice = input("Again? ['y','n']")
    if choice== 'y':
        pass

    if choice == 'n':
        Calculating = False 




print("I'm the best")