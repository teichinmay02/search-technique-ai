# import heapq
# from collections import deque

# def conflict(state):
#     # Count the number of conflicts between queens
#     conflicts = 0
#     for i in range(4):
#         for j in range(i + 1, 4):
#             if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
#                 conflicts += 1
#     return conflicts

# def solve():
#     # Initialize the starting state
#     start_state = (0, 0, 0, 0)
#     queue = []
#     heapq.heappush(queue, (conflict(start_state), start_state))
#     state_space_tree = {start_state: []}

#     while queue:
#         _, state = heapq.heappop(queue)
#         print("Current state:", state)
#         print("State space tree:", state_space_tree)

#         # Check if we have found a soluti   on
#         if conflict(state) == 0:
#             return state

#         # Generate all possible next states
#         for i in range(4):
#             for j in range(4):
#                 if j != state[i]:
#                     next_state = list(state)
#                     next_state[i] = j
#                     next_state = tuple(next_state)
#                     if next_state not in state_space_tree:
#                         state_space_tree[next_state] = []
#                     state_space_tree[state].append(next_state)
#                     heapq.heappush(queue, (conflict(next_state), next_state))

#     # If we have explored all states and not found a solution, return None
#     return None

# print(solve())



# import heapq

# def conflict(state):
#     # Count the number of conflicts between queens
#     conflicts = 0
#     for i in range(4):
#         for j in range(i + 1, 4):
#             if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
#                 conflicts += 1
#     return conflicts

# def print_tree(state_space_tree, state, level=0):
#     print("  " * level + str(state))
#     if state in state_space_tree:
#         for child in state_space_tree[state]:
#             print_tree(state_space_tree, child, level + 1)

# def solve():
#     # Initialize the starting state
#     start_state = (0, 0, 0, 0)
#     queue = []
#     heapq.heappush(queue, (conflict(start_state), start_state))
#     state_space_tree = {start_state: []}

#     while queue:
#         _, state = heapq.heappop(queue)
#         print("Current state:", state)
#         print_tree(state_space_tree, state)
#         print()

#         # Check if we have found a solution
#         if conflict(state) == 0:
#             return state

#         # Generate all possible next states
#         for i in range(4):
#             for j in range(4):
#                 if j != state[i]:
#                     next_state = list(state)
#                     next_state[i] = j
#                     next_state = tuple(next_state)
#                     if next_state not in state_space_tree:
#                         state_space_tree[next_state] = []
#                     state_space_tree[state].append(next_state)
#                     heapq.heappush(queue, (conflict(next_state), next_state))

#     # If we have explored all states and not found a solution, return None
#     return None

# print(solve())

import heapq
import networkx as nx
import matplotlib.pyplot as plt

def conflict(state):
    # Count the number of conflicts between queens
    conflicts = 0
    for i in range(4):
        for j in range(i + 1, 4):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                conflicts += 1
    return conflicts

def draw_graph(graph):
    pos = nx.spring_layout(graph)
    node_colors = []
    for node in graph.nodes():
        if conflict(node) == 0:
            node_colors.append('green')
        else:
            node_colors.append('lightblue')
    nx.draw(graph, pos, with_labels=True, node_color=node_colors, node_size=1000)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, font_size=10)
    plt.title("4-Queens State Space Graph")
    plt.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
    plt.xticks(range(5), range(5))
    plt.yticks(range(5), range(5))
    plt.grid(True, linestyle='--', color='gray', linewidth=0.5)
    plt.show()

def solve():
    # Initialize the starting state
    start_state = (0, 0, 0, 0)
    queue = []
    heapq.heappush(queue, (conflict(start_state), start_state))
    state_space_tree = nx.Graph()
    state_space_tree.add_node(start_state)

    while queue:
        _, state = heapq.heappop(queue)
        print("Current state:", state)
        print("State space tree:", state_space_tree.nodes())

        # Check if we have found a solution
        if conflict(state) == 0:
            draw_graph(state_space_tree)
            return state

        # Generate all possible next states
        for i in range(4):
            for j in range(4):
                if j != state[i]:
                    next_state = list(state)
                    next_state[i] = j
                    next_state = tuple(next_state)
                    if next_state not in state_space_tree.nodes():
                        state_space_tree.add_node(next_state)
                        state_space_tree.add_edge(state, next_state, weight=conflict(next_state))
                    heapq.heappush(queue, (conflict(next_state), next_state))

    # If we have explored all states and not found a solution, return None
    return None

print(solve())
