# 1.Write code that asks the user for their name, then opens a
# file called name.txt and writes that name to it. Use open and close for this question.
FILENAME = "name.txt"
name = input("Enter your name: ")
out_file = open(FILENAME, "w")
out_file.write(name)
out_file.close()

# 2.In the same file, but as if it were a separate program, write code that opens "name.txt"
# and reads the name (as above) then prints (note the exact output),
# Hi Bob! (or whatever the name is in the file). Do not simply print the user's input variable!
# Use open and close for this question.
in_file = open(FILENAME, "r")
read_name = in_file.read()
in_file.close()
print(read_name)

# 3.Create a text file called numbers.txt and save it in your prac directory.
# Put the following three numbers on separate lines in the file and save it:
# 17
# 42
# 400
# Write code that opens numbers.txt, reads only the first two numbers,
# adds them together then prints the result, which should be... 59.
# Use with instead of open and close for this question.
out_file = open("number.txt","w")
out_file.write("17\n42\n400")
out_file.close()
in_file = open("number.txt", "r")
number_1 = int(in_file.readline())
number_2 = int(in_file.readline())
in_file.close()
result = number_2 + number_1
print(result)

# 4.Now write a fourth block of code that prints the total for all lines in numbers.txt.
# This should work for a file with any number of numbers. Use with instead of open and close for this question.
with open("number.txt", "r") as in_file:
    for line in in_file:
        print(line)