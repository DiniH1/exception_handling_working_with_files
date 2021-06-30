# Working with files
## Exception handling
### File permissions

#### Examples of error/exception
- `value error`
- `syntax error`
- `out of bounds`
- `key error`
- `attribute error`
- `ZeroDivisionError`

#### File permissions

- `r` This is the default mode. It opens file for reading
- `w` This mode opens files for writing. If file doesn't exist, it creates a new file for us.
- `x` Creates a new file, if already exists the operation fails
- `a` Opens file in Append Mode, if file doesn't exist, it creates a new one
- `t` This the default mode to open in text mode
- `b` This is for binary mode
- `+` This will open a file for reading and writing (updating)

**We have `try` `except` and `finally`**
- `try` works as `if condition`
- `except` works as `elif`
- `finally` works as `else`, finally will execute regardless of `try` and `except` conditions

# print(1/0) #ZeroDivisionError: division by zero

`num = 9
if num > 8
print(num)` 
- This would throw a syntax error: invalid syntax

## we will create a file with required permission and see what errors/exceptions are possible to be seen
### First iteration
`file = open("order.txt") # open() takes a string arg with file name
print(file)` 
-Let's see the outcome and record it

### Second iteration 
```
try:
    file = open("order.txt")
    print("file found")` # try block required except or will throw an error 
except FileNotFoundError as errmsg:` # creating an alias same as a nickname
    print(f"file not found Panic {errmsg}")` 
finally: # finally will execute regardless of try and except block execution, also used to clean up the code  
    print("Thank you for visiting See you again")
```
# Let's apply 1) DRY - 2) OOP - 3)Python Packaging
## Step One
### Applying DRY through defining a function
```
def exception_handling(self):
    try:
        file = open("order.txt")
        print("file found")
    except FileNotFoundError as errmsg:
            print(f"file not found Panic {errmsg}")
    finally:
            print("Thank you for visiting See you again")
```
## Step Two
### OOP through inheriting from a class
- Creating a class with a function

```class FileHandling:
    def exception_handling(self):
        try:
            file = open("order.txt")
            print("file found")
        except FileNotFoundError as errmsg:
            print(f"file not found Panic {errmsg}")
        finally:
            print("Thank you for visiting See you again")
```
- Inheriting from the class and calling upon the function in the class
``` from file_handling import FileHandling

class file_and_exception_handling(FileHandling):
    pass
open_file = file_and_exception_handling()
print(open_file.exception_handling())
```
## Step Three
- Create a new directory named `app`
- In the new directory create a new `__init__.py` and a new `.py` that holds the code and test it works
```
class filehandling:
    def exception_handling(self):
        prompt_file = input("Name your file ")
        named_file = prompt_file + ".txt"
        try:
            file = open(named_file)
            print("file found")
        except FileNotFoundError as errmsg:
            print(f"file not found Panic {errmsg}")
        finally:
            print("Thank you for visiting See you again")
test = filehandling()
print(test.exception_handling())
```
- Create a file named `program.py` in the main dir and import from the `.py` file created in the app dir. Finally call a function from the `.py` file in the app dir
```
from app.file_exception_handling import filehandling
file_open = filehandling()
print(file_open.exception_handling())
```

