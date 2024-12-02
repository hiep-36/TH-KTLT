print("Le Hoa Hiep")
print("2357572021610073")
class RomanToInteger:
    def __init__(self, roman):
        self.roman = roman
        self.roman_dict = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 
            'C': 100, 'D': 500, 'M': 1000
        }
    def to_integer(self):
        total = 0
        length = len(self.roman)
        for i in range(length):
            if i + 1 < length and self.roman_dict[self.roman[i]] < self.roman_dict[self.roman[i + 1]]:
                total -= self.roman_dict[self.roman[i]]
            else:
                total += self.roman_dict[self.roman[i]]
        return total
roman_number = "IX"
converter = RomanToInteger(roman_number)
print(f"Số nguyên tương ứng với số La Mã {roman_number} là: {converter.to_integer()}")

roman_number = "MCMXCIV"
converter = RomanToInteger(roman_number)
print(f"Số nguyên tương ứng với số La Mã {roman_number} là: {converter.to_integer()}")
