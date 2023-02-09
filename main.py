import DbConnections
import TransferData
import ProcessData
import FilesFormatConverter
import queryStrings


# TransferData.copy_base_rates_tables("tmxportal", "workspace")


# cnx = DbConnections.mysqlConnector()
# ProcessData.customerFuelUpdate(cnx, "workspace", "base_rates_atl", 0.82)
# cnx.close()

# ProcessData.fuelUpdatesCustomerDriver("workspace")
# TransferData.copy_base_rates_tables("tmxportal", "backups");
# TransferData.copy_base_rates_tables("tmxportal", "workspace")
# ProcessData.fuelUpdatesCustomerDriver("workspace")

# cnx = DbConnections.mysqlConnector()
# FilesFormatConverter.mysqlToCsv(cnx,
#                                 "workspace",
#                                 "base_rates_atl",
#                                 queryStrings.customerDriverRatesFields,
#                                 queryStrings.customerCsvDest)
# cnx.close()


# # Backup tables
# TransferData.copy_base_rates_tables("tmxportal", "backups")
#
# # Move to workspace enviroment to test pricing
# TransferData.copy_base_rates_tables("tmxportal", "workspace")
# ProcessData.fuelUpdatesCustomerDriver("workspace")
FilesFormatConverter.csvFromBaseRatesTables("workspace")



print("Finish")


