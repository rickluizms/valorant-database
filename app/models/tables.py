class Table():
    
    
    def name(name):
        
        if name == "overview-01":
            table_name = ("teams_score")

        elif name == "overview-02":
            table_name = ("teams_cast")

        elif name == "matches":
            table_name = ("matches")

        elif name == "stats":
            table_name = ("players_stats")

        elif name == "agents":
            table_name = ("agents")

        else:
            print("Parametro Inválido!")

        return table_name
    
    def columns(name):

        if name == "overview-01":
            column_name = ['team', 'wins', 'loss', 'draw', 'map', 'rounds', 'round_diff']

        elif name == "overview-02":
            column_name = ['ranking', 'team']

        elif name == "matches":
            column_name = ['match', 'results']

        elif name == "stats":
            column_name = ['player', 'agents', 'rounds', 'rating', 'ACS', 'KD', 'KAST', 'ADR', 'KPR', 'APR', 
                           'FKPR', 'FDPR', 'HSp', 'CLp','CL', 'kmax', 'kills', 'deaths', 'assists', 'first_kill', 'first_deaths'] 

        elif name == "agents":
            column_name = ['map', 'picks', 'ATK_WIN', 'DEF_WIN', 'Agent_rnk1', 'Agent_rnk2', 'Agent_rnk3', 'Agent_rnk4', 'Agent_rnk5', 'Agent_rnk6', 
                           'Agent_rnk7', 'Agent_rnk8', 'Agent_rnk9', 'Agent_rnk10','Agent_rnk11', 'Agent_rnk12', 'Agent_rnk13', 'Agent_rnk14', 'Agent_rnk15', 'Agent_rnk16',
                           'Agent_rnk17', 'Agent_rnk18', 'Agent_rnk19']

        else:
            print("Parametro Inválido!")

        return column_name
    
   