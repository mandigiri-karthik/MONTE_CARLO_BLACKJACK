from Policies.base_policy import Policy

class Simplepolicy(Policy):
    def __init__(self, threshold: float):
        self.threshold = threshold

    def get_action(self, state):
        """
        Takes the state
        Returns : action based on the condition
        """
        player_sum, _, _ = state
        return 0 if player_sum >= self.threshold else 1
    
    def action_prob(self, state, action):
        return 1.0 if self.get_action(state=state) == action else 0.0
    
    def __repr__(self):
        return f"SimplePolicy(threshold = {self.threshold})"