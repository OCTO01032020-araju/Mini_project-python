import string
import random

select_charset = input("Enter Charse you want to : ")
char_length = int(input("Length of Character : "))

class Password():

    def __init__(self, charset, length):

        self.charset = charset
        self.length = length
        self.char_array = []

    def get_charset(self):

        if ('l' in self.charset):
            self.char_array.append(string.ascii_lowercase)

        if ('u' in self.charset):
            self.char_array.append(string.ascii_uppercase)

        if ('d' in self.charset):
            self.char_array.append(string.digits)

        if ('s' in self.charset):
            self.char_array.append(string.punctuation)

    def get_array(self):
        return self.char_array

    def generate_pass(self):
        print("character Array is =", self.char_array)
        pass_word = []

        for i in range(0, self.length):
            outer_ind = random.randrange(0, len(self.char_array))
            # print("Outer Index", outer_ind)
            # print("choosed Char from Array", self.char_array[outer_ind])
            inner_ind = random.randrange(0, len(self.char_array[outer_ind]))
            # print("Inner index ", inner_ind)
            inner_in_val = self.char_array[outer_ind][inner_ind]
            # print("Inner index value", inner_in_val )
            pass_word.append(inner_in_val)

        # print("Password Array", pass_word)
        pass_string = "".join(pass_word)
        print(pass_string)
        print(pass_string.capitalize())


password = Password(str(select_charset), char_length)

password.get_charset()
password.generate_pass()