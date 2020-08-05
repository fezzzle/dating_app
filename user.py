from db import Database

class User():
    sql = """
    INSERT INTO user_data
    (firstName, lastName, sex, age, country_location) VALUES
    (%s, %s, %s, %s, %s);
    """

    def __init__(self, first_name, last_name, age, sex, location):
        self.db = Database()
        self.cursor = self.db.cursor
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.location = location
        
        self.db_funcs()

    def db_funcs(self):
        self.db.ensure_database()
        self.db.ensure_table()
        self.db.insert_data()
    
    def db_add_user(self, name, lastname, sex, age, country):
        try:
            self.cursor.execute(self.sql, (name, lastname, age, sex, country))
            self.db.db.commit()
            user_id = self.db.db.insert_id()
        except Exception as e:
            print(e)
        return user_id


    def db_available_countries(self):
        str_countries = ""
        try:
            self.cursor.execute(
                "SELECT DISTINCT country_location FROM user_data;"
            )
            countries = self.db.cursor.fetchall()
            for country in countries:
                str_country = str(country[0])
                str_countries += str_country + "\n"

        except Exception as e:
            print(e)
        return str_countries


    def find_usr_close_range(self, *args):
        print()
        print("*" * 60)
        print(f"Searching at your age range ({args[0]-5}-{args[0]+5}) year old people to meet in {self.location}...")
        print("*" * 60)
        print()

        print(f"args0: {args[0]}")
        print(f"args1: {args[1]}")
        print(f"args1: {args[2]}")
        try: 
            self.cursor.execute(f"""
                SELECT firstName, age, sex, user_id
                FROM user_data 
                WHERE sex = "{args[2]}" and country_location = "{self.location}" and age BETWEEN "{args[0]-5}" and "{args[0]+5}";
                """
            )
            result = self.cursor.fetchall()
            print(f"LINE 64 in user.py: {result}")
        except Exception as e:
            print(e)
        return result


    def find_usr_10_older(self, *args):
        print()
        print("*" * 60)
        print(f"Searching {args[0] + 10} year old people to meet in {self.location}...")
        print("*" * 60)
        print()

        try: 
            self.cursor.execute(f"""
                SELECT firstName, age, user_id
                FROM dateNow.user_data 
                WHERE age = {args[0] + 10} and country_location = "{self.location}" and sex = "{args[2]}";
                """
            )
            result = self.cursor.fetchall()
        except Exception as e:
            print(e)
        return result
    
    
    def find_all(self, *args):
        print()
        print("*" * 60)
        print(f"Searching all opposite gender people to meet in {self.location}...")
        print("*" * 60)
        print()

        try: 
            self.cursor.execute(f"""
                SELECT firstName, age, user_id
                FROM dateNow.user_data 
                WHERE age >= '15' and country_location = "{self.location}" and sex = "{args[2]}";
                """
            )
            result = self.cursor.fetchall()
        except Exception as e:
            print(e)
        return result


    def change_location(self, *args):
        print("----")
        print(f"Available countries are: \n{self.db_available_countries()}")
        new_location = input("Change the location: ")
        self.location = new_location
        try: 
            self.cursor.execute(f"""
                UPDATE user_data
                SET country_location = "{new_location}"
                WHERE user_id = "{args[3]}"
                """
            )
            self.db.db.commit()
        except Exception as e:
            print(e)
        print(f"Location changed to: {self.location}")
        return

    def __repr__(self):
        return f"User({self.first_name}, {self.age}, {self.sex}, {self.location})"


