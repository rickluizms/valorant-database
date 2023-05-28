from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from ..models import getUrl
from ..models.tables import Table
from ..core.save_db import Database as db
class Valorant():

    def __init__(self):
        self.init_bot
        self.score
        self.teams
        self.players
        self.matches
        self.agents
        self.quit    

    def init_bot():  

        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
        
        return driver 
    
    def get_overview(driver, regions, connection):
        #OVERVIEW tem 3 elementos, Playoffs, regular season, e nome dos players.
        #No decorrer do campeonato a pagina se modifica
        #ELEMENT01
        # Get content

        for region in regions:
            print("Get Overview")
            url = getUrl.get.overviewUrl(region)
            driver.get(url)
            
            time.sleep(1)
            
            element = driver.find_element("xpath", "//div[@class='event-group mod-fullwidth']//table[@class='wf-table mod-simple mod-group']")
            html_content = element.get_attribute('outerHTML')

            # Parser HTML content
            soup = BeautifulSoup(html_content, 'html.parser')
            table = soup.find(name='table')

            # Make a dataframe
            df_full = pd.read_html(str(table))[0]
            df = df_full[['Unnamed: 0', 'W', 'L', 'T', 'MAP', 'RND', 'Δ']]
            column_name = Table.columns("overview-01")
            df.columns = column_name
            print(df)

            #Mudar nome da tabela com regiao antes
            sql_table=Table.name("overview-01")
            table_name = f'{region}_{sql_table}'
            db.inject(connection, df, table_name)
        
        
            #ELEMENT2 - GET PLAYERS

            element2 = driver.find_element("xpath", "//div[@class='event-teams-container']")
            html_content2 = element2.get_attribute('outerHTML')

            # Parser HTML content
            soup2 = BeautifulSoup(html_content2, 'html.parser')


            atributes = {'class': 'wf-card event-team'}
            respostas2 = soup2.find_all("div", attrs=atributes)

            teams2 = {}

            for i in range(0, 10):
                resposta2 = respostas2[i].get_text(" ", strip = True)
                teams2[i] = resposta2

            df = pd.DataFrame(list(teams2.items()))
            column_name = Table.columns("overview-02")
            df.columns = column_name
            print(df)

            sql_table=Table.name("overview-02")
            table_name = f'{region}_{sql_table}'
            db.inject(connection, df, table_name)

        return
    
    def get_stats(driver, regions, connection):

        for region in regions:
            url = getUrl.get.statsUrl(region)
            driver.get(url)
            time.sleep(1)

            element = driver.find_element("xpath", "//div[@class='wf-card mod-table mod-dark']//table[@class='wf-table mod-stats mod-scroll']")
            html_content = element.get_attribute('outerHTML')

            # Parser HTML content
            soup = BeautifulSoup(html_content, 'html.parser')
            table = soup.find(name='table')

            # Make a dataframe
            df_full = pd.read_html(str(table))[0]
            
            df = df_full[['Player', 'Agents', 'Rnd', 'R',  'ACS', 'K:D', 'KAST', 'ADR', 'KPR', 'APR', 'FKPR', 'FDPR', 'HS%', 'CL%', 'CL', 'KMax', 'K', 'D', 'A', 'FK', 'FD']]
            column_name = Table.columns("stats")
            df.columns = column_name
            df1 = df.fillna('no data')
            print(df1)

            sql_table=Table.name("stats")
            table_name = f'{region}_{sql_table}'
            db.inject(df1, connection, table_name)

        return df1
    
    def get_matches(driver, regions, connection):

        for region in regions:
           
            # Get content
            print("Get matches")
            url = getUrl.get.matchesUrl(region)
            driver.get(url)
            time.sleep(1)

            element = driver.find_element("css selector", ".col")
            html_content = element.get_attribute('outerHTML')

            # Parser HTML content
            soup = BeautifulSoup(html_content, 'html.parser')


            atributes = {'class': 'match-item-vs'}
            respostas = soup.find_all("div", attrs=atributes)

            matches = {}

            if region == "emea":
                num = 55
            elif region =="americas":
                num = 55
            elif region == "pacific":
                num = 56
            else:
                print('Regiao invalida')


            for i in range(0, num):
                resposta = respostas[i].get_text(",", strip = True)
                matches[i] = (f'{resposta}')

            df = pd.DataFrame(list(matches.items()))
            column_name = Table.columns("matches")
            df.columns = column_name
            print(df)

            sql_table=Table.name("matches")
            table_name = f'{region}_{sql_table}'
            db.inject(df, connection, table_name)
        return
    
    def get_agents(driver, regions, connection):

        for region in regions:
            # Get content
            print("Get agents")
            url = getUrl.get.agentsUrl(region)
            driver.get(url)
            time.sleep(1)

            element = driver.find_element("css selector", ".mod-pr-global")
            html_content = element.get_attribute('outerHTML')

            # Parser HTML content
            soup = BeautifulSoup(html_content, 'html.parser')
            table = soup.find(name='table')

            # Make a dataframe
            df_full = pd.read_html(str(table))[0]
            df = df_full[['Map', '#', 'ATK WIN', 'DEF WIN', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 
                            'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13','Unnamed: 14', 'Unnamed: 15', 'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19',
                            'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22']]
            column_name = Table.columns("agents")
            df.columns = column_name
            df1 = df.dropna()
            print(df1)
        
            sql_table=Table.name("agents")
            table_name = f'{region}_{sql_table}'
            db.inject(df1, connection, table_name)
        return
    

