# Python3 Roulette program to demonstrate the use of
# circular array without using extra memory space

import config
from suggestion import Suggestion
from spin import Spin

past_guesses = []
past_numbers = []

while True:
    # while True:
    #     keep_playing = str(input('Would you like to spin? (Yes/No)'))
    #     if (keep_playing.upper() == 'YES') or (keep_playing.upper() == 'Y'):
            # asking for how wide of selection from starting number selection
            # if not past_numbers:
            #     while True:
            #         try:
            #             user_range = int(input('Please enter the suggestion range: '))
            #             break
            #         except ValueError as v:
            #             print("Entry is not an INTEGER. Please Only Enter INTEGERS: ", v)
            #             continue
    while True:
        try:
            user_guess = input('Please enter your guess: ')
            break
        except ValueError as v:
            print("Entry is not an INTEGER. Please Only Enter INTEGERS: ", v)
            continue

    # Store the last guessed number and suggest surrounding numbers to play
    past_guesses.insert(0, user_guess)
    suggestion_list = Suggestion(user_guess, config.wheel.index(user_guess), 5).get_suggestion_list()
    print('Based on your Guess, you should play the following numbers: ', suggestion_list)

    while True:
        try:
            actual_number = input('Please enter actual number: ')
            break
        except ValueError as v:
            print("Entry is not an INTEGER. Please Only Enter INTEGERS: ", v)
            continue
            #            break
        # elif (keep_playing.upper() == 'NO') or (keep_playing.upper() == 'N'):
        #     exit()
        # else:
        #     print('Please Enter ONLY "Yes" or "No"')

#    landed_number = Spin().generate()
#    landed_number = "00"
#    print(config.wheel)
#    arr_index = config.wheel.index(landed_number)

    # Print Suggested numbers in entered range around the number where the ball landed
    # selection_list = Suggestion(landed_number, arr_index, user_range).range_selection()
    # print("Right of:", landed_number, "are these numbers:", selection_list)
    # selection_list = Suggestion(landed_number, arr_index, -abs(user_range)).range_selection()
    # print("Left of:", landed_number, "are these numbers:", selection_list)

    # Store the last winning number and suggest quadrant playable numbers
    past_numbers.insert(0, actual_number)
#    Suggestion(landed_number, arr_index, user_range).suggest_play_numbers()
    Suggestion(actual_number, config.wheel.index(actual_number), 0).suggest_play_numbers()

    # Print Passed Guessed and Winning Numbers
    print('Past GUESSED numbers are:', past_guesses)
    print('Past WINNING numbers are:', past_numbers)
