import sqlite3


class SqlOperator:

    def __init__(self):
        self.connection = sqlite3.connect("../data/database.db")
        self.cursor = self.connection.cursor()


SqlOperator()