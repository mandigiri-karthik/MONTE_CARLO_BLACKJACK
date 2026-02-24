from typing import Tuple, List

def compute_returns (episode : List[Tuple],gamma: float):
    returns = []
    G = 0.0
    for _, _, reward in reversed(episode):
        G = reward + gamma * G
        returns.append(G)
    returns.reverse()
    return returns