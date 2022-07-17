import config

class Suggestion:
    def __init__(self, selection, arr_index, user_range):
        self.selection = selection
        self.arr_index = arr_index
        self.user_range = user_range
        self.wheel = config.roulette

    def range_selection(self):
        n = len(self.wheel) - 1
        num_list = []

        right = False
        if self.user_range > 0:
            right = True

        # Loop through desired range
        for i in range(abs(self.user_range)):
            # Check range to right or left side of the selection
            if right:
                index = self.arr_index + i + 1
            else:
                index = self.arr_index - i - 1

            # Change index value to cycle around
            if index > n:
                index = (index % n) - 1
            elif index < 0:
                index = (index % n) + 1

            num_list.append(self.wheel[index])

        return num_list

    def print_suggestion(self):
        if self.user_range > 0:
            print("Right of : ", self.selection, " are these numbers: ", self.range_selection())
        elif self.user_range < 0:
            print("Left of : ", self.selection, " are these numbers: ", self.range_selection())
