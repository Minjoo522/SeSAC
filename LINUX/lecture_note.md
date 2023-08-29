# 운영체제
## 부팅과정
- BIOS
  - ROM BIOS(Basic Input / Output System(CMOS))
    - POST(Power On Self Test) 및 물리적 Boot 디바이스 선정
- MBR
  - Master Boot Record
    - HDD의 특정 섹터(0번 섹터 512Byte)
- GRUB
  - 부트로더(Bootloader)
    - 소프트웨어 영역(멀티 부트 등 처리를 위한 멀티 스테이지 부트)
    - LILO, GRUB(Grand Unified Bootloader), GRUB2, uboot
- Kernel
  - 커널(Linux Kernel) 운영체제 소프트웨어 메모리에 올려서 구동(HW 디ㅏ이스, FS 등)
    - /sbi/init을 실행하며 initrd 패키지의 실행 (pid 1)
- Init
  - 부팅(Init process)
    - 루트 유저 프로세스로 systemd 등의 부팅 과정 수행
    - /etc/inittab 등 실행
- Runlevel
  - 부팅(Runlevle)

## linux 명령어
### 성공한 것은 결과를 주지 않음
- cd(change directory) : 현재 경로 변경
- cd - : 바로 이전 위치로 돌아가기
- . : current directory
- .. : parent directory
- ~ : home directory
- / : 루트
- cd /etc : 에는 모든 설정파일이 있다

<br>

- ls(list) : 파일 보기
- ls -l(long) : 파일 상세 정보까지 보기
- ls -a(all) : 숨김파일(hidden)까지 봄(.으로 출발하는 파일이나 폴더)
- ls -a -l / ls -al / ls -la 등처럼 사용도 가능
- open . : 현재 경로를 파일 탐색기에서 열기

<br>

- touch <파일> : 파일 만들기(원래 목적은 파일 지금 내가 수정했다고 설정) / 파일이 없으면 파일을 만들고 있으면 수정한 날짜를 지금 날짜로 설정 / touch hello.txt
- cat <파일> : concatenate(연결) / 파일 내용 보기 / 파일과 터미널을 연결해준다
- more <파일> : 페이징 처리 되어 파일 내용 보임 / 스페이스바로 페이지 이동 가능
- less <파일> : 좌우 위 아래 이동 가능
- rm <파일> : remove / 지우기
  - rm hello* 같은 식으로도 지울 수 있음
- rm -r : 반복적으로 편하게 지움 / 복구 불가 / 사용시 주의❗️
- mkdir <폴더> : make directory / 폴더 만들기
- mkdir -p <폴더>/<폴더>/<폴더> : 폴더 안의 폴더안의 폴더 만들 수 있음
~~~zsh
mkdir -p dir4/subdir1/subdir2
~~~

- rmdir <폴더> : remove directory / 폴더 지우기
- pwd(Print Working Directory) : 현재 나의 working directory(나의 위치)
- $ : 프롬푸트(사용자의 입력을 나타내는 기호), 프롬푸트를 잘 설정하면 사용자 / 호스트 / 디렉토리 $ 처럼 보이게 만들 수도 있음
  - PS1 = prompt statement one
- ll : ls -l을 alias로 만들어 둔 것(OS 배포판마다 차이가 큼 ➡️ 이거는 우분투에만 기본적으로 있음)
- cp <출발지> <목적지> : copy / 파일 복사 / 있는 파일에 복사하는 경우 over write됨 / 파일 ➡️ 폴더 : 폴더 안으로 파일이 복사됨
~~~zsh
cp file1.txt dir1/
~~~

- cp -r : 폴더도 복사 가능
- echo : 화면에 글자를 출력하는 명령어
  - echo "hello" > hello.txt : redirection 기능을 통해서 hello.txt 파일에 결과를 보내줌
  - over write 됨
  - \>> : append 기능!
- file <파일> : 속성 알려줌
~~~zsh
ubuntu@ip-172-31-42-74:~$  file /usr/bin/file
/usr/bin/file: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=32715f59ea258e8fdf0dd8763fc501f958b0c4d6, for GNU/Linux 3.2.0, stripped
~~~
- reboot : 재부팅 / 관리자만 끌 수 있음 ➡️ sudo reboot ➡️ 전원 껐다 켜기, 중지와 다름!
- shutdown : 끄기 / 관리자만 가능 ➡️ sudo shutdown 
  - sudo shutdown -h now : 이 때 동작을 어떻게 할 것인가가 웹에서의 종료 동작 변경❗️ ➡️ 중지 / 다시 킬 때 ip 주소 변경됨
- man ls : ls에 대한 매뉴얼 보기

<br>

- which : 실행하고자 하는 프로그램이 어디에 설치되어 있는지, 실행되어 있는지 경로 확인
- whereis : 어디에 있는지 다 보여줌!
- 파이프(|) : 출력값 프로세스 간 연결 ➡️ 결과를 전달해서 재처리
~~~zsh
ls -l | grep "hello"
# 결과 : hello만 강조되어 나옴!
ls -al | wc -1 # wordcount
-rw-rw-r-- 1 ubuntu ubuntu  288 Aug 24 14:31 hello.txt
-rw-rw-r-- 1 ubuntu ubuntu   55 Aug 24 12:13 hello2.txt
lrwxrwxrwx 1 ubuntu ubuntu    9 Aug 24 12:16 hellosym -> hello.txt
~~~

- grep(Global Regular Expression Print) : 키워드로 검색
~~~zsh
# 모든 txt 파일에 대해서 world 검색
grep "world" *.txt
# -n : 몇 번째 줄에 있는지 확인
grep -n "world" *.txt
# -i : 대소문자 상관 없이 검색
grep -ni "world" *.txt
# -r : recursive
# 현재 경로와 하위 폴더에서 모두 검색
grep -nir "world" .
~~~ 

- history : 지금까지 친 명령어 보기
  - 느낌표 다음 줄 번호 치면 명령어 다시 실행 됨!
  - !! : 가장 최근에 실행한 명령어 다시 실행 됨!
~~~zsh
!128
!!
~~~
- alias : 기본적으로 있는 shortcut 기능들이 나옴
~~~zsh
# 새로운 alias 만들기
alias ..="cd .."
~~~
  - 껐다 키면 다시 없어짐
  - 부팅할 때 자동으로 실행해주는 명령어 : .bashrc
~~~zsh
touch .bash_aliases
echo 'alias ..="cd .."' > .bash_aliases
echo 'alias ...="cd ../.."' >> .bash_aliases
~~~
- find : 원하는 것을 찾는 기능
~~~zsh
# 현재 디렉토리에서 이름이 hello로 시작하는 모든 것
find . -name "hello*"
find . -type file -name "*.txt"
find . -type file -name "*.json"
find . -type directory -name "*2"
~~~
- 화면에 출력에 대한 "형태"
  - 0 stdin
  - 1 stdout
  - 2 stderr
~~~zsh
find / -name "hello*" 2> hello.txt
find / -name "hello*" > hello.stdout.txt 2> hello.stderr.txt

# 사이즈가 100M인 것 찾기
find / -size 100M
# 사이즈가 100M보다 큰거 찾기
find / -size +100M
~~~
- /dev/null : 휴지통
~~~zsh
find / -name "hello*" 2> /dev/null
~~~
- du : 디렉토리의 용량 확인
  - du -h : human readable
  - du -h --max-depth=1

### 환경 변수 설정
- export
~~~zsh
export MY_DIR="dir1"

# 이제 아래처럼 이용 가능 - $환경변수
cd $MY_DIR
~~~
- env : 설정된 모든 환경 변수 보기
- unset <환경변수> : 설정된 환경 변수 지우기

### 짱 중요
- ln : 링크(하드 링크)
- ln -s <타겟> <소스> : 심볼릭 링크(소프트 링크)
~~~zsh
ln -s hello.txt hellosym
# hellosym이라는 이름을 통해서 hello.txt로 갈 수 있음

# ⏰ 시간 설정해주기
sudo rm /etc/localtime
sudo ln -s /usr/share/zoneinfo/Asia/Seoul /etc/localtime
~~~

### 쉘 스크립트
~~~zsh
touch test1.sh
~~~
- vscode에서 연결해서 할 수 있음
~~~sh
#!/bin/bash ⬅️ 나의 파일이 어떤 건지 알려줌 #! : shabang

ls ➡️ 이 스크립트가 실행되면 ls가 실행됨

# 이런식으로 실행해야 할 것들 미리 정의
# 새로운 EC2 만들었을 때 편하게 설치 가능
sudo apt update
sudo apt install python3-dev -y
sudo apt install python3.8-venv -y
sudo apt install python3-pip -y
# python3 -mvenv ~/.venv/flask
# source ~/.venv/flask/bin/activate
# pip install flask
~~~
- if문 for문 등등 다양한 기능이 있음

## 패키지 관리자 - apt(Advanced Package Tool)
- apt 저장소를 카카오 미러 서버로 설정하는 것도 가능하다(우분투 카카오 미러서버)
- apt update : 리포지토리 내용 가져오기 / 소프트웨어 업데이트가 ❌ / 패키지의 경로, 정보들 갱신
- apt list : 리포지토리 패키지 목록 출력(로컬 캐쉬)
- apt list --installed : 설치된 패키지 목록 출력
- apt list --upgradeable : 업그레이드(업데이트) 가능한 목록 출력
- apt search : 리포지토리 검색(로컬 캐쉬)
~~~zsh
apt search nginx
~~~
- apt show : 패키지 정보 표시
- apt install : 리포지토리 내의 패키지 설치 ↔️ apt purge
~~~zsh
# 뒤에 -y 붙이면 묻지말고 yes
sudo apt install nginx -y
~~~
- apt remove : 설치된 패키지 삭제(설정파일 유지)
- apt purge : 설치된 패키지 삭제 + 설정파일 삭제
- apt autoremove : 더 이상 사용되지 않는패키지 삭제(업그레이드 이후 dependency 또한 업그레이드 되어 더이상 참조되지 않는 패키지)
- apt upgrade : 패키지 업그레이드(업데이트)
- apt full-upgrade : 패키지 업그레이드 과정에서 삭제가 필요하다면 그 또한 수행하며 업그레이드(업데이트) - 잘 사용되지

## 🚨 웹서버 확인 및 관리 - 중요❗️
- systemctl status nginx : 상태 확인
- sudo systemctl stop nginx : 끄기 ➡️ 껐더라도 재부팅하면 다시 뜸
  - 데몬 서비스 : 백그라운드에서 구동되면서 요청을 받아서 처리하는 것 ➡️ enabled면 껐다 켜도 자동으로 실행됨
  - sudo systemctl disable nginx : enabled ➡️ disable
- sudo systemctl start nginx : 시작하기

### 아래 네 차이를 인지하고 있어야 함!
- enable / stop
- enable / start (active / running)
- disable / stop (inactive)
- disable / start (active / running)

## 🚨 웹 서버를 통해 우리의 웹 서비스를 구동
- 웹 서버를 만들기 위한 후보군 : sites-available : 실제 데이터가 있음
- 실제 서비스를 on/off : sites-enabled : 심볼이 있음(sites-available에 있는 애들을 가리킴 / 여기다가 파일 만들면 동작은 하지만 원작자의 철학을 무시하는 것 💩)
~~~zsh
listen 80 default_server;
root /var/www/html;
# /etc/nginx/site-available의 default 파일에서 아래 내용 확인 가능!
# index.html이 있으면 이거 아니면 index.htm 이것도 없으면 index.nginx-debian.html
index index.html index.htm index.nginx-debian.html;

# sudo만 쓰면 echo "hello" 까지만 권한이 허용되기 때문에, 아래꺼 실행 안됨!
ubuntu@ip-172-31-42-74:/var/www/html$ sudo echo "hello" > index.html
# sudo 권한으로 새로운 shell을 열어서 실행!
sudo sh -c 'echo "hello" > index.html'
~~~

### sudo chmod -R o+w . : 보안을 매우 취약하게 만듦
~~~zsh
# 폴더 위치는 /etc/nginx
ubuntu@ip-172-31-42-74:/etc/nginx$ sudo chmod -R o+w .

ubuntu@ip-172-31-42-74:/etc/nginx/sites-available$ code default
ubuntu@ip-172-31-42-74:/etc/nginx/sites-available$ cd ..
ubuntu@ip-172-31-42-74:/etc/nginx$ cd sites-enabled/
ubuntu@ip-172-31-42-74:/etc/nginx/sites-enabled$ ln -s /etc/nginx/sites-available/sesac 
ubuntu@ip-172-31-42-74:/etc/nginx/sites-enabled$ ls -l
total 0
lrwxrwxrwx 1 root   root   34 Aug 23 15:13 default -> /etc/nginx/sites-available/default
lrwxrwxrwx 1 ubuntu ubuntu 32 Aug 24 15:47 sesac -> /etc/nginx/sites-available/sesac
# nginx가 두 개의 사이트를 운영 가능하게 됨

# 위와 같이 바꾼걸로 인해서 실패 됨
ubuntu@ip-172-31-42-74:/etc/nginx/sites-enabled$ sudo systemctl restart nginx
Job for nginx.service failed because the control process exited with error code.
See "systemctl status nginx.service" and "journalctl -xe" for details.

ubuntu@ip-172-31-42-74:/etc/nginx/sites-enabled$ systemctl status nginx.service
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
     Active: failed (Result: exit-code) since Thu 2023-08-24 15:48:05 KST; 40s ago
       Docs: man:nginx(8)
    Process: 2870 ExecStartPre=/usr/sbin/nginx -t -q -g daemon on; master_process on; (code=exited, status=1/FAILURE)

Aug 24 15:48:05 ip-172-31-42-74 systemd[1]: Starting A high performance web server and a reverse proxy server...
Aug 24 15:48:05 ip-172-31-42-74 nginx[2870]: nginx: [emerg] a duplicate default server for 0.0.0.0:80 in /etc/nginx/sites-enabled/sesac:22
Aug 24 15:48:05 ip-172-31-42-74 nginx[2870]: nginx: configuration file /etc/nginx/nginx.conf test failed
Aug 24 15:48:05 ip-172-31-42-74 systemd[1]: nginx.service: Control process exited, code=exited, status=1/FAILURE
Aug 24 15:48:05 ip-172-31-42-74 systemd[1]: nginx.service: Failed with result 'exit-code'.
lines 1-11...skipping...
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
     Active: failed (Result: exit-code) since Thu 2023-08-24 15:48:05 KST; 40s ago
       Docs: man:nginx(8)
    Process: 2870 ExecStartPre=/usr/sbin/nginx -t -q -g daemon on; master_process on; (code=exited, status=1/FAILURE)

Aug 24 15:48:05 ip-172-31-42-74 systemd[1]: Starting A high performance web server and a reverse proxy server...
# 🚨 80번 port가 duplicate!
Aug 24 15:48:05 ip-172-31-42-74 nginx[2870]: nginx: [emerg] a duplicate default server for 0.0.0.0:80 in /etc/nginx/sites-enabled/sesac:22
Aug 24 15:48:05 ip-172-31-42-74 nginx[2870]: nginx: configuration file /etc/nginx/nginx.conf test failed
Aug 24 15:48:05 ip-172-31-42-74 systemd[1]: nginx.service: Control process exited, code=exited, status=1/FAILURE
Aug 24 15:48:05 ip-172-31-42-74 systemd[1]: nginx.service: Failed with result 'exit-code'.
Aug 24 15:48:05 ip-172-31-42-74 systemd[1]: Failed to start A high performance web server and a reverse proxy server.
~~~

~~~sh
# sesac의 default 파일에서 server 88로 바꿔줌
server {
	listen 88 default_server;

	root /var/www/html;

	index index.html index.htm index.nginx-debian.html;

	location / {
	}
}
~~~

~~~zsh
# 수정한 파일에 오류가 없는지 미리 확인
# 설정파일의 문법을 체크
sudo nginx -t

# 문법에 오류가 없을 때!
# 재시작
sudo systemctl restart nginx
# 설정파일 다시 불러오기
sudo systemctl reload nginx
~~~

~~~sh
# 새싹 폴더에선 다른 파일 띄울거니까 root 변경
# 클라우드는 보안 허용 해주어야 함!
server {
	listen 88 default_server;

	root /var/www/html/sesac;

	index index.html index.htm index.nginx-debian.html;

	location / {
	}
}
~~~

~~~zsh
ubuntu@ip-172-31-42-74:/etc/nginx/sites-enabled$ cd /var/www/html
ubuntu@ip-172-31-42-74:/var/www/html$ sudo chmod -R o+w .
ubuntu@ip-172-31-42-74:/var/www/html$ mkdir sesac
ubuntu@ip-172-31-42-74:/var/www/html$ cd sesac
ubuntu@ip-172-31-42-74:/var/www/html/sesac$ code index.html
# html 수정해주고
ubuntu@ip-172-31-42-74:/var/www/html/sesac$ sudo systemctl restart nginx
~~~

- /etc
- /etc/nginx
- /etc/ssh
- /etc/vsftpd
- 내가 원하는 소프트웨어들의 설정을 변경할 때

- /var
- /var/log
- /var/log/syslog
- /var/log/ningx/*
- /var/log/vsftpd/* 등등
- 각종 로그나 운영 현황

- which/whereis : 내가 원하는 바이너리 찾기
- 모든 환경변수는 : env

- 심볼릭 링크(ln -s)를 통해서 활성화/비활성화한다

### 권한 오류가 나올 때마다 sudo 치는 것! ❌❌❌❌❌❌❌❌❌❌

- sudo lastb : 로그인 실패 로그 확인
- sudo lastb | wc -l : 로그인 실패 로그 확인