from ..core.scrapping import Valorant as Vlr
import mysql.connector
from ..core.save_db import update_dataframe
from ..core.save_db import close_connection
from ..models.tables import Table

class Controller():
    def __init__(self):
        self.getRegion

    def getRegion(region, connection):

        driver = Vlr.init_bot()

        #Vlr.get_overview(driver, region, connection)

        #Vlr.get_matches(driver, region, connection)

        

        df1 = Vlr.get_stats(driver, region, connection)
        print(df1)

        update_dataframe(connection, df1, table_name=Table.name("stats"))

        #Vlr.get_agents(driver, region, connection)

        close_connection(connection)



    

