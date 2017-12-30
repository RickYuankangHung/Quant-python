from security import Security
import pandas as pd
import datetime
import pymysql
import time
import sys



d=dict()
def data_export(dataframe, dir='', file='', extension='' ,delimiter=','):
    file_ = dir + file + extension

    #default column sequence
    dataframe.to_csv(file_, sep=delimiter, index=True, encoding='utf-8')

def output_single_record(path,file,data):

    outFile = path + file
    df = pd.DataFrame(data)
    df.transpose().to_csv(outFile, sep=',',index=False, header=False, mode='a')
    del df
def get_data(db, ticker_id_dict, tickerLong, tickerShort):
    # Step 1: geting and slicing data
    df1 = db.get_security_day_price_with_id(ticker_id_dict[tickerLong])[['time_x', 'ADJ_CLOSE']]
    df1.index = df1['time_x']

    df2 = db.get_security_day_price_with_id(ticker_id_dict[tickerShort])[['time_x', 'ADJ_CLOSE']]
    df2.index = df2['time_x']
    # Step 2: concatenation
    df_price = pd.DataFrame()
    s1 = pd.Series(df1['ADJ_CLOSE'], index=df1.index, name=tickerLong)
    s2 = pd.Series(df2['ADJ_CLOSE'], index=df2.index, name=tickerShort)
    df_price = pd.concat([df_price, s1], axis=1)
    df_price = pd.concat([df_price, s2], axis=1)

    df_price = df_price.dropna(axis=0, how='any')
    print(df_price)
    #print(df_price)
    return df_price





################## Get the idx of different month#################

def get_gap(data):
    gap = []
    for idx,t in enumerate(data.index):
        if idx == 0:
            gap.append(idx)
            prevT = str(t)[5:7]
        else:
            curT = str(t)[5:7]
            if curT != prevT:
                prevT = curT
                gap.append(idx)

    #for item in gap:
    #    print(item)
    return gap



def get_gap_same_month(data,strMonth):
    gap = []
    flag = True
    for idx,t in enumerate(data.index):
        curT = str(t)[5:7]
        if flag == True:
            if curT == strMonth:
                flag = False
                gap.append(idx)
        else:
            if curT != strMonth:
                flag = True

    return gap

def get_gap_every_month(data):
    gap = []
    flag = True
    prevT = None
    for idx,t in enumerate(data.index):
        curT = str(t)[5:7]
        if prevT is None:
            prevT = curT
            gap.append(idx)
            continue
        else:
            if curT == prevT:
                continue
            else:
                prevT = curT
                gap.append(idx)

    return gap


def get_gap_day_of_month(data,strDay):
    gap = []
    startFind = False
    for idx,t in enumerate(data.index):
        if idx == 0:
            prevM = str(t)[5:7] #
            startFind = True
        else:
            curM = str(t)[5:7]
            curD = str(t)[8:10]
            if curM != prevM:   #month changed
                startFind = True
                prevM = curM
                if curD >= strDay:
                    startFind = False
                    gap.append(idx)
            else:   #in the same month
                if startFind == True:
                    if curD >= strDay:
                        startFind = False
                        gap.append(idx)

    #for item in gap:
    #    print(data.index[item])
    return gap

def get_gap_nth_day_of_month(data,NthDay):
    gap = []
    startFind = False
    for idx,t in enumerate(data.index):
        if idx == 0:
            prevM = str(t)[5:7] #
            startFind = True
            n = NthDay
            n -= 1
            if n == 0:
                gap.append(idx)
                #startFind = False
        else:
            n -= 1
            curM = str(t)[5:7]
            if curM != prevM:   #month changed
                #vstartFind = True
                prevM = curM
                n = NthDay
                n -= 1
                if n == 0:
                    startFind = False
                    gap.append(idx)
            else:   #in the same month
                if n == 0:
                    # startFind = False
                    gap.append(idx)

    #for item in gap:
    #    print(data.index[item])
    return gap





def get_gap_day_of_week(data,weekday='MONDAY'):
    weekday = weekday.upper()
    if weekday == 'MONDAY':
        w = 0
    elif weekday == 'TUESDAY':
        w = 1
    elif weekday == 'WEDNESDAY':
        w = 2
    elif weekday == 'THURSDAY':
        w = 3
    elif weekday == 'FRIDAY':
        w = 4
    else:   #default is MONDAY
        w = 0

    gap = []

    startFind = False
    for idx,t in enumerate(data.index):
        curY = str(t)[0:4]
        curM = str(t)[5:7]
        curD = str(t)[8:10]
        d1 = datetime.datetime(int(curY), int(curM), int(curD))
        if d1.weekday() == w:
            gap.append(idx)

    # for item in gap:
   #     print(data.index[item])
    return gap


################ Get the idx of each different month########

######################### Get data into data frame#############
    # Step 1: get data
    tickerLong, tickerShort = tLong, tShort

    df_price = get_data(db, ticker_id_dict, tickerLong, tickerShort)
    # print(df_price)
    # data_export(df_price, dir=outPath, file='price.csv', delimiter=',')

#######################Get data into data frame ###########


def get_data(db, ticker_id_dict, tickerLong, tickerShort):
    # Step 1: geting and slicing data
    df1 = db.get_security_day_price_with_id(ticker_id_dict[tickerLong])[['time_x', 'ADJ_CLOSE']]
    df1.index = df1['time_x']

    df2 = db.get_security_day_price_with_id(ticker_id_dict[tickerShort])[['time_x', 'ADJ_CLOSE']]
    df2.index = df2['time_x']
    # Step 2: concatenation
    df_price = pd.DataFrame()
    s1 = pd.Series(df1['ADJ_CLOSE'], index=df1.index, name=tickerLong)
    s2 = pd.Series(df2['ADJ_CLOSE'], index=df2.index, name=tickerShort)
    df_price = pd.concat([df_price, s1], axis=1)
    df_price = pd.concat([df_price, s2], axis=1)

    df_price = df_price.dropna(axis=0, how='any')
    print(df_price)
    return df_price






def action(outPath, tLong,tShort,testMonth,db,ticker_id_dict):
    # config
    #outPath = 'D:\\dataset\\long_short\\single_month\\'
    outFile = 'Long_' + tLong+'.csv'

    mode = 2    #from mode 1 to mode 5, edit parameters in following if else block

    selectMonth,selectDayOfMonth, selectWeekDay, selectNthDay, moveBuy, moveSell = None, None, None, 0, 0, 0
    if mode == 1:   #get_gap_same_month
        selectMonth = testMonth  # from '01' to '12'
        moveBuy, moveSell = 10,10
    elif mode == 2: #get_gap_every_month
        #no parameter
        moveBuy, moveSell = 1, 1
    elif mode == 3: #get_gap_day_of_month
        selectDayOfMonth = '01'
        moveBuy, moveSell = 10, 10
    elif mode == 4: #get_gap_day_of_week
        selectWeekDay = 'MONDAY'    # from 'MONDAY' to 'FRIDAY'
        moveBuy, moveSell = 1, 1
    elif mode == 5: #get_gap_nth_day_of_month
        selectNthDay = 1    #from 1 to 30
        moveBuy, moveSell = 10, 10
    else:
        return

    # NOT EDIT FOLLOWING CODING #########################################################################
    if selectMonth is None:
        selectMonth = '01'
    if selectDayOfMonth is None:
        selectDayOfMonth = '01'
    if selectWeekDay is None:
        selectWeekDay = 'MONDAY'
    if selectNthDay == 0:
        selectNthDay = 1
    if moveBuy == 0:
        moveBuy = 10
    if moveSell == 0:
        moveSell = 10


    # Step 1: get data
    tickerLong, tickerShort = tLong, tShort

    df_price = get_data(db, ticker_id_dict, tickerLong, tickerShort)
    # print(df_price)
    # data_export(df_price, dir=outPath, file='price.csv', delimiter=',')


    # Step 2: select mode
    # gap = get_gap(df_price)
    if mode == 1:
        gap = get_gap_same_month(df_price, selectMonth)                #for special month, around the beginning of each month
    elif mode == 2:
        gap = get_gap_every_month(df_price)                             #for all months, around the beginning of all month
    elif mode == 3:
        gap = get_gap_day_of_month(df_price,selectDayOfMonth)           #for special day
    elif mode == 4:
        gap = get_gap_day_of_week(df_price,weekday=selectWeekDay)       #for special weekday
    elif mode == 5:
        gap = get_gap_nth_day_of_month(df_price,selectNthDay)           #for relative day of first day of month
    #print(gap)

    if not df_price.empty and len(gap)==212:
        # Step 3: data validation
        if gap[1] > 10: #make sure the first month has at least 10 days in previous month
            gap = gap[1:-1]
        else:
            gap = gap[2:-1]


        # Step 4: do analysis with special moving time window
        output_single_record(outPath, outFile,
                             ['Start_PrevMonthLastNthDay', 'End_CurMonthFirstNthDay', 'LongWeight', 'ShortWeight',
                              'returnOfEachTime','successRate'])
        # rate = [0.05 + 0.05*x for x in range(19)]       # span is 0.05
        # rate = [0.01 + 0.01 * x for x in range(99)]     # span is 0.01
        return_value=dict()
        rate = [1]
        print(gap)

        for r in rate:
            value = 0
            # successCnt = 0
            for idx in gap:
            #     buyLong = df_price[tickerLong].iloc[idx-1-buyD]
            #     sellLong = df_price[tickerLong].iloc[idx+sellD]
            #     buyShort = df_price[tickerShort].iloc[idx-1-buyD]
            #     sellShort = df_price[tickerShort].iloc[idx+sellD]
            #     val = (sellLong-buyLong)/buyLong*r + (sellShort-buyShort)/buyShort*(-1.0) *(1.0-r)   #short is negative
                if not df_price.empty:
                    if str(df_price.index[idx])[5:7] not in return_value.keys():
                        return_value[str(df_price.index[idx])[5:7]]=[]
                        return_value[str(df_price.index[idx])[5:7]].append(df_price[tickerLong].iloc[idx]/df_price[tickerLong].iloc[idx-1]-1)
                        return_value[str(df_price.index[idx])[5:7]]=sum(return_value[str(df_price.index[idx])[5:7]])/len(return_value[str(df_price.index[idx])[5:7]])
            print(return_value)
                # value /= len(gap)
                # #print(str(buyD+1) + ',' + str(sellD+1) + ',' + str(r) + ',' + str(1.0-r) + ',' + str(value))
                # record = [str(buyD+1),str(sellD+1),str(r),str(1.0-r),str(value),str(successCnt/len(gap))]
            d[tickerLong]=[]
            d[tickerLong]=return_value

            # output_single_record(outPath,outFile,record)

def Main():
    outPath = 'C:\\project5\\'

    conn=pymysql.connect(user='readonly',passwd='123456',host='160.79.239.235',port=3306,db='gmbp')
    cur=conn.cursor()
    cur.execute("Select STOCK_TICKER from index_component")
    tick=list()
    for row in cur:
        # print(row[0])
        tick.append(row)



    db = Security(user='readonly', password='123456', host='160.79.239.235', port=3306, db='gmbp')
    ticker_id_dict = db.get_security_lookup_ticker_id()
    tickerList=list()
    for name in ticker_id_dict.keys():
        tickerList.append(name)
    print(tickerList)
    monthList = ['01']


    start = time.time()
    for idx1 in range(len(tickerList)):
        for m in monthList:
            action(outPath, tickerList[idx1], 'IWM', m, db, ticker_id_dict)
            print(d)
            #     print(str(idx1) + ',' + str(idx2) + ',' + tickerList[idx1] + ',' + tickerList[idx2] + ',M' + m)
    end = time.time()
    db.disconnect()
    print('runtime: ' + str(end-start) + ' secs')





if __name__ == '__main__':
    Main()
