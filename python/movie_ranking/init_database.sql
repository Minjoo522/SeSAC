-- 파일 바로 적용하기 : sqlite3 movies.sqlite < init_database.sql
DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS rankings;

CREATE TABLE movies(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(200) NOT NULL,
  link VARCHAR(200),
  summary VARCHAR(200)
  );

CREATE TABLE rankings(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  movie_id INTEGER,
  ranking INTEGER,
  rating FLOAT,
  reservation_rate FLOAT,
  create_date TIMESTAMP,

  FOREIGN KEY ("movie_id")
  REFERENCES movies (id));