import seaborn as sns, pandas as pd, matplotlib.pyplot as plt

from get_results_dataframe import get_results_dataframe


def get_heatmap_plot(
    dataframe = get_results_dataframe(), 
    percentual = 10, 
    tipo = 'zero'
):
    pesos = dataframe[
        (dataframe['percentual'] == percentual)
        & (dataframe['tipo'] == tipo)
    ]['pesos'].values[0]
    
    kernel_names = dataframe[
        (dataframe['percentual'] == percentual) 
        & (dataframe['tipo'] == tipo)
    ]['kernel_names'].values[0]
    
    # assumindo que kernel_names nao muda em cada execucao
    kds = [kn.split('.txt')[0] for kn in kernel_names[:-1]]
    kcs = [kn.split('.txt')[1] for kn in kernel_names[:-1]]
    pesos = dataframe[
        (dataframe['percentual'] == 50)                     
        & (dataframe['tipo'] == 'zero')
    ]['pesos'].values[0]


    df2 = pd.DataFrame(
        data={
            'kd': kds,
            'kc': kcs,
            'peso': pesos
        } 
    )

    matrix = df2.groupby(['kd','kc'])['peso'].mean().unstack()

    return sns.heatmap(matrix)
    

# 10 
isvd_heatmap_plot = get_heatmap_plot(tipo='isvd')
isvd_heatmap_plot_fig = isvd_heatmap_plot.get_figure()

isvd_heatmap_plot_fig.savefig('heatmaps/isvd_10.png')
plt.clf()

# 30 
isvd_heatmap_plot = get_heatmap_plot(percentual=30, tipo='isvd')
isvd_heatmap_plot_fig = isvd_heatmap_plot.get_figure()

isvd_heatmap_plot_fig.savefig('heatmaps/isvd_30.png')
plt.clf()

# 50 
isvd_heatmap_plot = get_heatmap_plot(percentual=50, tipo='isvd')
isvd_heatmap_plot_fig = isvd_heatmap_plot.get_figure()

isvd_heatmap_plot_fig.savefig('heatmaps/isvd_50.png')
plt.clf()

# 70 
isvd_heatmap_plot = get_heatmap_plot(percentual=70, tipo='isvd')
isvd_heatmap_plot_fig = isvd_heatmap_plot.get_figure()

isvd_heatmap_plot_fig.savefig('heatmaps/isvd_70.png')
plt.clf()
