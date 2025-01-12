class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

class Tree:
    def __init__(self):
        self.root = None
        # self.insert(None, "root")  # Create root node
        self.root = TreeNode(value="root")


    def insert(self, parent_node, value):
        """Insert a value into the tree under the specified parent TreeNode."""
        if not self.root:
            if parent_node is not None:
                raise ValueError("Tree is empty; parent_node must be None to create root.")
            self.root = TreeNode(value)
        else:
            if not isinstance(parent_node, TreeNode):
                raise ValueError("parent_node must be a TreeNode object.")
            parent_node.children.append(TreeNode(value))

    def traverse(self, method="pre_order"):
        """Traverse the tree and return a list of values."""
        result = []
        if method == "pre_order":
            self._pre_order_recursive(self.root, result)
        elif method == "post_order":
            self._post_order_recursive(self.root, result)
        else:
            raise ValueError("Unsupported traversal method. Use 'pre_order' or 'post_order'.")
        return result

    def _pre_order_recursive(self, node, result):
        if node:
            result.append(node.value)
            for child in node.children:
                self._pre_order_recursive(child, result)

    def _post_order_recursive(self, node, result):
        if node:
            for child in node.children:
                self._post_order_recursive(child, result)
            result.append(node.value)

    def print_tree_levels(self):
        """Print each level of the tree."""
        if not self.root:
            print("Tree is empty.")
            return

        from collections import deque
        queue = deque([(self.root, 0)])  # Queue holds (node, level)
        current_level = 0
        level_nodes = []

        while queue:
            node, level = queue.popleft()

            if level != current_level:
                print(f"Level {current_level}: {', '.join(level_nodes)}")
                level_nodes = []
                current_level = level

            level_nodes.append(node.value)

            for child in node.children:
                queue.append((child, level + 1))

        # Print the last level
        if level_nodes:
            print(f"Level {current_level}: {', '.join(level_nodes)}")

    def print_tree_paths(self):
        """Print all paths (or lags) from root to each leaf node."""
        x=[]
        if not self.root:
            print("Tree is empty.")
            return

        def _print_paths_recursive(node, path, x):
            if node:
                path.append(node.value)
                if not node.children:  # Leaf node
                    print(" --> ".join(path))
                    x.append(path.copy())
                else:
                    for child in node.children:
                        _print_paths_recursive(child, path, x)
                path.pop()

        _print_paths_recursive(self.root, [], x)
        print(x)


# Example Usage
if __name__ == "__main__":
    tree = Tree()
    # tree.insert(None, "root")  # Create root node
    root_node = tree.root
    tree.insert(root_node, "child 0")
    tree.insert(root_node, "child 1")
    tree.insert(root_node, "child 2")

    child0_node = root_node.children[0]
    tree.insert(child0_node, "child 0.0")
    tree.insert(child0_node, "child 0.1")

    child1_node = root_node.children[1]
    tree.insert(child1_node, "child 1.0")
    tree.insert(child1_node, "child 1.1")

    child00_node = child0_node.children[0]
    tree.insert(child00_node, "child 0.0.0")
    tree.insert(child00_node, "child 0.0.1")
    tree.insert(child00_node, "child 0.0.2")

    # print("Pre-order Traversal:", tree.traverse(method="pre_order"))
    # print("Post-order Traversal:", tree.traverse(method="post_order"))
    # print("Tree Levels:")
    # tree.print_tree_levels()
    print("Tree Paths:")
    tree.print_tree_paths()
