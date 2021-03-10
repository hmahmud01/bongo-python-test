class Person(object):
  def __init__(self, first_name, last_name, father):
    self.first_name = first_name
    self.last_name = last_name,
    self.father = father


def print_depth(data):
  if isinstance(data, dict):
    i = 0
    depth_printer(data, i)

def depth_printer(d, i=0):
    for key, value in d.items():
        print(key, i + 1)
        if isinstance(value, Person):
          objdict = value.__dict__
          depth_printer(objdict, i=i+1)          
        if isinstance(value, dict):
          depth_printer(value, i=i+1)