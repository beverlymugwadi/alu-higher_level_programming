--Create another table
CREATE TABLE IF NOT EXIST second_table(
	id INT
        name VARCHAR(256)
        score INT
);
INSERT second_table VALUES(1, "John", 10), (2, "Alex", 3), (3, "bob", 14), (4, "George", 8);
