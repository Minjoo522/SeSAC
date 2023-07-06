# 연산자

```
SELECT name, num, price, num*price AS value FROM product;
# 변수로 연산에 대한 값 이름 지정 가능

SELECT *, price - discount FROM product;
# 원하는 필드 만들기
```

## WHEN, ELSE

```
SELECT name, result,
CASE
 WHEN result > 80 THEN 'PASS'
 WHEN result > 70 THEN 'Check'
 ELSE 'FAIL'
END AS judgement
FROM exam;
```

## COUNT, GROUP BY

- SELECT시 COUNT하는 습관을 들이는 것이 좋다
- m : 2, f : 2명인 경우

```
SELECT gender, COUNT(*) FROM user GROUP BY gender;
SELECT city, COUNT(*) FROM user GROUP BY city HAVING COUNT(*) >= 2;
```

- GROUP BY 앞에 조건을 걸 때는 WHERE, 뒤에 조건을 걸 때는 HAVING
