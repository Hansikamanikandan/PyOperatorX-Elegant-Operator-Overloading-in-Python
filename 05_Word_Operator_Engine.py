class Word:
    def __init__(self, text):
        self.text = text

    def __add__(self, other):
        return Word(self.text + other.text)

    def __eq__(self, other):
        return self.text == other.text

    def __lt__(self, other):
        return self.text < other.text

    def __str__(self):
        return self.text

w1 = Word(input("Enter first word: "))
w2 = Word(input("Enter second word: "))

print("Concatenation:", w1 + w2)
print("Equal:", w1 == w2)
print("Comparison:", w1 < w2)
