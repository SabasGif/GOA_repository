#შექმენით 3 ელემენტიანი სახელების სია. მომხმარებელს შემოატანინეთ 0-დან 2-ის ჩათვლით ნებისმიერი რიცხვი, სანამ მომხმარებელი არ შემოიტანს რიცხვს საჭირო დიაპაზონში, ხელახლა ვთხოვოთ რიცხვის შემოტანა.(გამოიყენეთ while loop-ი)
#დაბეჭდეთ სახელების სიაში მომხმარებლის მიერ შემოტანილ ინდექსზე მყოფი ელემენტი
names = ["bob","bobertto","boberinio"]
number = int(input("put any number 0 to 2:"))

while number < 0 or number > 2:
    print("the number is out of range. Try again")
    number = int(input("please enter a number 0 to 2:"))

print(names[number])


#2) რატომ გამოიტანს ეს კოდი შეცდომას?

word = "Python"
word[0] = "B"
print(word)

#ახსენით კომენტარით. რადგან, ამ სიტყვაში არარის ასო "B", და ვერც შეცვლი

#3) შექმენით 10 ელემენტიანი რიცხვების სია და slicing-ის გამოყენებით დაბეჭდეთ ყოველი მესამე ელემენტი ამ სიაში

num = [0,1,2,3,4,5,6,7,8,9,10]
print(num[ ::3])

#4) slicing-ის გამოყენებით. იგივე სიიდან დაბეჭდეთ მე-4, მე-7 და მე-10 ელემენტები

num = [1,2,3,4,5,6,7,8,9,10]
print(num[ ::3])