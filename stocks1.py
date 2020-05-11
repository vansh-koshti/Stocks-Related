from yahoo_fin import stock_info as si
import matplotlib.pyplot as plt

class bcolors:
    OKGREEN = '\033[92m'
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

c = 0
n = 0
t = 0
x = 1
company = input("Enter the NASDAQ code of the company ")
while (x!=0):
    t = n
    m = si.get_live_price(company)
    n = m
    d = m-t
    if (d>0):
        print(f"{bcolors.OKGREEN}UP {bcolors.ENDC} ",m ," by ",d)
        c = 0
    elif (d<0):
        print(f"{bcolors.FAIL}DOWN {bcolors.ENDC} ",m ," by ",d)
        c = 0
    else:
        c += 1
        if(c >= 50):
            print(f"{bcolors.OKBLUE}market stagnent{bcolors.ENDC}")
            break    
