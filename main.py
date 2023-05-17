import mysql.connector
from config.connection import connection2
from app.controller.sql_controller import Controller

regions = ['americas', 'emea', 'pacific']


Controller.getRegion(region=regions, connection=connection2)
