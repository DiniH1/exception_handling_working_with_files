# print(1/0) #ZeroDivisionError: division by zero
#
# num = 9
# if num > 8 # This would throw a syntax error: invalid syntax
#     print(num)

# we will create a file with required permission and see what errors/exceptions are possible to be seen
# first iteration
# file = open("order.txt") # open() takes a string arg with file name
# print(file) # Let's see the outcome and record it

#  Second iteration
# try:
#     file = open("order.txt")
#     print("file found") # try block required except or will throw an error
# except FileNotFoundError as errmsg: # creating an alias same as a nickname
#     print(f"file not found Panic {errmsg}") #
# finally: # finally will execute regardless of try and except block execution, also used to clean up the code
#     print("Thank you for visiting See you again")

# Let's create a file called order.txt - naming is essential so ensure the names match

# Let's apply DRY - OOP - Python Packaging
#              1     2           3

from file_handling import FileHandling

class file_and_exception_handling(FileHandling):
    pass
open_file = file_and_exception_handling()
print(open_file.exception_handling())

