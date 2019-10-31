
import sqlite3

class sqlCursor:
    __conn = sqlite3.connect('./mgp1.db')
    __singleton = None
    __cursor = None
    @staticmethod
    def get_instance():
        if (sqlCursor.__singleton == None):
            sqlCursor.__cursor = sqlCursor.__conn.cursor()
            sqlCursor.__singleton = sqlCursor()
            return sqlCursor.__singleton
        else:
            return sqlCursor.__singleton

    def get_connection(self):
        return self.__conn

    def get_cursor(self):
        return self.__cursor
    @staticmethod
    def get_error():
        return sqlite3.Error
    