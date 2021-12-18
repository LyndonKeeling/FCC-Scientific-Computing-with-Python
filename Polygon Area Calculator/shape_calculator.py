import math

class Rectangle:
  """
  Rectangle class with various get/ set methods to alter Rectangle
  or get specific information regarding.
  """
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"
  
  def set_width(self, new_width):
    self.width = new_width

  def set_height(self, new_height):
    self.height = new_height
  
  def get_area(self):
    return self.width * self.height
  
  def get_perimeter(self):
    return (2 * self.width) + (2 * self.height)
  
  def get_diagonal(self):
    return ((self.width**2) + (self.height**2))**0.5
  
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    
    output = ""
    for i in range(self.height):
      output += ("*" * self.width) + "\n"
    return output

  def get_amount_inside(self, shape):
    length_how_many = self.height // shape.height
    width_how_many = self.width // shape.width
    return length_how_many* width_how_many


class Square(Rectangle):
  """
  Inherited Rectangle class with various get/ set methods to alter Rectangle
  or get specific information regarding. 
  """
  def __init__(self, side):
    self.width = side
    self.height = side

  def __str__(self):
    return f"Square(side={self.width})"

  def set_side(self, new_side):
    self.width = self.height = new_side