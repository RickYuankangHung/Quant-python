import pandas as pd
import time
import sys

from security import Security


def Main():
    # step 1: db connection
    db = Security(user='root', password='Haha1234', host='127.0.0.1', port=3306, db='gmbp')

    # step 2: lookup dictionary and ticker list
    tickers = {'AAPL':16}

    # step 3: statistic
    for key in tickers:
        id = tickers[key]
        ticker = key
        df = db.get_security_day_price_with_id(id)

        # basic math operation
        mean = df['ADJ_CLOSE'].mean()       #average
        var = df['ADJ_CLOSE'].values.var()  # variance
        std = df['ADJ_CLOSE'].values.std()    # standard deviation

        print(ticker,mean,var,std)

        del df

    print('whole done...')

if __name__ == '__main__':
    Main()
