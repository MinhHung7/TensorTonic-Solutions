import numpy as np

def value_iteration_step(values, transitions, rewards, gamma):
    """
    Perform one step of value iteration and return updated values.
    """ 
    values = np.array(values)
    transitions = np.array(transitions)
    rewards = np.array(rewards)
    
    Q = rewards + gamma * np.dot(transitions, values)

    return np.max(Q, axis=1).tolist()
    # Write code here