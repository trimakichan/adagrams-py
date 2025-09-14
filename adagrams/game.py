from random import randint
from adagrams.constants import LETTER_POOL, SCORE_CHART

def generate_letter_bank_dict(letter_bank):
    letter_bank_dict = {}

    for letter in letter_bank:
        letter_bank_dict[letter] = letter_bank_dict.get(letter,0) + 1

    return letter_bank_dict

def draw_letters():
    all_letters = []
    hand = []

    for letter in LETTER_POOL:
        qty_of_letter = LETTER_POOL[letter]
        all_letters += [letter] * qty_of_letter

    for i in range(10):
        random_index = randint(0,len(all_letters)-1)
        hand.append(all_letters[random_index])
        all_letters.pop(random_index)
    
    return hand


def uses_available_letters(word, letter_bank):
    word = word.upper()

    letter_bank_dict = generate_letter_bank_dict(letter_bank)

    for letter in word:
        if letter not in letter_bank_dict or letter_bank_dict[letter] == 0:
            return False
        letter_bank_dict[letter] -= 1

    return True

    
def score_word(word):
    word = word.upper()
    score = 0

    for letter in word:
        if letter in SCORE_CHART:
            score += SCORE_CHART[letter]
    
    if 6 < len(word) < 11:
        score += 8
    
    return score


def get_highest_word_score(word_list):
    highest_score_word = ""
    highest_score = 0
    
    for word in word_list:
        score = score_word(word)

        if score == highest_score:
            if  len(word) < 10 and len(highest_score_word) == 10:
                continue
            elif len(word) == 10 and len(highest_score_word) < 10:
                highest_score_word = word
            elif len(word) < len(highest_score_word):
                highest_score_word = word
                
        elif score > highest_score:
                highest_score_word = word
                highest_score = score

    return highest_score_word, highest_score
    
