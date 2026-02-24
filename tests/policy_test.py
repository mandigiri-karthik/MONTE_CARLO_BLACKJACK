from Policies.simple_policy import Simplepolicy

policy = Simplepolicy(threshold=21)

state = (20,10,0)
action = 0

print(policy.get_action(state= state))
print(policy.action_prob(state= state, action=action))