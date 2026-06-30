from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        visited = set()
        visited.add(node)

        nodes = {}

        q = deque([node])

        new_node = Node(node.val, [])
        nodes[node] = new_node

        while q:
            curr = q.popleft()
            neighbors = curr.neighbors

            for neighbor in neighbors:
                if neighbor not in nodes:
                    nodes[neighbor] = Node(neighbor.val, [])
                nodes[curr].neighbors.append(nodes[neighbor])
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)

        return nodes[node]

        