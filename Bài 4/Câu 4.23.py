print("Le Hoa Hiep")
print("235752021610073")
def count_letters_and_digits(sentence):
    letter_count = 0
    digit_count = 0
    
    for char in sentence:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            digit_count += 1
    return letter_count, digit_count
input_sentence = input("Nhập một câu: ")
letters, digits = count_letters_and_digits(input_sentence)
print("Số chữ cái là:", letters )
print("Số chữ số là:", digits)
