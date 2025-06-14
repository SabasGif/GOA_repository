number = 0

while number < 6:
    print(number)
    number = number+1

number = 10

while number < 50:
    print(number)
    number = number+2


number = 142
input_number = int(input("what's my number?:"))
while number == input_number:
    print("you win")
else:
    print("your wronge")

number = 141
input_number = int(input("what's my second number?:"))
while number == input_number:
    print("you win")
else:
    print("your wronge")

number = 140
input_number = int(input("what's my third number?:"))
while number == input_number:
    print("you win")
else:
    print("you loose")