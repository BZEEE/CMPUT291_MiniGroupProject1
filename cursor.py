
import sqlite3

class sqlCursor:
    __conn = sqlite3.connect('./test.db')
    __singleton = None
    __cursor = __conn.cursor()
    @staticmethod
    def get_instance(self):
        if __singleton == None:
            __cursor = self.__conn.cursor()
            __singleton = sqlCursor()
            return __singleton
        return __singleton
    @staticmethod
    def get_cursor(self):
        return self.__cursor

    