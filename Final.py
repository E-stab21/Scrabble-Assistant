"""
Ethan Stabenow and Quinn Tyldesley
Final Project
"""


DICTIONARY = []

LV = {'a':1 , 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2, 'h':4,
      'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 
      'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10}

ALLOWED = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v',
           'w', 'x', 'y', 'z', '2', '3', '*', '^', '_', '?']

NFH = ['2', '3', '*', '^', '_']


def board_indexing(board_):
    for i, e in enumerate(board_):
        if e == '2' or e == '3':
            dob_trip.append((i, e))
            board_[i] = '_'
            e = '_'
        elif e == '*':
            dobw_tripw.append((i, 2))
            board_[i] = '_'
            e = '_'
        elif e == '^':
            dobw_tripw.append((i, 3))
            board_[i] = '_'
            e = '_'

        if e != '_':
            index_board.append((i, e))
        check = False


def num_of_let(dictionary, board_):
    for word in dictionary:
        if len(word) <= len(board_):
            filter1.append(word)


def first_turn(filter1_, hand_):
    scores = []
    for word in filter1_:
        hand_copy = list(hand_)
        myst = hand_copy.count("?")
            
        for index, letter in enumerate(word):
                        
                    
            check = True
            if letter in hand_copy:
                hand_copy.pop(hand_copy.index(letter))
            elif myst > 0:
                myst -= 1
                hand_copy.pop(hand_copy.index("?"))
            else:
                check = False
                break
        if check == True:
            scores.append(word)
    for word in scores: 
                        
        total = 0
        hand_cp = list(hand)
        highest = 0
        highest_let = None
        for index, letter in enumerate(word):
            
            if len(word) == 7:
                if LV[letter] > highest and letter in hand_ and index != 3:
                    highest = LV[letter]
                    highest_let = letter
            elif len(word) == 6:
                if LV[letter] > highest and letter in hand_ and index not in [2,3]:
                    highest = LV[letter]
                    highest_let = letter
            elif len(word) == 5:
                if LV[letter] > highest and letter in hand_ and index in [0,5]:
                    highest = LV[letter]
                    highest_let = letter
                
                    
        for letter in word:
            if letter in hand_cp and highest_let == letter:
                highest_let = None
                
                hand_cp.pop(hand_cp.index(letter))
                total += LV[letter] * 2
            elif letter in hand_cp:
                hand_cp.pop(hand_cp.index(letter))
                total += LV[letter]
            
                
                
        if len(word) == len(hand):           
            scoresheet.append((total * 2 + 50, word))
        else:
            scoresheet.append((total * 2, word))


def fits_given(filter1_):
    for word in filter1_:
        for i, let in enumerate(word):
            if let == index_board[0][1] and i <= index_board[0][0]: #left check

                check = False
                for item in index_board:
                    dis = item[0] - index_board[0][0] 
                    try: 
                        if word[i + dis] == item[1]: #letter check
                            check = True
                        else:
                            check = False
                            break
                    except IndexError:
                        check = False
                        break

                if check:
                    board_right = ((len(board_lst)-1) - index_board[-1][0])
                    right_check = ((len(word) - 1) - (i + dis)) <= board_right 
                    if right_check: #right check
                        filter2.append((word, i))   


def let_check(filter2_):
    for word, anchor_idx_ in filter2_:
        copy_word = list(word)
        for i, let in index_board:
            try:
                dis = i - index_board[0][0]
                copy_word[anchor_idx_ + dis] = 0
            except IndexError:
                continue

        copy_hand = hand_lst[:]
        for i, let in enumerate(copy_word):
            if let in copy_hand:
                copy_hand.pop(copy_hand.index(let))
                copy_word[i] = 0

        qindex = ['0']
        for i, let in enumerate(copy_word):
            if '?' in copy_hand and let != 0:
                copy_hand.pop(copy_hand.index('?'))
                copy_word[i] = 0
                qindex.append(i)

        if copy_word == [0] * len(copy_word):
            filter3.append((word, anchor_idx_, qindex))


def scrabblescore(word_, anchor_index_, qindex_): 
    total = 0
    word_multi = []
    for index, letter in enumerate(word_):
        for multi_index, multi in dobw_tripw:  
            if (index - anchor_index_) == (multi_index - index_board[0][0]):
                    word_multi.append(multi)
        check = True
        for q in qindex_:
            if index == q:
                check = False 
        if check:    
            check = True
            for multi_index, multi in dob_trip: 
                if multi == 1:
                    continue
                if (index - anchor_index_) == (multi_index - index_board[0][0]):
                        if word == 'vaults':
                            print(letter, LV[letter], multi)
                        total += (LV[letter] * int(multi))
                        check = False
            if check:
                total += LV[letter]      
    
    for multi in word_multi:
        total *= multi

    if len(word_) - len(index_board) == len(hand_lst):
        all_let.append((total + 50, word))

    return total




if __name__ == '__main__':
    game = True

    #srabble words
    with open('OWL3_Dictionary.txt', newline='') as text:
        for line in text:
            DICTIONARY.append(line.strip())
    while game:
        hand_lst = []
        board_lst = []
        dob_trip = [(0, 1)]
        dobw_tripw = [(0,1)]
        index_board = []
        filter1 = []
        filter2 = []
        filter3 = []
        scoresheet = []
        all_let = []
        ac_hand = False
        ac_board = False
        empty_exception = []
        
        while ac_hand == False:                
            hand =  input("\nEnter your current hand, use ? for wild tiles. "
                          "Enter 1 to quit: ") #User Input
            hand = hand.lower()

            if hand == "1":
                game = False
                break
            elif len(hand) > 10:
                print("\nOops! Looks like you have too "
                      "many tiles in your hand. Make "
                      "sure you don't have more than 7.\n")
                continue


            for value in hand:
                if value not in ALLOWED or value in NFH:
                    print(f"\n{value} is not a valid input "
                          "for your hand please try again\n")
                    ac_hand = False
                else:
                    ac_hand = True

        if game == False:
            break

        while ac_board == False:                  
            board = input("Enter the section of board you want to "
                          "place tiles in. Use _ for empty squares "
                          "and a 2 or 3 if a square has a letter multiplier. "
                          "Use an * for 2x word squares and ^ for 3x word squares:\n") #Board 
            board = board.lower()

            for value in board:           
                if value not in ALLOWED or value == '?':
                    print(f"\n{value} is not a valid input for "
                          "the board please try again\n")
                else:
                    ac_board = True



        for letter in hand:
            hand_lst.append(letter)

        for letter in board:
            board_lst.append(letter)

        #running filters
        word_multi = board_indexing(board_lst)
        print(dobw_tripw)
        num_of_let(DICTIONARY, board_lst)
        
        if not index_board:
            first_turn(filter1, hand)
        else:
            fits_given(filter1)
            let_check(filter2)
            #printing
            for word, anchor_idx, qindex in filter3:    
                scoresheet.append((scrabblescore(word, anchor_idx, qindex), word))

        scoresheet.sort(reverse=True)
        count = 0
        print("Highest scoring words using part of hand: ")
        if all_let:
            for score, word in scoresheet:
                count += 1     
                if word in all_let[0]:
                    continue
                else:
                    print(score, word)
                if count > 5:
                    break
            print("Highest scoring words using all of hand: ")
            for score, word in all_let:
                print(score, word)
        else:
            count = 0
            for score, word in scoresheet:
                count += 1
                if count <= 5:
                    print(score, word)

