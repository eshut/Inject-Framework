"""Framework: https://github.com/eshut/Inject-Framework"""

import mysql.connector
from framework_inject.logger.logger import Logger


class SQL(Logger):
    def __init__(self, host, user, password, database, port, dictionary=False, logger=__file__):
        super().__init__(logger)
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=int(port),
            collation="utf8mb4_general_ci"
        )
        self.dictionary = dictionary

    def cursor(self, dictionary=None):
        if dictionary is None:
            dictionary = self.dictionary
        return self.db.cursor(dictionary=dictionary)

    def run_script(self, script, args=None, dictionary=None):
        try:
            cursor = self.cursor(dictionary=dictionary)
            cursor.execute(script, args)
            result = cursor.fetchall()
            cursor.close()
            return result
        except mysql.connector.Error as err:
            self.logger.error(f"Error executing script: {err}")
            return None

    def update_data(self, query, args=None):
        try:
            self.db.reconnect()
            cursor = self.cursor()
            result_exec = cursor.execute(query, args)
            cursor_id = cursor.lastrowid
            result_commit = self.db.commit()
            result_close = cursor.close()
            self.logger.debug(f"Query executed successfully: {query}")
            return cursor_id
        except mysql.connector.Error as err:
            self.logger.error(f"Error executing update query: {err}")
            self.db.rollback()

    def close_connect(self):
        if self.db.is_connected():
            self.db.close()

    def commit(self):
        result = self.db.commit()
        return result
