r"""
>>> from clone_graph__bfs import cloneGraph, Node
>>> node1 = Node(1); node2 = Node(2); node3 = Node(3); node4 = Node(4)
>>> node1.neighbors = [node2, node4]; node2.neighbors = [node1, node3]
>>> node3.neighbors = [node2, node4]; node4.neighbors = [node1, node3]
>>> clone = cloneGraph(node1)
>>> clone is not node1 and clone.val == 1
True
>>> cloneGraph(None) is None
True
"""

from __future__ import annotations

from collections import defaultdict, deque


class Node:
    """Node in a graph with adjacency list."""

    def __init__(self, val: int = 0, neighbors: list | None = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


"""
class Node:
    def __init__(val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


def cloneGraph(node: "Node" | None) -> "Node" | None:
    if node is None:
        return None

    stack = deque()
    stack.append(node)

    old2new = defaultdict(Node)
    visited = set()
    while stack:
        old_node = stack.pop()

        if old_node in visited:
            continue

        visited.add(old_node)

        new_node = old2new[old_node]
        new_node.val = old_node.val
        new_node.neighbors = [
            old2new[neighbor] for neighbor in old_node.neighbors
        ]

        stack.extend(old_node.neighbors)

    return old2new[node]
