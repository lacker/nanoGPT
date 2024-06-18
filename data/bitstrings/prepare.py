import numpy as np
import os
import pickle
import random

input_txt_path = os.path.join(os.path.dirname(__file__), 'input.txt')

class Encoding:
    def __init__(self):
        print("creating encoding...")
        self.stoi = {}
        self.itos = {}
        text = open(input_txt_path).read()
        chars = set()
        for ch in text:
            chars.add(ch)
        for ch in sorted(chars):
            self.stoi[ch] = len(self.stoi)
            self.itos[self.stoi[ch]] = ch
            print(f"{repr(ch)} -> {self.stoi[ch]}")
        self.vocab_size = len(self.stoi)

    def encode(self, s):
        return np.array([self.stoi[c] for c in s], dtype=np.uint8)

    def decode(self, l):
        return "".join([self.itos[c] for c in l])


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
    meta_path = os.path.join(os.path.dirname(__file__), 'meta.pkl')

    # generate the input.txt file
    num_lines = 100000
    lines = [generate_str() for _ in range(num_lines)]
    text = "".join([line + "\n" for line in lines])

    # generate the train and val bin files
    enc = Encoding()
    with open(input_txt_path, 'w') as f:
        f.write(text)
    ids = enc.encode(text)
    cut = int(len(ids) * 0.9)
    train_ids = ids[:cut]
    print(f"train has {len(train_ids):,} tokens")
    val_ids = ids[cut:]
    print(f"val has {len(val_ids):,} tokens")
    train_ids = np.array(train_ids, dtype=np.uint16)
    val_ids = np.array(val_ids, dtype=np.uint16)
    train_ids.tofile(train_bin_path)
    val_ids.tofile(val_bin_path)

    # save the meta information
    meta = {
        'vocab_size': enc.vocab_size,
        'itos': enc.itos,
        'stoi': enc.stoi,
    }
    with open(meta_path, 'wb') as f:
        pickle.dump(meta, f)


if __name__ == "__main__":
    main()