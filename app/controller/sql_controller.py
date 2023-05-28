from ..core.scrapping import Valorant as Vlr


class Controller():
    def __init__(self):
        self.getRegion

    def getRegion(region, connection):
        #Inicializa o bot
        driver = Vlr.init_bot()


        #Realiza a busca

        Vlr.get_overview(driver, region, connection)
        #Vlr.get_matches(driver, region, connection)
        #Vlr.get_stats(driver, region, connection)
        #Vlr.get_agents(driver, region, connection)




    

