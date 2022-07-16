# Python3 program to demonstrate the use of
# circular array without using extra memory space

# function to print circular list starting
# from given index ind.
def range_around_selection(roulette, arr_index, user_range):
    n = len(roulette) - 1
    num_list = []

    right = False
    if user_range > 0:
        right = True

    for i in range(abs(user_range)):
        if right:
            index = arr_index + i + 1
        else:
            index = arr_index - i - 1
        print(arr_index, index, index % n)
        if index > n:
            index = (index % n) - 1
        elif index < 0:
            index = (index % n) + 1

        num_list.append(roulette[index])

    return num_list

# List of Roulette Wheel Numbers
roulette = ['00', '27', '10', '25', '29', '12', '8', '19',
            '31', '18', '06', '21', '33', '16', '4', '23',
            '35', '14', '2', '0', '28', '9', '26', '30',
            '11', '7', '20', '32', '17', '5', '22', '34',
            '15', '3', '24', '36', '13', '1']

# asking to find the number and reverse index location
selection = str(input('Please select a number: '))

# asking for how wide of selection from starting number selection
user_range = int(input('Please select a range size: '))

arr_index = roulette.index(selection)
print("Right of : ", selection, " are these numbers: ", range_around_selection(roulette, arr_index, user_range))
print("Left of : ", selection, " are these numbers: ", range_around_selection(roulette, arr_index, -abs(user_range)))
