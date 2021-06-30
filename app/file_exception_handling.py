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

