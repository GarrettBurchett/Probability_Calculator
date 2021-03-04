import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.contents = []
        for k in self.kwargs.keys():
            for _ in range(kwargs[k]):
                self.contents.append(k)
    
    def draw(self, number_of_draws):
        self.number_of_draws = number_of_draws
        self.balls_drawn = []
        if number_of_draws >= len(self.contents):
            self.balls_drawn = self.contents
        else:
            for _ in range(number_of_draws):
                position_of_list = random.randrange(0, len(self.contents))
                ball_drawn = self.contents.pop(position_of_list)
                self.balls_drawn.append(ball_drawn)
            
        return self.balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    trials = 1
    successes = 0
    while trials <= num_experiments:
        new_hat = copy.deepcopy(hat)
        new_hat.draw(num_balls_drawn)
        check_actual_equal_expected = [new_hat.balls_drawn.count(ball) >= expected_balls[ball] for ball in expected_balls.keys()]
        if False in check_actual_equal_expected:
            pass
        else:
            successes += 1
        trials += 1
    
    prob = successes / num_experiments

    return prob