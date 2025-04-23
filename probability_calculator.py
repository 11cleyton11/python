import copy
import random

class Hat:
    
    def __init__(self, **kwargs):
        self.dict = {key: val for key, val in kwargs.items()}
        self.contents = [key for key, val in self.dict.items() for _ in range(int(val))]

    def __repr__(self):
        arg_list = [f'{key}={val}' for key, val in vars(self).items()]
        args = ', '.join(arg_list)
        return f'{self.__class__.__name__}({args})'

    def draw(self, amount):
        drawn = []
        for i in range(amount):
            draw = random.choice(self.contents)
            self.contents.remove(draw)
            drawn.append(draw)
            if self.contents == []:
                break
        return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    positive = 0

    for i in range(num_experiments):
        this_hat = copy.deepcopy(hat)
        drawn = this_hat.draw(num_balls_drawn)
        
        drawn_count = {}
        for ball in drawn:
            if ball in drawn_count:
                drawn_count[ball] += 1
            else:
                drawn_count[ball] = 1
        
        success = True
        for ball, amt in expected_balls.items():
            if drawn_count.get(ball, 0) < amt:
                success = False
                break
        if success:
            positive += 1

    return positive / num_experiments
        
hat = Hat(black=6, red=4, green=3)

probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)

print(probability)
