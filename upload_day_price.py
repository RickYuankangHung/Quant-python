import pandas as pd
import time
import os
import sys

from security import Security
from upload_data import Upload_Data
from my_logger import MyLogger


def read_tickers_list(dir='', file='', extension=''):
    file_ = dir + file + extension
    df = pd.read_csv(file_, skiprows=[0], header=None,
                     names=['ticker'],
                     usecols=['ticker'])
    return df


def read_csv_by_dataframe(dir='', file='', extension='', delimiter=','):
    file_ = dir + file + extension
    df = pd.read_csv(file_, sep=delimiter) #title automatically becomes column name (need col name when upload to db)
    return df

def iterate_path(filepath):
    fList = []

    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        if os.path.isdir(child):
            pass
            #print("folder: " + str(child))
        else:   # os.path.isfile(child)
            #print('file: ' + str(child))
            arr = str(child).split('\\')
            t = arr[-1].split('.')
            fList.append(t[0])

    return fList

def Main():
    # prep 1: path and file
    sql = 'REPLACE INTO security_day_price VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);'

    localList = False  # False: get ticker list from folder existing files; True: get ticker list from local list file
    inPath = 'C:\\GTechFin\\2 pro\\GMBP_mysql_tutorial\\02.tickers_data\\'
    tickerPath = 'D:\\dataset\\tickerSet\\'
    tickerFile = 'bps_ticker_0429.txt'

    # # prep 2: logger
    # mylog = MyLogger('D:\\dataset\\download\\security_day_price\\upload_day_price.log')
    # mylog.log_info('Start:---------------------------')

    # step 1: database connection
    db = Security(user='root', password='Haha1234', host='127.0.0.1', port=3306, db='gmbp')

    ##########################################################################################
    #DO NOT EDIT FOLLOWING CODING
    ##########################################################################################

    # step 2: get ticker list
    if localList == True:
        tickers = read_tickers_list(dir=tickerPath, file=tickerFile)['ticker'].tolist()
    else:
        tickers = iterate_path(inPath)

    # step 3: upload
    start = time.time()
    for idx,ticker in enumerate(tickers):
        try:
            data = read_csv_by_dataframe(dir=inPath, file=ticker, extension='.csv')
            my_ud = Upload_Data(db.conn,100000,sql,data)
            my_ud.upload_with_counter()
            print(str(idx) + ',' + ticker + ',done')
            del data
            del my_ud
        except:
            warnInfo = str(idx) + ',' + ticker + ',failed'
            print(warnInfo)
            # mylog.log_warning(warnInfo)

    end = time.time()
    print('runtime:', end - start, 'seconds')

    # memory release and disconnection
    db.disconnect()
    del db
    del tickers
    print('whole done')
    # mylog.log_info('whole done, runtime: ' + str(end-start) + ' seconds.\n')

if __name__ == '__main__':
    Main()