##"DU473528,aapl,10,mkt"
import subprocess
def order(acc,ticker,quantity,type):
### acc is your account name
### ticker is the stock ticker
### quantity is the order quantity
### type is the order type
    text = acc +','+ ticker +','+quantity+','+type
    with open('get.txt', 'w') as f:
        f.write(text)
def main():
    order('DU473528','aapl','100','mkt')
    pname="C://ibpy//a.exe"
    p=subprocess.Popen(pname)
    result=p.communicate()
if __name__ == '__main__':
    main()