
from collections import defaultdict # default dict used as a map, to store node-value mapping.
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
# Tree Class
class Tree:
    def __init__(self):
        self.root = None
        self.map_nodes = defaultdict(Node)
    def Insert(self,parent, child,dir):
        if self.root is None:
            root_node = Node(parent)
            child_node = Node(child)
            if dir == 'L':
                root_node.left = child_node
            else:
                root_node.right = child_node
            self.root = root_node
            self.map_nodes[parent] = root_node
            self.map_nodes[child] = child_node
            return
        parent_node = self.map_nodes[parent]
        child_node = Node(child)
        self.map_nodes[child] = child_node
        if dir == 'L':
            parent_node.left = child_node
        else:
            parent_node.right = child_node
        return
def LeftView(root):
    max_level = 0
    sol=[]
    def leftViewUtil(root, level, max_level): 
        print(level)
        if root is None: 
            print("this")
            return
      
        if (max_level < level): 
            
            print(root.data)
            sol.append(root.data)
            print(sol)
            max_level = level 
      
        leftViewUtil(root.left, level+1, max_level) 
        leftViewUtil(root.right, level+1, max_level) 
        
        
    leftViewUtil(root, 1, max_level) 
    
    print(" ".join(str(x) for x in sol),end="")
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())  # number of nodes in tree
        a = list(map(str, input().strip().split()))  # parent child info in list
        # construct the tree according to given list
        tree = Tree()
        i = 0
        while (i < len(a)):
            parent = int(a[i])
            child = int(a[i + 1])
            dir = a[i + 2]
            i += 3
            tree.Insert(parent, child, dir)  # Insert the nodes in tree.
        LeftView(tree.root)
        print()
