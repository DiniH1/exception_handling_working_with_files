class FileHandling:
    def exception_handling(self):
        try:
            file = open("order.txt")
            print("file found")
        except FileNotFoundError as errmsg:
            print(f"file not found Panic {errmsg}")
        finally:
            print("Thank you for visiting See you again")

test = FileHandling


