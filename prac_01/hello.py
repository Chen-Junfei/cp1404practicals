# """
# get number_of_student
# get number_of_gift
# gift_each_student = number_of_gift // number_of_student
# gift_left_over = number_of_gift % number_of_student
# display gift_each_student
# display gift_left_over
# """
#
# number_of_student = int(input("Number of student: "))
# number_of_gift = int(input("Number of gift:"))
# gift_each_student = number_of_gift // number_of_student
# gift_left_over = number_of_gift % number_of_student
# print(f"Each student get {number_of_gift} gifts")
# print(f"{gift_left_over} left over")


# price = float(input("Enter price: $"))
# is_gst = str(input("whether it has GST(y/n): "))
# if is_gst == "y":
#     gst = float(input("Enter GST: $"))
#     price += gst
# print(f"The price is ${price:.2f}")

# number = int(input("Enter number: "))
# for i in range(1,number+1):
#     print(i, end=' ')
# print()
# ordinal = 1
# while ordinal <= number:
#     print(ordinal, end=' ')
#     ordinal += 1

# MAXIMUM = 10
# SECRET = 6
# guess_number = int(input("Guess number: "))
# while guess_number != SECRET:
#     if guess_number > MAXIMUM or guess_number < 0:
#         print("Invalid number!")
#     else:
#         print("Guess again.")
#     guess_number = int(input("Guess number: "))
# print("Bingo!")

# user_name = str(input("Enter your name: "))
# while user_name == ' ':
#     print("Invalid name.")
#     user_name = str(input("Enter your name: "))
# salary = float(input("Enter your salary: "))
# while salary < 0:
#     print("Invalid salary.")
#     salary = float(input("Enter your salary: "))
# print(f"{user_name.upper()}, your salary is ${salary:.2f}")

# number_of_age = int(input("Enter number of ages: "))
# total = 0
# for i in range(number_of_age):
#     age = int(input("Enter age: "))
#     total += age
# average = total / number_of_age
# print(f"Total = {total}, Average = {average}")

# total = 0
# count = 0
# age = int(input("Enter age: "))
# while age != -1:
#     total += age
#     count += 1
#     age = int(input("Enter age: "))
# average = total / count
# print(f"Total = {total}, Average = {average}")


for i in range(1,4):
    for j in range(2,10,3):
        print(i, "-", j + i)
