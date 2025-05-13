
name = input(" your name: ")
age = input(" your age: ")
your_curent_age = "12"
your_name = "Saba"

if your_curent_age == age: 
    print("it's your age")
else:
    print("is not age")

if your_name == name and your_curent_age == age:
    print("and")
else:
    print("but")

if your_name == name:
    print("it's your name")
else:
    print("it's not your name")



my_name_is = "Saba"
your_name_input = input("wats your name?:")

if my_name_is == your_name_input:
    print("coincidence")
else:
    print("ok")



score = input("wats your score?:")

if score >= 70:
    print("passed")
else:
    print("failed")



the_score = input("what's your score?:")

if the_score >= 80:
    print("your score A")
elif the_score >= 60:
    print("your score B")
elif the_score >= 40:
    print("your score C")
elif the_score >= 20:
    print("your score D")
elif the_score <= 20:
    print("your score F")



#ინსტრუქციების თანმიმდევრობა, რომელიც გამოიყენება კონკრეტული ამოცანის გადასაჭრელად ან პრობლემის მოსაგვარებლად. ის შეიძლება იყოს მარტივი ან რთული, მაგრამ ყოველთვის უნდა იყოს ზუსტი და ცხადი.

#მაგალითად:
#   1- აიღეთ რიცხვების სია (მაგალითად: [5, 3, 8, 6]).

#   2- შეადარეთ პირველი ორი რიცხვი:- თუ პირველი რიცხვი მეტია მეორეზე, გაცვალეთ მათი ადგილები.

#   3- გადადით შემდეგ წყვილზე და გაიმეორეთ იგივე პროცესი.

#   4- გაიმეორეთ ნაბიჯები მანამ, სანამ სია სრულად არ დალაგდება.

#   5-დალაგებული სია იქნება: [3, 5, 6, 8].