# Flask-Login

## 데코레이터

- 확장해서 꾸미는 것(annotation)
- 편리한 기능을 제공함

## @login_required

- 로그인된 사용자인지 검증하고, 로그인이 되어있지 않으면 자동으로 로그인 페이지로 redirect 시켜줌

# user_loader

- User.get()의 리턴 값인 객체를 추출!

```python
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
```

# migration

- DB의 변경사항을 트랙킹하는 모듈을 추가해 줌

```bash
pip install Flask-Migrate
```

```python
from flask_migrate import Migrate

# DB 마이그레이션 모듈 로딩
migrate = Migrate(app, db)
```

```bash
flask db init
```

- ⬆️ 최초 1회 실행
- migrations라는 폴더 생성됨(삭제해도 상관 없고, 다시 필요한 경우 flask db init 실행하면 됨)
- 일반적으로는 수동으로 함
- 현재 상태에 대한 싱크 맞추기

```bash
flask db migrate -m "나의 변경 사유"
flask db upgrade
```

- 변경 사유 작성
- 실제 db 업그레이드
- 데이터베이스 롤백을 위해 flask db downgrade 명령도 사용할 수 있음

```bash
flask db stamp head
```

- 구버전을 현재의 최신버전으로 강제 설정

```bash
flask db history
```

- 기록 보기

## 마이그레이션 로직

### 예시

1. Table A/B => C/D
2. 테이블에 컬럼을 추가(삭제)
3. Table C/D가 생성, (A/B 삭제)

### 문제가 생길 때

1. Table A/B => C/D
2. 테이블에 컬럼을 추가(삭제)
3. 데이터의 이관 진행(문제가 될 수 있는 것들이 발생)
   - A/B 이메일 unique 체크가 없었음
   - 자동으로 어떻게?
4. Table C/D가 생성, (A/B 삭제)

### DBA나 경험 있는 개발자들

1. 백업을 한다(**_중요_**)
2. 수동으로 작업을 한다
   - Transaction 시작(일관성/무결성/동시성 보장을 필요)
   - 중간 작업 수행
   - if 성공, Transaction 커밋/종료
   - if 실패, Transaction 롤백/종료
