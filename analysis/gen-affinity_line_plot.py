import numpy as np
import seaborn as sns


original_labels = np.loadtxt('../complete_drug_response_data/Labels.txt')


sns.set_style('whitegrid')
distplot = sns.distplot(
    original_labels.flatten(), hist=True, kde=True, 
    bins=int(180/5), color = 'darkblue', 
    hist_kws={'edgecolor':'black'},
    kde_kws={'linewidth': 4}
)
distplot.set(xlabel='Affinity', ylabel='Density')
fig = distplot.get_figure()
fig.subplots_adjust(left = 0.3)
fig.savefig('line_plots/affinity_density_histogram.png') 