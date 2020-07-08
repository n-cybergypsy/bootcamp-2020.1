from binarytree import build

def leaf_to_root(root, arr):

    if root == None:
        return None

    arr.append(root.val)

    if (root.left == None) and (root.right == None):
        print(arr)
    
    leaf_to_root(root.left, arr)
    leaf_to_root(root.right, arr)


def mirror(root):

    if root:
        # Swaps left and right nodes.
        temp = root.left
        root.left = root.right
        root.right = temp
        # Swaps left and right nodes of children recursively.
        mirror(root.left)
        mirror(root.right)
    
    return root



nodes = [1, 2, 3, 4, 5, 6, 7, None, None, None, None, 8, 9]
tree = build(nodes)

print(tree)
arr = []
leaf_to_root(tree, arr)

node_2 = [1, 2, 3, 4, 5, 6, 7]
second = build(node_2)

print(second)
print(mirror(second))

