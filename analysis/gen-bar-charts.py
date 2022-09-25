import seaborn as sns
import matplotlib.pyplot as plt

from get_results_dataframe import get_results_dataframe


df = get_results_dataframe()


# F1
f1_barplot = sns.barplot(x='tipo', y='F1', data=df, hue='percentual')

f1_barplot.set(ylim=(0, 1))
f1_barplot.set_ylabel('F1-score')
f1_barplot.set_xlabel('Technique')
f1_barplot.set_title('Techniques performance evaluation in comparison with F1 score')
f1_barplot.legend(loc='lower right')

for container in f1_barplot.containers:
    f1_barplot.bar_label(container, size=8, rotation='vertical', padding=2)

f1_barplot_fig = f1_barplot.get_figure()

f1_barplot_fig.savefig(f'bar_plots/mean_f1_score.png')
plt.clf()


# Pearson
pearson_barplot = sns.barplot(x='tipo', y='Pearson_Correlation', data=df, hue='percentual')

pearson_barplot.set(ylim=(0, 1.1))
pearson_barplot.set_ylabel('Pearson Correlation')
pearson_barplot.set_xlabel('Technique')
pearson_barplot.set_title('Techniques performance evaluation in comparison with Pearson Correlation')
pearson_barplot.legend(loc='lower right')

for container in pearson_barplot.containers:
    pearson_barplot.bar_label(container, size=8, rotation='vertical', padding=2)

pearson_barplot_fig = pearson_barplot.get_figure()

pearson_barplot_fig.savefig(f'bar_plots/mean_pearson.png')
plt.clf()


# RMSE
rmse_barplot = sns.barplot(x='tipo', y='RMSE', data=df, hue='percentual')

rmse_barplot.set(ylim=(0, 5.5))
rmse_barplot.set_ylabel('RMSE')
rmse_barplot.set_xlabel('Technique')
rmse_barplot.set_title('Techniques performance evaluation in comparison with RMSE')
rmse_barplot.legend(loc='lower right')

for container in rmse_barplot.containers:
    rmse_barplot.bar_label(container, size=8, rotation='vertical', padding=2)

rmse_barplot_fig = rmse_barplot.get_figure()

rmse_barplot_fig.savefig(f'bar_plots/rmse.png')
plt.clf()