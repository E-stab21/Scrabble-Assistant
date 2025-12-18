"""
Ethan
Scrabble bot
Brute Force approach
"""

import copy

SETUP = [['^', '_', '_', '2', '_', '_', '_', '^', '_', '_', '_', '2', '_', '_', '^'],
         ['_', '*', '_', '_', '_', '3', '_', '_', '_', '3', '_', '_', '_', '*', '_'],
         ['_', '_', '*', '_', '_', '_', '2', '_', '2', '_', '_', '_', '*', '_', '_'],
         ['2', '_', '_', '*', '_', '_', '_', '2', '_', '_', '_', '*', '_', '_', '2'],
         ['_', '_', '_', '_', '*', '_', '_', '_', '_', '_', '*', '_', '_', '_', '_'],
         ['_', '3', '_', '_', '_', '3', '_', '_', '_', '3', '_', '_', '_', '3', '_'],
         ['_', '_', '2', '_', '_', '_', '2', '_', '2', '_', '_', '_', '2', '_', '_'],
         ['^', '_', '_', '2', '_', '_', '_', '*', '_', '_', '_', '2', '_', '_', '^'],
         ['_', '_', '2', '_', '_', '_', '2', '_', '2', '_', '_', '_', '2', '_', '_'],
         ['_', '3', '_', '_', '_', '3', '_', '_', '_', '3', '_', '_', '_', '3', '_'],
         ['_', '_', '_', '_', '*', '_', '_', '_', '_', '_', '*', '_', '_', '_', '_'],
         ['2', '_', '_', '*', '_', '_', '_', '2', '_', '_', '_', '*', '_', '_', '2'],
         ['_', '_', '*', '_', '_', '_', '2', '_', '2', '_', '_', '_', '*', '_', '_'],
         ['_', '*', '_', '_', '_', '3', '_', '_', '_', '3', '_', '_', '_', '*', '_'],
         ['^', '_', '_', '2', '_', '_', '_', '^', '_', '_', '_', '2', '_', '_', '^']]

EQUIV = {'a': 0,
         'b': 1,
         'c': 2,
         'd': 3,
         'e': 4,
         'f': 5,
         'g': 6,
         'h': 7,
         'i': 8,
         'j': 9,
         'k': 10,
         'l': 11,
         'm': 12,
         'n': 13,
         'o': 14
         }

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

LV = {
    'a': 1,
    'b': 3,
    'c': 3,
    'd': 2,
    'e': 1,
    'f': 4,
    'g': 2,
    'h': 4,
    'i': 1,
    'j': 8,
    'k': 5,
    'l': 1,
    'm': 3,
    'n': 1,
    'o': 1,
    'p': 3,
    'q': 10,
    'r': 1,
    's': 1,
    't': 1,
    'u': 1,
    'v': 4,
    'w': 4,
    'x': 8,
    'y': 4,
    'z': 10
}


def state_indexing(game_state_):
    given_letter_pos = []
    surounding_pos = []
    for row_num, row in enumerate(game_state_):
        for colum, letter in enumerate(row):
            if letter in LETTERS:
                given_letter_pos.append((row_num , colum))
                for adj in [-1, 1]:
                    if (row_num + adj <= 14):
                        surounding_pos.append((row_num + adj, colum))
                    if (colum + adj <= 14):
                        surounding_pos.append((row_num, colum + adj))
    
    sur_filter_pos = copy.deepcopy(surounding_pos)
    for index, item in enumerate(surounding_pos):
        if item in given_letter_pos:
            sur_filter_pos.pop(sur_filter_pos.index(item))
         
    return given_letter_pos, sur_filter_pos


def board_scan(game_state_):
    game_words = [['', []]]
    t = 0
    for row_num, row in enumerate(game_state_):
        for colum, letter in enumerate(row):
            if letter in LETTERS:
                game_words[t][0] += letter
                game_words[t][1].append(((row_num, colum), letter))
            if game_words[t][0] and not(letter in LETTERS):
                game_words.append(['', []])
                t += 1
                
    for colum in range(15):
        for row in range(15):
            if game_state_[row][colum] in LETTERS:
                game_words[t][0] += game_state_[row][colum]
                game_words[t][1].append(((row, colum), game_state_[row][colum]))
            if game_words[t][0] and not(game_state_[row][colum] in LETTERS):
                game_words.append(['', []])
                t += 1
    
    return game_words

def waterfall(DICTIONARY_, game_state_):
    for word in DICTIONARY_:
        x = False
        #horizantal
        for row in range(15):
            for colum in range(16 - len(word)):
                check = False
                board = copy.deepcopy(game_state_)
                word_pos = []
                for index, letter in enumerate(word):
                    if ((colum + len(word)) <= 15) and not((row, colum + index) in given_letter_pos):
                        board[row][colum + index] = letter
                        word_pos.append((row, colum + index))
                    if ((row, colum + index) in given_letter_pos) or ((row, colum + index) in sur_filter_pos):
                        check = True
                if check:
                    new_words = word_scan(board)
                    if new_words:
                        passed_words = letter_check(new_words)
                        if passed_words:
                            total = score(passed_words, game_state_)
                            scoresheet.append((total, word, word_pos))
                        
        #vertical
        check = False
        for colum in range(15):
            for row in range(16 - len(word)):
                check = False
                board = copy.deepcopy(game_state_)
                word_pos = []
                for index, letter in enumerate(word):
                    if ((row + len(word)) <= 15)  and not((row + index, colum) in given_letter_pos):
                        board[row + index][colum] = letter
                        word_pos.append((row + index, colum))
                    if ((row + index, colum) in given_letter_pos) or ((row + index, colum) in sur_filter_pos):
                        check = True
                if check:
                    new_words = word_scan(board)
                    if new_words:
                        passed_words = letter_check(new_words)
                        if passed_words:
                            total = score(passed_words, game_state_)
                            scoresheet.append((total, word, word_pos))


def word_scan(board_):
    new_words = [['', []]]
    c = 0
    for row_num, row in enumerate(board_):
        for colum, letter in enumerate(row):
            if letter in LETTERS:
                new_words[c][0] += letter
                new_words[c][1].append(((row_num, colum), letter))
            if new_words[c][0] and not(letter in LETTERS):
                new_words.append(['', []])
                c += 1
               
    for colum in range(15):
        for row in range(15):
            if board_[row][colum] in LETTERS:
                new_words[c][0] += board_[row][colum]
                new_words[c][1].append(((row, colum), board_[row][colum]))
            if new_words[c][0] and not(board_[row][colum] in LETTERS):
                new_words.append(['', []])
                c += 1
    
    new_words2 = []
    for item in new_words:
        if len(item[0]) > 1:
            if not(item[0] in DICTIONARY):
                new_words2 = []
                break
            if not(item in game_words):
                new_words2.append(item)
        
    return new_words2


def letter_check(new_words_):
    passed_words = []
    for word, letter_pos in new_words_:
        lst_word = list(word)
        for index in range(len(word)):
            if letter_pos[index][0] in given_letter_pos:
                lst_word[index] = 0
                
        copy_hand = copy.deepcopy(hand)
        for index, letter in enumerate(lst_word):
            if letter in copy_hand:
                copy_hand.pop(copy_hand.index(letter))
                lst_word[index] = 0
                
        qindex = ['0']
        for index, letter in enumerate(lst_word):
            if '?' in copy_hand and leter != 0:
                copy_hand.pop(copy_hand.index('?'))
                lst_word[i] = 0
                qindex.append(letter_pos[index][0])

        if lst_word == [0] * len(lst_word):
            if not(copy_hand):
                passed_words.append((word, letter_pos, True))
            else:
                passed_words.append((word, letter_pos, False))
        
        
    return passed_words
            

def score(passed_words, game_state_):
    total = 0
    scores = []
    for word, letter_pos, all_let in passed_words:
        score = 0
        multi = []
        for pos, letter in letter_pos:
            if game_state_[pos[0]][pos[1]] == '3':
                score += 3 * LV[letter]
            elif game_state_[pos[0]][pos[1]] == '2':
                score += 2 * LV[letter]
            elif game_state_[pos[0]][pos[1]] == '^':
                score += LV[letter]
                multi.append(3)
            elif game_state_[pos[0]][pos[1]] == '*':
                score += LV[letter]
                multi.append(2)
            else:
                score += LV[letter]
        if multi:        
            for num in multi:
                score *= num
            
        if all_let is True:
            score += 50
            
        scores.append(score)
        
    for num in scores:
        total += num
        
    return total



DICTIONARY = []
FILTERED_DICTIONARY = []
hand = ['h', 'a', 'e', 't', 'r', 'i', 'w']
scoresheet = []


#scrabble words
with open('OWL3_Dictionary.txt', newline='') as text:
    for line in text:
        line = line.strip()
        DICTIONARY.append(line)
        
        c = 0
        copy_hand = copy.deepcopy(hand)
        for character in line:
            if character in copy_hand:
                copy_hand.pop(copy_hand.index(character))
                c += 1
        if c >= (len(line) - 1) and c > 3:
            FILTERED_DICTIONARY.append(line)
        
print(FILTERED_DICTIONARY)
print(len(FILTERED_DICTIONARY))
                

game_state =[['^', '_', '_', '2', '_', '_', '_', '^', '_', '_', '_', '2', '_', '_', '^'],
             ['_', '*', '_', '_', '_', '3', '_', '_', '_', '3', '_', '_', '_', '*', '_'],
             ['_', '_', '*', '_', '_', '_', '2', '_', '2', '_', '_', '_', '*', '_', '_'],
             ['2', '_', '_', '*', '_', '_', '_', '2', '_', '_', '_', '*', '_', '_', '2'],
             ['_', '_', '_', '_', '*', '_', '_', '_', '_', '_', '*', '_', '_', '_', '_'],
             ['_', '3', '_', '_', '_', '3', '_', 'b', '_', '3', '_', '_', '_', '3', '_'],
             ['_', '_', '2', '_', '_', '_', '2', 'i', '2', '_', '_', '_', '2', '_', '_'],
             ['^', '_', '_', '2', '_', '_', '_', 'k', '_', '_', '_', '2', '_', '_', '^'],
             ['_', '_', '2', '_', '_', '_', '2', 'e', '2', '_', '_', '_', '2', '_', '_'],
             ['_', '3', '_', '_', '_', '3', '_', 'r', '_', '3', '_', '_', '_', '3', '_'],
             ['_', '_', '_', '_', '*', '_', '_', '_', '_', '_', '*', '_', '_', '_', '_'],
             ['2', '_', '_', '*', '_', '_', '_', '2', '_', '_', '_', '*', '_', '_', '2'],
             ['_', '_', '*', '_', '_', '_', '2', '_', '2', '_', '_', '_', '*', '_', '_'],
             ['_', '*', '_', '_', '_', '3', '_', '_', '_', '3', '_', '_', '_', '*', '_'],
             ['^', '_', '_', '2', '_', '_', '_', '^', '_', '_', '_', '2', '_', '_', '^']]



#running functions
given_letter_pos, sur_filter_pos = state_indexing(game_state)
game_words = board_scan(game_state)
waterfall(FILTERED_DICTIONARY, game_state)

#printing
scoresheet.sort(reverse = True)
print(scoresheet[:6])
#for total, word, pos in scoresheet:
#    for coord in pos:
#        row, col = coord
#        game_state[row][col] = '&'
#    print(game_state)

        
