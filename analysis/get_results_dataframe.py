import numpy as np, pandas as pd


def get_results_dataframe(
    results_path = '../expirement_data/results',
    iterations = 5,
    techniques = ['isvd', 'knn', 'mean', 'median', 'zero'],
    percentages = [10, 30, 50, 70]
):
    data = {}
    data['tipo'] = []
    data['percentual'] = []
    data['F1'] = []
    data['Pearson_Correlation'] = []
    data['RMSE'] = []
    data['pesos'] = []
    data['kernel_names'] = []
    
    for technique in techniques:
        for percentage in percentages:
            
            mean_f1 = []
            mean_pearsonCorrelation = []
            mean_RMSE = []
            weights = []
            
            for iteration in range(iterations):
                base_path = f'{results_path}/{iteration}/{technique}/{percentage}'
                
                
                f1_file = f'{base_path}/F1_score.txt'
                f1 = np.loadtxt(f1_file)
                mean_f1.append(f1.mean())
                
                
                pearsonCorrelation_file = f'{base_path}/Pearson_correlation.txt'
                pearsonCorrelation = np.loadtxt(pearsonCorrelation_file)
                mean_pearsonCorrelation.append(pearsonCorrelation.mean())
                
                
                RMSE_file = f'{base_path}/RMSE.txt'
                RMSE = np.loadtxt(RMSE_file)
                mean_RMSE.append(RMSE.mean())
                
                
                mean_weights = np.loadtxt(f'{base_path}/pairwise_kernel_weights.txt').mean(axis=0)
                weights.append(mean_weights)
                
                
                kernel_names = open(f'{base_path}/pairwise_kernel_names.txt', 'r').read().split('\t')
                
                
            data['tipo'].append(technique)
            data['percentual'].append(percentage)
            data['F1'].append(np.mean(mean_f1))
            data['Pearson_Correlation'].append(np.mean(mean_pearsonCorrelation))
            data['RMSE'].append(np.mean(mean_RMSE))
            data['pesos'].append(np.mean(weights, axis=0))
            data['kernel_names'].append(kernel_names)
            
    return pd.DataFrame(data=data)
