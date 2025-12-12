print("Sinh vien: LE TRONG TRUNG")
print("Ma so SV : 245751030110070")
print("############################")
###################################

class RomanToInteger:
    def __init__(self, roman):
        self.roman = roman

    def convert(self):
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

        for char in reversed(self.roman):
            value = roman_values[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value

        return total

num1 = RomanToInteger("IX")
print("IX =", num1.convert)
