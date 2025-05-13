#binary code- ციფრული ენა, რომელიც იყენებს მხოლოდ ორი ტიპის სიმბოლოს—0 და 1—to represent information. ეს არის კომპიუტერების და ელექტრონული მოწყობილობების საფუძველი, რადგან ისინი ინფორმაციას ამგვარად ინახავენ, ამუშავებენ და გადაცემენ.


#ლოგიკური ოპერატორები გამოიყენება ლოგიკური გამოთვლებისთვის და სიმართლე/ტყუილის (True/False) შეფასებისთვის. 
#მაგალითები:


print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False

print(True or True)    # True
print(True or False)   # True
print(False or True)   # True
print(False or False)  # False

print(not True)  # False
print(not False) # True

print(True != True)   # False (ორივე ერთნაირია)
print(True != False)  # True
print(False != True)  # True
print(False != False) # False


email = str(input("enter your email: "))
password = str(input("enter your password:"))

print("someone@gmail.com" != email)
print("abcd1234" != password)