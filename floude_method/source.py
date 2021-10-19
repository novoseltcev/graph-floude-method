from logging import log

import numpy as np
from methodtools import lru_cache

from floude_method.error import *


class Answer:
    def __init__(self, start, end, msg, status='Failed', weight=np.inf, paths=None):
        self.start = start
        self.end = end
        self.status = status
        self.weight = weight
        self.paths = tuple(paths)
        self.min_paths = self._minimize_paths()
        self.msg = msg

    def _minimize_paths(self):
        result = [x.split(' -> ') for x in self.paths]
        min_length = len(result[0])
        for obj in result:
            if len(obj) <= min_length:
                min_length = len(obj)

        for obj in result:
            if len(obj) < min_length:
                del obj
        return tuple(' -> '.join(x) for x in result)

    def __str__(self):
        result = [
            'status - ' + self.status,
            str(self.start) + '->' + str(self.end) + ': ' + 'weight = ' + str(self.weight) + ';',
            'paths: ' + str(self.paths) + ';',
            'min_paths: ' + str(self.min_paths) + ';',
        ]
        return '\n'.join(result)


class FloudeMethod:
    def __init__(self, graph):
        self.graph = np.array(graph, dtype='float32')
        self._check_dimension()
        self._normalize_nonexistent_edges()
        self._paths = [self.graph.copy()]
        self._links = []

    def __len__(self):
        return len(self.graph)

    def _check_dimension(self):
        if len(self) ** 2 != self.graph.size:
            raise DimensionError()

    @staticmethod
    def _check_indexes(i, j):
        if i == j:
            raise NoPathError()

    def _check_path(self, i, j):
        if self._paths[-1][i, j] == np.inf:
            raise NoPathError()

    def _normalize_nonexistent_edges(self):
        null_indexes = np.where(self.graph == 0)
        null_indexes = list(zip(null_indexes[0], null_indexes[1]))
        for i, j in null_indexes:
            self.graph[i][j] = np.inf

    @lru_cache(maxsize=10)
    def _calculate_path_matrix(self):
        n = len(self)
        for k in range(n):
            path_matrix = self._paths[-1]
            next_path_matrix = np.zeros((n, n), dtype='float32')
            next_path_matrix[k] = path_matrix[k]
            next_path_matrix[:, k] = path_matrix[:, k]
            log(level=0, msg='Calculating matrix: ' + str(k+1))
            for i in range(n):
                for j in range(n):
                    without_node_weight = path_matrix[i, j]
                    with_node_weight = path_matrix[i, k] + path_matrix[k, j]
                    next_path_matrix[i, j] = without_node_weight if without_node_weight <= with_node_weight else with_node_weight
            self._paths.append(next_path_matrix)
        log(level=0, msg='Done calculating...')
        return self._paths[-1]

    def _generate_links(self, i, j):
        decisions = []
        last_path_matrix = self._paths[-1]
        weight = last_path_matrix[i, j]
        for k in range(len(self) - 1, -1, -1):
            if k in (i, j): continue
            last_path_matrix = self._paths[k]
            with_node_weight = last_path_matrix[i, k] + last_path_matrix[k, j]
            if with_node_weight == weight:
                decisions.append(k)
            weight = min(with_node_weight, last_path_matrix[i, j])

        if len(decisions) == 0:
            self._links.append([i, j])
        for key in decisions:
            yield from self._generate_links(i, key)
            yield from self._generate_links(key, j)

    def _get_shortest_paths(self, i, j):
        self._links.clear()
        linker = self._generate_links(i, j)
        while True:
            try:
                next(linker)
            except StopIteration:
                break

        paths = []  # TODO - topological sort
        while True:
            start = list(filter(lambda x: x[0] == i, self._links))
            if len(start) == 0:
                break
            self._links.remove(start[0])
            cur_path = [start[0]]
            while True:
                values = list(filter(lambda x: x[0] == cur_path[-1][1], self._links))
                if len(values) == 0:
                    break
                cur_path.append(values[0])
            paths.append(' -> '.join(str(obj[0]) for obj in cur_path) + ' -> ' + str(cur_path[-1][-1]))
        return paths

    def solve(self, start, end):
        try:
            i, j = start, end
            self._check_indexes(i, j)
            path_matrix = self._calculate_path_matrix()
            self._check_path(i, j)
            weight = path_matrix[i, j]
            shortest_paths = self._get_shortest_paths(i, j)
            answer = Answer(i, j, 'Done', 'Compete', weight, shortest_paths)
        except DimensionError as error:
            answer = Answer(start, end, error.args[0])
        except NoPathError as error:
            answer = Answer(start, end, error.args[0])
        return answer


if __name__ == '__main__':
    # print(, end='\n\n')
    matrix1 = [
        [0, 4, 0, 2],
        [0, 0, 6, 0],
        [0, 0, 0, 0],
        [0, 1, 10, 0]
    ]
    g = FloudeMethod(matrix1)

    print('\n')
    print("\n".join("\t".join(map(str, x)) for x in matrix1))
    print()
    print(g.solve(0, 1), end='\n\n')
    print(g.solve(1, 2), end='\n\n')
    print(g.solve(0, 3), end='\n\n')
    print(g.solve(0, 2), end='\n\n')

    matrix2 = [
        [0, 10, 20, 0, 20, 0, 0, 0],
        [10, 0,  0, 20, 0, 0, 0, 0],
        [10, 0,  0, 0, 0, 20, 0, 0],
        [0, 10, 0, 0, 20, 0, 20, 0],
        [10, 0, 0, 20, 0, 20, 0, 0],
        [0, 0, 10, 0, 20, 0, 0, 20],
        [0, 0, 0, 10, 0, 0, 0, 20],
        [0, 0, 0, 0, 0, 20, 3, 0]
    ]
    g2 = FloudeMethod(matrix2)
    print('\n')
    print("\n".join("\t".join(map(str, x)) for x in matrix2))
    print()
    print(g2.solve(0, 5), end='\n\n')

    matrix3 = [
        [0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 2, 0, 0, 0]
    ]
    g3 = FloudeMethod(matrix3)
    print('\n')
    print("\n".join("\t".join(map(str, x)) for x in matrix3))
    print()
    print(g3.solve(0, 1), end='\n\n')
