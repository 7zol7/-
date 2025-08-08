
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
print(plt.show())
years=pd.Series([14,15,16,17,18])
cash=pd.Series([25000,35000,70000,160000,230000])
print(sb.barplot(x=years,y=cash))
