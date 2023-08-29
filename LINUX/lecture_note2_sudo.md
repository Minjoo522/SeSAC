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

## 파일 다루기 상급