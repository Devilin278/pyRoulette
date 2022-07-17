# Python3 program to demonstrate the use of
# circular array without using extra memory space

# function to print circular list starting
# from given index ind.
import config
from suggestion import Suggestion
#from spin import Spin

# asking to find the number and reverse index location
selection = str(input('Please select a number: '))

# asking for how wide of selection from starting number selection
user_range = int(input('Please select a range size: '))

arr_index = config.roulette.index(selection)

Suggestion(selection, arr_index, user_range).print_suggestion()
Suggestion(selection, arr_index, -abs(user_range)).print_suggestion()
