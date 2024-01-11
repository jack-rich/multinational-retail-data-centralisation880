import psycopg2  # Replace with the appropriate database connector library

class DatabaseConnector:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None
        self.cursor = None

    def connect(self):
        """
        Establish a connection to the database.
        """
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            print("Connected to the database.")
        except psycopg2.Error as e:
            print(f"Error: Unable to connect to the database. {e}")

    def disconnect(self):
        """
        Close the database connection.
        """
        if self.connection:
            self.connection.close()
            print("Disconnected from the database.")

    def upload_data_to_table(self, table_name, data):
        """
        Upload data to a specified database table.

        Parameters:
        - table_name (str): Name of the target table.
        - data (list of dicts): Data to be uploaded to the table.
        """
        try:
            # Assuming data is a list of dictionaries
            for row in data:
                columns = ', '.join(row.keys())
                values = ', '.join([f"'{value}'" for value in row.values()])
                query = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
                self.cursor.execute(query)
            self.connection.commit()
            print(f"Data successfully uploaded to the '{table_name}' table.")
        except psycopg2.Error as e:
            self.connection.rollback()
            print(f"Error uploading data to the database: {e}")

# Example Usage:
# connector = DatabaseConnector(dbname='your_db', user='your_user', password='your_password', host='your_host', port='your_port')
# connector.connect()
# connector.upload_data_to_table('your_table', your_data)
# connector.disconnect()
