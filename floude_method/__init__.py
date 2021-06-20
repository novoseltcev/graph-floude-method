from floude_method.source import FloudeMethod


def shortest_path(graph, start, end):
    solver = FloudeMethod(graph)
    answer = solver.solve(start, end)
    return answer


__all__ = ['shortest_path']
