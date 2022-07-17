# Python3 Roulette program to demonstrate the use of
# circular array without using extra memory space

import config
from suggestion import Suggestion
from spin import Spin

past_numbers = []

while True:
    while True:
        keep_playing = str(input('Would you like to spin? (Yes/No)'))
        if (keep_playing.upper() == 'YES') or (keep_playing.upper() == 'Y'):
            # asking for how wide of selection from starting number selection
            if past_numbers == []:
                while True:
                    try:
                        user_range = int(input('Please enter the suggestion range: '))
                        break
                    except ValueError as v:
                        print("Entry is not an INTEGER. Please Only Enter INTEGERS: ", v)
                        continue
            break
        elif (keep_playing.upper() == 'NO') or (keep_playing.upper() == 'N'):
            exit()
        else:
            print('Please Enter ONLY "Yes" or "No"')

    landed_number = Spin().generate()
    # print(config.wheel)
    arr_index = config.wheel.index(landed_number)

    # Print Suggested numbers in entered range around the number where the ball landed
    Suggestion(landed_number, arr_index, user_range).print_suggestion()
    Suggestion(landed_number, arr_index, -abs(user_range)).print_suggestion()

    # Store the last number to the front of the list and print the list
    past_numbers.insert(0, landed_number)
    print('Past winning numbers are:', past_numbers)
