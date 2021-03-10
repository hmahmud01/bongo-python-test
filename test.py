import unittest
from q1 import print_depth as print_depth_dict
from q2 import print_depth as print_depth_object
from q2 import Person
from q3 import lca as lca_node
from main import Node


class TestBongo(unittest.TestCase):
  print("**************************")
  print("**UNIT TESTING FROM HERE**")
  print("**************************")

  def test_print_depth_dict(self):
    q1_test = {
      "key1": 1,
      }
    print_depth_dict(q1_test)

  def test_print_depth_object(self):
    person_a = Person("User", "1", None)
    q2_test = {
      "key1": 1,
      "user": person_a,
    }
    print_depth_object(q2_test)

  def test_lca(self):
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    self.assertEqual(lca_node(root, 2, 3).key, 1)

if __name__ == '__main__':
    unittest.main()