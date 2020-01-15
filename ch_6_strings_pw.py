#! python3
# pw.py - An insecure password locker program.

PASSWORDS = {'email':'adfklshdfislshefiohslkfnlk3@%#$klsf','blog':'sdflhslhiohIHOIHOsdfoIs#%235','luggate':'12345'}

import sys,pyperclip

#sys.argv[1]= input("Enter the account to fetch password: ")

if len(sys.argv)<2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Passsword for ' + account + 'copied to clipboard.')
else:
    print('There is no account named ' + account)
