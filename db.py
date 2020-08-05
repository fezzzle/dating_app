import pymysql


DATABASE_NAME = "dateNow"
TABLE_NAME = "user_data"
DATA_FILE = "users.csv"


class Database():
    dbc = ("127.0.0.1", "notroot", "123456", "dateNow")
    def __init__(self):
        self.db = pymysql.connect(*self.dbc)
        self.cursor = self.db.cursor()

    sql = """
        INSERT INTO user_data
        (user_id, firstName, lastName, sex, age, country_location) VALUES
        (%s, %s, %s, %s, %s, %s);
    """

    def convert_line_to_values(self, line):
        if "\n" in line:
            line = line.replace("\n", "")
        values = line.split(",")
        return values

    def ensure_database(self):
        try:
            self.cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {DATABASE_NAME} DEFAULT CHARACTER SET utf8")
        except Exception as e:
            print(e)
        print("Ensured database is created")

    def ensure_table(self):
        try:
            self.cursor.execute(
                f"""
                CREATE TABLE IF NOT EXISTS user_data (
                    `user_id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                    `firstName` varchar(50),
                    `lastName` varchar(50),
                    `sex` TEXT NOT NULL,
                    `age` INT,
                    `country_location` varchar(50)
                );
                """
            )
        except Exception as e:
            print(e)
        print("Ensured table is created")


    def insert_data(self):
        try:
            with open(DATA_FILE) as f:
                for i, line in enumerate(f):
                    if i == 0:
                        continue
                    values = self.convert_line_to_values(line)
                    self.cursor.execute(self.sql, values)
                    if i > 0 and i % 100 == 0:
                        self.db.commit()
                    # self.cursor.close()
                self.db.commit()
            # self.db.close()
        except Exception as e:
            print(e)
