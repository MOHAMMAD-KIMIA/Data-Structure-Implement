    def DFS(self, start, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)
        print(start, end=' ')

        current_node = self.vertex[start].head
        while current_node:
            neighbor = current_node.neighbor
            if neighbor not in visited:
                self.DFS(neighbor, visited)
            current_node = current_node.next