from env.blackjack_env import Blackhjackenv

env = Blackhjackenv()

print(f"actions are {env.actions}")
state = env.reset()
print(f"Initial States are: {state}")

next_state, reward, done = env.step(action=1)
print(f"Next_state: {next_state}, Reward: {reward}, Done: {done}")

env.close()