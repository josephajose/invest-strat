import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def plot_growth(): 
    pd.options.display.float_format = '{:,.0f}'.format

    # S&P Composite
    # daily = pd.read_csv('data/SPX-daily-1927-2024.csv', index_col='Date', parse_dates=True)
    # print(spxDaily.loc['1994-01-02'])
    # print(spxDaily.loc['1928-01-04']['Close'])
    # plot = dataFrame.plot(kind='line', x='Date', y='Close')
    # plt.show()

    # Vanguard 500
    # daily = pd.read_csv('data/VFIAX-daily-2000-2024.csv', index_col='Date', parse_dates=True)

    # APPLE
    # daily = pd.read_csv('data/AAPL-daily-1980-2024.csv', index_col='Date', parse_dates=True)

    # Tesla
    # daily = pd.read_csv('data/TSLA-daily.csv', index_col='Date', parse_dates=True)

    # Microsoft
    # daily = pd.read_csv('data/MSFT-daily.csv', index_col='Date', parse_dates=True)

    # Amazon
    daily = pd.read_csv('data/AMZN-daily-1997.csv', index_col='Date', parse_dates=True)

    # last 30 years
    months = 12*10
    firstMonthlyDayLast30years = daily.groupby(pd.Grouper(freq='ME')).nth(0).tail(months)
    firstMonthlyDayLast30years['Contribution'] = 1000
    contributions = firstMonthlyDayLast30years[['Contribution']]

    # Monthly contributions starting January 1994
    # start = pd.Timestamp(year=1994, month=1, day=1)  
    # months = 12*30+1
    # dates = [d.strftime('%Y-%m-%d') for d in pd.date_range(start, periods=months, freq="MS")]
    # dates = pd.date_range(start, periods=months, freq="MS")
    # print(dates)
    # print(dates[-1])
    # print(len(dates))
    # contributions = pd.DataFrame({'Date': dates,
    #                               'Contribution': [1000 for i in range(len(dates))]})
    # contributions = contributions.set_index(['Date'])
    # print(contributions)
    #print(contributions.loc['1995-01-01']['Contribution'])

    # Merge and fill NaN with 0
    merged = pd.merge(daily, contributions, how='left', on='Date').fillna(0)

    # Add cumulative sum for contributions
    merged['ContributionSum'] = merged['Contribution'].cumsum()

    # Add column for shares owned
    merged['PurchasedShares'] = merged['Contribution'] / merged['Close']
    merged['SharesSum'] = merged['PurchasedShares'].cumsum()
    merged['TotalValue'] = merged['SharesSum']*merged['Close']
    merged['TotalValue'].astype(int)

    # print(merged.tail())
    print(merged.query('Contribution > 0'))

    # plot line charts
    merged.plot(kind='line', use_index=True, y=['Close', 'TotalValue'])

    # show plots
    plt.show()