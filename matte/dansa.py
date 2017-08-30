# coding=utf-8
from kombinatorik import permutationer
import itertools

count=0
for obj in itertools.combinations('algebra',3):
    count+=1
    print(obj)
print(count)
print(itertools.product('algebra',repeat=2))

def no_repeats(n_letters, new_word_length):
    """Om, eller när xxxx.. från n tecken"""
    return permutationer(n_letters, new_word_length)

def repeat_one(letter_count=2, other_letters=6, new_word_length=5):
    """Anta att det finns 3st A i ordet"""
    for i in range(2, letter_count+1):
        positions = permutationer(new_word_length, )

def dansa (word="", new_word_length=3):
    """Hur många olika ord som är $new_word_length långa kan göras av $word"""
    nwl = new_word_length

    pass
