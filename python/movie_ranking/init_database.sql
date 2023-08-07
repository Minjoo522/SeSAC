DROP TABLE IF EXISTS movies;

CREATE TABLE movies(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ranking INTEGER,
  title VARCHAR(200) NOT NULL,
  grade FLOAT,
  sales_rate FLOAT,
  link VARCHAR(200),
  summary VARCHAR(200),
  create_at TIMESTAMP
);