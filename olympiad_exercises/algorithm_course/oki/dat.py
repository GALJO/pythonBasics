def make_graph(_input):
    _graph = {}
    for _i in range(len(_input)):
        _graph.setdefault(_input[_i], [])
        _graph.setdefault(_i + 2, [])
        _graph[_input[_i]].append(_i + 2)
        _graph[_i + 2].append(_input[_i])
    return _graph


n = int(input())
P = tuple(map(int, input().split()))
print(make_graph(P))