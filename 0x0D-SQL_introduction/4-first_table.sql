-- creates a table called first_table in the current database in my MySQL server

USE hbtn_0c_0;
CREATE TABLE IF NOT EXISTS first_table (
	id INT PRIMARY KEY,
	name VARCHAR(256)
);
