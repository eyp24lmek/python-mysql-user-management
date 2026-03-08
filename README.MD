#User Management System (Python & MySQL)

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-Database-orange.svg?style=for-the-badge&logo=mysql)](https://www.mysql.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

This repository features a **robust, Object-Oriented (OOP)** database management solution designed to bridge Python applications with MySQL. Unlike static query scripts, this project utilizes a **dynamic `MySQLDatabase` class** that automates SQL generation, allowing for scalable and clean backend operations.

---

## ✨ Features

* **➕ User Creation:** Seamlessly add new users to the database.
* **📋 Data Retrieval:** List all active users with formatted output.
* **🔄 Dynamic Updates:** Update any user field using dictionary-based logic.
* **🗑️ Soft Delete:** Safely deactivate users using the `user_active` flag (preserves data integrity).
* **🛡️ Secure & Modular:** Built with a focus on modularity and SQL injection prevention.

---

## 🛠️ Technologies Used

| Technology | Purpose |
| :--- | :--- |
| **Python 3** | Core application logic |
| **MySQL** | Relational data storage |
| **mysql-connector** | Database driver & connectivity |

---

## 📂 Project Structure

```text
project-folder/
├── main.py        # CLI Interface & Application Logic
├── db_class.py    # MySQL Abstraction Layer (OOP Class)
└── README.md      # Documentation
```

## 🗄️ Database Schema

```sql
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(50) NOT NULL,
    user_lastname VARCHAR(50) NOT NULL,
    user_age INT,
    user_active TINYINT DEFAULT 1
);


## ⚙️ Installation & Setup

### 1. Clone the Repository
Download the project to your local machine using the following commands:

```bash
git clone [https://github.com/eyp24lmek/python-mysql-user-management.git](https://github.com/eyp24lmek/python-mysql-user-management.git)
cd user-management-system
```

2. Install Dependencies

Install the required library via terminal:
```bash
pip install mysql-connector-python
```
3. Configure Connection

Open the db_class.py file and update your MySQL connection credentials to match your local environment:

self.__host = "localhost"
self.__user = "root"
self.__password = "YOUR_PASSWORD"
self.__database = "python"


🖥️ Usage

Execute the main script to launch the interactive menu:

python main.py






📚 References

    Python Documentation

    MySQL Connector/Python Documentation

    Fehmi Uyar - YouTube
