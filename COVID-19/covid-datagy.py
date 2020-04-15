import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker

# Section 2
SOURCE = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
df = pd.read_csv(SOURCE, parse_dates=['Date'])
countries = ['Canada', 'Germany', 'United Kingdom', 'US', 'France', 'China']
df = df[df['Country'].isin(countries)]  # select only the countries from our list

"""Section 3 - Creating and Summary Column
create a summary column that aggregates the total
number of cases across our confirmed cases, recovered cases, and deaths
"""
df['Cases'] = df[['Confirmed', 'Recovered', 'Deaths']].sum(axis=1)

"""Section 4 - Restructuring our Data
In Section 4, we pivot our dataframe df, creating columns out of countries, with the number of cases as the data fields.
This new dataframe is called covid. We then set the index of the dataframe to be the date 
and assign the country names to column headers."""

df = df.pivot(index='Date', columns='Country', values='Cases')
countries = list(df.columns)
covid = df.reset_index('Date')
covid.set_index(['Date'], inplace=True)
covid.columns = countries

"""Section 5 - Calculating Rates per 100 000
In Section 5, we copy our dataframe covid and call it percapita. 
We use a dictionary that is storing all our countries’ populations and divide each value by the population 
and multiply it by 100,000 to generate a number of cases per 100,000 people."""

populations = {
    'Canada': 37664517,
    'Germany': 83721496,
    'United Kingdom': 67802690,
    'US': 330548815,
    'France': 65239883,
    'China': 1438027228,
}

percapita = covid.copy()
for country in list(percapita.columns):
    percapita[country] = percapita[country] / populations[country] * 100000


"""Section 6 - Generating Colours and Style
In Section 6, we created a dictionary that contains hex values for different countries. 
Storing this in a dictionary will allow us to easily call it later in a for-loop. 
We also assign the FiveThirtyEight style to add some general formatting, which we’ll heavily build upon."""
colors = {
    'Canada': '#045275',
    'Germany': '#089099',
    'United Kingdom': '#7C1D6F',
    'US': '#DC3977',
    'France': '#7CCBA2',
    'China': '#089099',
}
plt.style.use('fivethirtyeight')

"""Section 7 - Creating and Visualization
In Section 7, we create our first visualization using Pandas’ plot function. 
We use the colors parameter to assign the colors to different columns. 
We also use the set_major_formatter method to format values with separators for thousands."""

plot = covid.plot(figsize=(12, 8), color=list(colors.values()), linewidth=5, legend=False)
plot.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
plot.grid(color='#d4d4d4')
plot.set_xlabel('Date')
plot.set_ylabel('# of Cases')


"""Section 8 - Assigning Colour
Then, in Section 8, we create a for-loop that generates label text for the various countries. This for-loop gets 
each country’s name from the keys in the dictionary in the form of a list and iterates over this list. It places text 
containing the country’s name to the right of the last x-value (covid.index[-1] → the last date in the dataframe), 
at the current day’s y-value (which will always be equal to the max value of that column). """

for country in list(colors.keys()):
    plot.text(x=covid.index[-1], y=covid[country].max(), c=colors[country], s=country, weight='bold')


"""Section 9 - Adding Labels Finally, in Section 9, we add a title, subtitle, and source information about the chart. 
We use variables again to position the data so as the graph updates these positions are updated dynamically! """

plot.text(x=covid.index[1], y=int(covid.max().max()) + 45000, s='COVID-19 Cases by Country',
          fontsize=23, weight='bold', alpha=.75)
plot.text(x=covid.index[1], y=int(covid.max().max()) + 15000,
          s='For the USA, China, Germany, France, United Kingdom and'
            'Canada\nIncludes Current Cases, Recoveries, and Deaths',
          fontsize=16, alpha=.75)
plot.text(x=percapita.index[1], fontsize=10, y=-100000,
          s='datagy.io Source: https://github.com/datasets/covid-19/blob/master/data/countries-aggregated.csv', )


percapitaplot = percapita.plot(figsize=(12, 8), color=list(colors.values()), linewidth=5, legend=False)
percapitaplot.grid(color='#d4d4d4')
percapitaplot.set_xlabel('Date')
percapitaplot.set_ylabel('# of Cases per 100,000 People')
for country in list(colors.keys()):
    percapitaplot.text(x=percapita.index[-1], y=percapita[country].max(), c=colors[country], s=country, weight='bold')
percapitaplot.text(x=percapita.index[1], y=percapita.max().max() + 25, s="Per Capita COVID-19 Cases by Country",
                   fontsize=23, weight='bold', alpha=.75)
percapitaplot.text(x=percapita.index[1], y=percapita.max().max() + 10,
                   s="For the USA, China, Germany, France, United Kingdom, and Canada\nIncludes Current Cases, Recoveries, and Deaths",
                   fontsize=16, alpha=.75)
percapitaplot.text(x=percapita.index[1], y=-55,
                   s='datagy.io Source: https://github.com/datasets/covid-19/blob/master/data/countries-aggregated.csv',
                   fontsize=10)
plt.show()
