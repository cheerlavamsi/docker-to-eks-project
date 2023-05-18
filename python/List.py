import random

numbers = input("Enter the numbers")
numbers_list = numbers.split(",")

for num in numbers_list:
    if int(num) % 2 == 0:
        print(num)

cards = ["A","B","C","D","E","F"]


random.shuffle(cards)

print(cards)