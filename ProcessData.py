import DbConnections
import queryStrings

# Fuel Percentage Updates Customer and Drivers
# As long as the percentage are the same no matter how many
# times this process is executed, the result is always the same
def fuelUpdatesCustomerDriver(schema):
    customerFuelUpdates(schema, queryStrings.customerFuelPercentages)
    driverFuelUpdates(schema, queryStrings.driverFuelPercentages)


# **************************************** CUSTOMER FUEL UPDATES ***********************************
def customerFuelUpdates(schema, tables_percentages):
    print("CUSTOMER FUEL UPDATED TABLES:")
    # Connect to the database
    cnx = DbConnections.mysqlConnector()
    for table, percentage in tables_percentages.items():
        customerFuelUpdate(cnx, schema, table, percentage)
    # Close the connection
    cnx.close()

# call a store procedure to calculate customer Fuel, based on a percentage
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


# ********************************* DRIVER FUEL UPDATES ********************************************
def driverFuelUpdates(schema, tables_percentages):
    print("DRIVER FUEL UPDATED TABLES:")
    # Connect to the database
    cnx = DbConnections.mysqlConnector()
    for table, percentage in tables_percentages.items():
        driverFuelUpdate(cnx, schema, table, percentage)
    # Close the connection
    cnx.close()

# call a store procedure to calculate driver Fuel, based on a percentage
def driverFuelUpdate(cnx, schema, table, percentage):
    cursor = cnx.cursor()
    # Execute store procedure
    query = f"call {schema}.driverFuel_webRates('{table}',{percentage});"
    cursor.execute(query)
    cnx.commit()
    print(f"{table}")
    cursor.close()