import numpy as np
import matplotlib.pyplot as plt


N_SIM = 10000


#parameters
BETS_PER_YEAR = 109
AVG_STAKE = 25
STAKE_SIGMA = 1.09
ODDS = 1.91
HOLD = 0.1016
P_TRUE = 1 / ODDS * (1 - HOLD) + HOLD


age_groups = {
  "18-29": 1.409,
  "30-49": 1.182,
  "50-64": 0.864,
  "65+": 0.545
}


#simulate one year
def simulate_one_year(bets_per_year, avg_stake, stake_sigma, p_true, odds):
  profit = 0
  for _ in range(bets_per_year):
      stake = np.random.lognormal(mean=np.log(avg_stake), sigma=stake_sigma)
      win = np.random.rand() < p_true
      profit += stake * (odds - 1) if win else -stake
  return -profit  # positive = money lost


results = {}
for age_label, scale in age_groups.items():
  total_bets = int(BETS_PER_YEAR * scale)
  results[age_label] = np.array([
      simulate_one_year(total_bets, AVG_STAKE, STAKE_SIGMA, P_TRUE, ODDS)
      for _ in range(N_SIM)
  ])


mean_losses = {age: np.mean(vals) for age, vals in results.items()}


#plot the graph
plt.figure(figsize=(12,6))
colors = ['skyblue', 'blue', 'navy', 'darkblue']
for i, (age, vals) in enumerate(results.items()):
  plt.hist(vals, bins=100, color=colors[i], alpha=0.5, label=f'{age} (Mean: ${mean_losses[age]:.2f})')
  plt.axvline(mean_losses[age], color=colors[i], linestyle='dashed', linewidth=2)


plt.xlim(-5000, 4000)
plt.title('Low Risk Male — Annual Money Lost by Age Group', fontsize=14)
plt.xlabel('Annual Loss ($)', fontsize=12)
plt.ylabel('Number of Simulations', fontsize=12)
plt.legend(fontsize=10)
plt.grid(alpha=0.3)
plt.show()