from ..core.scrapping import Valorant as Vlr
import mysql.connector
from ..core.save_db import close_connection

class Controller():
    def __init__(self):
        self.getRegion

    def getRegion(region, connection):

        driver = Vlr.init_bot()

        #Vlr.get_overview(driver, region, connection)

        #Vlr.get_matches(driver, region, connection)

        for i in region:

            Vlr.get_stats(driver, i, connection)

        #Vlr.get_agents(driver, region, connection)

        close_connection(connection)



    

