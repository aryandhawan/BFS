# TODO create a node
# TODO create a space for the node
# TODO create a queue strucutre for BFS
# TODO create a BFS function
# TODO create a function to check if the node is the goal
# TODO create a function to expand the node
# TODO create a function to check if the node is in the space
# TODO create a function to check if the node is in the queue
class Node:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action

class QueueFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def remove(self):
        if self.is_empty():
            raise Exception("Frontier is empty!")
        return self.frontier.pop(0)  # FIFO (Queue)

    def is_empty(self):
        return len(self.frontier) == 0

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

class SearchAlgorithm:
    def __init__(self, start_state, goal_state, neighbors_func):
        self.start_state = start_state
        self.goal_state = goal_state
        self.neighbors_func = neighbors_func

    def breadth_first_search(self):
        start_node = Node(self.start_state)
        frontier = QueueFrontier()
        frontier.add(start_node)
        explored = set()

        while not frontier.is_empty():
            node = frontier.remove()

            # Goal check
            if node.state == self.goal_state:
                return self.reconstruct_path(node)

            explored.add(node.state)

            # Expand node
            for action, state in self.neighbors_func(node.state):
                if state not in explored and not frontier.contains_state(state):
                    child_node = Node(state, node, action)
                    frontier.add(child_node)

        return None  # No solution found

    def reconstruct_path(self, node):
        path = []
        while node.parent is not None:
            path.append((node.action, node.state))
            node = node.parent
        path.reverse()
        return path

def test_bfs():
    # Define a simple graph
    graph = {
        'A': [('go to B', 'B'), ('go to C', 'C')],
        'B': [('go to D', 'D'), ('go to E', 'E')],
        'C': [('go to F', 'F')],
        'D': [],
        'E': [('go to G', 'G')],
        'F': [],
        'G': []
    }

    # Function to get neighbors
    def neighbors(state):
        return graph.get(state, [])

    # Create the search object
    search = SearchAlgorithm(start_state='A', goal_state='G', neighbors_func=neighbors)

    # Run BFS
    solution = search.breadth_first_search()

    # Print the solution path
    if solution:
        print("Path found:", solution)
    else:
        print("No path found.")

# Run the test
test_bfs()

