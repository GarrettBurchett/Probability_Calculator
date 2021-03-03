import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.contents = []
        for k, v in self.kwargs.items():
            for i in range(kwargs[k]):
                self.contents.append(i)
    
    def draw(self, number_of_draws):
        self.number_of_draws = number_of_draws
        self.balls_drawn = []

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    trials = 1
    while trials <= num_experiments:
        hat.draw(num_balls_drawn)
