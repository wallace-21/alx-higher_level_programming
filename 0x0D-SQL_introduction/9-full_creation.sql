-- creates a table second_table in the database hbtn_0c_0 in my MySQL server and add multiples rows
CREATE TABLE IF NOT EXISTS second_table(
	id INT PRIMARY KEY,
	name VARCHAR(256),
	score INT
);

INSERT IGNORE INTO second_table VALUES (1, "John", 10);
INSERT IGNORE INTO second_table VALUES (2, "Alex", 3);
INSERT IGNORE INTO second_table VALUES (3, "Bob", 14);
INSERT IGNORE INTO second_table VALUES (4, "George", 8);
