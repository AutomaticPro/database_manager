import csv
import DbConnections
import queryStrings

def csvFromBaseRatesTables(srcSchema):
    mysqlToCsvMultiples(srcSchema, queryStrings.base_rates_tables_array, queryStrings.customerDriverRatesFields, queryStrings.customerDriverCsvDest)
    mysqlToCsvMultiples(srcSchema, queryStrings.base_rates_tables_array, queryStrings.customerRatesFields, queryStrings.customerCsvDest)
    mysqlToCsvMultiples(srcSchema, queryStrings.base_rates_tables_array, queryStrings.driverRatesFields, queryStrings.driverCsvDest)

# Transfer any array of tables from one Schema to Csv Files
def mysqlToCsvMultiples(srcSchema, tables, fields, destCsv):
    # Connect to the database
    cnx = DbConnections.mysqlConnector()
    print("Getting CSV from next tables:")
    for table in tables:
        mysqlToCsv(cnx, srcSchema, table, fields, destCsv)
    # Close the connection
    cnx.close()

# Transfer a table from one srcSchema to a Csv File
def mysqlToCsv(cnx, srcSchema, table, fields, destCsv):
    cursor = cnx.cursor()
    query = f"Select {fields} from {srcSchema}.{table};"
    cursor.execute(query)
    with open(f'{destCsv}\{table}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([column[0] for column in cursor.description])
        writer.writerows(cursor)
    cursor.close()
    print(f"{table}")
