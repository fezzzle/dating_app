from db import Database
import time

class User():
    def __init__(self, first_name, last_name, age, sex, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.location = location
        self.db = Database()
        self.cursor = self.db.cursor

    sql = """
    INSERT INTO user_data
    (firstName, lastName, sex, age, country_location) VALUES
    (%s, %s, %s, %s, %s);
    """
    
    def db_add_user(self, name, lastname, sex, age, country):
        try:
            self.cursor.execute(self.sql, (name, lastname, age, sex, country))

        except Exception as e:
            print(e)

    def db_available_countries(self):
        str_countries = ""
        try:
            self.cursor.execute(
                "SELECT DISTINCT country_location FROM user_data;"
            )
            # print(self.db.cursor.fetchall())
            countries = self.db.cursor.fetchall()
            for country in countries:
                # print(str(country[0]))
                str_country = str(country[0])
                str_countries += str_country + "\n"

        except Exception as e:
            print(e)
        return str_countries


    # Show members of opposite sex 10 years old ( Hint: you filter should take note of current member age and increment
    def find_usr_10_older(self, user_age, user_location, user_sex):
        print()
        print("*" * 60)
        print(f"Searching {user_age + 10} year old people to meet in {user_location}...")
        print("*" * 60)
        print()
        try: 
            self.cursor.execute(f"""
                SELECT firstName, age 
                FROM dateNow.user_data 
                WHERE age >= {user_age + 10} and country_location = "{user_location}" and sex = "{user_sex}";
                """
            )
            result = self.cursor.fetchall()
        except Exception as e:
            print(e)

        return result


    # def task_list(db):
    #     with db.cursor() as c:
    #         c.execute(f"SELECT id, task FROM `{TABLE_NAME}` WHERE NOT DONE")
    #         for row in c.fetchall():
    #             id_, task = row
    #             print(f"#{id_}: {task}")


    # def add_task(db):
    #     text = input("Task description: ")
    #     if text == "":
    #         print("Cannot insert empty task")
    #         return
    #     with db.cursor() as c:
    #         c.execute(
    #             f"INSERT INTO `{TABLE_NAME}` (`task`, `done`) VALUES (%s, FALSE)", (text)
    #         )
    #         db.commit()


    # def close_task(db):
    #     id_ = input("Task id: ")
    #     with db.cursor() as c:
    #         c.execute(f"UPDATE `{TABLE_NAME}` SET `done`=TRUE WHERE `id`=%s", (id_))
    #         db.commit()
    #     print(f"Task #{id_} closed")

    def __repr__(self):
        return f"User({self.first_name}, {self.age}, {self.sex}, {self.location})"


