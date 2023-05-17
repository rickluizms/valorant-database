class get():

    def __init__(self):
        self.scoreUrl
        self.teamsUrl
        self.playersUrl
        self.matchesUrl
        self.agentsUrl      

    #Pagina "Home"
    def driver():

        driverUrl = (f"https://www.vlr.gg/event/1189/champions-tour-2023-americas-league")

        return driverUrl
    
    #Overview
    def overviewUrl(region):
        
        if region == "americas":
            overviewUrl = (f"https://www.vlr.gg/event/1189/champions-tour-2023-{region}-league")

        elif region == "emea":
            overviewUrl = (f"https://www.vlr.gg/event/1190/champions-tour-2023-{region}-league")

        elif region == "pacific":
            overviewUrl = (f"https://www.vlr.gg/event/1191/champions-tour-2023-{region}-league")
        
        else:
            print("REGIAO ERRADA")
            overviewUrl = ""

        return overviewUrl
    
    #Matches
    def matchesUrl(region):
        aba = "matches"

        if region == "americas":
            matchesUrl = (f"https://www.vlr.gg/event/{aba}/1189/champions-tour-2023-{region}-league/")
        
        elif region == "emea":
            matchesUrl = (f"https://www.vlr.gg/event/{aba}/1190/champions-tour-2023-{region}-league/")

        elif region == "pacific":
            matchesUrl = (f"https://www.vlr.gg/event/{aba}/1191/champions-tour-2023-{region}-league/")
        return matchesUrl

    #Stats
    def statsUrl(region):
        aba = "stats"

        if region == "americas":
            playersUrl = (f"https://www.vlr.gg/event/{aba}/1189/champions-tour-2023-{region}-league/")
        
        elif region == "emea":
            playersUrl = (f"https://www.vlr.gg/event/{aba}/1190/champions-tour-2023-{region}-league/")

        elif region == "pacific":
            playersUrl = (f"https://www.vlr.gg/event/{aba}/1191/champions-tour-2023-{region}-league/")
        return playersUrl
    
    #Agents
    def agentsUrl(region):
        aba = "agents"
        if region == "americas":
            agentsUrl = (f"https://www.vlr.gg/event/{aba}/1189/champions-tour-2023-{region}-league/")
        
        elif region == "emea":
            agentsUrl = (f"https://www.vlr.gg/event/{aba}/1190/champions-tour-2023-{region}-league/")

        elif region == "pacific":
            agentsUrl = (f"https://www.vlr.gg/event/{aba}/1191/champions-tour-2023-{region}-league/")
        return agentsUrl





