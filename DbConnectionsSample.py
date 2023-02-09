import mysql.connector

def connect_to_database():
    # Connect to the database
    cnx = mysql.connector.connect(
        host="host",
        user="user",
        password="pass",
        database="schema_name"
    )
    print("Connection Established")
    return cnx