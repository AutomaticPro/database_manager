import DbConnections
import queryStrings

# region Fuel PCT Updates CUSTOMER and DRIVERS
def fuelUpdatesCustomerDriver(schema):
    customerFuelUpdates(schema, queryStrings.customerFuelPercentages)
    driverFuelUpdates(schema, queryStrings.driverFuelPercentages)
# As long as the percentage are the same no matter how many
# times this process is executed, the result is always the same
# endregion


# region Query DictData(Store Procedures) to calc CUSTOMER Fuel, PCT based
def customerFuelUpdates(schema, tables_percentages):
    print("CUSTOMER FUEL UPDATED TABLES:")
    # Connect to the database
    cnx = DbConnections.mysqlConnector()
    for table, percentage in tables_percentages.items():
        customerFuelUpdate(cnx, schema, table, percentage)
    # Close the connection
    cnx.close()
# endregion

# region Query Store Procedure to calc CUSTOMER Fuel, PCT based
def customerFuelUpdate(cnx, schema, table, percentage):
    # Create a cursor
    cursor = cnx.cursor()
    # Execute the query to execute store procedure
    query = f"call {schema}.customerFuel_webRates('{table}',{percentage});"
    cursor.execute(query)
    cnx.commit()
    print(f"{table}")
    # Close the cursor
    cursor.close()
# endregion

# region Query DictData(Store Procedures) to calc driver Fuel, PCT based
def driverFuelUpdates(schema, tables_percentages):
    print("DRIVER FUEL UPDATED TABLES:")
    # Connect to the database
    cnx = DbConnections.mysqlConnector()
    for table, percentage in tables_percentages.items():
        driverFuelUpdate(cnx, schema, table, percentage)
    # Close the connection
    cnx.close()
# endregion

# region Query Store Procedure to calc driver Fuel, PCT based
def driverFuelUpdate(cnx, schema, table, percentage):
    cursor = cnx.cursor()
    # Execute store procedure
    query = f"call {schema}.driverFuel_webRates('{table}',{percentage});"
    cursor.execute(query)
    cnx.commit()
    print(f"{table}")
    cursor.close()
# endregion
