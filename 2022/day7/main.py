#!/usr/bin/python3

class TrieNode:
    def __init__(self, size: int, parent_node):
        self.parent_node: TrieNode = parent_node
        self.is_file = size > 0
        self.children: dict[str, TrieNode] = {}
        self.total_size: int = size

    def __str__(self):
        return f"{{'size':{self.size}, 'children': {[k+': '+ str(v) for k,v in self.children.items()]}}})"

    def get_total_size(self) -> int:
        if self.total_size:
            pass
        else:
            self.total_size = sum([child.get_total_size() for child in self.children.values()])
        return self.total_size

def read_file(filename):
    with open(filename) as f:
        return [row.strip('\n') for row in f.readlines()]

def build_filesystem(commands_and_results):
    root = TrieNode(0, None)
    current_node = None

    for row in commands_and_results:
        if row.startswith('$ cd'):
            dir = row.split(' ')[2]
            match dir:
                case '/':
                    current_node = root
                case '..':
                    current_node = current_node.parent_node
                case _:
                    current_node = current_node.children[dir]
        elif row.startswith('$ ls'):
            pass
        elif row.startswith('dir'):
            current_node.children[row.split(' ')[1]] = TrieNode(0, current_node)
        else:
            file_size, file_name = row.split(' ')
            current_node.children[file_name] = TrieNode(int(file_size), current_node)

    return root


def part1():
    commands_and_result = read_file('input.txt')
    root = build_filesystem(commands_and_result)
    folders = [root]

    res = 0
    while folders:
        folder = folders.pop(0)
        if(folder.get_total_size() <= 100000):
            res += folder.get_total_size()
            
        for child in folder.children.values():
            if not child.is_file:
                folders.append(child)

    print(res)

def part2():
    commands_and_result = read_file('input.txt')
    root = build_filesystem(commands_and_result)
    minimum_to_remove = 30000000 - (70000000 - root.get_total_size())

    folders = [root]

    minimum_removed = 70000000
    while folders:
        folder = folders.pop(0)
        folder_size = folder.get_total_size()
        if(folder_size >= minimum_to_remove and folder_size < minimum_removed):
            minimum_removed = folder_size
            
        for child in folder.children.values():
            if not child.is_file:
                folders.append(child)

    print(minimum_removed)

part1()
part2()

# Lire l'input => refaire un filesystem
# On veut compter la taille des dossiers
# qui font moins de 100ko
