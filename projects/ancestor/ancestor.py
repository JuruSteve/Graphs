class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self,vertex_id):
        self.vertices[vertex_id] = set()
    
    def add_edges(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That Vertex does not exist. Unable to add edge")

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


def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    for ancestor in ancestors:
        g.add_vertex(ancestor[0])
        g.add_vertex(ancestor[1])
        g.add_edges(ancestor[0], ancestor[1])



    qq = Queue()
    visited = set()
    qq.enqueue([starting_node])

    while qq.size() > 0:
        path = qq.dequeue()
        v = path[-1]
        if v not in visited:
            visited.add(v)
            for neighbor in g.vertices[v]:
                new_path = list(path)
                new_path.append(neighbor)
                qq.enqueue(new_path)
