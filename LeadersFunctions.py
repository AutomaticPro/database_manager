import TransferData
import FilesFormatConverter
import ProcessData
import DictionaryFunctions

def fuelUpdatesBaseRatesMain(environment):
    if environment == "testing":
        TransferData.copy_base_rates_tables("tmxportal", "backups")

        print("Move Data to test environment")
        TransferData.copy_base_rates_tables("tmxportal", "workspace")

        print("Proccessing Data on test environment")
        ProcessData.fuelUpdatesCustomerDriver("workspace")

        print("Getting data from mysql to CSV 3 Folders(customerProd, driverProd, cust_driver_QC)")
        FilesFormatConverter.csvFromBaseRatesTables("workspace")

    elif environment == "production":
        print("Backup")
        TransferData.copy_base_rates_tables("tmxportal", "backups")

        print("Proccessing Data on production environment")
        ProcessData.fuelUpdatesCustomerDriver("tmxportal")

        print("Getting data from mysql to CSV 3 Folders(customerProd, driverProd, cust_driver_QC)")
        FilesFormatConverter.csvFromBaseRatesTables("tmxportal")

    elif environment == "help":
        print(DictionaryFunctions.LeadersFunction__fuelUpdatesBaseRatesMain)

    else:
        print("Enviroment no proper Defined")
