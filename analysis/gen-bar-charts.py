import numpy as np, matplotlib.pyplot as plt


original_f1_mean = np.loadtxt('../complete_drug_response_data/RMSE.txt').mean()
results_path = '../imputed_kernels_results'


for percentage in [10, 30, 50, 70]:
    data = {'original': original_f1_mean}
    
    for technique in ['zero', 'mean', 'median', 'isvd', 'knn']:
        data[technique] = np.loadtxt(results_path + f'/{technique}/{percentage}/RMSE.txt').mean()
    
    # Assembly plot
    labels = data.keys()
    values = data.values()
    
    fig, ax = plt.subplots()
    bars = ax.bar(labels, values)
    ax.bar_label(bars)
    
    plt.xlabel('Techniques')
    plt.ylabel('RSME')
    plt.title(f'RSME per Tecnique with {percentage}% NANs')
    
    plt.savefig(f'./plots/rsme/rsme_{percentage}.png')