import numpy as np, matplotlib.pyplot as plt

original_f1_mean = np.loadtxt('../complete_drug_response_data/F1_score.txt').mean()

zero_10_mean = np.loadtxt('../imputed_kernels_results/zero/10/F1_score.txt').mean()

print(original_f1_mean, zero_10_mean)

data = {'Original': original_f1_mean, 'Zero 10': zero_10_mean}

labels = data.keys()
values = data.values()

fig, ax = plt.subplots()
bars = ax.bar(labels, values)
ax.bar_label(bars)

plt.xlabel("Iterations")
plt.ylabel("Mean F1 Score")

plt.savefig('./plots/mean_f1_score.png')