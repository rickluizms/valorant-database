from ..core.scrapping import Valorant as Vlr


class Controller():
    def __init__(self):
        self.getRegion

    def getRegion(region, connection, config):
        #Inicializa o bot
        driver = Vlr.init_bot()

        #Realiza a busca
        if config.overview:
            Vlr.get_overview(driver, region, connection, config)
        if config.matches:
            Vlr.get_matches(driver, region, connection)
        if config.stats:
            Vlr.get_stats(driver, region, connection)
        if config.agents:
            Vlr.get_agents(driver, region, connection)




    

