"""
The main idea is to generate graph which which has an Eulerian path in it.
Node is a cell in our board, edge between two cells means that path exists.

We will construct such graph that:
 - each node has even degree
 - graph is one connectivity component
 - total number of edges will be less than n * m * 5 (it's completed by declaration)
"""

import sys
from dataclasses import dataclass
from typing import TypeAlias

sys.setrecursionlimit(100 * 100 * 10)


@dataclass(frozen=True, eq=True, order=True)
class Node:
    x: int
    y: int


class Graph:

    Edge: TypeAlias = tuple[Node, Node]
    Response: TypeAlias = list[tuple[int, int]]
    _ALL_FRONT_MOVES = [
        (2, 1),
        (2, -1),
        (-2, 1),
        (-2, -1),
        (1, 2),
        (-1, 2),
        (1, -2),
        (-1, -2),
    ]

    def __init__(self, n: int, m: int):
        assert n >= 4 and m >= 4, "Our board should be at least 4 by 4"
        self.n = n
        self.m = m
        self._path: self.Response = []
        self._forbidden_edges: set[self.Edge] = set()
        self._build_graph()        

    def calculate_ans(self) -> Response:
        self._euler_path(Node(0, 0))
        assert len(self._path) < self.n * self.m * 5
        return self._path

    def _valid_node(self, node: Node):
        return 0 <= node.x < self.n and 0 <= node.y < self.m

    def _build_graph(self):
        self._occure_graph: list[list[int]] = [[0] * self.m for _ in range(self.n)]
        self._calculate_forbidden_edges()

    def _calculate_forbidden_edges(self):
        """
        We have 8 nodes with odd degree: 
        (1, 0), (0, 1), (n - 1, 0), (n, 1)
        (0, m - 2), (1, m - 1), (n, m - 2), (n - 2, m - 1)
        let's calculate simple path between every two of them
        """
        # print('hele')
        self.make_edges_forbidden([
            (Node(1, 0), Node(0, 2)), 
            (Node(self.n - 2, 0), Node(self.n - 1, 2)),
            (Node(0, self.m - 3), Node(1, self.m - 1)),
            (Node(self.n - 1, self.m - 3), Node(self.n - 2, self.m - 1)),
        ])

        for i in range(1, self.m - 3):
            self.make_edges_forbidden([
                (Node(0, i), Node(2, i + 1)),
                (Node(0, i + 2), Node(2, i + 1)),
                (Node(self.n - 3, i + 1), Node(self.n - 1, i)),
                (Node(self.n - 3, i + 1), Node(self.n - 1, i + 2)),
            ])

    def _euler_path(self, node: Node):
        stack = [node]
        while len(stack):
            cur_node = stack[-1]
            found_node = False
            while (cur_occure := self._occure_graph[cur_node.x][cur_node.y]) < len(self._ALL_FRONT_MOVES):
                cur_dist = self._ALL_FRONT_MOVES[cur_occure]
                new_node = Node(cur_node.x + cur_dist[0], cur_node.y + cur_dist[1])
                self._occure_graph[cur_node.x][cur_node.y] += 1
                edge = (cur_node, new_node)
                if edge not in self._forbidden_edges and self._valid_node(new_node):
                    self.make_edge_forbidden(edge)
                    found_node = True
                    stack.append(new_node)
                    break
            if not found_node:
                stack.pop()
                self._path.append(cur_node)

    def make_edges_forbidden(self, edges: list[Edge]):
        # map(self.make_edge_forbidden, edges)
        for i in edges:
            self.make_edge_forbidden(i)

    def make_edge_forbidden(self, edge: Edge):
        self._forbidden_edges.add(edge)
        self._forbidden_edges.add((edge[1], edge[0]))


def main():
    n, m = map(int, input().split()) 
    from pprint import pprint
    pprint(Graph(n, m).calculate_ans())


if __name__ == "__main__":
    main()
