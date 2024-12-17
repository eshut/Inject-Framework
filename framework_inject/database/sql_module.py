"""Framework: https://github.com/eshut/Inject-Framework"""


import os

import dotenv

from framework_inject.logger.logger import Logger
from framework_inject.services.sql_service import SQL

dotenv.load_dotenv()

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")
db_port = os.getenv("DB_PORT")


class Database(Logger):
    def __init__(self, logger=__file__):
        super().__init__(logger)
        self.sql_connection = SQL(db_host, db_user, db_password, db_name, db_port, dictionary=True)

    def get_db_data(self, query, args=None, dictionary=None):
        query_result = self.sql_connection.run_script(query, args=args, dictionary=dictionary)
        self.logger.debug(f"GET DB JSON RESULT FOR ENTRY: \n {query_result}")
        return query_result

    def update_db_data(self, query, args=None):
        query_result = self.sql_connection.update_data(query, args=args)
        return query_result
