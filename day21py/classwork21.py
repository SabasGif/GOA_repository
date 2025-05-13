for i in range(11):  # for i in range(10+1):  
  print(i)             #print(i)

for i in range(10):
  print(i)

for i in range(20,100):
  print(i)

for i in range(0,20,2):
  print(i)

for i in range(30,50,4):
  print(i)



#for i in range(1,10+2):    #+2 to count
#  print(i)

#for i in range(1,10,2):    #-2 allways
#    print(i)


#5) მომხარებელს შემოატანინეთ რიცხვი. შეამოწმეთ, თუ შემოტანილი რიცხვი არის ლუწი დაბეჭდეთ "The numbers is even", სხვა შემთხვევაში დაბეჭდეთ "The number is odd"


your_number_input = input("wats your number?:")
for i in range(0,100,2):
    print(i)

if your_number_input == i:
    print("the number is even")
else:
    print("the number is odd")