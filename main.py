import mysql.connector
from config.connection import SQL

from app.controller.sql_controller import Controller

regions = ['americas', 'emea', 'pacific']

class Config():
    playoffs = False
    regular_season = True
    team_players = ""
    
    overview = True
    matches = True
    stats = True
    agents = True



Controller.getRegion(region=regions, connection=SQL, config=Config)
