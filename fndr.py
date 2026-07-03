#!/usr/bin/env python3
# fndr.py
# FiNDeR will help YOU find and count characters in your text
import sys, os
cut='''
=========================
'''
def cl():
    os.system('cls'if os.name=='nt'else'clear')
def fndr():
    while True:
        try:
            while True:
                cl()
                text=input(f'Enter YOUR text here: ')
                if text=='':
                    break
                finder={}
                count=1
                for t in text:
                    finder[t]=finder.get(t,0)+1
                print(cut)
                for a, b in finder.items():
                    print(f'[{count}] <{a}> appears <{b}> times')
                    count+=1
                print(cut)
                usr_cnt=input(f'[A]gain / [Q]uit ? ').lower().strip()
                if usr_cnt=='a':
                    break
                else:
                    sys.exit()
        except KeyboardInterrupt:
            print(cut)
            print(f'FiNDeR has been stopped... ')
            sys.exit()
        except Exception as e:
            print(f'\n[ERROR] -> {e} ')
fndr()
