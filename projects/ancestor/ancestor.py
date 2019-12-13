class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else: 
            return None
    def size(self):
        return len(self.queue)

class Graph:
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edges(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2) 
        else:
            raise IndexError('Cannot add edge based on given vertices')

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        # build graph in reverse since child knows about parent and not vice versa
        graph.add_edges(pair[1], pair[0])

    qq = Queue()
    qq.enqueue([starting_node])

    max_path_len = 1
    earliest_anc = -1

    while qq.size() > 0:
        path = qq.dequeue()
        v = path[-1]
        if(len(path) >= max_path_len and v < earliest_anc) or (len(path) > max_path_len):
            earliest_anc = v
            max_path_len = len(path)
        for neigh in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neigh)
            qq.enqueue(path_copy) 
    return earliest_anc
