import os
import random

input_txt_path = os.path.join(os.path.dirname(__file__), 'input.txt')

class Encoding:
    def __init__(self, text=None):
        self.encoding = {}
        self.decoding = {}
        if text is None:
            text = open(input_txt_path).read()
        chars = set()
        for ch in text:
            chars.add(ch)
        for ch in sorted(chars):
            self.encoding[ch] = len(self.encoding)
            self.decoding[self.encoding[ch]] = ch
            print(f"{repr(ch)} -> {self.encoding[ch]}")

    def encode(self, s):
        return [self.encoding[c] for c in s]

    def decode(self, l):
        return "".join([self.decoding[c] for c in l])


def generate_digits():
    return [random.randrange(10) for _ in range(6)]

def make_string(char, f):
    input_digits = generate_digits()
    output_digits = f(input_digits)
    parts = [char] + list(map(str, input_digits)) + ["="] + list(map(str, output_digits))
    return "".join(parts)

# R = reverse the list
def generate_r():
    r_func = lambda digits: list(reversed(digits))
    return make_string("R", r_func)

# F = flip each digit
def generate_f():
    f_func = lambda digits: [9 - digit for digit in digits]
    return make_string("F", f_func)

def generate_str():
    return random.choice([generate_r, generate_f])()

def main():
    train_bin_path = os.path.join(os.path.dirname(__file__), 'train.bin')
    val_bin_path = os.path.join(os.path.dirname(__file__), 'val.bin')

    num_lines = 40000
    lines = [generate_str() for _ in range(num_lines)]
    text = "".join([line + "\n" for line in lines])
    enc = Encoding(text)
    with open(input_txt_path, 'w') as f:
        f.write(text)


if __name__ == "__main__":
    main()