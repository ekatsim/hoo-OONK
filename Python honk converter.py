import random
import re

with open("C:\Python Text Files\Goosebible.txt", "r") as f:
    bible = f.read()

# print(bible)
# bible_lines = bible.split("\n")
# print(bible_lines)

goose_list_of_honks = ["hön", 
                       "hönk", 
                       "honk", 
                       "hink", 
                       "hoonk", 
                       "hooooooo-oooonk",
                       "hank",
                       "henk",
                       "hooowonk"
                                    ]

non_alpha = "([^A-Za-z]+)"
capital_word = "[A-Z].*"


def get_random_honk():
    return goose_list_of_honks[random.randint(0, len(goose_list_of_honks) - 1)]


def honkify_word(word, honk_supplier):
    if re.match(non_alpha, word):
        return word
    else:
        honk = honk_supplier()
        return honk.capitalize() if re.match(capital_word, word) else honk


def honkify_expression(expression, honk_supplier):
    words = filter(lambda word: word != '', re.split(non_alpha, expression))
    # print(words)
    return "".join(map(lambda word: honkify_word(word, honk_supplier), words))


def honkify(sentence, honk_supplier):
    expressions = sentence.split(" ")
    return " ".join(map(lambda expression: honkify_expression(expression, honk_supplier), expressions))

if __name__ == "__main__":
    translate = honkify(bible, get_random_honk)
    print(translate)