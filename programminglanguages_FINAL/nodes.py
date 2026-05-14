class Node:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        self.children = []

    def add_child(self, child):
        if child:
            self.children.append(child)

    def print_tree(self, indent="", is_last=True):
        marker = "└── " if is_last else "├── "
        print(indent + marker + self.name + (f" ({self.value})" if self.value else ""))
        indent += "    " if is_last else "│   "
        child_count = len(self.children)
        for i, child in enumerate(self.children):
            child.print_tree(indent, i == child_count - 1)

    def to_dict(self):
        if not self.children:
            return self.value if self.value else {}
        res = {}
        for child in self.children:
            clean_name = child.name.strip("<>")
            res[clean_name] = child.to_dict()
        return res