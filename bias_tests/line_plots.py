import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('test_stats.csv')

print(data.head())
sns.set_context('paper')
sns.lineplot(x='Time Period', y='Normalized Test Statistic', hue='Region', data = data)

plt.savefig('normalized_test_stats.png')