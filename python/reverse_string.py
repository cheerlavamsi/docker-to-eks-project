## Program 1
string = input("Enter the string")

Rstring = string[::-1]

print(Rstring)

## Program 2

num = input("Enter the numbers")
num_list = num.split(",")

for num in num_list:
    if int(num) % 2 != 0:
        print(num)
