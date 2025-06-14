#1)
#.upper() და .lower() სასარგებლოა ტექსტის სტანდარტიზაციისთვის, მაგალითად, ვრცელი სტრიქონების შედარების დროს.
#.capitalize() გამოსადეგია, როცა გინდა ტექსტის სათაური სწორად გამოაჩინო.
#.find() საშუალებას გაძლევს, მოძებნო ტექსტში კონკრეტული სიტყვა ან სიმბოლო და გაიგო, სად მდებარეობს იგი.


#2)
word = input("please put your word here:")
print(word.lower())


#3)
Gmail = input("put your Gmail here:")

if Gmail.find("@") == -1:
    print("It's not a exiscting Gmail. Please try another")
else:
    print(Gmail.upper())


#4)
book_name = input("put the title here:")
print(book_name.title())


#5)
sentence = input("insurt sentenc with simbole here: ")
char = input("incurt the simble here: ")
count = sentence.count(char)
print(f"simbole '{char}' {count} times in the sentence")


#6)
word = input("put the word here: ")
if word.upper():
    print("its already uppercase")
else:
    print("now it is:", word.upper())