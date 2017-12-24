import pandas as pd
import time
import sys
import pymysql
from security import Security
import csv

def Main():
    # step 1: db connection
    db = Security(user='readonly', password='123456', host='160.79.239.235', port=3306, db='gmbp',country=100)
    conn=pymysql.connect(user='readonly',passwd='123456',host='160.79.239.235',port=3306,db='gmbp')
    cur=conn.cursor()

    tickers=list()
    import csv
    with open('tic.csv', 'r') as csvfile:
        t = csv.reader(csvfile)
        for row in t:
            tickers.append(row)
    iterat=str()
    for k in range(len(tickers)):
        if k!=0:
            iterat=iterat+','+tickers[k][0]
        else:
            iterat = iterat + tickers[k][0]
    iterat='('+iterat
    iterat=iterat+')'
    print(iterat)
    cur.execute("Select id,ticker from security_lookup_cn where ticker in "+iterat)

    #
    # # step 2: lookup dictionary and ticker list
    # # tickers = {'AAPL':16.}
    #
    # # step 3: statistic
    # for i in range(len(tickers)):
    #     id = tickers[i]
    #     df = db.get_security_day_price_with_id(int(id[0]))
    #     time=df['time_x']
    #     # basic math operation
    #     price=df['ADJ_CLOSE']
    #
    #     for t in range(len(time)):
    #         date
    #     std=df['ADJ_CLOSE'].values.std()    # standard deviation
    #
    #     print(time,tickers,price,std)
    identification=str()
    for row in cur:
        print(row[0])
        identification=identification+','+str(row[0])
    identification=identification[1:]
    identification='('+identification
    identification=identification+')'


    print(identification)
        # del df
    startdate=20171122
    enddate=20171218
    price=dict()
    cur.execute("Select ticker,time_x,adj_close from security_day_price_cn where security_lookup_id in "+identification)
    for row in cur:
        if(int(str(row[1].date())[0:4]+str(row[1].date())[5:7]+str(row[1].date())[8:10])>=startdate) \
                and (int(str(row[1].date())[0:4]+str(row[1].date())[5:7]+str(row[1].date())[8:10])<=enddate):
            if row[0] not in price.keys():
                price[row[0]]=[]
            price[row[0]].append(row[2])
    print(price)
    ret=dict()
    for iden in price.keys():
        for d in range(len(price[iden])-1):
            if iden not in ret.keys():
                ret[iden]=[]
            ret[iden].append((price[iden][d+1]/price[iden][d]-1))
    print(ret)
    averet=dict()
    stdret=dict()
    for tick in ret.keys():
        print(tick)
        if tick not in averet.keys():
            averet[tick] = []
        averet[tick]=sum(ret[tick])/len(ret[tick])
    for tick in ret.keys():
        if tick not in stdret.keys():
            stdret[tick] = []
        stdret[tick]=(sum([(x-averet[tick])**2 for x in ret[tick]])/len(ret[tick])**0.5)
    rk = zip(averet.values(), averet.keys())
    print(stdret)
    # print
    finalrk=sorted(rk)
    print(finalrk)
    finalreport=dict()
    for i in range(len(finalrk)):
        finalreport[finalrk[i][1]]=[]
        finalreport[finalrk[i][1]].append(i)
        finalreport[finalrk[i][1]].append(finalrk[i][0])
        finalreport[finalrk[i][1]].append(stdret[finalrk[i][1]])
    print(finalreport)

    with open(str(startdate)+'_'+str(enddate)+".txt", 'w') as outfile:
        csv_writer = csv.writer(outfile, delimiter=',')

        for k, v in finalreport.items():
            csv_writer.writerow([k] + v)

    print('whole done...')

if __name__ == '__main__':
    Main()
