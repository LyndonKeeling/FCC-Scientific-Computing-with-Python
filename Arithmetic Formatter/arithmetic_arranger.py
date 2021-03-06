def arithmetic_arranger(problems, default = False):
  """
  Given an input, returns equations in a way which would be similar to a math quiz given in
  grade school. Should default = True, it will also return the solutions given.
  """
  # too many problems
  if len(problems) > 5:
    return "Error: Too many problems."

  # creates case for when solutions may be entered to, creates layers for output
  active = 0
  if default == True:
    result_layer = []
    active = 1
  top_layer, bot_layer, line_layer = [], [], []
  
  # ct needed so final iteration, white space is not added to end of lists
  ct = 0
  for i in problems:
    problem = i.split(" ")
    # test for error cases
    if problem[1] == "+" or problem[1] == "-":
      if (len(problem[0]) <= 4) and (len(problem[2]) <= 4):
        if problem[0].isnumeric() == True and problem[2].isnumeric() == True:
          # determine line_layer
          line_layer_length = max(len(problem[0]),len(problem[2])) + 2
          line_layer.append(line_layer_length*"-")
          # determine white space for top and bottom of equation, and append all together
          top_white_space = line_layer_length - len(problem[0])
          top_layer.append(top_white_space*" " + problem[0])
          bot_white_space = line_layer_length - len(problem[2]) - 1
          bot_layer.append(problem[1] + bot_white_space*" " + problem[2])
          # case for when true passed to function
          if active == 1:
            if problem[1] == "+":
              result = str(int(problem[0]) + int(problem[2]))
            else:
              result = str(int(problem[0]) - int(problem[2]))
            result_white_space = line_layer_length - len(result)
            result_layer.append(result_white_space*" " + result)
          # add white space for between each problem, except for final iteration
          ct += 1
          if ct != len(problems):
            top_layer.append("    ")
            bot_layer.append("    ")
            line_layer.append("    ")
            if active == 1:
              result_layer.append("    ")
        else:
          return "Error: Numbers must only contain digits."
      else:
        return "Error: Numbers cannot be more than four digits."
    else:
      return "Error: Operator must be '+' or '-'."

    # combine it all
    arranged_problems = ""
  if active == 0:
    arranged_problems += "".join(top_layer) + "\n"
    arranged_problems += "".join(bot_layer) + "\n" 
    arranged_problems += "".join(line_layer)
  else:
    arranged_problems += "".join(top_layer) + "\n"
    arranged_problems += "".join(bot_layer) + "\n" 
    arranged_problems += "".join(line_layer) + "\n"
    arranged_problems += "".join(result_layer)
    
  return arranged_problems
