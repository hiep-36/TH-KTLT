print("Le Hoa Hiep")
print("235752021610073")
def count_upper_lower(sentence):
    upper_count = 0
    lower_count = 0
    for char in sentence:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count  
input_sentence = input("Nhập một câu: ")
upper_letters, lower_letters = count_upper_lower(input_sentence)
print("Số chữ hoa là:", upper_letters)
print("Số chữ thường là:", lower_letters)
