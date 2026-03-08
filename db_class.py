import mysql.connector

class MySQLDatabase:
    def __init__(self, database):
        self.__host = "localhost"
        self.__user = "root"
        self.__password = ""
        self.__database = database
        self.__connection = None
        self.__cursor = None

    def connection(self):
        self.__connection = mysql.connector.connect(
            host=self.__host,
            user=self.__user,
            password=self.__password,
            database=self.__database
        )
        if self.__connection.is_connected():
            self.__cursor = self.__connection.cursor(buffered=True)
        else:
            print("Connection failed")

    def create_db(self, db_name, charset="utf8mb4", collation="utf8mb4_general_ci"):
        sql = f"CREATE DATABASE IF NOT EXISTS {db_name} CHARACTER SET {charset} COLLATE {collation}"
        self.__cursor.execute(sql)
        print(f"'{db_name}' database created successfully")

    def create_table(self, db_name, table_name, columns):
        self.__cursor.execute(f"USE {db_name}")
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.__cursor.execute(sql)
        print(f"'{table_name}' table created successfully")

    def insert_record(self,table_name,data):
        columns=", ".join(data.keys())
        values=tuple(data.values())
        placeholders=", ".join(["%s"]*len(data))
        sql=f"INSERT INTO {table_name}({columns}) values({placeholders})"
        self.__cursor.execute(sql,values)
        self.__connection.commit()
        print(f"The  record has been successfully  inserted!" )
    
    def update(self, table_name, columns, conditions):
        set_clause = ",".join([f"{key}=%s" for key in columns.keys()])
        where_clause = " AND ".join([f"{key}=%s" for key in conditions.keys()])

        sql_query = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"
        values = tuple(columns.values()) + tuple(conditions.values())

        self.__cursor.execute(sql_query, values)
        self.__connection.commit()
        print(f"{self.__cursor.rowcount} row(s) updated")
    
    def getRows(self,query,params=None):
        self.__cursor.execute(query,params or ())
        return self.__cursor.fetchall()
    def getRow(self,query,params=None):
        self.__cursor.execute(query,params or ())
        return self.__cursor.fetchone()      
    
    def update_record(self,query,values):
        self.__cursor.execute(query,values)
        self.__connection.commit()
        print(f"{self.__cursor.rowcount} rows(s) updated")
        
    def disconnect(self):
        if self.__cursor:
            self.__cursor.close()
        if self.__connection:
            self.__connection.close()


