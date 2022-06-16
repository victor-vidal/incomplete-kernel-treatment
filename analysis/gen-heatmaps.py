import numpy as np, seaborn as sns, pandas as pd, matplotlib.pyplot as plt

complete_data_path = '../complete_drug_response_data'
results_path = '../imputed_kernels_results'

techniques = ['mean', 'knn', 'median', 'isvd', 'zero']
percentages = ['30', '70', '50', '10']

data = {}
data['tipo'] = []
data['percentual'] = []
data['F1'] = []
data['Pearson_Correlation'] = []
data['RMSE'] = []
data['pesos'] = []
data['kernel_names'] = []

# adding baseline
data['tipo'].append('baseline')
data['percentual'].append(0)
data['F1'].append(np.loadtxt(f'{complete_data_path}/F1_score.txt').mean())
data['Pearson_Correlation'].append(np.loadtxt(f'{complete_data_path}/Pearson_correlation.txt').mean())
data['RMSE'].append(np.loadtxt(f'{complete_data_path}/RMSE.txt').mean())
data['pesos'].append(np.loadtxt(f'{complete_data_path}/pairwise_kernel_weights.txt').mean(axis=0))

with open(f'{complete_data_path}/pairwise_kernel_names.txt', 'r') as f:
    kernel_names = f.read().split('\t')
data['kernel_names'].append(kernel_names)


# adding technique-percentage combinations
for technique in techniques:
    for percentage in percentages:
        base_path = f'{results_path}/{technique}/{percentage}'
        
        mean_f1 = np.loadtxt(f'{base_path}/F1_score.txt').mean()
        mean_pearsonCorrelation = np.loadtxt(f'{base_path}/Pearson_correlation.txt').mean()
        mean_RMSE = np.loadtxt(f'{base_path}/RMSE.txt').mean()
        weights = np.loadtxt(f'{base_path}/pairwise_kernel_weights.txt').mean(axis=0)
        
        with open(f'{base_path}/pairwise_kernel_names.txt', 'r') as f:
            kernel_names = f.read().split('\t')
            
        data['tipo'].append(technique)
        data['percentual'].append(int(percentage))
        data['F1'].append(mean_f1)
        data['Pearson_Correlation'].append(mean_pearsonCorrelation)
        data['RMSE'].append(mean_RMSE)
        data['pesos'].append(weights)
        data['kernel_names'].append(kernel_names)
df = pd.DataFrame(data=data)


def plot_heatmap(dataframe, percentage=10, technique='isvd'):
    pesos = dataframe[(dataframe['percentual'] == percentage) \
                    & (dataframe['tipo'] == technique)]['pesos'].values[0]
    kernel_names = dataframe[(dataframe['percentual'] == percentage) \
                           & (dataframe['tipo'] == technique)]['kernel_names'].values[0]
    
    kds = [kn.split('.txt')[0] for kn in kernel_names[:-1]]
    kcs = [kn.split('.txt')[1] for kn in kernel_names[:-1]]
    pesos = dataframe[(dataframe['percentual'] == 10) \
                    & (dataframe['tipo'] == 'isvd')]['pesos'].values[0]

    df2 = pd.DataFrame(data={
        'kd': kds,
        'kc': [kc.replace('_KRONECKER_', '') for kc in kcs],
        'peso': pesos
    })

    matrix = df2.groupby(['kd','kc'])['peso'].mean().unstack()

    return sns.heatmap(matrix, cmap="YlGnBu", cbar=True, annot=False)


def handle_technique_title(technique):
    if technique == 'isvd':
        return 'iSVD'
    if technique == 'knn':
        return 'KNN'
    return technique.capitalize()


for percentage in percentages[:-1]:
    heatmap = plot_heatmap(
        df, 
        percentage=int(percentage),
        technique='isvd'
    )

    heatmap.set_ylabel('')    
    heatmap.set_xlabel('')

    heatmap.set_title(f'Technique: iSVD; Percentage: {percentage}%')

    fig = heatmap.get_figure()
    fig.tight_layout()
    fig.savefig(f'heatmaps/isvd_{percentage}_heatmap.png', format='png')
    
    plt.clf()