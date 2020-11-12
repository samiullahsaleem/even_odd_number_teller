#Even and Odd Number Teller
while True:
    value = input ("Write your integer or Press 'q' to exit \n")
    if value=="q":
        break
    number = int(value)
    if number%2==0:
        print(str(number)+ " is even")
        continue
    elif number%2!=0:
        print(str(number)+ " is odd")
        continue


exit = input("Press Enter to exit!")
