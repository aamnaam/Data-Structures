class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None

    # Inserting a node into the tree
    def insert(self, val):

        # If no nodes in the tree yet
        if self.root is None:
            self.root = Node(val)

        else:
            self.insert_child(val, self.root)

    # Inserting in an already existing tree
    def insert_child(self, val, parent):

        # If val is equal to any node, it is ignored to prevent duplicates
        # Inserting in left subtree if val is less than root
        if val < parent.key:
            if parent.left is None:  # nothing in left subtree
                parent.left = Node(val)
            else:
                self.insert_child(val, parent.left)  # inserting into left subtree recursively

        # Inserting in right subtree if val is greater than root
        elif val > parent.key:
            if parent.right is None:
                parent.right = Node(val)
            else:
                self.insert_child(val, parent.right)

    def rank(self, val):
        pass

    def print_inorder(self, node):
        if node is None:
            pass

        else:
            self.print_inorder(node.left)
            print(node.key)
            self.print_inorder(node.right)


def main():
    t = BST()
    t.insert(49)
    t.insert(79)
    t.insert(46)
    t.insert(41)
    t.insert(46)

    print("Inorder:")
    t.print_inorder(t.root)


if __name__ == '__main__':
    main()
