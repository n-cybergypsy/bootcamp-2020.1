from binarytree import build

def leaf_to_root(root, arr):

    if root == None:
        return None

    arr.append(root.val)

    if (root.left == None) and (root.right == None):
        print(arr)
    
    leaf_to_root(root.left, arr)
    leaf_to_root(root.right, arr)


nodes = [1, 2, 3, 4, 5, 6, 7, None, None, None, None, 8, 9]
tree = build(nodes)

print(tree)
arr = []
leaf_to_root(tree, arr)
