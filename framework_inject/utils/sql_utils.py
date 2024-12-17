import mysql.connector
from logger.logger import Logger


class SQLUtil(Logger):
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

    def ensure_connection(self):
        """Ensure the database connection is alive, reconnect if needed."""
        if not self.db.is_connected():
            self.logger.warning("Database connection lost. Reconnecting...")
            self.db.reconnect()

    def cursor(self, dictionary=None):
        """Get a database cursor."""
        self.ensure_connection()
        if dictionary is None:
            dictionary = self.dictionary
        return self.db.cursor(dictionary=dictionary)

    def run_script(self, script, args=None, dictionary=None):
        """Run a SQL script and fetch results."""
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
        """Update data in the database."""
        try:
            cursor = self.cursor()
            cursor.execute(query, args)
            cursor_id = cursor.lastrowid
            self.db.commit()
            cursor.close()
            self.logger.debug(f"Query executed successfully: {query}")
            return cursor_id
        except mysql.connector.Error as err:
            self.logger.error(f"Error executing update query: {err}")
            self.db.rollback()
            return None

    def close_connect(self):
        """Close the database connection."""
        if self.db.is_connected():
            self.db.close()

    def commit(self):
        """Commit the current transaction."""
        self.ensure_connection()
        return self.db.commit()
