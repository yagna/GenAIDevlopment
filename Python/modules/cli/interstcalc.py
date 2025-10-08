'''
this is calculator for interset 

interest_calc.py prinicipa-10000 inteset-3 tim-12 months


'''

import argparse

def calc_interset(principal:float, time:int, rate:int ):
   interest = principal * time * rate /100
   return interest
   

def main():
    parser = argparse.ArgumentParser("interset", description="interset Calculator")
    parser.add_argument("--principal", type =float,help ='prinicpal amount taken')
    parser.add_argument("--rate", type=int,help='rate of interset /year ')
    parser.add_argument("--time", type=int, help='number of years ')
    args = parser.parse_args()
    print(calc_interset(args.principal,args.time, args.rate))

if __name__ == '__main__':
 main()