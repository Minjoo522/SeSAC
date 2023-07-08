# DB

- Collection of related Information
- Stores large number of data

# DBMS System : Database Management System

- 사용자가 DB를 생성하고 관리할 수 있게 해주는 시스템
- 기본 기능 : CRUD(Create, Read, Update, Delete)

# CAP 이론

- 분산 시스템에서 일관성(Consistency), 가용성(Avaliability), 분리 내구성(Partitions Tolerance)을 모두 만족하는 것은 불가능하다
- 서비스에 맞게 적합한 DBMS를 사용

<hr>

## 동기화 : 일관성(consistance), 정확성

- 동시성 문제가 없게 : lock & busy wait 방식의 기능 구현

### Race Condition : 두 개 이상의 프로세스(쓰레드)가 동시에 공유된 자원에 접근하려고 할 때 발새하는 오류 상황

- Critical Section : 동시성이 보호 되어야 하는 구간

### 트랜잭션 : 데이터베이스의 상태를 변화시키는 하나의 작업 단위

- 하나의 트랜잭션은 Rollback되거나 commit된다
- 트랜잭션이 실패 했을 때 예외처리 -> 남은 기능 회수 : Rollback
- 성공 : commit
- 특징 : 원자성, 일관성, 독립성, 영속성

# DB 유형

## RDBMS : 관계형 데이터베이스

- MySQL, MSSQL, Sqlite3, Postgresql

## 비정형 데이터베이스

- NoSQL : 빅데이터(비정형, 규칙성 없음)
- T Value 형태

- 인스타그램, 페북 등과 같이 글, 사진, 동영상들

## Sqlite3 : 엄청 많이 사용됨

- 단일 사용자 용도로 만들어짐
- 다중 사용자(= 멀티 쓰레드) 사용시 오류가 발생할 가능성이 있음

# Table 구조

- Table
- Column
- Row
- Field
- Primary Key(기본키) : 유일한 값을 갖는 column
- Foreign Key(외래키, 참조키) : 다른 테이블을 참조할 때 사용되는 키
  - 나의 Primaty key가 상대방의 Foreign Key가 된다
- Schema(컬럼 및 속성)

<hr>

# DB용 언어 : SQL(Structured Query Language)

# 이상 현상이 발생하지 않도록 스키마를 잘 설계해야함

- 기준이 되는 ID는 절대 중복되면 안됨 : AUTOINCREMENT

## 이상 현상

- 삽입 이상 : 원치 않는 정보까지도 삽입해야 하는 현상
- 갱신 이상 : 특정 속성 값 갱신시, 중복 저장되어 있는 속성 값 중 하나만 갱신하고, 나머지는 갱신하지 않아 발생하는 데이터의 불일치 현상
- 삭제 이상 : 특정 튜플을 삭제할 경우 원하지 않는 정보까지도 삭제되는 현상

## ✨ QUIZ - chinook.db

1. non_usa_customers.sql: Provide a query showing Customers (just their full names, customer ID and country) who are not in the US.

```
SELECT FirstName||" "||LastName AS "Full Name", LastName, CustomerId, Country FROM customers WHERE country != 'USA';
```

2. brazil_customers.sql: Provide a query only showing the Customers from Brazil.

```
SELECT * FROM Customers WHERE Country == 'Brazil';
```

3. brazil_customers_invoices.sql: Provide a query showing the Invoices of customers who are from Brazil. The resultant table should show the customer's full name, Invoice ID, Date of the invoice and billing country.

```
SELECT C.FirstName||" "||C.LastName AS "Full Name", I.InvoiceId, I.InvoiceDate, I.BillingCountry FROM Customers C INNER JOIN invoices I ON C.CustomerId == I.CustomerId AND C.Country == 'Brazil' ;
```

4. sales_agents.sql: Provide a query showing only the Employees who are Sales Agents.

```
SELECT * FROM employees WHERE Title='Sales Support Agent' OR 'Sales Manager';
```

5. unique_invoice_countries.sql: Provide a query showing a unique/distinct list of billing countries from the Invoice table.

```
SELECT DISTINCT BillingCountry FROM invoices;
```

6. sales_agent_invoices.sql: Provide a query that shows the invoices associated with each sales agent. The resultant table should include the Sales Agent's full name.

```
SELECT I.*, E.FirstName||" "||E.LastName
FROM invoices I
INNER JOIN customers C
ON I.CustomerId == C.CustomerId
INNER JOIN employees E
ON C.SupportRepId == E.EmployeeId;
```

7. invoice_totals.sql: Provide a query that shows the Invoice Total, Customer name, Country and Sale Agent name for all invoices and customers.

```
SELECT I.Total, C.LastName, I.BillingCountry, E.LastName FROM invoices I INNER JOIN customers C ON I.CustomerId == C.CustomerId INNER JOIN employees E ON C.SupportRepId == E.EmployeeId;
```

8. total*invoices*{year}.sql: How many Invoices were there in 2009 and 2011?

```
SELECT COUNT(Total) FROM invoices WHERE InvoiceDate BETWEEN DATE('2009-01-01') AND DATE('2011-12-31');
```

9. total*sales*{year}.sql: What are the respective total sales for each of those years?

```
SELECT STRFTIME('%Y', InvoiceDate) year, SUM(Total) FROM invoices WHERE InvoiceDate BETWEEN DATE('2009-01-01') AND DATE('2011-12-31') GROUP BY STRFTIME('%Y', InvoiceDate);
```

10. invoice_37_line_item_count.sql: Looking at the InvoiceLine table, provide a query that COUNTs the number of line items for Invoice ID 37.

```
SELECT COUNT(*) FROM invoice_items WHERE InvoiceId == 37;
```

11. line_items_per_invoice.sql: Looking at the InvoiceLine table, provide a query that COUNTs the number of line items for each Invoice. HINT: GROUP BY

```
SELECT COUNT(*), InvoiceId From invoice_items GROUP BY InvoiceId;
```

12. line_item_track.sql: Provide a query that includes the purchased track name with each invoice line item.

```
SELECT I.*, T.Name FROM invoice_items I INNER JOIN tracks T ON I.TrackId == T.TrackId;
```

13. line_item_track_artist.sql: Provide a query that includes the purchased track name AND artist name with each invoice line item.

```
SELECT I.*, T.Name, AR.Name FROM invoice_items I INNER JOIN tracks T ON T.TrackId == I.TrackId INNER JOIN albums AL ON T.AlbumId == AL.AlbumId INNER JOIN artists AR ON AL.ArtistId == AR.ArtistId;
```

14. country_invoices.sql: Provide a query that shows the # of invoices per country. HINT: GROUP BY

```
SELECT BillingCountry, COUNT(*) FROM invoices GROUP BY BillingCountry;
```

15. playlists_track_count.sql: Provide a query that shows the total number of tracks in each playlist. The Playlist name should be include on the resulant table.

```
SELECT P.Name, COUNT(*) FROM tracks T INNER JOIN playlist_track PT ON T.TrackId == PT.TrackId INNER JOIN playlists P ON PT.PlaylistId == P.PlaylistId GROUP BY PT.PlaylistId;
```

16. tracks_no_id.sql: Provide a query that shows all the Tracks, but displays no IDs. The result should include the Album name, Media type and Genre.

```
SELECT T.Name, A.Title, M.Name, G.Name FROM tracks T INNER JOIN genres G ON T.GenreId == G.GenreId INNER JOIN albums A ON T.AlbumId == A.AlbumId INNER JOIN media_types M ON T.MediaTypeId == M.MediaTypeId;
```

17. invoices_line_item_count.sql: Provide a query that shows all Invoices but includes the # of invoice line items.

```
SELECT I.*, SUM(II.Quantity) FROM invoices I INNER JOIN invoice_items II ON I.InvoiceId == II.InvoiceId GROUP BY I.InvoiceId;
```

18. sales_agent_total_sales.sql: Provide a query that shows total sales made by each sales agent.

```
SELECT E.EmployeeId, E.FirstName, SUM(II.UnitPrice * II.Quantity) FROM invoice_items II INNER JOIN invoices I ON II.InvoiceId = I.InvoiceId INNER JOIN customers C ON I.CustomerId = C.CustomerId INNER JOIN employees E ON C.SupportRepId = E.EmployeeId GROUP BY E.EmployeeId;
```

19. top_2009_agent.sql: Which sales agent made the most in sales in 2009?
    Hint: Use the MAX function on a subquery. top_agent.sql: Which sales agent made the most in sales over all?
20. sales_agent_customer_count.sql: Provide a query that shows the count of customers assigned to each sales agent.
21. sales_per_country.sql: Provide a query that shows the total sales per country.
22. top_country.sql: Which country's customers spent the most?
23. top_2013_track.sql: Provide a query that shows the most purchased track of 2013.
24. top_5_tracks.sql: Provide a query that shows the top 5 most purchased songs.
25. top_3_artists.sql: Provide a query that shows the top 3 best selling artists.
26. top_media_type.sql: Provide a query that shows the most purchased Media Type.
