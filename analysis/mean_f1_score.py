import numpy as np, matplotlib.pyplot as plt


original_f1_mean = np.loadtxt('../complete_drug_response_data/F1_score.txt').mean()
results_path = '../imputed_kernels_results'


for percentage in [10, 30, 50, 70]:
    data = {'original': original_f1_mean}
    
    for technique in ['zero', 'mean', 'median', 'isvd', 'knn']:
        data[technique] = np.loadtxt(results_path + f'/{technique}/{percentage}/F1_score.txt').mean()
    
    # Assembly plot
    labels = data.keys()
    values = data.values()
    
    fig, ax = plt.subplots()
    bars = ax.bar(labels, values)
    ax.bar_label(bars)
    
    plt.xlabel('Techniques')
    plt.ylabel('Mean F1 Score')
    plt.title(f'Mean F1 Score per Tecnique with {percentage}% NANs')
    
    plt.savefig(f'./plots/mean_f1_score/mean_f1_score_{percentage}.png')