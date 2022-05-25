import json

movies_list = []


def home_page():
    print("******WELCOME TO BOOK MY SHOW******")
    print("(CHOOSE AN OPTION)")
    who = int(input("1. Admin\n2. User\n>>>"))
    if who == 1:
        print("CHOOSE AN OPTION")
        choice = int(input("1. Register\n2. Log in\n3. Exit\n>>>"))
        if choice == 1:
            admin_register()
        elif choice == 2:
            admin_access()
        elif choice == 3:
            exit_bms()
        else:
            print("CHOOSE A VALID OPTION")
    elif who == 2:
        print("CHOOSE AN OPTION")
        choice = int(input("1. Register\n2. Log in\n3. Exit\n>>>"))
        if choice == 1:
            user_register()
        elif choice == 2:
            user_access()
        elif choice == 3:
            exit_bms()
        else:
            print("CHOOSE A VALID OPTION")
    else:
        print("CHOOSE A VALID OPTION")
        home_page()


def admin_register():
    fhand = open("database.txt", 'r')
    username = input("ENTER USERNAME: ")
    password = input("ENTER PASSWORD: ")
    fhand = open("database.txt", 'a')
    fhand.write(username + " ," + password + "\n")
    print("LOG IN TO YOUR ACCOUNT")
    admin_access()


def admin_access():  # working
    fhand = open("database.txt", 'r')
    username = input("ENTER USERNAME: ")
    password = input("ENTER PASSWORD: ")
    if username in fhand.read():
        print("WELCOME ADMIN: ", username)
        print("CHOOSE AN OPTION\n1. Add New Movie Info\n2. Edit Movie Info\n3. Delete Movies\n4. Logout")
        a_choice = int(input(">>>"))
        if a_choice == 1:
            admin_add()
        elif a_choice == 2:
            admin_edit()
        elif a_choice == 3:
            admin_del()
        elif a_choice == 4:
            log_out()
        else:
            print("CHOOSE A VALID OPTION")


def exit_bms():  # working
    quit()


def log_out():
    home_page()


def admin_add():  # working
    d = {}
    ranges = int(input("HOW MANY MOVIES DO YOU WISH TO ADD?\n>>>"))
    for i in range(ranges):
        title = input("Title: ")
        genre = input('Genre: ')
        length = int(input("Length (in minutes): "))
        cast = input("Cast: ")
        director = input("Director: ")
        ratings = input("Admin Rating: ")
        language = input("Language: ")
        # timings = input("Timings: ")
        number_of_shows = int(input("Number of shows in a day: "))
        first_show = input("First show: ")
        interval_time = int(input("Interval time (in minutes) : "))
        gaps = int(input("Gap between shows (in minutes) : "))
        capacity = int(input("Capacity: "))

        class ShowTimings:
            def solve(self, first_show, num):
                hour, minute = map(int, first_show[:-2].split(':'))
                hour %= 12
                if first_show[-2:] == 'pm':
                    hour += 12
                time = hour * 60 + minute + num
                hour, minute = divmod(time, 60)
                hour %= 24
                suffix = 'a' if hour < 12 else 'p'
                hour %= 12
                if hour == 0:
                    hour = 12

                new_time = "{:02d}:{:02d}{}m".format(hour, minute, suffix)
                if first_show != new_time:
                    return "{} - {}".format(first_show, new_time)

        ob = ShowTimings()
        n = interval_time + length
        total_time = 0
        nos = number_of_shows
        timings = list()
        while nos != 0:
            timing = (ob.solve(first_show, n))
            nos = nos - 1
            total_time = interval_time + length + gaps
            n = n + total_time
            timings.append(timing)

        d["Title"] = title
        d["Genre"] = genre
        d["Length"] = length
        d["Cast"] = cast
        d["Director"] = director
        d["Admin Ratings"] = ratings
        d["Language"] = language
        d["Timings"] = timings
        d["Number of shows in a day"] = number_of_shows
        d["Fist show"] = first_show
        d["Interval time:"] = interval_time
        d["Gap between shows:"] = gaps
        d["Capacity"] = capacity
        movies_list.append(d)

        with open('movies.json', 'a') as file:
            json.dump(movies_list, file)
    print("MOVIES ADDED SUCCESSFULLY")
    admin_edit()
    admin_del()
    op = input("Logout?\nType Y/N\n>>> ")
    if op == 'Y' or op == 'y':
        home_page()
    elif op == 'n' or op == "N":
        admin_add()


def user_access():
    fhand = open("user.txt", 'r')
    username = input("ENTER USERNAME: ")
    password = input("ENTER PASSWORD: ")
    if username in fhand.read():
        print("WELCOME USER,", username)
    print("CHOOSE AN OPTION")
    print("1. Lorem\n2. Movie2\n3. Movie3\n4. Logout")
    option = int(input(">>>"))
    if option == 1 or option == 2 or option == 3:
        movie_details()
    elif option == 4:
        home_page()
    else:
        print("CHOOSE A VALID OPTION")


def admin_del():  # working
    with open('movies.json', 'r') as file:
        movies_list = json.load(file)
    movie = input("Title of the movie to be deleted: ")
    for index in range(len(movies_list)):
        if movies_list[index]['Title'] == movie:
            del movies_list[index]
            break


def admin_edit():
    movie = input("TITLE OF THE MOVIE YOU WANT TO EDIT: ")
    print("DETAILS OF ", movie)
    with open('movies.json', 'r') as file:
        movies_list = json.load(file)
        for index in range(len(movies_list)):
            if movies_list[index]['Title'] == movie:
                print(json.dumps(movies_list[index], sort_keys=False, indent=4))
            print("ENTER THE DETAILS OF THE MOVIE YOU WANT TO EDIT")
            edit = input(">>>")
            print(movies_list[index][edit])
            changed = input("CHANGE THE VALUE: ")
            movies_list[index][edit] = changed
            print(movies_list[index][edit])
            print(json.dumps(movies_list[index], sort_keys=False, indent=4))
            with open('movies.json', 'w') as file:  # so that the result is reflected
                json.dump(movies_list, file)


def user_register():  # working
    print("****CREATE A NEW ACCOUNT*****")
    fhand = open("user.txt", 'a')
    username = input("ENTER USERNAME: ")
    password = input("ENTER PASSWORD: ")
    name = input("ENTER NAME: ")
    phone = input("ENTER YOUR PHONE NUMBER: ")
    age = input("ENTER YOUR AGE: ")

    fhand.write(username + " : " + phone + " : " + age + " : " + name + " : " + password + "\n")
    print("USER REGISTERED SUCCESSFULLY")
    user_access()


def movie_details():  # working
    movie = input("TITLE OF THE MOVIE: ")
    print("DETAILS OF ", movie)
    with open('movies.json', 'r') as file:
        movies_list = json.load(file)
        for index in range(len(movies_list)):
            if movies_list[index]['Title'] == movie:
                print(json.dumps(movies_list[index], sort_keys=False, indent=4))

            def cancel_tickets():
                print("\n******CANCEL TICKETS*******")
                total = int(movies_list[index]['Capacity'])

                seats = int(input("ENTER NUMBER OF SEATS YOU WANT TO CANCEL: "))
                total += seats
                movies_list[index]['Capacity'] = total
                print("REMAINING SEATS: ", total)

                print(json.dumps(movies_list[index], sort_keys=False, indent=4))
                with open('movies.json', 'w') as file:  # so that the result is reflected
                    json.dump(movies_list, file)
                print("THANK YOU, SEE YOU SOON.")
                ratings = input("Movie ratings: ")
                op = input("Logout?\nType Y/N\n>>> ")
                if op == 'Y' or op == 'y':
                    home_page()
                elif op == 'n' or op == "N":
                    movie_details()

            def book_tickets():
                print("\n******BOOK TICKETS*******")
                print("TIMINGS ARE:")
                print(movies_list[index]['Timings'])
                total = int(movies_list[index]['Capacity'])

                seats = int(input("ENTER NUMBER OF SEATS: "))
                total -= seats
                movies_list[index]['Capacity'] = total
                print("REMAINING SEATS: ", total)

                print(json.dumps(movies_list[index], sort_keys=False, indent=4))
                with open('movies.json', 'w') as file:  # so that the result is reflected
                    json.dump(movies_list, file)
                print("THANK YOU FOR BOOKING.")
                cancel_tickets()

            choice = int(input("\n(CHOOSE YOUR OPTION)\n1. Book Tickets\n2. Cancel Tickets\n>>>"))
            if choice == 1:
                book_tickets()
            elif choice == 2:
                cancel_tickets()
            else:
                print("ENTER A VALID CHOICE")


class ShowTimings:
    def solve(self, first_show, n):
        h, m = map(int, first_show[:-2].split(':'))
        h %= 12
        if first_show[-2:] == 'pm':
            h += 12
        t = h * 60 + m + n
        h, m = divmod(t, 60)
        h %= 24
        suffix = 'a' if h < 12 else 'p'
        h %= 12
        if h == 0:
            h = 12

        new_time = "{:02d}:{:02d}{}m".format(h, m, suffix)
        if first_show != new_time:
            return "{} - {}".format(first_show, new_time)


# ob = ShowTimings()
# first_show= input("first show- ")
# interval= int(input("interval (mins)- "))
# length= int(input("length (mins)- "))
# gap= int(input("gap (mins)- "))
# nos=int(input("number of shows- "))
# n=interval+length
# total=0
#
# while nos!=0:
#    print(ob.solve(first_show, n))
#    nos=nos-1
#    total= interval+length+gap
#    n=n+total

home_page()
