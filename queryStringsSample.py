base_rates_tables_array = \
      ["table1",
       "table2",
       "table3",
       "table4",
       "table5",
       "table6",
       "table7",
       "table8",
       "table9"]

customerFuelPercentages = \
           {"table1":0.15,
            "table2":0.15,
            "table3":0.15,
            "table4":0.15,
            "table5":0.15,
            "table6":0.15,
            "table7":0.6,
            "table8":0.5,
            "table9":0.5}

driverFuelPercentages = \
            {"table1": 0.15,
             "table2": 0.15,
             "table3": 0.15,
             "table4": 0.15,
             "table5": 0.15,
             "table6": 0.15,
             "table7": 0.6,
             "table8": 0.5,
             "table9": 0.5}

customerDriverRatesFields = \
        """fieldx   AS alias,
           fieldx,
           fieldx   AS alias,
           fieldx   AS alias,
           fieldx   AS alias,
           fieldx   AS alias,
           ROUND(fieldx/fieldx,3) AS alias,
           fieldx   AS alias,
           fieldx   AS alias,
           fieldx   AS alias,
           ROUND((fieldx/(fieldx*fieldx)-1),3) AS alias,
           fieldx AS alias"""

customerRatesFields = \
        """fieldx   AS alias,
           fieldx,
           fieldx   AS alias,
           fieldx   AS alias,
           fieldx   AS alias"""

driverRatesFields = \
        """fieldx   AS alias,
           fieldx,
           fieldx   AS alias,
           fieldx   AS alias,
           fieldx   AS alias"""

customerDriverCsvDest = ".\CSV\somefolder\QualityControl"
customerCsvDest       = ".\CSV\somefolder\Production\customer"
driverCsvDest         = ".\CSV\somefolder\Production\driver"
