class DisJointSets:

    def __init__(self, vertices):
        self.vertices = vertices
        self.mapData = {i: -1 for i in vertices}

    def union(self, vertex1, vertex2):
        status, parent1, parent2 = self.hasCycle(vertex1, vertex2)
        if not status:
            self.mapData[parent2] = parent1
            print(self.mapData)
        else:
            print("cycle detected")

    def find(self, vertex):
        return self.mapData.get(vertex)

    def getParent(self, vertex):
        if self.find(vertex) == -1:
            return vertex
        else:
            vertex = self.find(vertex)
            return self.getParent(vertex)

    def hasCycle(self, vertex1, vertex2):
        parent1 = self.getParent(vertex1)
        parent2 = self.getParent(vertex2)
        if parent1 == parent2:
            return True, None, None
        else:
            return False, parent1, parent2


if __name__ == "__main__":
    vertices = [1, 2, 3, 4, 5, 6, 7, 8]
    t1 = DisJointSets(vertices)
    t1.union(1, 2)
    t1.union(3, 4)
    t1.union(5, 6)
    t1.union(7, 8)
    t1.union(2, 4)
    t1.union(2, 5)
    t1.union(1, 3)
    t1.union(6, 8)
    t1.union(5, 7)
