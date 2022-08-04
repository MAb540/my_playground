import os
import psycopg2
from configparser import ConfigParser
from pathlib import Path


#establishing the connection

from modules.logger import logger
class DB_MODEL:
    def __init__(self):
        self.conn = None
        self.cursor = None



    def __config(self,filename, section):
        # # create a parser
        parser = ConfigParser()
        # # read config file
        parser.read(filename)

        # get section, default to postgresql
        db = {}

        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))
        return db




    def db_connect(self):
        filename='db/database.ini'
        section='postgresql'
        try:
            params = self.__config(filename,section)
            conn = psycopg2.connect(**params)
                    
            cursor = conn.cursor()
            self.conn = conn
            self.cursor = cursor

        except(Exception, psycopg2.DatabaseError) as error:
            logger.info('\ndatabase connection error: ',str(error))
            os.abort()


