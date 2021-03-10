import q1
import q2
import q3

print("*************************")
print("-----------Q1------------")
print("*************************")


# sample data for dictionary depth printers
q1_sample = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4,
        }
    }
}

q1.print_depth(q1_sample)

print("*************************")
print("-----------Q2------------")
print("*************************")
# sample data for dictionary and class obect depth printer
person_a = q2.Person("User", "1", None)
person_b = q2.Person("user", "2", person_a)


q2_sample = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4,
            "user": person_b,
        }
    }
}

q2.print_depth(q2_sample)


print("*************************")
print("-----------Q3------------")
print("*************************")

# sample binary tree for least common ancestor finding problem
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)


print("LCA(6,7) = ", q3.lca(root, 6, 7).key)
print("LCA(3,7) = ", q3.lca(root, 3, 7).key)
