import mysql.connector
from config.connection import SQL

from app.controller.sql_controller import Controller

regions = ['americas', 'emea', 'pacific']


Controller.getRegion(region=regions, connection=SQL)
