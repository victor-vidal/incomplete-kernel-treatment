import numpy as np, matplotlib.pyplot as plt

metric = "Pearson_correlation"

results_path = "../imputed_kernels_results"

x = [10, 30, 50, 70]

zero_y = [np.loadtxt(results_path + f'/zero/{percentage}/{metric}.txt').mean() for percentage in x]

mean_y = [np.loadtxt(results_path + f'/mean/{percentage}/{metric}.txt').mean() for percentage in x]

median_y = [np.loadtxt(results_path + f'/median/{percentage}/{metric}.txt').mean() for percentage in x]

isvd_y = [np.loadtxt(results_path + f'/isvd/{percentage}/{metric}.txt').mean() for percentage in x]

knn_y = [np.loadtxt(results_path + f'/knn/{percentage}/{metric}.txt').mean() for percentage in x]

# plot lines
plt.plot(x, zero_y, label = "Zero")
plt.plot(x, mean_y, label = "Mean")
plt.plot(x, median_y, label = "Median")
plt.plot(x, isvd_y, label = "iSVD")
plt.plot(x, knn_y, label = "KNN")
plt.legend()

plt.xlabel("Missing data percentage")
plt.ylabel(metric)

plt.savefig(f'./line_plots/{metric}.png')