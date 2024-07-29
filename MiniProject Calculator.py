first = input("Enter a First No. :")
operator = input("Enter Operator (+ , - , * , /)")
second = input("Enter a Second No. :")

first = int(first)
second = int(second)

if operator == "+" :
    print(first + second)
elif operator == "-" :
    print(first - second)
elif operator == "*" :
    print(first * second)
elif operator == "/" :
    print(first / second)
else :
    print("Invalid Value")