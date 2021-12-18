import math

class Category:
  """
  Categories in a budget. Able to do transfers, and withdrawals between other category classes.
  """

  def __init__(self, item):
    self.item = item
    self.ledger = []
    self.funds  = 0
    self.maxDiff = None
    
  def deposit(self, amount, description = ""):
    self.ledger.append({"amount": amount, "description": description})
    self.funds += amount

  def withdraw(self, amount, description = ""):
    if (self.funds - amount) >= 0:
      self.ledger.append({"amount": -(amount), "description": description})
      self.funds -= amount
      return True
    return False

  def get_balance(self):
    return self.funds

  def transfer(self, amount, other_category):
    test = self.withdraw(amount, f"Transfer to {other_category.item}")
    if test == True:
      other_category.deposit(amount, f"Transfer from {self.item}")
      return True
    return False

  def check_funds(self, amount):
    if amount > self.funds:
      return False
    return True

  def __str__(self):
    # top line calc
    stars = 30 - len(self.item)
    stars = (("*"*int(stars/2))+self.item+("*"*int(stars/2)))
    budget_list = stars + "\n"
    for i in self.ledger:
      description = i["description"]
      amount = str(i["amount"])
      # does amount need .00 ?
      if "." not in amount:
        amount += ".00"
      #calculate white space needed
      if len(description) > 23:
        description = description[0:23]
      white_space = 30 - len(description) - len(amount)
      output = description + (" " * white_space) + amount + "\n"
      budget_list += output
    
    budget_list += "Total: " + str(self.funds)
    return budget_list

def create_spend_chart(categories):
  # compute total amount
  total_spent = 0
  category_spending = []
  for i in categories:
    category_spent = 0
    for j in i.ledger:
      if j["amount"] < 0:
        total_spent += j["amount"]
        category_spent += j["amount"]
    category_spending.append(category_spent)
  
  percent_array = []
  # % per array rounded to 10
  for i in category_spending:
    percent_array.append(int((math.floor((i/total_spent)*10))))

  output_array = [["  0|"],[" 10|"],[" 20|"],[" 30|"],[" 40|"],[" 50|"],[" 60|"],[" 70|"],[" 80|"],[" 90|"],["100|"]]
  for i in percent_array:
    for j in range(10):
      if (i+1) > j:
        output_array[j].append(" o ")
      else:
        output_array[j].append("   ")
  
  ct = 0
  for i in output_array:
    x = "".join(i)
    output_array[ct] = x
    
    # white space calculation
    white_space = 14 - len(output_array[ct])
    output_array[ct] += " " * white_space
    output_array[ct] += "\n"
    ct += 1

  output = "Percentage spent by category\n"
  for i in reversed(output_array):
    output += i
  output += "    ----------\n"

  iterator = 0
  iterator_arr = []
  for i in categories:
    iterator_arr.append(i.item)
    if len(i.item) > iterator:
      iterator = len(i.item)
    
  word_arr = iterator*["     "]
  for i in categories:
    it = 0
    for j in i.item:
      word_arr[it] += (j + "  ")
      it += 1
    for x in range(len(i.item),len(word_arr)):
      word_arr[x] += "   "

  for i in range(iterator):
    if i != iterator-1:
      word_arr[i] += "\n"
  for i in range(iterator):
    output += word_arr[i]

  return output
  