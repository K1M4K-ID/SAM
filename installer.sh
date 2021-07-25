#!/bin/sh
#code by kimak

function dependencies_termux(){
if [ -f /data/data/com.termux/files/usr/opt/metasploit-framework/msfconsole ]; then
                        printf "\033[31;1m[\033[32;1m✔\033[31;1m] \033[37;1mmetasploit already installed\033[31;1m [\033[32;1mOK\033[31;1m]\n"
	                else
                        printf "\033[37;1m[\033[31;1mX\033[37;1m]\033[37;1m metasploit \033[31;1mnot found\033[37;1m, installing metasploit!\n"


			# Remove  Old Folder if exist
			apt autoremove -y > /dev/null 2>&1
			apt remove -y ruby
			apt autoremove -y
			apt install -y libiconv zlib autoconf bison clang coreutils curl findutils git apr apr-util libffi libgmp libpcap postgresql readline libsqlite openssl libtool libxml2 libxslt ncurses pkg-config wget make libgrpc termux-tools ncurses-utils ncurses unzip zip tar termux-elf-cleaner
			ln -sf $PREFIX/include/libxml2/libxml $PREFIX/include/
			loc='/data/data/com.termux/files/home'
			ver='6.0.27'
			cd $loc
			apt-mark unhold ruby
			curl -LO https://github.com/rapid7/metasploit-framework/archive/$ver.tar.gz
			cd $loc
			tar -xf $ver.tar.gz
			mv $loc/metasploit-framework-$ver $loc/metasploit-framework
			cd $paths/msfkit
			wget https://github.com/K1M4K-ID/rubymeta/blob/main/ruby.deb?raw=true > /dev/null 2>&1 && mv -f ruby.deb?raw=true ruby.deb > /dev/null 2>&1
			apt install -y ./ruby.deb
			apt-mark hold ruby
			cd $loc/metasploit-framework
			bundle config build.nokogiri --use-system-libraries
			bundle update
			wget https://github.com/termux/termux-packages/files/2912002/fix-ruby-bigdecimal.sh.txt > /dev/null 2>&1
			bash fix-ruby-bigdecimal.sh.txt && rm fix-ruby-bigdecimal.sh.txt
			cd $loc
			mkdir -p $PREFIX/var/lib/postgresql
			initdb $PREFIX/var/lib/postgresql
			rm 6.0.27.tar.gz
			cd ../usr && mkdir opt && cd $HOME
			mv -f metasploit-framework ../usr/opt
			cd $HOME && rm -fr adbfiles ruby.deb > /dev/null 2>&1
			echo
      echo "install sukses, run ${PREFIX}/opt/metasploit-framework/msfvenom && msfconsole"
			sleep 3

      fi
			sleep 0.1
}

  dependencies_termux
