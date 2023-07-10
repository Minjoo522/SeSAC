1. 특정 사용자(한 명 이름 잡아서(UUID))가 구매한 주문 내역(order)을 모두 가져오시오.

```sql
SELECT U.Id, U.Name, O.Id, O.OrderAt
FROM user U
JOIN orders O
ON U.Id = O.UserId
WHERE UserId = "0a234508-1a52-4339-9e49-9c3dcf3d8d33";
```

- 2-0. 특정 사용자가 주문한 상점명과 상품명을 모두 출력하시오.

```sql
SELECT U.ID, U.Name, O.OrderAt, S.Name AS StoreName, I.Name AS ItemName
FROM user U
JOIN orders O
ON U.Id = O.UserId
JOIN store S
ON O.StoreId = S.Id
JOIN orderitem OI
ON O.Id = OI.OrderId
JOIN item I
ON OI.ItemId = I.Id
WHERE U.Id = "0a234508-1a52-4339-9e49-9c3dcf3d8d33";
```

2. 특정 사용자(한 명 이름 잡아서(UUID))가 구매한 주문 내역의 상품명을 모두 가져오시오(유닉한 상품명).

```sql
SELECT DISTINCT I.Name
FROM item I
JOIN orderitem OI
ON I.Id = OI.ItemId
JOIN orders O
ON O.Id = OI.OrderId
JOIN user U
ON O.UserId = "0a234508-1a52-4339-9e49-9c3dcf3d8d33";
```

3. 특정 사용자가 구매한 매출액의 합산을 구하시오.

```sql
SELECT U.Name, SUM(I.UnitPrice)
FROM user U
JOIN orders O ON U.Id = O.UserId
JOIN orderitem OI ON OI.OrderId = O.Id
JOIN item I ON I.Id = OI.ItemId
WHERE U.Id = "0a234508-1a52-4339-9e49-9c3dcf3d8d33";
```

4. 상점별 월간 통계(매출액)을 구하시오.

```sql
SELECT DISTINCT S.Name, SUBSTR(O.OrderAt, 6, 2) AS "ordermonth", AVG(I.UnitPrice)
FROM store S
JOIN orders O
ON S.Id = O.StoreId
JOIN orderitem OI
ON O.Id = OI.OrderId
JOIN item I
ON OI.ItemId = I.Id
GROUP BY S.Name, ordermonth;
```

5. 연령대별 고객 수

```sql
SELECT CASE WHEN Age < 20 THEN '10대'
            WHEN Age BETWEEN 20 AND 29 THEN '20대'
            WHEN Age BETWEEN 30 AND 39 THEN '30대'
            WHEN Age BETWEEN 40 AND 49 THEN '40대'
            WHEN Age >= 60 THEN '60대 이상'
            END AS age_group
      , COUNT(*)
FROM user
GROUP BY age_group
ORDER BY age_group
```

6. 아이템별 총매출(이름으로)

```sql
SELECT I.Name, SUM(I.UnitPrice)
FROM item I
JOIN orderitem OI
ON I.Id = OI.ItemId
GROUP BY I.Name
```

7. 월별 최고 매출 아이템 타입
   😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭

```sql
SELECT SUBSTR(O.OrderAt, 6, 2) AS "ordermonth", I.Name, SUM(I.UnitPrice)
FROM orders O
JOIN orderitem OI
ON O.Id = OI.OrderId
JOIN item I
ON OI.ItemId = I.Id
GROUP BY ordermonth, I.Name;
```

```sql

```

8. 성별 가장 많이 산 아이템
   😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭
   user : Id, Gender
   orders : Id, UserId
   orderitem : Id, OrderId, ItemId
   item : Id, Name

```sql
SELECT "Gender", MAX("Total Amount Of Month"), "Name"
FROM (
  SELECT U.Gender AS "Gender", SUM(I.UnitPrice) AS "Total Amount Of Month", I.Name AS "Name"
  FROM user U, orders O, orderitem OI, item I
  WHERE U.Id = O.UserId AND O.Id = OI.OrderId AND I.Id = OI.ItemId
  GROUP BY U.Gender
);
```

```sql
SELECT users.Gender, items.Name ,count(orderitems.ItemId) AS 'purchaseCount'
FROM user users
INNER JOIN orders ON users.Id = orders.UserId
INNER JOIN orderitem orderitems On orders.Id = orderitems.OrderId
INNER JOIN item items ON orderitems.ItemId = items.Id
GROUP BY users.Gender;
```

9. 구매한 매출액의 합산이 가장 높은 사용자 10명을 구하고 각각의 매출액을 구하시오

```sql
SELECT U.Id, U.Name, SUM(CAST(I.UnitPrice AS INTEGER)) AS TotalRevenue
FROM user U
JOIN orders O
ON U.Id = O.UserId
JOIN orderitem OI
ON O.Id = OI.OrderId
JOIN item I
On OI.ItemId = I.Id
GROUP BY U.Id, U.Name
ORDER BY TotalRevenue DESC
LIMIT 10;
```

10가지 정도 통계 해보기...
쿼리문 리뷰.............
