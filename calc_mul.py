#!/usr/bin/python3

import re
                
def calc(A,B):
        ai=str(A)
        bi=str(B)
        p = re.compile('^[1-9][0-9]*$') #(1)文字列が数字のみで構成されている場合のみ
        if p.match(ai) and p.match(bi): #(2)aとb両方が条件を満たしているか確認する
                a=int(ai)
                b=int(bi)
                if 0<a and a<b and b<1000:
                        valid=True
                else:
                        valid=False
        else:
                valid=False
                
        if valid:
                ans=a*b
                return ans
        else:
                return -1
        

                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()
