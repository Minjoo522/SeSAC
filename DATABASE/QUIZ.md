## ✨ QUIZ - chinook.db

1. non_usa_customers.sql: Provide a query showing Customers (just their full names, customer ID and country) who are not in the US.

```sql
SELECT FirstName||" "||LastName AS "Full Name", CustomerId, Country
FROM customers
WHERE Country != 'USA';
```

2. brazil_customers.sql: Provide a query only showing the Customers from Brazil.

```sql
SELECT * FROM Customers WHERE Country == 'Brazil';
```

3. brazil_customers_invoices.sql: Provide a query showing the Invoices of customers who are from Brazil. The resultant table should show the customer's full name, Invoice ID, Date of the invoice and billing country.

```sql
SELECT C.FirstName||" "||C.LastName AS "Full Name", I.InvoiceId, I.InvoiceDate, I.BillingCountry
FROM Customers C
INNER JOIN invoices I
ON C.CustomerId == I.CustomerId
AND C.Country == 'Brazil';
```

- LEFT JOIN 사용 가능!

```sql
SELECT C.FirstName||" "||C.LastName AS "Full Name", I.InvoiceId, I.InvoiceDate, I.BillingCountry
FROM Customers C
LEFT JOIN invoices I
ON C.CustomerId == I.CustomerId
WHERE C.Country == 'Brazil';
```

4. sales_agents.sql: Provide a query showing only the Employees who are Sales Agents.

```sql
SELECT * FROM employees WHERE Title='Sales Support Agent';
```

- Title에 Sales가 포함된 사람들

```sql
SELECT * FROM employees WHERE Title like "Sales%";
```

5. unique_invoice_countries.sql: Provide a query showing a unique/distinct list of billing countries from the Invoice table.

```sql
SELECT DISTINCT BillingCountry FROM invoices;
```

6. sales_agent_invoices.sql: Provide a query that shows the invoices associated with each sales agent. The resultant table should include the Sales Agent's full name.

```sql
SELECT I.*, E.FirstName||" "||E.LastName
FROM invoices I
INNER JOIN customers C
ON I.CustomerId == C.CustomerId
INNER JOIN employees E
ON C.SupportRepId == E.EmployeeId;
```

7. invoice_totals.sql: Provide a query that shows the Invoice Total, Customer name, Country and Sale Agent name for all invoices and customers.

```sql
SELECT I.Total, C.LastName, I.BillingCountry, E.LastName
FROM invoices I
INNER JOIN customers C
ON I.CustomerId == C.CustomerId
INNER JOIN employees E
ON C.SupportRepId == E.EmployeeId;
```

8. total*invoices*{year}.sql: How many Invoices were there in 2009 and 2011?

```sql
SELECT COUNT(Total) FROM invoices WHERE InvoiceDate BETWEEN DATE('2009-01-01') AND DATE('2011-12-31');
```

9. total*sales*{year}.sql: What are the respective total sales for each of those years?

```sql
SELECT STRFTIME('%Y', InvoiceDate) year, SUM(Total)
FROM invoices
WHERE InvoiceDate
BETWEEN DATE('2009-01-01') AND DATE('2011-12-31')
GROUP BY STRFTIME('%Y', InvoiceDate);
```

10. invoice_37_line_item_count.sql: Looking at the InvoiceLine table, provide a query that COUNTs the number of line items for Invoice ID 37.

```sql
SELECT COUNT(*) FROM invoice_items WHERE InvoiceId == 37;
```

11. line_items_per_invoice.sql: Looking at the InvoiceLine table, provide a query that COUNTs the number of line items for each Invoice. HINT: GROUP BY

```sql
SELECT COUNT(*), InvoiceId From invoice_items GROUP BY InvoiceId;
```

12. line_item_track.sql: Provide a query that includes the purchased track name with each invoice line item.

```sql
SELECT I.*, T.Name
FROM invoice_items I
INNER JOIN tracks T
ON I.TrackId == T.TrackId;
```

13. line_item_track_artist.sql: Provide a query that includes the purchased track name AND artist name with each invoice line item.

```sql
SELECT I.*, T.Name, AR.Name
FROM invoice_items I
INNER JOIN tracks T
ON T.TrackId == I.TrackId
INNER JOIN albums AL
ON T.AlbumId == AL.AlbumId
INNER JOIN artists AR
ON AL.ArtistId == AR.ArtistId;
```

14. country_invoices.sql: Provide a query that shows the # of invoices per country. HINT: GROUP BY

```sql
SELECT BillingCountry, COUNT(*) FROM invoices GROUP BY BillingCountry;
```

15. playlists_track_count.sql: Provide a query that shows the total number of tracks in each playlist. The Playlist name should be include on the resulant table.

```sql
SELECT P.Name, COUNT(*)
FROM tracks T
INNER JOIN playlist_track PT
ON T.TrackId == PT.TrackId
INNER JOIN playlists P
ON PT.PlaylistId == P.PlaylistId
GROUP BY PT.PlaylistId;
```

16. tracks_no_id.sql: Provide a query that shows all the Tracks, but displays no IDs. The result should include the Album name, Media type and Genre.

```sql
SELECT T.Name, A.Title, M.Name, G.Name
FROM tracks T
INNER JOIN genres G
ON T.GenreId == G.GenreId
INNER JOIN albums A
ON T.AlbumId == A.AlbumId
INNER JOIN media_types M
ON T.MediaTypeId == M.MediaTypeId;
```

17. invoices_line_item_count.sql: Provide a query that shows all Invoices but includes the # of invoice line items.

```sql
SELECT I.*, SUM(II.Quantity)
FROM invoices I
INNER JOIN invoice_items II
ON I.InvoiceId == II.InvoiceId
GROUP BY I.InvoiceId;
```

18. sales_agent_total_sales.sql: Provide a query that shows total sales made by each sales agent.

```sql
SELECT E.EmployeeId, E.FirstName, SUM(II.UnitPrice * II.Quantity)
FROM invoice_items II
INNER JOIN invoices I
ON II.InvoiceId = I.InvoiceId
INNER JOIN customers C
ON I.CustomerId = C.CustomerId
INNER JOIN employees E
ON C.SupportRepId = E.EmployeeId
GROUP BY E.EmployeeId;
```

19. top_2009_agent.sql: Which sales agent made the most in sales in 2009?
    Hint: Use the MAX function on a subquery. top_agent.sql: Which sales agent made the most in sales over all?
    max()

```sql
SELECT E.FirstName||" "||E.LastName
FROM invoice_items II
INNER JOIN invoices I
ON II.InvoiceId = I.InvoiceId
INNER JOIN customers C
ON I.CustomerId = C.CustomerId
INNER JOIN employees E
ON C.SupportRepId = E.EmployeeId
GROUP BY E.EmployeeId
ORDER BY SUM(II.UnitPrice * II.Quantity)
LIMIT 1;
```

20. sales_agent_customer_count.sql: Provide a query that shows the count of customers assigned to each sales agent.
    employees : EmployeeId, LastName, FirstName
    customers : SupportRepId

```sql
SELECT E.Firstname||" "||E.LastName, COUNT(C.CustomerId)
FROM employees E
INNER JOIN customers C
ON E.EmployeeId = C.SupportRepId
GROUP BY E.EmployeeId;
```

21. sales_per_country.sql: Provide a query that shows the total sales per country.
    invoices : BillingCountry, Total

```sql
SELECT BillingCountry, SUM(Total)
FROM invoices
GROUP BY BillingCountry;
```

22. top_country.sql: Which country's customers spent the most?

```sql
SELECT BillingCountry, SUM(Total) AS Sales
FROM invoices
GROUP BY BillingCountry
ORDER BY Sales DESC
LIMIT 1;
```

23. top_2013_track.sql: Provide a query that shows the most purchased track of 2013.
    tracks : TrackId, Name
    invoices : InvoiceId, InvoiceDate
    invoice_items : InvoiceId, TrackId, Quantity

```sql
SELECT T.Name, SUM(II.Quantity)
FROM tracks T
INNER JOIN invoice_items II
ON II.TrackId = T.TrackId
INNER JOIN invoices I
ON I.InvoiceId = II.InvoiceId
WHERE I.InvoiceDate
BETWEEN DATE('2013-01-01') AND DATE('2013-12-31')
GROUP BY T.Name
ORDER BY SUM(II.Quantity) DESC
LIMIT 1;
```

24. top_5_tracks.sql: Provide a query that shows the top 5 most purchased songs.

```sql
SELECT T.Name, SUM(II.Quantity)
FROM tracks T
INNER JOIN invoice_items II
ON II.TrackId = T.TrackId
INNER JOIN invoices I
ON I.InvoiceId = II.InvoiceId
GROUP BY T.Name
ORDER BY SUM(II.Quantity) DESC
LIMIT 5;
```

25. top_3_artists.sql: Provide a query that shows the top 3 best selling artists.

```sql
SELECT A.Name, SUM(II.Quantity)
FROM artists A
INNER JOIN albums AL
ON AL.ArtistId = A.ArtistId
INNER JOIN tracks T
ON T.AlbumId = AL.AlbumId
INNER JOIN invoice_items II
ON II.TrackId = T.TrackId
GROUP BY A.Name
ORDER BY SUM(II.Quantity) DESC
LIMIT 3;
```

26. top_media_type.sql: Provide a query that shows the most purchased Media Type.
