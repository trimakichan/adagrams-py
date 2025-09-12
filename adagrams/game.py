from random import randint

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}


def generate_shuffled_letter_list():
    all_letters = []
    shuffled_letters = []

    for letter in LETTER_POOL:
        qty_of_letter = LETTER_POOL[letter]
        all_letters += letter * qty_of_letter

    while all_letters:
        random_index = randint(0,len(all_letters)-1)
        shuffled_letters.append(all_letters[random_index])
        all_letters.pop(random_index)

    return shuffled_letters
    

def draw_letters():
    shuffled_letters = generate_shuffled_letter_list()
    hand = []

    for i in range(10):
        random_index = randint(0,len(shuffled_letters)-1)
        hand.append(shuffled_letters[random_index])
        shuffled_letters.pop(random_index)
    
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
    pass

def get_highest_word_score(word_list):
    pass
