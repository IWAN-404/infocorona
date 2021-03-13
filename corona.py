#!/usr/bin/python2
# coding=utf-8
# Jangan Recode Ya Anjing Tinggal Fake Aja Apa Susah Nya
'''
Author : Iwan Hadiansah ID
Fungsi : Get Data Corona
Versi  : 0.3 (Latest Update)

'''
class Corona:

 def __init__(self):
  self.prov = 'https://api.kawalcorona.com/indonesia/provinsi'
  self.indo = 'https://api.kawalcorona.com/indonesia/'
  self.coun = 'https://api.kawalcorona.com/'
  self.main()

 def indonesia(self):
  self.res = requests.get(self.prov).json()
  time.sleep(5)
  self.b = requests.get(self.indo).json()
  for x in self.b:
   runtext.load('\x1b[37m[+] Positive : '+x['positif'])
   runtext.load('\x1b[37m[\x1b[32;1m*\x1b[37m]\x1b[32;1m Recovered : '+x['sembuh'])
   runtext.load('\x1b[37m[\x1b[31m-\x1b[37m]\x1b[31m Died : '+x['meninggal'])
   time.sleep(3)
  self.ask = raw_input('\x1b[37mShow Province (y/n) ')
  if 'y' in self.ask:
   n = []
   for i in self.res:
    n.append(i['attributes'])
   for a in n:
    pv = a['Provinsi']
    print('═'*25)
    print('\x1b[37m[~] Province : '+pv)
    print('\x1b[37m[+] Positive : '+str(a['Kasus_Posi']))
    print('\x1b[37m[\x1b[32;1m*\x1b[37m]\x1b[32;1m Recovered : '+str(a['Kasus_Semb']))
    print('\x1b[37m[\x1b[31m-\x1b[37m]\x1b[31m Died : '+str(a['Kasus_Meni'])+'\x1b[37m')
  if 'n' in self.ask:
   exit()

 def all_country(self):
  self.p = requests.get(self.coun).text
  self.cnt = re.findall('"Country_Region":"(.*?)"',self.p)
  while True:
   self.mm = raw_input('Country : ')
   self.wrl = "".join(src(self.mm,self.cnt,n=1,cutoff=0))
   self.t= r'{"OBJECTID":.*?,"Country_Region":"'+self.wrl+'","Last_Update":.*?,"Lat":.*?,"Long_":.*?,"Confirmed":(.*?),"Deaths":(.*?),"Recovered":(.*?),"Active":.*?}}'
   self.xx = re.search(self.t,self.p)
   print('\n{} Info'.format(self.wrl))
   print('''\x1b[37m[+] Positive : {}
\x1b[37m[\x1b[32;1m*\x1b[37m]\x1b[32;1m Recovered : {}
\x1b[37m[\x1b[31m-\x1b[37m]\x1b[31m Died : {}\x1b[37m'''.format(self.xx.group(1),self.xx.group(2),self.xx.group(3)))

 def main(self):
  print('''1. Indonesian Status
2. All Country Status
''')
  nanya = int(raw_input('status >> '))
  if nanya == 1:
   self.indonesia()
  if nanya == 2:
   self.all_country()

try:
 import requests,os,runtext,sys,time,re
 from difflib import get_close_matches as src
 os.system('clear')
 print('''\x1b[32;1m 
\033[1;91m╭━━━┳━━━┳━━━┳━━━┳━╮╱╭┳━━━╮
\033[1;91m┃╭━╮┃╭━╮┃╭━╮┃╭━╮┃┃╰╮┃┃╭━╮┃
\033[1;91m┃┃╱╰┫┃╱┃┃╰━╯┃┃╱┃┃╭╮╰╯┃┃╱┃┃
\033[1;97m┃┃╱╭┫┃╱┃┃╭╮╭┫┃╱┃┃┃╰╮┃┃╰━╯┃
\033[1;97m┃╰━╯┃╰━╯┃┃┃╰┫╰━╯┃┃╱┃┃┃╭━╮┃
\033[1;97m╰━━━┻━━━┻╯╰━┻━━━┻╯╱╰━┻╯╱╰╯ 
\033[1;93m• https://github.com/IWAN-404•
     
\033[1;93m• Created By : Iwan Hadiansah ID
''')
 Corona()
except requests.exceptions.ConnectionError:
 exit('No Connection')
