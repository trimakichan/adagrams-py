from random import randint
from adagrams.constants import LETTER_POOL, SCORE_CHART

def generate_letter_bank_dict(letter_bank):
    """
    Generate a dictionary where a letter as a key and a count as a value

    Args:
        letter_bank (list[str]): A list of letters.

    Returns: 
        dict[str, int]: A dictionary where each key is a letter and
        each value is the number of times that letter appears in the list.
    """
    letter_bank_dict = {}

    for letter in letter_bank:
        letter_bank_dict[letter] = letter_bank_dict.get(letter,0) + 1

    return letter_bank_dict

def draw_letters():
    """
    Draw 10 random letters from the letter pool.
    The letters are selected randomly based on the frequency in LETTER_POOL.

    Returns: 
        list[str]: A list containing 10 single-character strings, 
        each representing a letter.
    """
    all_letters = []
    hand = []

    for letter in LETTER_POOL:
        qty_of_letter = LETTER_POOL[letter]
        all_letters += [letter] * qty_of_letter

    for i in range(10):
        random_index = randint(0, len(all_letters) - 1)
        hand.append(all_letters[random_index])
        all_letters.pop(random_index)
    
    return hand


def uses_available_letters(word, letter_bank):
    """
    Check if a word is made from the given letter bank.
    
    Args:
        word (str): The word to check.
        letter_bank (list[str]): The available letters.
    
    Returns:
        bool: True if the word can be made from the letter_bank, False otherwise.
    """
    word = word.upper()

    letter_bank_dict = generate_letter_bank_dict(letter_bank)

    for letter in word:
        if letter not in letter_bank_dict or letter_bank_dict[letter] == 0:
            return False
        letter_bank_dict[letter] -= 1

    return True

    
def score_word(word):
    """
    Calculate the total score of a word using the SCORE_CHART.
    If the length of a word is between 7 and 10, add an extra 8 points to the total score.
    
    Args:
        word (str): The word to score.

    Returns:
        int: The total score of the word.
    """
    word = word.upper()
    score = 0

    for letter in word:
        if letter in SCORE_CHART:
            score += SCORE_CHART[letter]
    
    if 6 < len(word) < 11:
        score += 8
    
    return score

def get_highest_word_score(word_list):
    """
    Determine the highest scoring word from a list of words.

    In the case of a tie:
    - The shorter word wins, unless one of the words has exactly 10 letters. 
    - If multiple words have the same score and the same length, 
    the first word in the list wins.

    Args:
        word_list (list[str]): A list of words to compare.

    Returns:
        tuple[str, int]: The first element is the 
        highest scoring word and the second element is the highest score. 
    """
    best_word = ""
    best_score = 0
    
    for word in word_list:
        score = score_word(word)

        if score == best_score:
            if  len(word) < 10 and len(best_word) == 10:
                continue
            
            if len(word) == 10 and len(best_word) < 10:
                best_word = word
            elif len(word) < len(best_word):
                best_word = word
                
        elif score > best_score:
                best_word = word
                best_score = score

    return best_word, best_score
