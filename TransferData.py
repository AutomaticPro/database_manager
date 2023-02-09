import DbConnections;
import queryStrings;

# Transfer Predefined tables belongs base_rates Web from one schema to other
def copy_base_rates_tables(src_schema, dest_schema):
    # Copy a list of tables
    if dest_schema != "tmxportal":
        tables = queryStrings.base_rates_tables_array
        copyTables(src_schema, dest_schema, tables)
    else:
        print("Looks like you are about to do a big disaster, and it was prevented on this condition")
        print("your destiny schema is production schema and you are about to delete all base rates tables")

# Transfer any array of tables from one Schema to other
def copyTables(src_schema, dest_schema, tables):
    # Connect to the database
    cnx = DbConnections.mysqlConnector()

    print("Coping next tables:")
    for table in tables:
        copyTable(cnx, src_schema, dest_schema, table)

    # Close the connection
    cnx.close()

# Transfer a table from one schema to other
def copyTable(cnx, src_schema, dest_schema, table):
    # Create a cursor
    cursor = cnx.cursor()

    # Execute the query to copy the table
    query = f"DROP TABLE IF EXISTS {dest_schema}.{table};"
    cursor.execute(query)

    query = f"CREATE TABLE {dest_schema}.{table} LIKE {src_schema}.{table};"
    cursor.execute(query)

    query = f"INSERT INTO {dest_schema}.{table} SELECT * FROM {src_schema}.{table};"
    cursor.execute(query)

    cnx.commit()

    print(f"{table}")

    # Close the cursor
    cursor.close()

# # Sample Implementation:
# # Connect to the database
# cnx = mysql_connection.mysqlConnector()
# # Copy the table
# transfer_data.copyTable(cnx, "tmxportal", "workspace", "aropen")
# # Close the connection
# cnx.close()
# print("Finish")
