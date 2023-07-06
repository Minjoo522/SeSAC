# CRUD

- 테이블 생성 :

```
CREATE TABLE user ( id INTEGER, name TEXT );
# 멀티라인으로 쳐도 됨
```

- 테이블 내용 조회 :

```
SELECT * FROM user;
```

- 데이터 삽입 :

```
INSERT INTO user VALUES(4, "lee");
```

- WHERE clause(WHERE 절)

```
SELECT * FROM people WHERE age=21
SELECT * FROM people WHERE gender="F" AND age=19;
SELECT * FROM people WHERE age BETWEEN 20 AND 27;
SELECT * FROM people WHERE age BETWEEN 20 AND 27 ORDER BY age DESC;
SELECT * FROM people WHERE age IN (21, 23);
SELECT * FROM people WHERE first_name LIKE "%first%";
SELECT * FROM people WHERE first_name LIKE "first*";
SELECT * FROM people WHERE first_name NOT LIKE "%3%";
```

- 테이블 삭제 :

```
DROP TABLE user;
```

- ORDER BY

```
SELECT * FROM people ORDER BY age ASC;
SELECT * FROM people ORDER BY age DESC;
```

- LIMIT

```
SELECT * FROM people LIMIT 2 OFFSET 2;
```

- DISTINCT : 중복 제거

```
SELECT DISTINCT gender FROM people;
```

- 갱신(Update) :

```
UPDATE people SET first_name="first2222" WHERE first_name="first2";
```

- 삭제(Delete) :

```
DELETE FROM people WHERE age=21;
```
