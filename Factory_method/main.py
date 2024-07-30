from abc import ABC, abstractmethod

class DatabaseConnection(ABC):
  @abstractmethod
  def connect(self):
    """Establish a database connection"""
    pass

  @abstractmethod
  def close(self):
    """Close the database connection"""
    pass

import mysql.connector
import psycopg2
import sqlite3

class MySQConnection(DatabaseConnection):
  def __init__ (self,user,password,host,database):
    self.user = user
    self.password = password
    self.host = host
    self.database = database
    self.connection = None

  def connect(self):
    print("Connecting to MySQL database")
    self.connection = mysql.connector.connect(user=self.user,password=self.password,host=self.host,database=self.database)
    print("MySQL database connected")

  def close(self):
    if self.connection is not None:
      self.connection.close()
      print("Connection to MySQL database closed")

class PostgreSQLConnection(DatabaseConnection):
  def __init__ (self,user,password,host,database):
    self.user = user
    self.password = password
    self.host = host
    self.database = database
    self.connection = None

  def connect(self):
    print("Connecting to PostgreSQL database")
    self.connection = psycopg2.connect(user=self.user, password=self.password,database=self.database,host=self.host)
    print("Connected to PostgreSQL database")

  def close(self):
    if self.connection is not None:
      self.connection.close()
      print("Closed connection to PostgreSQL database")

class SQLiteConnection(DatabaseConnection):
  def __init__(self,user,password,host,database):
    self.user = user
    self.password = password
    self.host = host
    self.database = database
    self.connection = None

  def connect(self):
    print("Connecting to SQLite database")
    self.connection = sqlite3.connect(self.database)
    print("Connected to SQLite database")

  def close(self):
    if self.connection is not None:
      self.connection.close()
      print("Closed connection to SQLite database")

class DatabaseConnectionFactory:
  @staticmethod
  def create_connection(db_type,**kwargs):
    if db_type == 'mysql':
      return MySQConnection(**kwargs)
    elif db_type == 'postgresql':
      return PostgreSQLConnection(**kwargs)
    elif db_type == 'sqlite':
      return SQLiteConnection(**kwargs)
    else:
      raise ValueError("Unknown database type")
    
def main():
  db_type = 'mysql'

  connection_params = {
    'user':'admin',
    'password' : 'admin_pass',
    'host': 'localhost',
    'database' : 'test_db'
  }

  connection = DatabaseConnectionFactory.create_connection(db_type,**connection_params)

  connection.connect()

  connection.close()

if __name__ == '__main__':
  main()

