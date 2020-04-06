class BasicDbDemo:
    def get_current_time(self, db_factory):
        cnx = db_factory.getConnection()
        cur = cnx.cursor()

        # Execute a query
        cur.execute("SELECT CURDATE()")

        # Fetch one result
        row = cur.fetchone()
        return row[0]
