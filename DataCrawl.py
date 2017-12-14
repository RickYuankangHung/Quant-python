# Please try to obtain the data as shown below by following three steps:
# 1. Crawl the data on this page
# 2. Set a specific date range (01-01-2017 to 09-21-2017 ), achieving all the date information and store them in the local file. (one day per csv file)
# 3. Try to learn the basic data format translation when you save to csv file. (transfer Sep to 09/2017 format, Aug transfer to 08/2017)



#####Generate timelist#####
import bs4 as bs
import csv
import urllib.request
import datetime
datelist=list()
begin = datetime.date(2017,1,1)
end = datetime.date(2017,9,21)
d = begin
delta = datetime.timedelta(days=1)
while d <= end:
    datelist.append(d.strftime("%Y-%m-%d"))
    d += delta
#####Datelist from 2017/01/1 to 2017/09/21

#####To get data day by day and save file by file
for date in datelist:
    html='https://finance.yahoo.com/calendar/economic?from=2017-11-26&to=2017-12-02&day='+date
###    html='https://finance.yahoo.com/calendar/economic?from=2017-09-20'
    sauce=urllib.request.urlopen(html).read()
    soup=bs.BeautifulSoup(sauce,'html.parser')
    table=soup.find('table')
    if table:
        table_rows=table.find_all('tr')
        one_day_data=list()
        for tr in table_rows:
            td=tr.find_all('td')
            row=[i.text for i in td]
            if row != []:
                # print(row[2])
                if row[2]=='Jan':
                    row[2]='01/2017'
                if row[2] == 'Feb':
                    row[2] = '02/2017'
                if row[2] == 'Mar':
                    row[2] = '03/2017'
                if row[2] == 'Apr':
                    row[2] = '04/2017'
                if row[2] == 'May':
                    row[2] = '05/2017'
                if row[2] == 'Jun':
                    row[2] = '06/2017'
                if row[2] =='Jul':
                    row[2] = '07/2017'
                if row[2] == 'Aug':
                    row[2] = '08/2017'
                if row[2] == 'Sep':
                    row[2] = '09/2017'
                if row[2] == 'Oct':
                    row[2] = '10/2016'
                if row[2] == 'Nov':
                    row[2] = '11/2016'
                if row[2] == 'Dec':
                    row[2] = '12/2016'
                one_day_data.append(row)
        file_name=date+'.csv'
        with open(file_name,'w',newline='') as fp:
            a=csv.writer(fp,delimiter=(','))
            a.writerows(one_day_data)
