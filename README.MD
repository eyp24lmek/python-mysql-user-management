User Management System (Python & MySQL)

This repository features a robust, Object-Oriented (OOP) database management solution designed to bridge Python applications with MySQL. Unlike static query scripts, this project utilizes a dynamic MySQLDatabase class that automates SQL generation, allowing for scalable and clean backend operations.

It serves as a comprehensive example of a Command-Line Interface (CLI) application managing real-time data flow with a focus on modularity and security.

Features

Add new users to the database

List active users

Update user information

Soft delete users (using user_active flag)

Modular database class

MySQL integration using mysql-connector-python

Simple CLI menu system

Technologies Used

Python 3

MySQL

mysql-connector-python

Project Structure
project-folder/
│
├── main.py
├── db_class.py
└── README.md

main.py → Command line user interface and application logic

db_class.py → MySQL database class for database operations

Database Schema

Example users table structure:

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(50),
    user_lastname VARCHAR(50),
    user_age INT,
    user_active TINYINT DEFAULT 1
);
Installation
1. Clone the repository
git clone https://github.com/yourusername/user-management-system.git
cd user-management-system
2. Install required package
pip install mysql-connector-python
3. Configure database connection

Edit the database credentials in db_class.py:

self.__host = "localhost"
self.__user = "root"
self.__password = ""
self.__database = "python"

Make sure the database exists in MySQL.

Usage

Run the program:

python main.py

You will see the following menu:

--- Management System ---

1. Add User
2. List Users
3. Update User
4. Delete User
5. Exit

Select the desired operation and follow the prompts.

Example Output
ID    Name     Lastname    Age
1     John     Doe         25
2     Alice    Smith       30
Future Improvements

Add input validation

Add error handling

Implement logging

Create a GUI interface (Tkinter / PyQt)

REST API integration



## References

- Python Documentation
- MySQL Connector/Python Documentation
-https://www.youtube.com/@fehmiuyarnet
