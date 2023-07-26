# SQLAlchemy

## filter(), filter_by()

- filter() : 조건 표현식 사용하여 복잡한 필터 작성
  - 매개변수 사용하여 복잡한 필터링
  - 여러개의 필터링 조건, 복잡한 쿼리 작성
- filter_by() : 속성과 값 사용하여 단순한 필터 작성
  - 키워드 인자 사용하여 필터링 조건 지정
  - 여러개의 필터링 조건을 함께 사용하기 어려움
  - 간단한 쿼리인 경우 편리하고 가독성 좋음

```python
from sqlalchemy import and_, or_

users = User.query.filter(and_(User.age >= 30, User.city == 'New York')).all()
```

## with_entities()

- 쿼리 결과에서 가져올 열(속성)을 선택하는데 사용

## join()

- 여러 테이블 간에 조인 수행

## order_by()

- 쿼리 결과 정렬

```python
users = User.query.order_by(User.age.asc()).all()
```

## group_by()

- 쿼리 결과 그룹화

## limit(), offset()

```python
users = User.query.offset(10).limit(5).all()
```

## distinct()

- 중복된 결과를 제거

## db.session.query, User(클래스 명).query

- **_db.session.query_** : 테이블과 컬럼을 직접 참조하지 않음 => 특정 모델이나 여러 모델을 동시에 조작해야 할 때 유용
- **_User(클래스명).query_** : db.session.query(User)과 동일 => 특정 모델에 특화된 쿼리 작성, 코드 간결해짐

## 새로운 행 추가

```python
new_user = User(username = 'alice', email='alice@exaple.com')
db.session.add(new_user)
db.session.commit()
```

## 행 업데이트

```python
user = User.query.filter_by(username = 'alice').first()
if user:
  user.age = 40
  db.session.commit()
```

## 행 삭제

```python
user = User.query.filter_by(username='john_doe').first()
if user:
  db.session.delete(user)
  db.session.commit()
```

## count(func), 결과값 컬럼명 지정(label())

```python
from sqlalchemy import func

result = db.session.query(Post.user_id, func.count(*).label('post_count')).group_by(Post.user_id).all()
```

## 집계함수(avg, count, max, min...)

- scalar()
  - 한 개의 데이터를 가져옴(sqlalchemy.engine.ScalarResult 반환), 여러개일 경우 에러, 없을 경우 None 반환

```python
from sqlalchemy import func

avg_age = db.session.query(func.avg(User.age).label('avg_age')).scalar()
```

## scalar_subquery()

- 하위 쿼리의 결과를 스칼라 값으로 가져와서 메인 쿼리에서 사용할 수 있게 함

```python
from sqlalchemy import func, subquery

sub_query = db.session.query(func.avg(User.age)).scalar_subquery()
users = User.query.filter(User.age > sub_query).all()
```

## having()

```python
from sqlalchemy import func

result = db.session.query(User.city, func.avg(User.age).label('avg_age')).group_by(User.city).having(func.avg(User.age) > 30).all()
```
