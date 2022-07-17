import config


class Suggestion:
    def __init__(self, landed_number, arr_index, user_range):
        self.wheel = config.wheel
        self.wheel_length = config.wheel_length
        self.landed_number = landed_number
        self.arr_index = arr_index
        self.user_range = user_range

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
            if index > self.wheel_length:
                index = (index % self.wheel_length) - 1
            elif index < 0:
                index = (index % self.wheel_length) + 1

            num_list.append(self.wheel[index])

        return num_list

    def print_suggestion(self):
        if self.user_range > 0:
            print("Right of:", self.landed_number, "are these numbers:", self.range_selection())
        elif self.user_range < 0:
            print("Left of:", self.landed_number, "are these numbers:", self.range_selection())
