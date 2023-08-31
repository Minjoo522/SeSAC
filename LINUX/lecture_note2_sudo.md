# 권한 설정

- sudoer : root 권한을 빌려올 수 있는 사용자

## 사용자 계정(권한 조사)
- whoami : 내가 누군지 할 수 있음
~~~bash
ubuntu@ip-172-31-42-74:~$ whoami
ubuntu

# sudo를 칠 때는 root 권한을 빌려와서 액션을 취하는 것이기 때문에 내가 내가 아니다!
ubuntu@ip-172-31-42-74:~$ sudo whoami
root
~~~
- id : 나에 부여된 권한을 살펴볼 수 있음
~~~bash
ubuntu@ip-172-31-42-74:~$ id
# 나의 아이디, 그룹 아이디, 내가 포함된 그룹(adm: admin, dialout: 전화선 통신 계정(지금은 별 의미 없음), 하드웨어 디바이스에 대한 접근, 제어 권한)
# adm : 관리자들이 보고 사용하는 권한
# sudo : sudo를 실행할 수 있는 권한(sudoer)
# gid : 나 자신이 포함된 그룹
uid=1000(ubuntu) gid=1000(ubuntu) groups=1000(ubuntu),4(adm),20(dialout),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46,(plugdev),118(netdev),119(lxd)
~~~

## 사용자 생성과 그룹 생성
- adduser : 계정 생성
~~~bash
ubuntu@ip-172-31-42-74:~$ sudo adduser user2
Adding user `user2' ...
Adding new group `user2' (1001) ...
Adding new user `user2' (1001) with group `user2' ...
Creating home directory `/home/user2' ...
Copying files from `/etc/skel' ...
New password:
Retype new password:
passwd: password updated successfully
Changing the user information for user2
Enter the new value, or press ENTER for the default
# 넣어도 되고 안넣어도 된다 / 실무적으로 이름 정도는 넣음!
	Full Name []:
	Room Number []:
	Work Phone []:
	Home Phone []:
	Other []:
Is the information correct? [Y/n]
# 클라우드에서는 로그인이 안됨 - 아이디, 비밀번호 사용하기 때문에
# 🚨 실무에서는 안함!! - 실습을 위해
ubuntu@ip-172-31-42-74:~$ sudo vi /etc/ssh/sshd_config
# passwordauthentication no <-- yes로 변경
ubuntu@ip-172-31-42-74:~$ sudo systemctl restart sshd

# 새로만든 다른 계정으로 로그인
ssh user2@54.80.92.40
~~~

- 새로 만든 계정에서 id
~~~bash
user2@ip-172-31-42-74:~$ id
# 아무런 권한이 없음
uid=1001(user2) gid=1001(user2) groups=1001(user2)
~~~

- 볼 수 있는 파일 vs 볼 수 없는 파일
~~~bash
# ubuntu 계정
cat /etc/passwd
# 볼 수 없음
cat /etc/shadow
# 볼 수 있음
sudo cat /etc/shadow

# user2
cat /etc/passwd
# 볼 수 없음
cat /etc/shadow
sudo cat /etc/shadow

user2@ip-172-31-42-74:~$ sudo cat /etc/shadow
[sudo] password for user2:
user2 is not in the sudoers file.  This incident will be reported.
~~~

~~~bash
ls -al /var/log
# 사용자 행위가 찍히는 감사 로그 보기
cat /var/log/auth.log
Aug 29 11:40:11 ip-172-31-42-74 sudo:   ubuntu : TTY=pts/1 ; PWD=/home/ubuntu ; USER=root ; COMMAND=/usr/bin/cat /etc/shadow
Aug 29 11:41:26 ip-172-31-42-74 sudo:    user2 : user NOT in sudoers ; TTY=pts/2 ; PWD=/home/user2 ; USER=root ; COMMAND=/usr/bin/cat /etc/shadow
~~~

## 파일 권한 다루기
- 소유자(User) / 그룹(Group) / 그 외(Other)
~~~bash
ubuntu@ip-172-31-42-74:~$ ls -l
total 116
# 유형(d = directory, l=link), ✨권한 / 링크수 / ✨소유자 / ✨그룹 / 파일크기 / 변경일자 / 이름
drwxrwxr-x 3 ubuntu ubuntu  4096 Aug 23 14:11 SESAC
-rw-rw-r-- 1 ubuntu ubuntu   214 Aug 24 14:50 dev_env_setup.sh
drwxrwxr-x 3 ubuntu ubuntu  4096 Aug 24 11:55 dir1
-rw-rw-r-- 1 ubuntu ubuntu 47182 Aug 24 15:05 hello.stderr.txt
-rw-rw-r-- 1 ubuntu ubuntu   337 Aug 24 15:05 hello.stdout.txt
-rw-rw-r-- 1 ubuntu ubuntu 47182 Aug 24 15:05 hello.txt
-rw-rw-r-- 1 ubuntu ubuntu    55 Aug 24 12:13 hello2.txt
lrwxrwxrwx 1 ubuntu ubuntu     9 Aug 24 12:16 hellosym -> hello.txt
~~~
### 🚨 외우기~
- 읽기 : r / 4
- 쓰기 : w / 2
- 실행 : x / 1 
  - 파일 : 실행(execute)
  - 디렉토리 : 접근(access)
- 읽기 + 실행 : 4 + 1 = 5
- 읽기 + 쓰기 + 실행 : 4 + 2 + 1 = 7

- 0 --- : 권한무
- 1 --x : 실행
- 2 -w- : 쓰기
- 3 -wx : 쓰기 & 실행
- 4 r-- : 읽기
- 5 r-x : 읽기 & 실행
- 6 rw- : 읽기 & 쓰기
- 7 rwx : 읽기 & 쓰기 & 실행

~~~bash
-rw-rw-r-- 1 ubuntu ubuntu     6 Aug 29 11:51 hello.txt
# user2
user2@ip-172-31-42-74:/home/ubuntu$ cat hello.txt
hello
user2@ip-172-31-42-74:/home/ubuntu$ echo "hello" > hello.txt
-bash: hello.txt: Permission denied
# user2는 읽기 권한은 있지만 쓰기 권한은 없음
~~~

- 권한 변경 (읽기, 쓰기, 실행)
~~~bash
# ubuntu 계정
# chmod  == change mode
chmod 660 hello.txt
-rw-rw---- 1 ubuntu ubuntu     6 Aug 29 11:51 hello.txt

user2@ip-172-31-42-74:/home/ubuntu$ cat hello.txt
cat: hello.txt: Permission denied
~~~

- 파일에 대한 소유권 변경
~~~bash
# chown == change owner
# chown <사용자>:<그룹> <파일명>
chown user2:user2 hello.txt
# 내 마음대로 소유권 변경 불가 ➡️ 관리자만 가능
ubuntu@ip-172-31-42-74:~$ chown user2:user2 hello.txt
chown: changing ownership of 'hello.txt': Operation not permitted

# 관리자
sudo chown user2:user2 hello.txt
-rw-rw-rw- 1 user2  user2     13 Aug 29 12:05 hello.txt
~~~

- 폴더 권한 변경
~~~bash
ubuntu@ip-172-31-42-74:~/dir1$ ls -al
total 12
drwxrwxr-x 2 ubuntu ubuntu 4096 Aug 29 12:10 .
drwxr-xr-x 9 ubuntu ubuntu 4096 Aug 29 12:09 ..
-rw-rw-r-- 1 ubuntu ubuntu    6 Aug 29 12:10 hello.txt
# 실행 권한만 주기
ubuntu@ip-172-31-42-74:~/dir1$ chmod 771 .

# user2
user2@ip-172-31-42-74:/home/ubuntu/dir1$ ls -al
ls: cannot open directory '.': Permission denied

# 엑세스 권한 ❌, 읽기 권한 ⭕️
# 굳이 이렇게 줄 필요가 없음!
ubuntu@ip-172-31-42-74:~/dir1$ chmod 774 .

# user2
# dir1에 들어갈 수 없지만(읽기 불가) 억지로 엑세스 가능
# 파일이랑 폴더일 때 x 차이 구분!
user2@ip-172-31-42-74:/home/ubuntu$ ls -l dir1
ls: cannot access 'dir1/hello.txt': Permission denied
total 0
-????????? ? ? ? ?            ? hello.txt
~~~

### 문자로 편하게 할수도 있음
~~~bash
# chmod u+r / u-r / g+w / g-w / o+rw / o=rw
chmod o-w .
~~~

- 이거 권한 한 번 분석해보기~
~~~bash
ubuntu@ip-172-31-42-74:~/dir1$ ls -al /etc/passwd
# User : rw
-rw-r--r-- 1 root root 1946 Aug 29 11:26 /etc/passwd
ubuntu@ip-172-31-42-74:~/dir1$ ls -al /etc/shadow
-rw-r----- 1 root shadow 1129 Aug 29 11:26 /etc/shadow
ubuntu@ip-172-31-42-74:~/dir1$ ls -al /var/log/auth.log
# ubuntu 계쩡이 adm 그룹에 속하기 때문에 읽기 권한이 있어서 읽을 수 있다❗️
-rw-r----- 1 syslog adm 84313 Aug 29 12:18 /var/log/auth.log
~~~

~~~bash
# 계정보기
cat /etc/passwd
# 아이디 / 패스워드 
user2:x:1001:1001:,,,:/home/user2:/bin/bash

# 그룹보기
cat /etc/group
# 그룹 / 사용자 목록
adm:x:4:syslog,ubuntu
ubuntu:x:1000:
user2:x:1001:
~~~

- 새로운 그룹 만들기
- addgroup
- sudo를 통해서
~~~bash
# GID 1002번이라는 새로운 그룹이 만들어짐
ubuntu@ip-172-31-42-74:~$ sudo addgroup developers
Adding group `developers' (GID 1002) ...
Done.
~~~

- 그룹에 유저 추가
~~~bash
# a : append
# G : group
sudo usermod -a -G developers ubuntu
sudo usermod -aG developers user2

developers:x:1002:ubuntu,user2



total 20
drwxr-xr-x 3 root   root   4096 Aug 24 15:55 .
drwxr-xr-x 3 root   root   4096 Aug 23 15:13 ..
-rw-r--rw- 1 root   root      6 Aug 24 15:35 index.html
-rw-r--rw- 1 root   root    612 Aug 23 15:13 index.nginx-debian.html
drwxrwxr-x 2 ubuntu ubuntu 4096 Aug 24 15:56 sesac
ubuntu@ip-172-31-42-74:/var/www/html$ sudo chown -R root:developers .
ubuntu@ip-172-31-42-74:/var/www/html$ ls -al
total 20
drwxr-xr-x 3 root developers 4096 Aug 24 15:55 .
drwxr-xr-x 3 root root       4096 Aug 23 15:13 ..
-rw-r--rw- 1 root developers    6 Aug 24 15:35 index.html
-rw-r--rw- 1 root developers  612 Aug 23 15:13 index.nginx-debian.html
drwxrwxr-x 2 root developers 4096 Aug 24 15:56 sesac
ubuntu@ip-172-31-42-74:/var/www/html$ sudo chmod -R g+w .
ubuntu@ip-172-31-42-74:/var/www/html$ ls -al
total 20
drwxrwxr-x 3 root developers 4096 Aug 24 15:55 .
drwxr-xr-x 3 root root       4096 Aug 23 15:13 ..
-rw-rw-rw- 1 root developers    6 Aug 24 15:35 index.html
-rw-rw-rw- 1 root developers  612 Aug 23 15:13 index.nginx-debian.html
drwxrwxr-x 2 root developers 4096 Aug 24 15:56 sesac
~~~
- 그룹 권하는 로그인하는 시점에 부여된다!
~~~bash
# 원래는 권한 부여받고 나서 나갔다 들어와야 권한 부여되지만 나가지 않고 바로 권한 부여 받는 방법
# 권장하지 않음
 developers
~~~

- 권한 빼기
- deluser <유저> <그룹>
~~~bash
ubuntu@ip-172-31-42-74:/var/www/html$ sudo deluser user2 developers
Removing user `user2' from group `developers' ...
Done.

developers:x:1002:ubuntu
~~~

## 파일 다루기 상급
- 파일의 특수 실행 권한
- setuid : 실행할 때 해당 사용자의 권한으로 실행
  - 이 파일을 실행할 때 이 파일의 소유주로 실행을 하라
  - sudo : 관리자의 권한으로 실행하는 것처럼
~~~bash
# 그래서 sudo 찾아서 보면 -rw✨s라고 되어있음
ubuntu@ip-172-31-42-74:/var/www/html$ ls -al /usr/bin/sudo
-rwsr-xr-x 1 root root 166056 Apr  4 20:56 /usr/bin/sudo
# s : setuid(special permission 중에서)
# s는 setuid와 실행권한이 둘다 있음
# S는 setuid만 있고 실행권한은 없음

ubuntu@ip-172-31-42-74:~$ which cat
/usr/bin/cat
ubuntu@ip-172-31-42-74:~$ cp /usr/bin/cat mycat
ubuntu@ip-172-31-42-74:~$ ls -al
-rwxr-xr-x 1 ubuntu ubuntu     43416 Aug 29 13:55 mycat
ubuntu@ip-172-31-42-74:~$ ./mycat hello.txt
hello
hello2
ubuntu@ip-172-31-42-74:~$ chmod u+s mycat
ubuntu@ip-172-31-42-74:~$ ls -al
-rwsr-xr-x 1 ubuntu ubuntu     43416 Aug 29 13:55 mycat
~~~

- setgid : 안에서 만들어지는 파일들은 그 사용자의 그룹 권한을 상속받게 되어있음
  - 협업 공간을 만들 때 많이 쓰임
  - 해당 폴더에 만들어지는 파일이 그룹 권한을 자동적으로 상속받는다
~~~bash
# 기존
drwxrwxr-x 3 root   developers 4096 Aug 29 14:01 .
# 권한 부여
ubuntu@ip-172-31-42-74:/var/www/html$ sudo chmod g+s .
ubuntu@ip-172-31-42-74:/var/www/html$ ls -al
total 32
drwxrwsr-x 3 root   developers 4096 Aug 29 14:01 .
drwxr-xr-x 3 root   root       4096 Aug 23 15:13 ..
-rw-rw-r-- 1 user2  developers    6 Aug 29 13:59 hello.html
-rw-rw-r-- 1 ubuntu ubuntu        7 Aug 29 13:44 home.html
-rw-rw-rw- 1 root   developers    6 Aug 24 15:35 index.html
-rw-rw-rw- 1 root   developers  612 Aug 23 15:13 index.nginx-debian.html
-rw-rw-r-- 1 user2  user2         7 Aug 29 13:45 myfile.html
drwxrwxr-x 2 root   developers 4096 Aug 24 15:56 sesac
ubuntu@ip-172-31-42-74:/var/www/html$ echo "user1 file" > user1.html
ubuntu@ip-172-31-42-74:/var/www/html$ ls -al
total 36
drwxrwsr-x 3 root   developers 4096 Aug 29 14:02 .
drwxr-xr-x 3 root   root       4096 Aug 23 15:13 ..
-rw-rw-r-- 1 user2  developers    6 Aug 29 13:59 hello.html
-rw-rw-r-- 1 ubuntu ubuntu        7 Aug 29 13:44 home.html
-rw-rw-rw- 1 root   developers    6 Aug 24 15:35 index.html
-rw-rw-rw- 1 root   developers  612 Aug 23 15:13 index.nginx-debian.html
-rw-rw-r-- 1 user2  user2         7 Aug 29 13:45 myfile.html
drwxrwxr-x 2 root   developers 4096 Aug 24 15:56 sesac
-rw-rw-r-- 1 ubuntu developers   11 Aug 29 14:02 user1.html
~~~
- sitcky bit : 해당 디렉토리에 생성된 파일은 해당 사용자의 소유주로 지정

- 계정 삭제
~~~bash
sudo deluser user3
# 기본적으로 계정이 지워질 때 home 폴더가 같이 지워지지 않음

ubuntu@ip-172-31-42-74:/home$ ls -al
total 20
drwxr-xr-x  5 root   root   4096 Aug 29 14:04 .
drwxr-xr-x 20 root   root   4096 Aug 29 10:10 ..
drwxr-xr-x  9 ubuntu ubuntu 4096 Aug 29 13:55 ubuntu
drwxr-xr-x  3 user2  user2  4096 Aug 29 13:44 user2
drwxr-xr-x  3 user3  user3  4096 Aug 29 14:06 user3

# 새로운 user3를 만들면 파일이 매핑될 수 있음
ubuntu@ip-172-31-42-74:/home$ sudo adduser suer3
Adding user `suer3' ...
Adding new group `suer3' (1005) ...
Adding new user `suer3' (1003) with group `suer3' ...
Creating home directory `/home/suer3' ...
Copying files from `/etc/skel' ...
New password:

# 홈까지 지우기 ➡️ 필요한 정보가 전부 지워질 수 있으니 주의!
sudo deluser user3 --remove-home
ubuntu@ip-172-31-42-74:/home$ sudo deluser user3 --remove-home
Looking for files to backup/remove ...
Removing files ...
Removing user `user3' ...
Warning: group `user3' has no more members.
Done.

ubuntu@ip-172-31-42-74:/home$ ls -al
total 20
drwxr-xr-x  5 root   root   4096 Aug 29 14:08 .
drwxr-xr-x 20 root   root   4096 Aug 29 10:10 ..
drwxr-xr-x  2 suer3  suer3  4096 Aug 29 14:07 suer3
drwxr-xr-x  9 ubuntu ubuntu 4096 Aug 29 13:55 ubuntu
drwxr-xr-x  3 user2  user2  4096 Aug 29 13:44 user2
~~~

## id / key 기반의 인증 시스템 만들기
- 대칭키 암호화 : 암호화 - 복호화시 같은 키 사용
- PSK : Pre Shared Key
- PKI : Public Key Infrastructure(공개 키 기반 구조)
  - 암호화(공개키) - 복호화(개인키)시 다른 키 사용 : 공개키로 암호화한 내용을 공개키로 복호화 할 수 없음
  - RSA : 2048비트 정도
  - 속도가 느림
- 실무적으로는 PSK, PSI를 하이브리드로 사용함
- 키를 저장하는 공간 : 홈디렉토리에 .ssh 폴더(hidden folder)에 있음
~~~bash
# ✨나만✨ 보고 쓰고 접근 가능해야 함!
ubuntu@ip-172-31-42-74:~$ cd .ssh
ubuntu@ip-172-31-42-74:~/.ssh$ ls -al
total 12
drwx------ 2 ubuntu ubuntu 4096 Aug 23 11:39 .
drwxr-xr-x 9 ubuntu ubuntu 4096 Aug 29 13:55 ..
-rw------- 1 ubuntu ubuntu  391 Aug 23 11:39 authorized_keys

# user2에는 없음
user2@ip-172-31-42-74:~$ cd .ssh
bash: cd: .ssh: No such file or directory
# 만들기
user2@ip-172-31-42-74:~$ mkdir .ssh
user2@ip-172-31-42-74:~$ ls -al
total 32
drwxr-xr-x 4 user2 user2      4096 Aug 29 14:29 .
drwxr-xr-x 5 root  root       4096 Aug 29 14:14 ..
-rw------- 1 user2 user2       384 Aug 29 14:26 .bash_history
-rw-r--r-- 1 user2 user2       220 Aug 29 11:25 .bash_logout
-rw-r--r-- 1 user2 user2      3771 Aug 29 11:25 .bashrc
drwx------ 2 user2 user2      4096 Aug 29 11:32 .cache
-rw-r--r-- 1 user2 user2       807 Aug 29 11:25 .profile
drwxrwxr-x 2 user2 user2      4096 Aug 29 14:29 .ssh
# ✨나만✨ 보고 쓰고 접근 가능해야 함!
user2@ip-172-31-42-74:~$ chmod 700 .ssh

# 파일
user2@ip-172-31-42-74:~$ cd .ssh
user2@ip-172-31-42-74:~/.ssh$ touch authorized_keys
user2@ip-172-31-42-74:~/.ssh$ ls -al
total 8
drwx------ 2 user2 developers 4096 Aug 29 14:30 .
drwxr-xr-x 4 user2 user2      4096 Aug 29 14:29 ..
-rw-rw-r-- 1 user2 user2    0 Aug 29 14:30 authorized_keys
# 파일이니까 실행할 필요 없음 : 600
user2@ip-172-31-42-74:~/.ssh$ chmod 600 authorized_keys
~~~

- 개인키를 통해 공개키를 추출하는 방법!
~~~bash
❯ ssh-keygen -y -f mjkim-key.pem
ssh-rsa ~~~
~~~

~~~bash
# user2의 authorized_keys 파일에 공개키 넣어줌
user2@ip-172-31-42-74:~/.ssh$ echo "~~~" > authorized_keys
# vim으로 넣어도 됨!
# 여러개의 키를 넣을수도 있음
# 아이디 - 패스워드 로그인 불허! 설정하기 위 참고!
~~~

## sudoer
- sudo visudo : 사용자 계정 권한들을 설정
~~~bash
# 필요한 경우 아래 기능을 통해 sudo 실행시 패스워드 없이 입력받게 한다
# sudo 권한이 있는 사용자에 대해서 패스워드 없이 실행하게 한다
%sudo ALL=(ALL:ALL) NOPASSWD: ALL
# 호스트명=(사용자명:그룹명) 실행명령어

# 패스워드 없는 사용자 만들 수 있음
sudo adduser --disabled-password user3
# 1. 이대로 끝내면 로그인 안됨
# 2. sudo로 key 사용하게 mkdir.. 해주고
# 3. 사용자 sudo chown 바꿔주기
# 4. sudo로 만들고
# 5. 소유권 원래 User로 바꾸기
# 6. 권한도 600으로 다시!
# ✨ chown -R로 폴더에 하면 권한 다 변경 가능
~~~
- /etc/sudoers.d/* 로딩 여기서 살펴보면 클라우드는
- ubuntu ALL=(ALL) NOPASSWD:ALL 로 되어있다!

### 웹 개발을 하려면?
- /var/www/html이라는 폴더에 실제 정적 컨텐츠를 생성/수정/삭제할 수 있어야 함
- 현재값은 root:root로 되어 있고, 744 상태

#### 해결책
1. /home/ubuntu/www 생성해서 작업
   - 1인 개발이라면 가능, 협업 ❌
2. /var/www/html 폴더에 그룹 권한으로 ubuntu 그룹 권한을 부여
   - 1인 개발이라면 가능, 협업 ❌
3. /var/www/html 폴더에 그룹 권한으로 devs 그룹을 부여 후 ubuntu라는 사용자를 devs 그룹에 추가

#### 내 서버에 추가적인 개발자 등록하기
- 나의 개인키를 그 사용자에게 전달하고 ubuntu라는 계정에 로그인해서 쓰게한다 ❌❌❌❌❌❌❌❌❌❌❌❌
- 실무적으로는 배시 쉘 스크립트를 개발해서 자동으로 할 수 있도록 만들어서 사용함
- 키를 여러개를 넣을 수도 있음

#### vscode 특성상 최초 접속만 ssh로 하고, 그 이후로는 사실상 node-js 기반에 tcp 소켓을 맺고 통신하는 형태(ssh처럼 보이지만, 실제로는 ssh 로그인은 아님) - vscode 서버를 껐다 켜야 됨!
~~~bash
killall node
~~~