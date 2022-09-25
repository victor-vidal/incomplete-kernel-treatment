import seaborn as sns
import matplotlib.pyplot as plt

from get_results_dataframe import get_results_dataframe


df = get_results_dataframe()


# F1
f1_lineplot = sns.lineplot(x='tipo', y='F1', data=df, hue='percentual', style="percentual", palette='bright')

f1_lineplot.set_ylabel('F1-score')
f1_lineplot.set_xlabel('Technique')
f1_lineplot.set_title('Techniques performance evaluation in comparison with F1 score')
f1_lineplot.legend(loc='lower right')

f1_lineplot_fig = f1_lineplot.get_figure()

f1_lineplot_fig.savefig(f'line_plots/mean_f1_score.png')
plt.clf()


# Pearson
pearson_lineplot = sns.lineplot(x='tipo', y='Pearson_Correlation', data=df, hue='percentual', style="percentual", palette='bright')

pearson_lineplot.set_ylabel('Pearson Correlation')
pearson_lineplot.set_xlabel('Technique')
pearson_lineplot.set_title('Techniques performance evaluation in comparison with Pearson Correlation')
pearson_lineplot.legend(loc='lower right')

pearson_lineplot_fig = pearson_lineplot.get_figure()

pearson_lineplot_fig.savefig(f'line_plots/mean_pearson.png')
plt.clf()


# RMSE
rmse_barplot = sns.lineplot(x='tipo', y='RMSE', data=df, hue='percentual', style="percentual", palette='bright')

rmse_barplot.set_ylabel('RMSE')
rmse_barplot.set_xlabel('Technique')
rmse_barplot.set_title('Techniques performance evaluation in comparison with RMSE')
rmse_barplot.legend(loc='lower right')

rmse_barplot_fig = rmse_barplot.get_figure()

rmse_barplot_fig.savefig(f'line_plots/mean_rmse.png')
plt.clf()
