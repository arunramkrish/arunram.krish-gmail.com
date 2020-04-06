import mysql.connector
class DbFactory:
    def __init__(self):
        # Connect to server
        self.cnx = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            database="data_analysis",
            user="root",
            password="root",
            use_unicode=True,
            charset="utf8")

    def getConnection(self):
        return self.cnx

