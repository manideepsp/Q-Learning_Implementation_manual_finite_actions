import numpy as np

gamma = 0.75
alpha = 0.9

location_to_state = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11
}
actions = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

R = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 1, 0, 0, 0, 1000, 1, 0, 0, 0, 0],  #
              [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]])

Q = np.array(np.zeros([12, 12]))

for i in range(1000):  # Reinforcing for 1000 times
    current_state = np.random.randint(0, 12)
    playable_actions = []
    for j in range(12):  # for each state
        if R[current_state, j] > 0:  # From Rewards matrix
            playable_actions.append(j)

    # selecting any random action from playable actions
    next_state = np.random.choice(playable_actions)

    TD = R[current_state, next_state]
    + gamma * Q[next_state, np.argmax(Q[next_state,])]
    - Q[current_state, next_state]

    Q[current_state, next_state] = Q[current_state, next_state] + alpha * TD

print(Q.astype(int))

state_to_location = {state: location for location, state in location_to_state.items()}


# print(state_to_location)
# print(location_to_state)

def route(starting_location, ending_location):
    route = [starting_location]
    current_location = starting_location

    while current_location != ending_location:
        current_state = location_to_state[current_location]
        next_state = np.argmax(Q[current_state])
        next_location = state_to_location[next_state]

        # Check if next location is same as current location or if it's already in the route
        if next_location == current_location or next_location in route:
            # If so, break out of the loop to avoid infinite loop
            break

        route.append(next_location)
        current_location = next_location

    return route


# print("Route:")
rout = route('E', 'D')
print(rout)
