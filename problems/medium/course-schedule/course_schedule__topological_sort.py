r"""
>>> from course_schedule__topological_sort import canFinish
>>> canFinish(2, [[1, 0]])
True
>>> canFinish(2, [[1, 0], [0, 1]])
False
"""

from collections import defaultdict, deque


def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    graph = defaultdict(list)
    in_degrees = defaultdict(int)

    for [a, b] in prerequisites:
        graph[b].append(a)
        graph[a]
        in_degrees[a] += 1
        in_degrees[b]

    queue = deque()
    for node, in_degree in in_degrees.items():
        if in_degree == 0:
            queue.append(node)

    courses = set()
    while queue:
        node = queue.popleft()
        courses.add(node)

        for neighbor in graph[node]:
            in_degrees[neighbor] -= 1
            if in_degrees[neighbor] == 0:
                queue.append(neighbor)

    if len(courses) == len(graph):
        return True
    else:
        return False
