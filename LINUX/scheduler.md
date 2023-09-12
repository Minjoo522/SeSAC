## Scheduling

- 원격지로부터 정보를 가져올 때 수동으로 실행하지 않고 자동으로 돌리면서 원하는 데이터 수집하기
- cron(command run on)이라는 기능을 통해서 스케줄된 잡 처리

~~~bash
ubuntu@ip-172-31-39-149:~$ cd /etc
ubuntu@ip-172-31-39-149:/etc$ systemctl status cron
● cron.service - Regular background program processing daemon
     Loaded: loaded (/lib/systemd/system/cron.service; enabled; vendor preset: enabled)
     Active: active (running) since Tue 2023-09-12 01:15:03 UTC; 38s ago
       Docs: man:cron(8)
   Main PID: 462 (cron)
      Tasks: 1 (limit: 2299)
     Memory: 468.0K
     CGroup: /system.slice/cron.service
             └─462 /usr/sbin/cron -f

Sep 12 01:15:03 ip-172-31-39-149 systemd[1]: Started Regular background program processing daemon.
Sep 12 01:15:03 ip-172-31-39-149 cron[462]: (CRON) INFO (pidfile fd = 3)
Sep 12 01:15:03 ip-172-31-39-149 cron[462]: (CRON) INFO (Running @reboot jobs)
~~~

- cron 설명 / 문법
~~~bash
ubuntu@ip-172-31-39-149:/etc$ cat crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name command to be executed
# ✨ 매시 17분에 cron.hourly 안에 있는 내용 실행
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
# ✨ 매일 아침 6시 25분에 crom.daily 실행
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
# ✨ 매주 일요일 6시 47분에 cron.weekly 실행
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
# ✨ 매달 1일 6시 52분에 cron.mothly 실행
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
~~~

- 시간들이 애매한 이유 🤔 일반적으로 잘 안하는 시간으로 분배시켜 놓은 것
- 매일 3시 정각에 실행 : 0 3 * * * 명령어

~~~bash
# nginx의 로그파일 정리
ubuntu@ip-172-31-39-149:/etc/cron.daily$ cat /etc/logrotate.d/nginx
/var/log/nginx/*.log {
        daily
        missingok
        rotate 14
        compress
        delaycompress
        notifempty
        create 0640 www-data adm
        sharedscripts
        prerotate
                if [ -d /etc/logrotate.d/httpd-prerotate ]; then \
                        run-parts /etc/logrotate.d/httpd-prerotate; \
                fi \
        endscript
        postrotate
                invoke-rc.d nginx rotate >/dev/null 2>&1
        endscript
}
ubuntu@ip-172-31-39-149:/etc/cron.daily$ ls -al /var/log/nginx/
total 48
drwxr-xr-x  2 root     adm     4096 Sep 12 01:15 .
drwxrwxr-x 10 root     syslog  4096 Sep 12 01:15 ..
-rw-r-----  1 www-data adm        0 Sep 12 01:15 access.log
-rw-r-----  1 www-data adm    22234 Sep  4 02:41 access.log.1
-rw-r-----  1 www-data adm      868 Aug 31 03:27 access.log.2.gz
-rw-r-----  1 www-data adm     3951 Aug 30 23:56 access.log.3.gz
-rw-r-----  1 www-data adm        0 Sep 12 01:15 error.log
-rw-r-----  1 www-data adm      819 Sep  4 02:39 error.log.1
~~~

- root만 사용 가능
~~~bash
drwxr-xr-x   2 root root        4096 May 17 21:42 cron.d
drwxr-xr-x   2 root root        4096 May 17 21:42 cron.daily
drwxr-xr-x   2 root root        4096 May 17 21:41 cron.hourly
drwxr-xr-x   2 root root        4096 May 17 21:41 cron.monthly
drwxr-xr-x   2 root root        4096 May 17 21:42 cron.weekly
~~~

- 개별 사용자용
~~~bash
ubuntu@ip-172-31-39-149:~$ crontab -l
no crontab for ubuntu

ubuntu@ip-172-31-39-149:~$ crontab -e
no crontab for ubuntu - using an empty one

Select an editor.  To change later, run 'select-editor'.
  1. /bin/nano        <---- easiest
  2. /usr/bin/vim.basic
  3. /usr/bin/vim.tiny
  4. /bin/ed

Choose 1-4 [1]: 1
crontab: installing new crontab

# m h  dom mon dow   command
30 10 * * * echo "hello world"
~~~

~~~bash
# 참고 : localtime 바꾸기
ubuntu@ip-172-31-39-149:~$ ls -al /etc/localtime
lrwxrwxrwx 1 root root 27 May 17 21:41 /etc/localtime -> /usr/share/zoneinfo/Etc/UTC
ubuntu@ip-172-31-39-149:~$ sudo rm /etc/localtime
ubuntu@ip-172-31-39-149:~$ sudo ln -s /usr/share/zoneinfo/Asia/Seoul /etc/localtime
ubuntu@ip-172-31-39-149:~$ date
Tue Sep 12 10:31:07 KST 2023
~~~

- 실행되지 않는다
- cron이 실행된 결과를 알고싶으면 로그로 ➡️ but 확인 어렵다
- 확인하기 위한 log 파일 따로 만들기!
  
~~~bash
# m h  dom mon dow   command
37 10 * * * echo "hello world" >> /tmp/mycron.txt
~~~

- 이래도 확인이 안된다
- 스크립트 파일 만들기!

~~~bash
ubuntu@ip-172-31-39-149:~$ code my-docs-backup.sh
ubuntu@ip-172-31-39-149:~$ mkdir backup
~~~

~~~sh
📂 my-docs-backup.sh
# !/bin/bash
DATE=$(date +%Y%m%d)
BACKUP_DIR=/home/ubuntu/backup
echo $DATE >> $BACKUP_DIR/backup.txt
~~~

~~~bash
sudo systemctl restart cron
# 재시작하니까 되긴 됨... 원래는 이렇게 할 필요는 없다함
~~~

~~~python
import requests
from bs4 import BeautifulSoup

url = 'http://example.com'

def crawl_website():
  try:
    response = requests.get(url)
    if response.status_code == 200:
      soup = BeautifulSoup(response.text, 'html.parser')
      print('Successfully retrieved the website')
    else:
      print('Failed to get website. Status_code:', response.status_code)
  except Exception as e:
    print('Error', str(e))

if __name__ == "__main__":
  crawl_website()
~~~

~~~sh
📂 my-scrap-job.sh
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)

source /home/ubuntu/.venv/sesac/bin/activate
echo $DATE >> /home/ubuntu/backup/my-scrap.log
python /home/ubuntu/my-scrap.py >> /home/ubuntu/backup/my-scrap.log 2>&1
~~~

- 도커로 실행 시켜도 됨(docker run --rm my-scrap:1.0) 이런식으로!

~~~bash
# m h  dom mon dow   command
0~59 11 * * * /home/ubuntu/my-scrap-job.sh
~~~

- 접근할 수 있는 권한설정 해주어야 함!