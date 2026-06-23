r"""
>>> from course_schedule_ii__topological_sort import findOrder
>>> findOrder(2, [[1, 0]])
[0, 1]
>>> findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) in ([0, 1, 2, 3], [0, 2, 1, 3])
True
>>> findOrder(1, [])
[0]
"""

from collections import deque


def findOrder(numCourses: int, prerequisites: list[list[int]]) -> list[int]:

    graph = {course: [] for course in range(numCourses)}
    in_degrees = {course: 0 for course in range(numCourses)}

    for [a, b] in prerequisites:
        graph[b].append(a)
        in_degrees[a] += 1

    queue = deque()
    for node, in_degree in in_degrees.items():
        if in_degree == 0:
            queue.append(node)

    courses = []
    while queue:
        node = queue.popleft()
        courses.append(node)

        for neighbor in graph[node]:
            in_degrees[neighbor] -= 1
            if in_degrees[neighbor] == 0:
                queue.append(neighbor)

    if len(courses) == numCourses:
        return courses
    else:
        return []
