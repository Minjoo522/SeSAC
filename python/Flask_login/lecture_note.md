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
