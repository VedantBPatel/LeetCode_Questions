#Delete Duplicate Folders in System
from typing import List
from collections import defaultdict

class Folder:
    def __init__(self):
        self.children = {}
        self.name = ""
        self.duplicate = False

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = Folder()

        # Step 1: Build the folder tree
        def add_path(path):
            node = root
            for folder in path:
                if folder not in node.children:
                    node.children[folder] = Folder()
                    node.children[folder].name = folder
                node = node.children[folder]

        for path in paths:
            add_path(path)

        # Step 2: Serialize each subtree
        serial_map = defaultdict(list)

        def serialize(node):
            if not node.children:
                return ""
            serials = []
            for child in sorted(node.children.values(), key=lambda x: x.name):
                child_serial = serialize(child)
                serials.append(f"({child.name}{child_serial})")
            subtree = "".join(serials)
            serial_map[subtree].append(node)
            return subtree

        serialize(root)

        # Step 3: Mark duplicate folders
        for nodes in serial_map.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.duplicate = True

        # Step 4: Prune duplicates
        def prune(node):
            for name in list(node.children.keys()):
                child = node.children[name]
                if child.duplicate:
                    del node.children[name]
                else:
                    prune(child)

        prune(root)

        # Step 5: Collect remaining paths
        result = []

        def collect_paths(node, path):
            for child in node.children.values():
                new_path = path + [child.name]
                result.append(new_path)
                collect_paths(child, new_path)

        collect_paths(root, [])
        return result

        