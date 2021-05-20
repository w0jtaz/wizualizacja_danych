import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#wykres linniowy
s = pd.Series(np.random.randn(1000), index=pd.date_range('01/01/2015', periods=1000))
s = s.cumsum()
g = sns.relplot(kind='line', data=s)
g.fig.set_size_inches(6,6)
g.fig.autofmt_xdate()
g.set_xlabels('daty')
g.set_ylabels('wartości')
plt.show()

#wykres liniowy z ramki danych
dane = {'wartosci': np.random.randn(1000),
        'daty': pd.date_range('01/01/2015', periods=1000)}
df = pd.DataFrame(dane)
df.wartosci = df.wartosci.cumsum()
g = sns.relplot(kind='line', x='daty', y='wartosci', data=df)
g.fig.set_size_inches(6,6)
g.fig.autofmt_xdate()
plt.show()

#wykres punktowy
data = {'a': np.arange(50),
        'c': np.random.randint(0,50,50),
        'd': np.random.rand(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100
df = pd.DataFrame(data)
wykres = sns.relplot(kind='scatter', data=df, x='a', y='b', hue='c', size='d', palette='bright', legend=False)
wykres.fig.set_size_inches(6, 6)
plt.show()

#wykres słupkowy
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
        'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
        'Populacja': [11190846, 1303171035, 207847528, 38674567]}
df = pd.DataFrame(data)
wykres = sns.catplot(data=df, x='Kontynent', y='Populacja', hue='Kontynent', kind='bar', dodge=False, ci=None)
wykres.fig.set_size_inches(7, 6)
wykres.set(title='Wykres słupkowy', ylim=(0, 1400000000))
plt.legend(loc='upper right', title='Populacja na kontynencie')
plt.show()

#histogram
a = np.random.randn(10000)
histogram = sns.histplot(data=a, bins=50, color='g', alpha=0.75, stat='probability', kde=True, line_kws={'linewidth': 4})
histogram.set(title='Histogram', xlabel='x', ylabel='Prawdopodobieństwo')
plt.show()