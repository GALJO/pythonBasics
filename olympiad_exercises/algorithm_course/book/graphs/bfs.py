from collections import deque


def bfs(_graph, _search):
    _queue = deque()
    _queue += graph['Jan']
    _searched = []
    while _queue:
        actual_el = _queue.popleft()
        if actual_el not in _searched:
            if actual_el == _search:
                return True
            else:
                _queue += _graph[actual_el]
    return False


graph = {}
graph.setdefault('Jan', ['Olek', 'Scibor', 'Kacper'])
graph.setdefault('Olek', ['Maja', 'Kacper'])
graph.setdefault('Scibor', [])
graph.setdefault('Kacper', [])
graph.setdefault('Maja', [])

stat = bfs(graph, 'Kacper')
if stat:
    print('Jest Kacper')
else:
    print('Nie ma Kacpra')
