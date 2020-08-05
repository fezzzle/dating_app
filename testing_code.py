def enter_sex():
    try:
        user_sex = input("Please enter your sex (Male/Female): ")
        print(type(user_sex))
        print(user_sex)
        if user_sex != "Male" and user_sex != "Female":
            raise ValueError
    except ValueError:
        print("You must enter Male/Female")
        enter_sex()


enter_sex()