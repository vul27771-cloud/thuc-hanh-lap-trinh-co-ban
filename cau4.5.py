print("Sinh vien: LE TRONG TRUNG")
print("Ma so SV : 245751030110070")
print("############################")
###################################

class ReverseWords:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        words = self.text.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)

input_str = "hello .py"
obj = ReverseWords(input_str)
print("Đầu ra:", obj.reverse())  
