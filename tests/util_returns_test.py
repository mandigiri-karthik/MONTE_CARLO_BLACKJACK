from utils.returns import compute_returns

episodes = ([((14, 5, 0), 1, 2.0), ((16, 5, 0), 1, -1.0)])
returns = compute_returns(episode= episodes, gamma=1.0)
print(returns)
