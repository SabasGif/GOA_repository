#1) 
def get_numbers():
    count = int(input("How many numbers do you want to enter? "))
    numbers = []  # Using a list to store input numbers

    for _ in range(count):
        num = int(input("Enter a number: "))
        numbers.append(num)

    return numbers

def count_even_odd(numbers):
    even_count = sum(1 for num in numbers if num % 2 == 0)
    odd_count = len(numbers) - even_count
    return even_count, odd_count

if __name__ == "__main__":
    numbers = get_numbers()
    sorted_numbers = sorted(numbers)  
    even_count, odd_count = count_even_odd(numbers)

    print(f"Sorted Numbers: {sorted_numbers}")
    print(f"Total Even Numbers: {even_count}")
    print(f"Total Odd Numbers: {odd_count}")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
for num in numbers:
    if num % 2 == 0:
        print(f"{num} - Number is even")
    else:
        print(f"{num} - Number is odd")


#2)
words = ["apple", "banana", "cherry", "grape", "watermelon", "kiwi", "lemon", "blubary", "carrot", "tomato"]

for word in words[1::2]: 
    print(word)


#3) 
sentence = input("what's your word:")

for index, char in enumerate(sentence, start=1): 
    print(f"{char}-{index}")


#4)
numbers = [1, 2, 3, 4, 5]
reversed_numbers = numbers[::-1]  # სიის შემოტრიალება

print(reversed_numbers)  # [5, 4, 3, 2, 1]

#reverse()-რის Python-ის ჩაშენებული მეთოდი, რომელიც სიის ადგილზევე შემოტრიალებას აკეთებს დამატებითი კოპირების გარეშე.

numbers = [1, 2, 3, 4, 5]
numbers.reverse()  # სიის ადგილზევე შემოტრიალება
print(numbers)  # [5, 4, 3, 2, 1]


#5)
text = "Hello, world!"
print(len(text))

numbers = [10, 20, 30, 40, 50]
print(len(numbers))


#6)
my_list = ["apple", "banana", "cherry", "date", "elderberry"]  # 5 ელემენტიანი სია
my_name = "Saba"  # თქვენი სახელი

for i in range(1, len(my_list), 2):  # range() ქმნის ინდექსებს 1-დან დაწყებული ყოველ მეორე ელემენტზე
    my_list[i] = my_name  # ცვლის ყოველი მეორე ელემენტს თქვენს სახელით

print(my_list)