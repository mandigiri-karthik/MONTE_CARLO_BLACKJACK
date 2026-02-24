from env.blackjack_env import Blackhjackenv
from Policies.simple_policy import Simplepolicy

env = Blackhjackenv()
pol = Simplepolicy(threshold=20)

episodes = env.generate_episode(policy= pol)
print (f"Episodes are {episodes}")

next_state, reward, done = env.step(action=1)
print(f"Next_state: {next_state}, Reward: {reward}, Done: {done}")

env.close()