from user import User

def gender_search(gender):
    if gender == "Male":
        return "Female"
    else:
        return "Male"

def show_results(results):
    for i, result in enumerate(results):
        print(f"{i}. {result[0]}, {result[1]}")

def enter_age():
    try:
        user_age = int(input("Enter your age: "))
        print(f"INSIDE THE FUNC: {type(user_age)}, {user_age}")
        return user_age
    except ValueError:
        print("You must enter a number")
        return enter_age()

def enter_sex():
    try:
        user_sex = input("Please enter your sex (Male/Female): ")
        if user_sex != "Male" and user_sex != "Female":
            raise ValueError
        return user_sex
    except ValueError:
        print("You must enter Male/Female")
        return enter_sex()

def enter_location():
    user_location = input("Enter your current country location / where you want to search: ").capitalize()
    return user_location


if __name__ == "__main__":


    # print(
    #     f"""Welcome to Dating app Ponder. Our app is only available in those countries:
    #         1. Estonia
    #         2. Latvia
    #         3. Lithuania
    #         4. Sweden
    #         5. Russia
    #         6. Finland
    #         7. United Arab Emirates
    #         8. Madagascar
    #         9. Saudi Arabia
    #         10. Canada
    #     """)

    # input("Hello! Welcome to dating app Ponder. Press enter to continue...")
    # input(
    #     f"""Welcome to Dating app Ponder. Our app is only available in those countries:
    #         1. Estonia
    #         2. Latvia
    #         3. Lithuania
    #         4. Sweden
    #         5. Russia
    #         6. Finland
    #         7. United Arab Emirates
    #         8. Madagascar
    #         9. Saudi Arabia
    #         10. Canada
    #         Press enter to continue...
    #     """)
    # print("Please enter your information: ")
    # user_name = input("Enter your name: ").capitalize()
    user_name = "John"
    # user_last_name = input("Enter your last name: ").capitalize()
    user_last_name = "Johnson"
    # user_age = enter_age()

    # print(f"OUTSIDE THE FUNC: {type(user_age)}, {user_age}")
    user_age = 20
    # user_sex = enter_sex()
    # print(type(user_sex))
    user_sex = "Female"
    # user_location = enter_location()
    user_location = "Estonia"
    user = User(user_name, user_last_name, user_age, user_sex, user_location)
    user.db_add_user(user_name, user_last_name, user_age, user_sex, user_location)


    countries = user.db_available_countries()
    print(f"App is available in those countries: \n{countries}")

    # choice_functions = {"l": user.find_usr_10_older, "a": user.add_task, "d": user.close_task}
    choice_functions = {"l": user.find_usr_10_older}
    print("----")
    while True:
        print(
            "What do you want to do?:\n",
            "l: Search a person 10 year OLDER than you\n",
            "a: add a new task\n",
            "d: Mark task as done\n",
            "q: quit\n",
        )
        choice = input("> ").lower()
        if choice == "q":
            print("Closing...")
            break
        elif choice in choice_functions:
            res = choice_functions[choice](user_age, user_location, gender_search(user_sex))
            show_results(res)
        else:
            print(f"Unknown choice: '{choice}'. Try again.")
        print("----")


