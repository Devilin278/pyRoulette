import config
import random


class Spin:
    def __init__(self):
        self.wheel = config.wheel
        self.wheel_length = config.wheel_length
        self.choice = {'left': -1, 'right': 1, 'center': 0}
        self.direction = 'center'
        self.contact_number = 0

    def generate(self):
        print('The ball is released around the wheel...')
        self.contact_number = random.randrange(self.wheel_length)
        print('and bounces near the number', self.contact_number, ',')

        max_num = random.randrange(5)
        for i in range(max_num):
            self.direction, move = random.choice(list(self.choice.items()))
            index = self.wheel.index(str(self.contact_number)) + move
            if index > self.wheel_length:
                index = (index % self.wheel_length) - 1
            elif index < 0:
                index = (index % self.wheel_length) + 1

            self.contact_number = self.wheel[index]
            if i < max_num - 1:
                self.print_bounce()
        print('and the ball lands on the number:', self.contact_number)
        return str(self.contact_number)

    def print_bounce(self):
        if self.direction == 'center':
            print('then bounces around number', self.contact_number, ',')
        else:
            print('then bounces around the number', self.contact_number, 'towards the', self.direction, ',')
