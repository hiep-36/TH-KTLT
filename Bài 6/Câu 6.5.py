print("Le Hoa Hiep")
print("235752021610073")
class StringReverser:
    def __init__(self, input_string):
        self.input_string = input_string
    def reverse_words(self):  
        words = self.input_string.split()      
        reversed_words = words[::-1]
        return ' '.join(reversed_words)
input_string = 'hello .py'
reverser = StringReverser(input_string)
output_string = reverser.reverse_words()
print(output_string)
