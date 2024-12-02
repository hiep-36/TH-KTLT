class StringHandler:
    def __init__(self):
        self.user_string = ""

    def get_String(self):
        self.user_string = input("Nhập chuỗi: ")
    def print_String(self):
        print(self.user_string.upper())
string_handler = StringHandler()
string_handler.get_String()
string_handler.print_String()
