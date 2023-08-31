# Docker 🐳

> - [🐳 수업 내용 🐳](https://github.com/lovehyun/tutorial-docker)

## 시대별 배포 유형
- Traditional Deployment
- Virtualized Deployment
  - 운영체제 깔아야 함 : 무거움!
  - overhead
- Container Deployment
  - 샌드박스
  - 스마트폰 처럼 하나의 기기에 여러 앱을 깔 수 있음

## 컨테이너의 장점
- 기민한 애플리케이션 생성과 배포
  - 개발할 때 문제가 없었으면 그대로 이미지를 만들어서 다른 PC, 서버에서도 문제없이 사용할 수 있도록
- CI/CD
- 개발 / 운영 관심사 분리
- 개발, 테스팅 및 운영 환경에 걸친 일관성
- 클라우드 및 OS 배포판 간 이식성
- 애플리케이션 중심 관리
- 느슨하고 커플되고 분산되고 유연하며 자유로운 마이크로 서비스
- 자원 격리
- 자원 사용량

## Docker : 컨테이너 기술을 실체화 해둔 도구
- 컨테이너 기술 : 리눅스 커널에 기본적으로 있음
- 컨테이너 생태계(eco system)를 잘 만들어 둬서 뜸!
- 윈도우, 맥북에서 Docker가 도는 것이 아닌, 윈도우, 맥북의 리눅스 커널에서 도는 것임

## 이미지(Image)
- 컨테이너 실행에 필요한 파일과 설정값 포함하고 있는 것으로 상태값을 가지지 않고 변하지 않음(Immutable)
- 이미지를 실행하는 것이 컨테이너!(예시 : 객체지향 class = image, instantiation 해서 running = container하는 느낌)
  - 하나의 이미지로 여러 컨테이너를 띄울 수 있음(예시 : 객체지향 class 하나로 여러개의 instance를 만드는 것과 비슷한 느낌)
- public / private한 docker가 있음

> - [🐳 dockerhub](https://hub.docker.com/)

## 도커 설치 및 상태 확인
~~~bash
sudo apt install docker.io -y

# 도커 상태 확인
systemctl status docker
docker version

Client:
 Version:           20.10.25
 API version:       1.41
 Go version:        go1.20.3
 Git commit:        20.10.25-0ubuntu1~20.04.2
 Built:             Thu Aug 10 20:14:50 2023
 OS/Arch:           linux/amd64
 Context:           default
 Experimental:      true
Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/version": dial unix /var/run/docker.sock: connect: permission denied

# 오류 ➡️ sudo로 확인
ubuntu@ip-172-31-39-149:~$ sudo docker version
Client:
 Version:           20.10.25
 API version:       1.41
 Go version:        go1.20.3
 Git commit:        20.10.25-0ubuntu1~20.04.2
 Built:             Thu Aug 10 20:14:50 2023
 OS/Arch:           linux/amd64
 Context:           default
 Experimental:      true

Server:
 Engine:
  Version:          20.10.25
  API version:      1.41 (minimum version 1.12)
  Go version:       go1.20.3
  Git commit:       20.10.25-0ubuntu1~20.04.2
  Built:            Thu Aug  3 18:03:37 2023
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.7.2
  GitCommit:
 runc:
  Version:          1.1.7-0ubuntu1~20.04.1
  GitCommit:
 docker-init:
  Version:          0.19.0
  GitCommit:

# sudo docker라는 명령어를 사용하는 것은 보안적으로 좋지 않음
# ➡️ 사용자를 docker 그룹에 넣기
sudo usermod -aG docker ubuntu
# ➡️ 다시 로그인 필요
~~~

## 도커 hello-world
~~~zsh
docker run hello-world
~~~

## 도커 image
~~~bash
ubuntu@ip-172-31-39-149:~$ docker images
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
hello-world   latest    9c7a54a9a43c   3 months ago   13.3kB

docker run docker/whalesay cowsay "Hello World!"
ubuntu@ip-172-31-39-149:~$ docker run docker/whalesay cowsay "Hello SESAC!"
 ______________
< Hello SESAC! >
 --------------
    \
     \
      \
                    ##        .
              ## ## ##       ==
           ## ## ## ##      ===
       /""""""""""""""""___/ ===
  ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ /  ===- ~~~
       \______ o          __/
        \    \        __/
          \____\______/

# 두 개의 이미지가 받아져 있음
ubuntu@ip-172-31-39-149:~$ docker images
REPOSITORY        TAG       IMAGE ID       CREATED        SIZE
hello-world       latest    9c7a54a9a43c   3 months ago   13.3kB
docker/whalesay   latest    6b362a9f73eb   8 years ago    247MB

# active하게 떠 있는 컨테이너만 보여줌
ubuntu@ip-172-31-39-149:~$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

# 종료된 것까지 보기
ubuntu@ip-172-31-39-149:~$ docker ps -a
CONTAINER ID   IMAGE             COMMAND                  CREATED              STATUS                          PORTS     NAMES
574111b8c690   docker/whalesay   "cowsay 'Hello SESAC…"   About a minute ago   Exited (0) About a minute ago             loving_johnson
80232d1fc9a5   docker/whalesay   "cowsay 'Hello World…"   2 minutes ago        Exited (0) 2 minutes ago                  clever_einstein
1b1693e84f63   hello-world       "/hello"                 6 minutes ago        Exited (0) 6 minutes ago                  charming_nobel
~~~

- docker run = docker pull + docker create + docker start
- docker pull <이름>:<태그>
- docker pull ubuntu:latest ➡️ latest가 항상 최신을 의미하지는 않음(그냥 태그)
~~~bash
# pull
docker pull ubuntu:16.04

# 컨테이너 생성
docker create ubuntu:16.04
# 컨테이너 해시값
3c414df2a29c11408415939c0bb7dd340e3b0f05e25cbfb58223c4f5021cdb21

ubuntu@ip-172-31-39-149:~$ docker ps -a
CONTAINER ID   IMAGE             COMMAND                  CREATED          STATUS                      PORTS     NAMES
3c414df2a29c   ubuntu:16.04      "/bin/bash"              48 seconds ago   Created                               friendly_kowalevski
574111b8c690   docker/whalesay   "cowsay 'Hello SESAC…"   10 minutes ago   Exited (0) 10 minutes ago             loving_johnson
80232d1fc9a5   docker/whalesay   "cowsay 'Hello World…"   11 minutes ago   Exited (0) 11 minutes ago             clever_einstein
1b1693e84f63   hello-world       "/hello"                 15 minutes ago   Exited (0) 15 minutes ago             charming_nobel
# 컨테이너 실행(컨테이너 아이디 넣기)
docker start 3c414df2a29c
# 실제로 기대하는 것은 bash(프롬포트)를 띄우는 것을 바라지만 그냥 실행하고 끝남

# -i : interactive
# -t : tty(터미널)
docker run -it ubuntu:16.04
# 도커 컨테이너 안에 잠시 들어와 있는 상태가 됨
docker run -it ubuntu:16.04 bash
# 기본값이 /bin/bash이기 때문에 bash를 넣어주지 않아도 bash가 실행됨
# 이렇게 실행할 때마다 계속 새로운 컨테이너가 만들어짐

# 이전에 실행했던(멈춰있는) 컨테이너 다시 들어가기
# exit된 상태로 start로 시작!
docker start -i 7ac8e

# 이런 식으로 명령어 실행도 가능
docker run -it ubuntu:20.04 ls -al
~~~

- 컨테이너 안은 완전히 격리된 별도의 공간
~~~bash
# 컨테이너 안은 완전히 다른 환경임을 아래와 같이 확인 가능
root@7ac8e58e0f67:/# cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-timesync:x:100:102:systemd Time Synchronization,,,:/run/systemd:/bin/false
systemd-network:x:101:103:systemd Network Management,,,:/run/systemd/netif:/bin/false
systemd-resolve:x:102:104:systemd Resolver,,,:/run/systemd/resolve:/bin/false
systemd-bus-proxy:x:103:105:systemd Bus Proxy,,,:/run/systemd:/bin/false
_apt:x:104:65534::/nonexistent:/bin/false
root@7ac8e58e0f67:/# hostname
7ac8e58e0f67
~~~

## docker ps
- 리눅스 ps : process
- 직관적이지 않아서 ➡️ docker container ls로 명령어 변경함
~~~bash
ubuntu@ip-172-31-39-149:~$ docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
ubuntu@ip-172-31-39-149:~$ docker container ls -a
CONTAINER ID   IMAGE             COMMAND                  CREATED          STATUS                          PORTS     NAMES
7ac8e58e0f67   ubuntu:16.04      "bash"                   6 minutes ago    Exited (0) About a minute ago             eager_black
508efacdd551   ubuntu:16.04      "/bin/bash"              8 minutes ago    Exited (0) 7 minutes ago                  musing_agnesi
3c414df2a29c   ubuntu:16.04      "/bin/bash"              16 minutes ago   Exited (0) 14 minutes ago                 friendly_kowalevski
574111b8c690   docker/whalesay   "cowsay 'Hello SESAC…"   26 minutes ago   Exited (0) 26 minutes ago                 loving_johnson
80232d1fc9a5   docker/whalesay   "cowsay 'Hello World…"   26 minutes ago   Exited (0) 26 minutes ago                 clever_einstein
1b1693e84f63   hello-world       "/hello"                 30 minutes ago   Exited (0) 30 minutes ago                 charming_nobel
~~~

## 컨테이너 지우기
- 아이디 일부만 쳐도(partial) 지워짐
- NAME 쳐도 지워짐(랜덤으로 만들어진 이름)
~~~bash
ubuntu@ip-172-31-39-149:~$ docker rm 1b1693e84f63
1b1693e84f63

# 이름은 무조건 full-match 되어야함
# tab 완성 가능
docker rm loving_johnson
~~~

### 컨테이너 전체 지우기
- docker ps -aq로 id만 뽑아서 확인 가능
~~~bash
docker ps -aq
7ac8e58e0f67
508efacdd551
3c414df2a29c

# 인자로 넘겨서 한 번에 지울 수 있음
docker rm $(docker ps -aq)

# 돌아가고 있는 컨테이너도 강제로 지우기
docker rm -f $(docker ps -aq)
~~~

## 이미지 지우기
- docker rmi
~~~bash
docker rmi ubuntu:16.04
docker rmi $(docker images -q)
~~~

## 웹서버 실행
~~~bash
# 아래처럼 입력하면 nginx:latest가 실행되는 것
docker run nginx

Unable to find image 'nginx:latest' locally
latest: Pulling from library/nginx
52d2b7f179e3: Pull complete
fd9f026c6310: Pull complete
055fa98b4363: Pull complete
96576293dd29: Pull complete
a7c4092be904: Pull complete
e3b6889c8954: Pull complete
da761d9a302b: Pull complete
Digest: sha256:104c7c5c54f2685f0f46f3be607ce60da7085da3eaa5ad22d3d9f01594295e9c
Status: Downloaded newer image for nginx:latest
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2023/08/31 03:06:09 [notice] 1#1: using the "epoll" event method
2023/08/31 03:06:09 [notice] 1#1: nginx/1.25.2
2023/08/31 03:06:09 [notice] 1#1: built by gcc 12.2.0 (Debian 12.2.0-14)
2023/08/31 03:06:09 [notice] 1#1: OS: Linux 5.15.0-1036-aws
2023/08/31 03:06:09 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2023/08/31 03:06:09 [notice] 1#1: start worker processes
2023/08/31 03:06:09 [notice] 1#1: start worker process 29
2023/08/31 03:06:09 [notice] 1#1: start worker process 30

# 데몬화 시켜서 돌려라
ubuntu@ip-172-31-39-149:~$ docker run -d nginx
03ac310ee443ee1ca03c3ddbff9008558316eaec6d4e99e64d9e16dd21dda07d

# 실행하는게 종료하는 건데 우리가 종료를 원치 않으면
# -it

# 실행하는게 forground process 상태로 있으면
# -d 돌아라(종료되는게 아니라 active하게 running 중)

# 돌고 있는 컨테이너 안에 들어가 보려면?
docker exec -it <컨테이너id> bash
# bash가 있는 컨테이너도 있음!
# 없으면 sh(shell)
# 그냥 실행
docker exec <컨테이너id> ls -l
docker exec <컨테이너id> ps
docker exec <컨테이너id> curl localhost
~~~

## 격리된 공간에서 연결
~~~bash
docker run -d nginx
# -p publish (포트 바인딩)

# <호스트 포트>:<컨테이너 포트>
docker run -d -p 80:80 nginx


root@03ac310ee443:/etc/nginx# cat nginx.conf

user  nginx;
worker_processes  auto;

error_log  /var/log/nginx/error.log notice;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}h


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    include /etc/nginx/conf.d/*.conf;
}
root@03ac310ee443:/etc/nginx# cd conf.d
root@03ac310ee443:/etc/nginx/conf.d# cat default.conf
server {
    listen       80;
    listen  [::]:80;
    server_name  localhost;

    #access_log  /var/log/nginx/host.access.log  main;

    location / {
        root   /usr/share/nginx/html;
        index  index.html index.htm;
    }

    #error_page  404              /404.html;

    # redirect server error pages to the static page /50x.html
    #
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }

    # proxy the PHP scripts to Apache listening on 127.0.0.1:80
    #
    #location ~ \.php$ {
    #    proxy_pass   http://127.0.0.1;
    #}

    # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
    #
    #location ~ \.php$ {
    #    root           html;
    #    fastcgi_pass   127.0.0.1:9000;
    #    fastcgi_index  index.php;
    #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
    #    include        fastcgi_params;
    #}

    # deny access to .htaccess files, if Apache's document root
    # concurs with nginx's one
    #
    #location ~ /\.ht {
    #    deny  all;
    #}
}

root@03ac310ee443:/etc/nginx/conf.d# find / -name index.html
/usr/share/nginx/html/index.html
find: '/proc/29/task/29/fdinfo': Permission denied
find: '/proc/29/map_files': Permission denied
find: '/proc/29/fdinfo': Permission denied
find: '/proc/30/task/30/fdinfo': Permission denied
find: '/proc/30/map_files': Permission denied
find: '/proc/30/fdinfo': Permission denied
root@03ac310ee443:/etc/nginx/conf.d# find / -name index.html 2> /dev/null
/usr/share/nginx/html/index.html

cat /etc/*-release
apt update
apt install vim
~~~

~~~bash
# 기존에 웹 서버에 있었던 nginx 때문에 실행 안되기 때문에, nginx 꺼주기
sudo systemctl stop nginx
sudo systemctl disabel nginx

docker run -d -p 80:80 nginx
docker run -d -p 81:80 nginx
docker run -d -p 82:80 nginx

docker exec -it 7e869023568e bash
# 실행 중인 컨테이너에 들어가짐
cd /usr/share/nginx/html
# 관리자 계정으로 들어갔기 때문에 sudo 없어도 됨
apt update
apt install vim
echo "<h1>welcome to nginx1</h1>" > index.html

# 각각 들어가서 하나씩 설정해 주면 공용ip:포트번호 에서 다른 화면 확인 가능함!
# 단, aws 사용하는 경우 SG 추가 해주어야함
~~~

## DATABASE
~~~bash
docker run -d mysql

ubuntu@ip-172-31-39-149:~$ docker ps -a
CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS                          PORTS     NAMES
0f684f933cea   mysql     "docker-entrypoint.s…"   About a minute ago   Exited (1) About a minute ago             festive_poitras
# 정상 종료(0) / 얘는 정상 종료되지 않음!
~~~
- 도커를 디버깅하는 방법
  1. 들어가서 본다(docker exec -it <cont-id> bash)
  2. 로그를 본다(docker logs <cont-id>)

~~~bash
ubuntu@ip-172-31-39-149:~$ docker logs 0f684f933cea
2023-08-31 05:06:43+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.1.0-1.el8 started.
2023-08-31 05:06:43+00:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
2023-08-31 05:06:43+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.1.0-1.el8 started.
2023-08-31 05:06:43+00:00 [ERROR] [Entrypoint]: Database is uninitialized and password option is not specified
    You need to specify one of the following as an environment variable:
    - MYSQL_ROOT_PASSWORD
    - MYSQL_ALLOW_EMPTY_PASSWORD
    - MYSQL_RANDOM_ROOT_PASSWORD
# 계정 초기화가 되지 않아서 접속이 안됨
# 기본 계정은 root로 있으나 기본 암호가 없다!
# 도커의 환경변수를 통해서 이런 다양한 variable 변수값들을 설정할 수 있게 되어있다.
# -e라는 옵션을 사용함
docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=sesac1234 mysql
# MYSQL_ALLOW_EMPTY_PASSWORD=true or 1도 가능
# MYSQL_RANDOM_ROOT_PASSWORD도 가능
mysql -u root -p
# 부팅될 때까지 시간이 좀 걸려서 바로 안될 수도 있음
mysql -h 127.0.0.1 -u root -p
~~~
- 상태를 가지고 있지 않는 것이 컨테이너화를 하기에 좋은 애플리케이션임(DB 같은 경우 상태가 날아갈 수 있으므로 컨테이너화하기 좋지 않음)
- 별도의 저장소에 컨텐츠(상태=state)를 저장하는 공간이 필요하다
  1. 호스트패스 바인딩
     1. -v라는 옵션으로 호스트패스(path=경로=디렉토리)를 연결
~~~bash
# -v 호스트경로:컨테이너경로
# 호스트경로 = full path
# 상대 경로 안됨! 무조건 절대경로
# 저장소 찾기!
# dockerhub에서 설명 보고 찾기
docker run -d -p 3306:3306 -e MYSQL_ALLOW_EMPTY_PASSWORD=1 -v /home/ubuntu/my-database:/var/lib/mysql mysql

# 컨테이너 삭제하고 다시 똑같은 경로에 바인딩하면 데이터 그대로 살아있음

# 문제
# 소유주가 systemd-coredump로 되어있고 내가 제어할 수 없음
# 여러명이 사용해야 하는데 나의 home 폴더에 있어서 다른 사람이 제어할 수 없음
drwxr-xr-x 8 systemd-coredump root   4096 Aug 31 05:36 my-database

# 컨테이너 내부 : mysql:x:999:999::/var/lib/mysql:/bin/bash
# 내 서버 :systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin 여서 systemd-coredump
~~~
  2. 볼륨 바인딩 ✨ 실무적으로 많이 사용함
~~~bash
docker volume create my-sesac-db
docker run -d -p 3306:3306 -e MYSQL_ALLOW_EMPTY_PASSWORD=1 -v my-sesac-db:/var/lib/mysql mysql
~~~

## docker info
~~~bash
docker info
# /var/lib/docker
# 모든 정보 확인 가능

ubuntu@ip-172-31-39-149:~$ sudo ls -al /var/lib/docker
total 52
drwx--x--- 13 root root 4096 Aug 31 01:49 .
drwxr-xr-x 46 root root 4096 Aug 31 01:49 ..
drwx--x--x  4 root root 4096 Aug 31 01:49 buildkit
drwx--x---  3 root root 4096 Aug 31 05:49 containers
drwx------  3 root root 4096 Aug 31 01:49 image
drwxr-x---  3 root root 4096 Aug 31 01:49 network
drwx--x--- 28 root root 4096 Aug 31 05:49 overlay2
drwx------  4 root root 4096 Aug 31 01:49 plugins
drwx------  2 root root 4096 Aug 31 01:49 runtimes
drwx------  2 root root 4096 Aug 31 01:49 swarm
drwx------  2 root root 4096 Aug 31 05:06 tmp
drwx------  2 root root 4096 Aug 31 01:49 trust
drwx-----x  6 root root 4096 Aug 31 05:45 volumes

# /var/lib
# 루트에 있음 - 공간이 적음
# 실무적으로 EBS 새로 생성하고 /data -> EBS 연결(mount)
# /data/docker or /data/docker_dir등 폴더 만들고 변경 시켜주면 root 공간 사용하지 않고 가능

docker system df
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          5         1         1.035GB   457.4MB (44%)
Containers      1         1         6B        0B (0%)
Local Volumes   4         1         628.1MB   418.7MB (66%)
Build Cache     0         0         0B        0B
# 볼륨을 만들고 관리하지 않으면 디스크 공간이 낭비될 수 있음

# 볼륨 지우고 디스크 공간 확인
ubuntu@ip-172-31-39-149:~$ docker volume rm my-sesac-db
my-sesac-db
ubuntu@ip-172-31-39-149:~$ docker system df
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          5         0         1.035GB   1.035GB (100%)
Containers      0         0         0B        0B
Local Volumes   3         0         418.7MB   418.7MB (100%)
Build Cache     0         0         0B        0B

ubuntu@ip-172-31-39-149:~$ docker volume

Usage:  docker volume COMMAND

Manage volumes

Commands:
  create      Create a volume
  inspect     Display detailed information on one or more volumes
  ls          List volumes
  prune       Remove all unused local volumes
  rm          Remove one or more volumes

Run 'docker volume COMMAND --help' for more information on a command.

# 쓰이지 않는 볼륨 다 지워줌
ubuntu@ip-172-31-39-149:~$ docker volume prune
WARNING! This will remove all local volumes not used by at least one container.
Are you sure you want to continue? [y/N] y
Deleted Volumes:
b784248a3816ae2029d3343e9b71d644dba0d14fe9b0b876d50eb5410d03ae77
7a5e8b027e4f8b611ff67267c2ec5af82841bc2a10819094678cf760a777fc10
a9c3782473e23ff5b9c152bd4dc713f8c3885cc81b427ccaea113434e2ddfdd4

Total reclaimed space: 418.7MB

ubuntu@ip-172-31-39-149:~$ docker volume ls
DRIVER    VOLUME NAME
~~~

## --name
- --name my-db 이런식으로 쓰면 이름 정할 수 있음
~~~bash
ubuntu@ip-172-31-39-149:~$ docker run -d -p 80:80 --name my-web nginx
b0091606482f2778567f451d9c0dca31d7054ef5682d6782f84b298fb9dbb1ac
ubuntu@ip-172-31-39-149:~$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                               NAMES
b0091606482f   nginx     "/docker-entrypoint.…"   6 seconds ago   Up 5 seconds   0.0.0.0:80->80/tcp, :::80->80/tcp   my-web
~~~