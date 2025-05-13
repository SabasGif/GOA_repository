password = "nika123"
user_input = input("Please enter a password: ")

while user_input != password:
    print("Inccorect password!")
    user_input = input("Please enter a password: ")
print("Password is correct!")