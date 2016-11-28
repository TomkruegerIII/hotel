from random import randint

def new_day():
    print("""\n
    -------------------------------------------
    -------------------------------------------""")
    print("""                        Menu
    -------------------------------------------
    s --> Skip. Don't do anything today. \n
    b --> Build a new hotel. \n
    m --> Move manager to neighboured city. \n
    h --> Hire a new manager. Takes three days!
    -------------------------------------------
                    End of Menu
    -------------------------------------------
    -------------------------------------------""")

    selection = input("    Please choose what to do: ")

    if selection == "s":
        pass
    elif selection == "b":
        pass
    elif selection == "m":
        pass
    elif selection == "h":
        pass
    elif selection == "help": #muss da sein, name egal
        pass
    else:
        print("Invalid input! Please try again.")

def set_startvalues(n, m, d, p_i, s_k_l):
    # irgendwie müssen wir die Funktionsparameter optional machen,
    # vielleicht so wie hier:
    # http://stackoverflow.com/questions/14749328/python-how-to-check-whether-optional-function-parameter-is-set

    '''
    Soll der User Städtenamen eingeben? Wie genau soll der
    User denn die Straßen festlegen, wir übergeben ja die
    s_k_l Variable, aber ?
    '''

    n = str(randint(5, 20))
    print(n)

set_startvalues(2, 4, 5, -10, 0)

###Noch kein nutzen, dienen zur orientierung

def city(name, hotel, manager, streets):
    
    #stadt, und was dazu gehört


def income(n, m, d, p_i, s_k_l):
    #einkommen


def hometown
    #ma gucke
