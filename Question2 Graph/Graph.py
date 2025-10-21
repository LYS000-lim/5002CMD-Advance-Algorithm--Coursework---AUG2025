class Person:
    def __init__(self, name, gender, biography, privacy):
        self.name = name
        self.gender = gender
        self.biography = biography
        self.privacy = privacy
        
class Graph:
    def __init__(self,size):
        self.adj_matrix = [[0] * size for num in range(size)]
        self.size = size
        self.vertex_data = [""] * size