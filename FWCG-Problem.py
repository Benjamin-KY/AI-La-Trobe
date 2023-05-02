
### Import library
import heapq


print("Problem Description: Farmer, Wolf, Goat and Cabbage Problem. A farmer has a wolf, a goat, and a cabbage on the east side of a river.")
print("He wants to move them to the west side of the river. He has a boat in which he and only one other thing may fit.The wolf will eat the goat if they are left together unattended.")
print("The goat will eat the cabbage if they are left together unattended. Generate a plan for the farmer to safely move all items including himself to the west side of the river.") 

### Defines State class to represent states of the problem
class State:
    id_counter = 0
    
    def __init__(self, farmer, wolf, goat, cabbage):
        self.state = (farmer, wolf, goat, cabbage) ### Stores the state as a tuple
        self.safe = (wolf != goat or farmer == goat) and (goat != cabbage or farmer == cabbage) ### Checks if the state is safe
        self.id = State.id_counter
        State.id_counter += 1

### Defines a method to check if the state is the goal state (all items on the west side)
    def is_goal(self):
        return all(not x for x in self.state)
### Defines a method to convert the state into a readable string format
    def __str__(self):
        f, w, g, c = self.state
        positions = {0: "On East Side", 1: "On West Side"}
        return f"Farmer: {positions[f]}, Wolf: {positions[w]}, Goat: {positions[g]}, Cabbage: {positions[c]}"

    def __repr__(self):
        return self.__str__()

### Check if two State objects are equal by comparing their state tuples
    def __eq__(self, other):
        return self.state == other.state

### This method returns a hash value for the State object. It uses the built-in hash function on the state tuple to return a unique value.
    def __hash__(self):
        return hash(self.state)

### This method calculates and returns the list of next possible States that can be reached from the current State.
### It loops through all the possible actions, which include all combinations of the farmer and one of the items.
### It creates a new State object for each possible action and checks if it is safe.
### If the new State is safe, it is added to the list of new States that can be reached from the current State.
    def next_states(self):
        f, w, g, c = self.state
        new_states = []
        for action in [(1 - f, w, g, c), (1 - f, 1 - w, g, c), (1 - f, w, 1 - g, c), (1 - f, w, g, 1 - c)]:
            new_state = State(*action)
            if new_state.safe:
                new_states.append(new_state)
        return new_states


def heuristic(state):
    # Rule 1: Don't let the wolf eat the goat
    # Rule 2: Don't let the goat eat the cabbage
    # Rule 3: Move the farmer with each item, so that the farmer doesn't have to come back
    f, w, g, c = state.state
    return (w != g) + (g != c) + (f == w) + (f == g) + (f == c)


def depth_first_search(initial_state):
    visited, stack = set(), [(initial_state, [])]
    while stack:
        state, path = stack.pop()
        if state.is_goal():
            return path + [state]
        visited.add(state)
        for new_state in state.next_states():
            if new_state not in visited:
                stack.append((new_state, path + [state]))
    return None


def a_star_search(initial_state):
    visited, queue = set(), [(heuristic(initial_state), initial_state.id, initial_state, [])]
    while queue:
        _, _, state, path = heapq.heappop(queue)
        if state.is_goal():
            return path + [state]
        visited.add(state)
        for new_state in state.next_states():
            if new_state not in visited:
                heapq.heappush(queue, (heuristic(new_state) + len(path) + 1, new_state.id, new_state, path + [state]))
    return None
    
def display_state_space():
    print("\nState Space")
    print("Showing all possible states, including invalid ones:")
    for farmer in [0, 1]:
        for wolf in [0, 1]:
            for goat in [0, 1]:
                for cabbage in [0, 1]:
                    state = State(farmer, wolf, goat, cabbage)
                    print(state)
    print()

### Define the initial state space
initial_state = State(1, 1, 1, 1)


### Display the state space
display_state_space()

###Display the solution for the DFS algorithm or return a failure message if it cannot be reached
dfs_solution = depth_first_search(initial_state)
if dfs_solution:
    print("Depth-First Search Solution:")
    for state in dfs_solution:
        print(state)
else:
    print("Depth-First Search failed to find a solution.")

print()


###Display the solution for the A* algorithm or return a failure message if it cannot be reached
astar_solution = a_star_search(initial_state)
if astar_solution:
    print("A* Search Solution:")
    for state in astar_solution:
        print(state)
else:
    print("A* Search failed to find a solution.")