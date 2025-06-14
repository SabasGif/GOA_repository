
Positive_numberscount = 0
Negative_numberscount = 0

for i in range(5):
    num = int(input("plese enter your number:"))

    if num > 0:
        Positive_numberscount = Positive_numberscount + 1
    elif num < 0:
        Negative_numberscount = Negative_numberscount + 1

print("Positive numbers count:" + str(Positive_numberscount))
print("Negative numbers count:" + str(Negative_numberscount))




number = int(input("Please enter one number:"))
num = True

for i in range(2, number):
    if number % i == 0:
        num = False

if num:
    print("It's a prime number")
else:
    print("It's not a prime number")
