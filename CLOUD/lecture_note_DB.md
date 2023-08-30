~~~bash
sudo apt update
sudo apt install mysql-server
# install 하면서 나오는 내용들 다 이해해야함!

Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  libcgi-fast-perl libcgi-pm-perl libencode-locale-perl libevent-core-2.1-7 libevent-pthreads-2.1-7 libfcgi-perl libhtml-parser-perl libhtml-tagset-perl
  libhtml-template-perl libhttp-date-perl libhttp-message-perl libio-html-perl liblwp-mediatypes-perl libmecab2 libtimedate-perl liburi-perl mecab-ipadic
  mecab-ipadic-utf8 mecab-utils mysql-client-8.0 mysql-client-core-8.0 mysql-common mysql-server-8.0 mysql-server-core-8.0
Suggested packages:
  libdata-dump-perl libipc-sharedcache-perl libwww-perl mailx tinyca
The following NEW packages will be installed:
  libcgi-fast-perl libcgi-pm-perl libencode-locale-perl libevent-core-2.1-7 libevent-pthreads-2.1-7 libfcgi-perl libhtml-parser-perl libhtml-tagset-perl
  libhtml-template-perl libhttp-date-perl libhttp-message-perl libio-html-perl liblwp-mediatypes-perl libmecab2 libtimedate-perl liburi-perl mecab-ipadic
  mecab-ipadic-utf8 mecab-utils mysql-client-8.0 mysql-client-core-8.0 mysql-common mysql-server mysql-server-8.0 mysql-server-core-8.0
0 upgraded, 25 newly installed, 0 to remove and 103 not upgraded.
Need to get 36.7 MB of archives.
After this operation, 318 MB of additional disk space will be used.
Do you want to continue? [Y/n] 
Get:1 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal/main amd64 mysql-common all 5.8+1.0.5ubuntu2 [7496 B]
Get:2 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal-updates/main amd64 mysql-client-core-8.0 amd64 8.0.34-0ubuntu0.20.04.1 [5075 kB]
Get:3 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal-updates/main amd64 mysql-client-8.0 amd64 8.0.34-0ubuntu0.20.04.1 [22.0 kB]
Get:4 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal/main amd64 libevent-core-2.1-7 amd64 2.1.11-stable-1 [89.1 kB]
Get:5 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal/main amd64 libevent-pthreads-2.1-7 amd64 2.1.11-stable-1 [7372 B]
Get:6 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal/main amd64 libmecab2 amd64 0.996-10build1 [233 kB]
Get:7 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal-updates/main amd64 mysql-server-core-8.0 amd64 8.0.34-0ubuntu0.20.04.1 [22.6 MB]
Get:8 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal-updates/main amd64 mysql-server-8.0 amd64 8.0.34-0ubuntu0.20.04.1 [1325 kB]
Get:9 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal/main amd64 libhtml-tagset-perl all 3.20-4 [12.5 kB]
Get:10 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal/main amd64 liburi-perl all 1.76-2 [77.5 kB]
Get:11 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal/main amd64 libhtml-parser-perl amd64 3.72-5 [86.3 kB]
Get:12 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal/main amd64 libcgi-pm-perl all 4.46-1 [186 kB]
Get:13 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal/main amd64 libfcgi-perl amd64 0.79-1 [33.1 kB]
Get:14 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal/main amd64 libcgi-fast-perl all 1:2.15-1 [10.5 kB]
Get:15 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal/main amd64 libencode-locale-perl all 1.05-1 [12.3 kB]
Get:16 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal/main amd64 libhtml-template-perl all 2.97-1 [59.0 kB]
Get:17 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal/main amd64 libtimedate-perl all 2.3200-1 [34.0 kB]
Get:18 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal/main amd64 libhttp-date-perl all 6.05-1 [9920 B]
Get:19 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal/main amd64 libio-html-perl all 1.001-1 [14.9 kB]
Get:20 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal/main amd64 liblwp-mediatypes-perl all 6.04-1 [19.5 kB]
Get:21 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal/main amd64 libhttp-message-perl all 6.22-1 [76.1 kB]
Get:22 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal/main amd64 mecab-utils amd64 0.996-10build1 [4912 B]
Get:23 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal/main amd64 mecab-ipadic all 2.7.0-20070801+main-2.1 [6714 kB]
Get:24 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal/main amd64 mecab-ipadic-utf8 all 2.7.0-20070801+main-2.1 [4380 B]
Get:25 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal-updates/main amd64 mysql-server all 8.0.34-0ubuntu0.20.04.1 [9468 B]
Fetched 36.7 MB in 1s (40.0 MB/s)  
Preconfiguring packages ...
Selecting previously unselected package mysql-common.
(Reading database ... 61929 files and directories currently installed.)
Preparing to unpack .../0-mysql-common_5.8+1.0.5ubuntu2_all.deb ...
Unpacking mysql-common (5.8+1.0.5ubuntu2) ...
Selecting previously unselected package mysql-client-core-8.0.
Preparing to unpack .../1-mysql-client-core-8.0_8.0.34-0ubuntu0.20.04.1_amd64.deb ...
Unpacking mysql-client-core-8.0 (8.0.34-0ubuntu0.20.04.1) ...
Selecting previously unselected package mysql-client-8.0.
Preparing to unpack .../2-mysql-client-8.0_8.0.34-0ubuntu0.20.04.1_amd64.deb ...
Unpacking mysql-client-8.0 (8.0.34-0ubuntu0.20.04.1) ...
Selecting previously unselected package libevent-core-2.1-7:amd64.
Preparing to unpack .../3-libevent-core-2.1-7_2.1.11-stable-1_amd64.deb ...
Unpacking libevent-core-2.1-7:amd64 (2.1.11-stable-1) ...
Selecting previously unselected package libevent-pthreads-2.1-7:amd64.
Preparing to unpack .../4-libevent-pthreads-2.1-7_2.1.11-stable-1_amd64.deb ...
Unpacking libevent-pthreads-2.1-7:amd64 (2.1.11-stable-1) ...
Selecting previously unselected package libmecab2:amd64.
Preparing to unpack .../5-libmecab2_0.996-10build1_amd64.deb ...
Unpacking libmecab2:amd64 (0.996-10build1) ...
Selecting previously unselected package mysql-server-core-8.0.
Preparing to unpack .../6-mysql-server-core-8.0_8.0.34-0ubuntu0.20.04.1_amd64.deb ...
Unpacking mysql-server-core-8.0 (8.0.34-0ubuntu0.20.04.1) ...
Setting up mysql-common (5.8+1.0.5ubuntu2) ...
update-alternatives: using /etc/mysql/my.cnf.fallback to provide /etc/mysql/my.cnf (my.cnf) in auto mode
Selecting previously unselected package mysql-server-8.0.
(Reading database ... 62145 files and directories currently installed.)
Preparing to unpack .../00-mysql-server-8.0_8.0.34-0ubuntu0.20.04.1_amd64.deb ...
Unpacking mysql-server-8.0 (8.0.34-0ubuntu0.20.04.1) ...
Selecting previously unselected package libhtml-tagset-perl.
Preparing to unpack .../01-libhtml-tagset-perl_3.20-4_all.deb ...
Unpacking libhtml-tagset-perl (3.20-4) ...
Selecting previously unselected package liburi-perl.
Preparing to unpack .../02-liburi-perl_1.76-2_all.deb ...
Unpacking liburi-perl (1.76-2) ...
Selecting previously unselected package libhtml-parser-perl.
Preparing to unpack .../03-libhtml-parser-perl_3.72-5_amd64.deb ...
Unpacking libhtml-parser-perl (3.72-5) ...
Selecting previously unselected package libcgi-pm-perl.
Preparing to unpack .../04-libcgi-pm-perl_4.46-1_all.deb ...
Unpacking libcgi-pm-perl (4.46-1) ...
Selecting previously unselected package libfcgi-perl.
Preparing to unpack .../05-libfcgi-perl_0.79-1_amd64.deb ...
Unpacking libfcgi-perl (0.79-1) ...
Selecting previously unselected package libcgi-fast-perl.
Preparing to unpack .../06-libcgi-fast-perl_1%3a2.15-1_all.deb ...
Unpacking libcgi-fast-perl (1:2.15-1) ...
Selecting previously unselected package libencode-locale-perl.
Preparing to unpack .../07-libencode-locale-perl_1.05-1_all.deb ...
Unpacking libencode-locale-perl (1.05-1) ...
Selecting previously unselected package libhtml-template-perl.
Preparing to unpack .../08-libhtml-template-perl_2.97-1_all.deb ...
Unpacking libhtml-template-perl (2.97-1) ...
Selecting previously unselected package libtimedate-perl.
Preparing to unpack .../09-libtimedate-perl_2.3200-1_all.deb ...
Unpacking libtimedate-perl (2.3200-1) ...
Selecting previously unselected package libhttp-date-perl.
Preparing to unpack .../10-libhttp-date-perl_6.05-1_all.deb ...
Unpacking libhttp-date-perl (6.05-1) ...
Selecting previously unselected package libio-html-perl.
Preparing to unpack .../11-libio-html-perl_1.001-1_all.deb ...
Unpacking libio-html-perl (1.001-1) ...
Selecting previously unselected package liblwp-mediatypes-perl.
Preparing to unpack .../12-liblwp-mediatypes-perl_6.04-1_all.deb ...
Unpacking liblwp-mediatypes-perl (6.04-1) ...
Selecting previously unselected package libhttp-message-perl.
Preparing to unpack .../13-libhttp-message-perl_6.22-1_all.deb ...
Unpacking libhttp-message-perl (6.22-1) ...
Selecting previously unselected package mecab-utils.
Preparing to unpack .../14-mecab-utils_0.996-10build1_amd64.deb ...
Unpacking mecab-utils (0.996-10build1) ...
Selecting previously unselected package mecab-ipadic.
Preparing to unpack .../15-mecab-ipadic_2.7.0-20070801+main-2.1_all.deb ...
Unpacking mecab-ipadic (2.7.0-20070801+main-2.1) ...
Selecting previously unselected package mecab-ipadic-utf8.
Preparing to unpack .../16-mecab-ipadic-utf8_2.7.0-20070801+main-2.1_all.deb ...
Unpacking mecab-ipadic-utf8 (2.7.0-20070801+main-2.1) ...
Selecting previously unselected package mysql-server.
Preparing to unpack .../17-mysql-server_8.0.34-0ubuntu0.20.04.1_all.deb ...
Unpacking mysql-server (8.0.34-0ubuntu0.20.04.1) ...
Setting up libmecab2:amd64 (0.996-10build1) ...
Setting up mysql-client-core-8.0 (8.0.34-0ubuntu0.20.04.1) ...
Setting up libhtml-tagset-perl (3.20-4) ...
Setting up liblwp-mediatypes-perl (6.04-1) ...
Setting up libencode-locale-perl (1.05-1) ...
Setting up mecab-utils (0.996-10build1) ...
Setting up libevent-core-2.1-7:amd64 (2.1.11-stable-1) ...
Setting up libio-html-perl (1.001-1) ...
Setting up libtimedate-perl (2.3200-1) ...
Setting up mysql-client-8.0 (8.0.34-0ubuntu0.20.04.1) ...
Setting up libfcgi-perl (0.79-1) ...
Setting up liburi-perl (1.76-2) ...
Setting up libevent-pthreads-2.1-7:amd64 (2.1.11-stable-1) ...
Setting up libhttp-date-perl (6.05-1) ...
Setting up mecab-ipadic (2.7.0-20070801+main-2.1) ...
Compiling IPA dictionary for Mecab.  This takes long time...
reading /usr/share/mecab/dic/ipadic/unk.def ... 40
emitting double-array: 100% |###########################################| 
/usr/share/mecab/dic/ipadic/model.def is not found. skipped.
reading /usr/share/mecab/dic/ipadic/Noun.adverbal.csv ... 795
reading /usr/share/mecab/dic/ipadic/Noun.demonst.csv ... 120
reading /usr/share/mecab/dic/ipadic/Noun.csv ... 60477
reading /usr/share/mecab/dic/ipadic/Noun.number.csv ... 42
reading /usr/share/mecab/dic/ipadic/Others.csv ... 2
reading /usr/share/mecab/dic/ipadic/Noun.adjv.csv ... 3328
reading /usr/share/mecab/dic/ipadic/Adverb.csv ... 3032
reading /usr/share/mecab/dic/ipadic/Noun.name.csv ... 34202
reading /usr/share/mecab/dic/ipadic/Filler.csv ... 19
reading /usr/share/mecab/dic/ipadic/Prefix.csv ... 221
reading /usr/share/mecab/dic/ipadic/Noun.org.csv ... 16668
reading /usr/share/mecab/dic/ipadic/Postp-col.csv ... 91
reading /usr/share/mecab/dic/ipadic/Verb.csv ... 130750
reading /usr/share/mecab/dic/ipadic/Suffix.csv ... 1393
reading /usr/share/mecab/dic/ipadic/Postp.csv ... 146
reading /usr/share/mecab/dic/ipadic/Interjection.csv ... 252
reading /usr/share/mecab/dic/ipadic/Auxil.csv ... 199
reading /usr/share/mecab/dic/ipadic/Symbol.csv ... 208
reading /usr/share/mecab/dic/ipadic/Adnominal.csv ... 135
reading /usr/share/mecab/dic/ipadic/Adj.csv ... 27210
reading /usr/share/mecab/dic/ipadic/Noun.nai.csv ... 42
reading /usr/share/mecab/dic/ipadic/Conjunction.csv ... 171
reading /usr/share/mecab/dic/ipadic/Noun.others.csv ... 151
reading /usr/share/mecab/dic/ipadic/Noun.proper.csv ... 27328
reading /usr/share/mecab/dic/ipadic/Noun.place.csv ... 72999
reading /usr/share/mecab/dic/ipadic/Noun.verbal.csv ... 12146
emitting double-array: 100% |###########################################| 
reading /usr/share/mecab/dic/ipadic/matrix.def ... 1316x1316
emitting matrix      : 100% |###########################################| 

done!
update-alternatives: using /var/lib/mecab/dic/ipadic to provide /var/lib/mecab/dic/debian (mecab-dictionary) in auto mode
Setting up mysql-server-core-8.0 (8.0.34-0ubuntu0.20.04.1) ...
Setting up mecab-ipadic-utf8 (2.7.0-20070801+main-2.1) ...
Compiling IPA dictionary for Mecab.  This takes long time...
reading /usr/share/mecab/dic/ipadic/unk.def ... 40
emitting double-array: 100% |###########################################| 
/usr/share/mecab/dic/ipadic/model.def is not found. skipped.
reading /usr/share/mecab/dic/ipadic/Noun.adverbal.csv ... 795
reading /usr/share/mecab/dic/ipadic/Noun.demonst.csv ... 120
reading /usr/share/mecab/dic/ipadic/Noun.csv ... 60477
reading /usr/share/mecab/dic/ipadic/Noun.number.csv ... 42
reading /usr/share/mecab/dic/ipadic/Others.csv ... 2
reading /usr/share/mecab/dic/ipadic/Noun.adjv.csv ... 3328
reading /usr/share/mecab/dic/ipadic/Adverb.csv ... 3032
reading /usr/share/mecab/dic/ipadic/Noun.name.csv ... 34202
reading /usr/share/mecab/dic/ipadic/Filler.csv ... 19
reading /usr/share/mecab/dic/ipadic/Prefix.csv ... 221
reading /usr/share/mecab/dic/ipadic/Noun.org.csv ... 16668
reading /usr/share/mecab/dic/ipadic/Postp-col.csv ... 91
reading /usr/share/mecab/dic/ipadic/Verb.csv ... 130750
reading /usr/share/mecab/dic/ipadic/Suffix.csv ... 1393
reading /usr/share/mecab/dic/ipadic/Postp.csv ... 146
reading /usr/share/mecab/dic/ipadic/Interjection.csv ... 252
reading /usr/share/mecab/dic/ipadic/Auxil.csv ... 199
reading /usr/share/mecab/dic/ipadic/Symbol.csv ... 208
reading /usr/share/mecab/dic/ipadic/Adnominal.csv ... 135
reading /usr/share/mecab/dic/ipadic/Adj.csv ... 27210
reading /usr/share/mecab/dic/ipadic/Noun.nai.csv ... 42
reading /usr/share/mecab/dic/ipadic/Conjunction.csv ... 171
reading /usr/share/mecab/dic/ipadic/Noun.others.csv ... 151
reading /usr/share/mecab/dic/ipadic/Noun.proper.csv ... 27328
reading /usr/share/mecab/dic/ipadic/Noun.place.csv ... 72999
reading /usr/share/mecab/dic/ipadic/Noun.verbal.csv ... 12146
emitting double-array: 100% |###########################################| 
reading /usr/share/mecab/dic/ipadic/matrix.def ... 1316x1316
emitting matrix      : 100% |###########################################| 

done!
update-alternatives: using /var/lib/mecab/dic/ipadic-utf8 to provide /var/lib/mecab/dic/debian (mecab-dictionary) in auto mode
Setting up libhtml-parser-perl (3.72-5) ...
Setting up libhttp-message-perl (6.22-1) ...
Setting up mysql-server-8.0 (8.0.34-0ubuntu0.20.04.1) ...
update-alternatives: using /etc/mysql/mysql.cnf to provide /etc/mysql/my.cnf (my.cnf) in auto mode
Renaming removed key_buffer and myisam-recover options (if present)
mysqld will log errors to /var/log/mysql/error.log
mysqld is running as pid 4655
Created symlink /etc/systemd/system/multi-user.target.wants/mysql.service → /lib/systemd/system/mysql.service.
Setting up libcgi-pm-perl (4.46-1) ...
Setting up libhtml-template-perl (2.97-1) ...
Setting up mysql-server (8.0.34-0ubuntu0.20.04.1) ...
Setting up libcgi-fast-perl (1:2.15-1) ...
Processing triggers for systemd (245.4-4ubuntu3.21) ...
Processing triggers for man-db (2.9.1-1) ...
Processing triggers for libc-bin (2.31-0ubuntu9.9) ...
~~~

- 중간중간 그리고 끝나갈 때
- /etc/mysql/mysql.cnf
- /etc/mysql/my.cnf를 통해서 설정파일들 확인할 것!
<br>
<br>
- 로그는 /var/log/mysql/에 쌓임
<br>
<br>
- /etc/systemd/system/multi-user.target.wants/mysql.service -> /lib/systemd/system/mysql.service 통해서 연결되는 심볼릭 링크를 통한 서비스 활성화/비활성화
<br>
<br>
- 끝나고 서비스 확인 systemctl status mysql
<br>
<br>
- sudo systemctl stop mysql
- sudo systemctl start mysql
- sudo systemctl disable mysql
- sudo systemctl enable mysql

## 서버는 mysqld 데몬 서비스가 동작하고 있는 것
- 접속을 원하면? 접속을 원하는 클라이언트 도구가 있음
- 원래는 별도 설치를 해야 함!
- 하지만, 서버를 설치할 때 함께 설치가 되었음
~~~bash
ubuntu@ip-172-31-42-46:~$ mysql
ERROR 1045 (28000): Access denied for user 'ubuntu'@'localhost' (using password: NO)
~~~
- DB 입장에서도 계정 관리 : ubuntu라는 계정이 존재하지 않는 상황
- 모든 서버들에는 기본 계정이 있음 -> MySQL은 root
~~~bash
ubuntu@ip-172-31-42-46:~$ mysql -u root
ERROR 1698 (28000): Access denied for user 'root'@'localhost'
~~~
- 원격 접속은 보안상 취약하기 때문에 허용되어 있지 않음
~~~bash
ubuntu@ip-172-31-42-46:~$ sudo mysql
~~~
- 관리자로만 접속되는 것이 기본!
~~~sql
-- 계정 확인하기
SELECT User, Host FROM mysql.user;
+------------------+-----------+
| User             | Host      |
+------------------+-----------+
| debian-sys-maint | localhost |
| mysql.infoschema | localhost |
| mysql.session    | localhost |
| mysql.sys        | localhost |
| root             | localhost |
+------------------+-----------+
5 rows in set (0.02 sec)

-- 원하는 사용자 만들어서 추가
-- 계정은 myuser / 비밀번호는 mypassword
CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'mypassword';

-- 권한 설정
-- 실무적으로 모든 DB에 접속 가능하게 하는 것은 좋지 않음
GRANT ALL PRIVILEGES ON *.* TO 'myuser'@'localhost';

-- 설정 잘 되었는지 확인
SELECT User, Host FROM mysql.user;
+------------------+-----------+
| User             | Host      |
+------------------+-----------+
| debian-sys-maint | localhost |
| mysql.infoschema | localhost |
| mysql.session    | localhost |
| mysql.sys        | localhost |
| myuser           | localhost |
| root             | localhost |
+------------------+-----------+

-- myuser가 할 수 있는 일들 확인 가능
SHOW GRANTS FOR 'myuser'@'localhost';
| GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, RELOAD, SHUTDOWN, PROCESS, FILE, REFERENCES, INDEX, ALTER, SHOW DATABASES, SUPER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, REPLICATION SLAVE, REPLICATION CLIENT, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, CREATE USER, EVENT, TRIGGER, CREATE TABLESPACE, CREATE ROLE, DROP ROLE ON *.* TO `myuser`@`localhost`                                                                                                                                                                                                                                                                                                                                                                                     |
| GRANT APPLICATION_PASSWORD_ADMIN,AUDIT_ABORT_EXEMPT,AUDIT_ADMIN,AUTHENTICATION_POLICY_ADMIN,BACKUP_ADMIN,BINLOG_ADMIN,BINLOG_ENCRYPTION_ADMIN,CLONE_ADMIN,CONNECTION_ADMIN,ENCRYPTION_KEY_ADMIN,FIREWALL_EXEMPT,FLUSH_OPTIMIZER_COSTS,FLUSH_STATUS,FLUSH_TABLES,FLUSH_USER_RESOURCES,GROUP_REPLICATION_ADMIN,GROUP_REPLICATION_STREAM,INNODB_REDO_LOG_ARCHIVE,INNODB_REDO_LOG_ENABLE,PASSWORDLESS_USER_ADMIN,PERSIST_RO_VARIABLES_ADMIN,REPLICATION_APPLIER,REPLICATION_SLAVE_ADMIN,RESOURCE_GROUP_ADMIN,RESOURCE_GROUP_USER,ROLE_ADMIN,SENSITIVE_VARIABLES_OBSERVER,SERVICE_CONNECTION_ADMIN,SESSION_VARIABLES_ADMIN,SET_USER_ID,SHOW_ROUTINE,SYSTEM_USER,SYSTEM_VARIABLES_ADMIN,TABLE_ENCRYPTION_ADMIN,TELEMETRY_LOG_ADMIN,XA_RECOVER_ADMIN ON *.* TO `myuser`@`localhost` |
~~~

~~~bash
# 생성한 계정으로 로그인
mysql -u myuser -p
~~~

## 웹 서버에서 다른 서버의 DB 접속
~~~bash
# MySQL 클라이언트 설치
sudo apt install mysql-client-core-8.0

# MySQL 옵션 확인
man mysql

# 서버에 접속
# 같은 local network에 존재하는 서버이기 때문에 사설 ip 넣어주기
mysql -h 172.31.42.46
# SG : 모든 EC2 인스턴스는 보호받고 있어서 바로 접속 안됨(방화벽)
# DB 서버가 사용하는 포트를 알아야 함 : MySQL - 3306
~~~

### DB를 위한 SG 생성
- ssh
- mysql 소스 : 우리의 웹 서버
- 여러개의 서버를 다 넣으려면 어떻게? 웹 서버가 확장이 되거나 또는 WAS 서버가 생겨나거나 등등 우리의 LAN 구간 내의 모든 서버를 허용하려면? : 서브넷의 네트워크 주소!(172.31.0.0/20, 172.31.16.0/20 ...) ➡️ 원래는 AWS VPC에서 확인 가능 - Default VPC 안에 서브넷이 여러개 만들어질 수 있음(IPv4 CIDR) ➡️ LAN을 넣어주면 됨(누구든지 접속 가능 🚨)
- EC2 ➡️ DB 서버 선택 ➡️ 작업 ➡️ 보안 ➡️ 보안그룹 변경
- 기존거 빼고 db 보안그룹 추가

~~~sql
CREATE USER 'myuser'@'172.31.%.%' IDENTIFIED BY 'mypassword';
GRANT ALL PRIVILEGES ON SESAC.* TO 'myuser'@'172.31.%.%';
mysql> SELECT User, Host FROM mysql.user;
+------------------+------------+
| User             | Host       |
+------------------+------------+
| myuser           | 172.31.%.% |
| debian-sys-maint | localhost  |
| mysql.infoschema | localhost  |
| mysql.session    | localhost  |
| mysql.sys        | localhost  |
| myuser           | localhost  |
| root             | localhost  |
+------------------+------------+
7 rows in set (0.00 sec)

mysql> SHOW GRANTS FOR 'myuser'@'172.31.%.%';
+------------------------------------------------------------+
| Grants for myuser@172.31.%.%                               |
+------------------------------------------------------------+
| GRANT USAGE ON *.* TO `myuser`@`172.31.%.%`                |
| GRANT ALL PRIVILEGES ON `SESAC`.* TO `myuser`@`172.31.%.%` |
+------------------------------------------------------------+
~~~
- DBMS 시스템 자체에도 보안 기능이 있음 : 기본 값은 외부 허용이 불허
- /etc/mysql/mysql.conf.d/ 안에 있는 mysqld.cnf 파일을 통해서 외부 접속이 가능하게
~~~zsh
ubuntu@ip-172-31-42-46:/etc/mysql$ cd /etc/mysql/mysql.conf.d/
ubuntu@ip-172-31-42-46:/etc/mysql/mysql.conf.d$ sudo vi mysqld.cnf
~~~
~~~vim
bind-address            = 0.0.0.0 
mysqlx-bind-address     = 0.0.0.0
~~~
- db 재시작해야 함!
~~~zsh
sudo systemctl restart mysql
~~~
- 여기까지하면 웹 서버에서 로그인 가능
~~~zsh
mysql -h 172.31.42.46 -u myuser -p
~~~
~~~sql
mysql> use SESAC
Database changed
mysql> create table user(id INTEGER, username VARCHAR(20));
Query OK, 0 rows affected (0.03 sec)

mysql> insert into user (id, username) values (1, 'user1');
Query OK, 1 row affected (0.00 sec)

mysql> insert into user (id, username) values (2, 'user2');
Query OK, 1 row affected (0.01 sec)

mysql> select * from user;
+------+----------+
| id   | username |
+------+----------+
|    1 | user1    |
|    2 | user2    |
+------+----------+
~~~

### 웹서버에서 새로운 파일로 실습
- mysql-connector-python : mysql이 공식적으로 개발
- pymysql : python에서 만듦
~~~zsh
sudo apt install python3-dev
sudo apt install python3-pip
python3 -mvenv ~/.venv/sesac
source ~/.venv/sesac/bin/activate
pip install mysql-connector-python
pip install pymysql
~~~
- mysql-connector 사용한 예시
~~~python
import mysql.connector

conn = mysql.connector.connect(
    host="172.31.42.46",
    user="myuser",
    password="mypassword",
    database="SESAC",
)

cursor = conn.cursor()

# cursor.execute('''
#   CREATE TABLE IF NOT EXISTS users (
#               id INT AUTO_INCREMENT PRIMARY KEY,
#               username VARCHAR(255),
#               age INT,
#               email VARCHAR(255)
#     )
# ''')

# sql = "INSERT INTO users (username, age, email) VALUES (%s, %s, %s)"
# values = ("John", 25, "john@sesac.com")
# cursor.execute(sql, values)

# values = ("Tom", 27, "tom@sesac.com")
# cursor.execute(sql, values)

# values = ("Sam", 30, "sam@sesac.com")
# cursor.execute(sql, values)

# conn.commit()

sql = "UPDATE users SET age = %s WHERE id = %s"
values = (26, 1)

cursor.execute(sql, values)

conn.commit()

cursor.execute("SELECT * FROM users")

rows = cursor.fetchall()

for row in rows:
    print(row)
~~~

- pymysql 사용한 예시
~~~python
import pymysql

conn = pymysql.connect(
    host="172.31.42.46",
    user="myuser",
    password="mypassword",
    database="SESAC",
    # 딕셔너리로 받아오는 옵션 ⬇️
    cursorclass=pymysql.cursors.DictCursor
)

cursor = conn.cursor()

select_query = "SELECT * FROM users"
cursor.execute(select_query)
users = cursor.fetchall()
print("users:")
for user in users:
    print(user)

~~~