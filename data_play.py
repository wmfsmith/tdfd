# coding: utf-8
dir()
import matplotlib as mpl
mpl.pyplot.plot(range(5), range(5,10)
)
import pandas as pd
import seaborn as sns
td = pd.read_csv('train_new.csv')
get_ipython().set_next_input('td_s = td.take');get_ipython().run_line_magic('pinfo', 'td.take')
get_ipython().set_next_input('td_s = td.take');get_ipython().run_line_magic('pinfo', 'td.take')
td_s = td.take(range(10000))
sns.pairplot(td_s)
get_ipython().run_line_magic('pinfo', 'sns.pairplot')
sns.pairplot(td_s, size=.75)
sns.pairplot(td_s, size=1)
sns.pairplot(td_s, size=1.3)
sns.pairplot(td_s, size=1.2)
get_ipython().run_line_magic('pinfo', 'sns.pairplot')
sns.pairplot(td_s, size=1.2, plot_kws=dict(s=3))
sns.pairplot(td_s, size=1.1, plot_kws=dict(s=5))
td_s.columns
sns.pairplot(td_s, size=1.1, plot_kws=dict(s=5), vars=['ip', 'app', 'device', 'os', 'channel', 'click_attributed_delta'])
td_s = td.take(range(1000000))
sns.pairplot(td_s, size=1.1, plot_kws=dict(s=5), vars=['ip', 'app', 'device', 'os', 'channel', 'click_attributed_delta'])
td_s.iloc(0)
td_s.iloc(0)[]
td_s.iloc[0]
sns.pairplot(td_s, size=1.1, plot_kws=dict(s=5), vars=['ip', 'app', 'device', 'os', 'channel', 'click_attributed_delta'])
