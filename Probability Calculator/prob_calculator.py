import copy
import random
# Consider using the modules imported above.

class Hat:
  """
  Initialized with passed contents for probabiltiy calculations below.
  """
  def __init__(self, **kwargs):
    self.contents = []
    for key in kwargs:
      for i in range(kwargs[key]):
        self.contents.append(key)

  def draw(self, num):
    # base case
    if num > len(self.contents):
      return self.contents
    
    temp = self.contents
    random_ball_list = []
    for i in range(num):
      random_ball = random.choice(temp)
      random_ball_list.append(random_ball)
      temp.remove(random_ball)
    return random_ball_list
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  expected_balls_list = []
  for key in expected_balls:
    for i in range(expected_balls[key]):
      expected_balls_list.append(key)

  count = 0
  for i in range(num_experiments):
    expected = copy.deepcopy(expected_balls)
    hat_copy = copy.deepcopy(hat)
    compare = hat_copy.draw(num_balls_drawn) # random assortment
    for color in compare:
      if color in expected:
        expected[color] -=1

    if(all(x <= 0 for x in expected.values())):
      count += 1
      
  return count / num_experiments