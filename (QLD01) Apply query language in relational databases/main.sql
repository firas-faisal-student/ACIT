-- create a table
CREATE TABLE songs (
  id INTEGER PRIMARY KEY auto_increment,
  name VARCHAR(70) NOT NULL,
  length float not null,
  album_id INTEGER not null
);
-- insert some values
INSERT INTO songs VALUES (1, 'Ryansdgfdgfghfgf',  ' 1.0', '1');
INSERT INTO songs VALUES (2, 'my', '1.0', '1');
-- fetch some values
SELECT * FROM songs;