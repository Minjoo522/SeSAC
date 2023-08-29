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
- i : insert (커서 앞)
- a : append (커서 뒤)
- I : 문장 시작
- A : 문장 끝


### 종료 옵션
- :q 그냥 종료
- :q! 강제 종료
- :w 저장(write changes)
- :w! 강제 저장
- :wq 저장하고 종료
- :wq! 강제 저장하고 종료


### command + object
#### 명령 + 무엇에게

- d3w : delete 3 words
- dit : 근접한 태그 안에 있는 모든 데이터를 삭제해라


- d : delete(cut)
- y : yank(copy)
- c : change


- 3w
- 3b : 앞에 있는 세 개의 단어


- aw : a word
- at : a tag
- ap : a paragraph
- as : a sentence


- it : inner, inside tag
- i” : “안에
- ip : paragraph 안에


- . : 이전 명령 반복
- u : un-do, 되감기
- ctrl r : re-do, 앞감기


- daw : 한 단어 삭제
- d2j : 아래 두 문장 삭제
- di{ : 중괄호 안의 정보 다 삭제 / delete inside {
- da” : “까지 **포함**해서 삭제


- ci” : “안 수정 / change


- df( : (까지 찾아서 모든 것 삭제
- dt( : (제외하고 앞까지 삭제
- d/(sh : (sh까지 삭제 / 하면 써치모드로 들어가서 원하는 내용 적으면 됨 vscode 왼쪽 하단에 보임 


- / : 검색모드 진입
- n : 검색 다음 단어
- ? : 거꾸로
- v :  셀렉 모드
- ctrl + v : 블럭 단위 셀렉 가능

### vimtutor로 연습 가능!
