import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#wykres linniowy
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2015', periods=1000))
ts = ts.cumsum()
print(ts)
ts.plot()
plt.show()

#wykres z ramki danych
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
        'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
        'Populacja': [11190846, 1303171035, 287847528, 38675446]}

df = pd.DataFrame(data)
print(df)
grupa = df.groupby(['Kontynent']).agg({'Populacja': ['sum']})
print(grupa)
wykres = grupa.plot.bar()
wykres.set_xlabel('Kontynent')
wykres.set_ylabel('Mld')
wykres.legend()
plt.xticks(rotation=0)
plt.savefig('wykres_populacja.png')
plt.title('Populacja z podziałem na kontynenty')
plt.show()