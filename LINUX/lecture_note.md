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
- ls(list) : 파일 보기
- ls -l(long) : 파일 상세 정보까지 보기
- ls -a(all) : 숨김파일(hidden)까지 봄(.으로 출발하는 파일이나 폴더)
- ls -a -l / ls -al / ls -la 등처럼 사용도 가능
- touch <파일> : 파일 만들기(원래 목적은 파일 지금 내가 수정했다고 설정) / touch hello.txt
- cat <파일> : concatenate(연결) / 파일 내용 보기 / 파일과 터미널을 연결해준다
- more <파일> : 페이징 처리 되어 파일 내용 보임 / 스페이스바로 페이지 이동 가능
- less <파일> : 좌우 위 아래 이동 가능
- rm <파일> : remove / 지우기
  - rm hello* 같은 식으로도 지울 수 있음
- rm -r : 반복적으로 편하게 지움 / 복구 불가 / 사용시 주의❗️
- mkdir <폴더> : make directory / 폴더 만들기
- rmdir <폴더> : remove directory / 폴더 지우기
- . : current directory
- .. : parent directory
- pwd : 현재 나의 working directory(나의 위치)
- $ : 프롬푸트(사용자의 입력을 나타내는 기호), 프롬푸트를 잘 설정하면 사용자 / 호스트 / 디렉토리 $ 처럼 보이게 만들 수도 있음
  - PS1 = prompt statement one
- ~ : 나의 홈
- / : 루트
- ll : ls -l을 alias로 만들어 둔 것(OS 배포판마다 차이가 큼 ➡️ 이거는 우분투에만 기본적으로 있음)
- cd - : 바로 이전 위치로 돌아가기
- cp <출발지> <목적지> : copy / 파일 복사 / 있는 파일에 복사하는 경우 over write됨 / 파일 ➡️ 폴더 : 폴더 안으로 파일이 복사됨
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
- which : 실행하고자 하는 프로그램이 어디에 설치되어 있는지, 실행되어 있는지 경로 확인
- whereis : 어디에 있는지 다 보여줌!

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

# VIM
- 1976 빌조이가 vi를 만듦(텍스트 에디터)
- 1991 Bram M vi IMproved 만듦
- → 키보드만으로 빠르게 타이핑 가능


- vim 파일명 → 파일 읽기


- 명령모드 : 처음 / esc


- h,j,k,l : 왼 하 상 우


- 0 : 문장 제일 앞
- $ : 문장 제일 뒤
- w : word, 단어
- b : backward 단어


- 3w : 3단어씩 이동
- ctrl u : 위로 스크롤링
- ctrl d : 아래로 스크롤링
- { : 문단 시작
- } : 문단 끝


- H : 화면 위
- M : 화면 중간
- L : 화면 끝


- gg : 파일 앞
- G : 파일 끝


- 20G : 20번째 줄로 이동
- x : 커서 아래 글자 삭제
- dd: 문장 삭제
- yy : 문장 복사
- p : 붙여 넣기
- *p : 클립보드 붙여넣기


- 입력모드 : i / 
- i: insert (커서 앞)
- a: append (커서 뒤)
- I : 문장 시작
- A: 문장 끝


### 종료 옵션
- :q 그냥 종료
- :q! 강제 종료
- :w 저장
- :w! 강제 저장
- :wq 저장하고 종료
- :wq! 강제 저장하고 종료


### command + object
- 명령 + 무엇에게
- d 3w : delete 3 words
- d it : 근접한 태그 안에 있는 모든 데이터를 삭제해라
- d : delete(cut)
- y : yank(copy)
- c : change
- 3w
- 3b
- aw : a word
- at : a tag
- ap : a paragraph
- as : a sentence
- it : inner, inside tag
- i” : “안에
- ip : paragraph 안에
- ⇒ 반복 가능
- . : 이전 명령 반복
- u : un-do, 되감기
- ctrl r : re-do, 앞감기
- d2j : 아래 두 문장 삭제
- di{ : 중괄호 안의 정보 다 삭제
- da” : “까지 포함해서 삭제
- ci” : “안 수정
- d 잘라내고 p 붙여넣기 가능
- df( : (까지 찾아서 모든 것 삭제
- dt( : (제외하고 앞까지 삭제
- d/(sh : (sh까지 삭제 / 하면 써치모드로 들어가서 원하는 내용 적으면 됨 vscode 왼쪽 하단에 보임 
- / : 검색모드 진입
- n : 검색 다음 단어
- ? : 거꾸로
- v :  셀렉 모드
- ctrl + v : 블럭 단위 셀렉 가능

### vimtutor로 연습 가능!