import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
sns.set_style('whitegrid')


with open('house_prices.txt') as f:
    values = [l.strip().replace(',', '') for l in f]

with open('months.txt') as f:
    months = [l.strip() for l in f]

# Build dictionary of all years and months.
year_dict = {}
years = list(range(2006,2024))
for year in years:
    year_dict[str(year)] = {}

    for index, month in enumerate(months):

        print(str(year))
        print(month)
        print(str(year) in month)

        if str(year) in month:
            year_dict[str(year)][month.split(' ')[0].lower()] = int(values[index])


averages = []
sd = []
for month in list(year_dict['2006'].keys()):
    averages.append(int(np.average([l[month] for l in year_dict.values() if month in l.keys()])))
    sd.append(int(np.std([l[month] for l in year_dict.values() if month in l.keys()])))

line_above = [x+y for x,y in zip(averages, sd)]
line_below = [x-y for x,y in zip(averages, sd)]

# Plot the graph
for year in year_dict:
    if year != '2023':
        if '200' in year:
            ax = sns.lineplot(data=list(year_dict[year].values()), color='darkgreen', linestyle = '--', linewidth=0.4)
            ax.set_xticks(list(range(0,12)), labels = list(year_dict[year].keys()), rotation = 70)


        if '201' in year:
            ax = sns.lineplot(data=list(year_dict[year].values()), color='darkgreen', linestyle = '--', linewidth=0.4)


        if '202' in year:
            ax = sns.lineplot(data=list(year_dict[year].values()), color='darkgreen', linestyle = '--', linewidth=0.4)

    else:
        sns.lineplot(data=list(year_dict[year].values()), color='darkred', label=year)
        ax.text(x= 10 + 0.1, y=list(year_dict[year].values())[10], s=year, va="center", c ='darkred')

ax = sns.lineplot(data = averages, color = 'darkblue', label = 'average', linestyle='--')
ax.text(x=11 + 0.1, y=averages[-1], s='average', va="center", c ='darkblue')

ax.fill_between(list(range(0,12)), line_below, line_above, alpha=0.2)
ax.text(x=11 + 0.1, y=line_above[-1], s='+ 1 std', va="center", c ='darkblue')
ax.text(x=11 + 0.1, y=line_below[-1], s='- 1 std', va="center", c ='darkblue')
    # print(list(year_dict[year].values()))
    # print(list(year_dict[year].keys()))

plt.title('House sales in Wales by year [since Jan 2006]', loc='left')
plt.ylabel('count: #')
plt.xlabel('month of the year')
plt.tight_layout()
plt.legend()

plt.show()