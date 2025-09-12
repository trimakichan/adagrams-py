from random import randint
from adagrams.constants import LETTER_POOL, SCORE_CHART


def draw_letters():
    all_letters = []
    hand = []

    for letter in LETTER_POOL:
        qty_of_letter = LETTER_POOL[letter]
        all_letters += letter * qty_of_letter

    for i in range(10):
        random_index = randint(0,len(all_letters)-1)
        hand.append(all_letters[random_index])
        all_letters.pop(random_index)
    
    return hand


def uses_available_letters(word, letter_bank):
    word_uppercase = word.upper()
    letter_bank_dict = {}

    # create a helper function for this later
    for letter in letter_bank:
        letter_bank_dict[letter] = letter_bank_dict.get(letter,0) + 1

    for letter in word_uppercase:
        if letter not in letter_bank_dict or (letter_bank_dict[letter] == 0):
            return False
        letter_bank_dict[letter] -= 1  

    return True

    
def score_word(word):
    word_uppercase = word.upper()
    score = 0

    for letter in word_uppercase:
        if letter in SCORE_CHART:
            score += SCORE_CHART[letter]
        else:
            return "Invalid Input"
    
    if len(word) > 6:
        score += 8
    
    return score


def get_highest_word_score(word_list):
    highest_word = None
    highest_score = 0
    
    for i in range(len(word_list)):
        word = word_list[i] 
        score = score_word(word)
        if len(word) == 10:
            return word, score
        elif score == highest_score:
            if len(word) < len(highest_word):
                highest_word = word
        elif score > highest_score:
            highest_score = score
            highest_word = word

        
    return highest_word, highest_score
    
