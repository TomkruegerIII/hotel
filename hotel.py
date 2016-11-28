from random import randint

var_stor = {}

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

    #var_stor zu städten: varstore[Stadtname[Sub]]
    #Sub ist Hotel (bool) manager (int) , straßen kein teil von städten, sondern eigene kategorie

    '''
    Soll der User Städtenamen eingeben? Wie genau soll der
    User denn die Straßen festlegen, wir übergeben ja die
    s_k_l Variable, aber ?
    '''
    while True:
        selection = input("Use random start? [y/n]")
        if selection == "y":
            var_stor["e cities"] = randint(5, 20)
            var_stor["m hometown"] = randint(5, 20)
            var_stor["rounds"] = randint(5, 40)
            #var_stor["usw"] = randint(5, 20) # nur wenn wir noch was brauchen
            return var_stor
        elif selection == "n":
            for current in [["e cities", "existing cities: "], ["m hometown", "managers in your hometown: "], ["rounds" ,"rounds: "]]:
                inval_input = True
                while inval_input:
                    user_value = input("Enter the start value for the number of " + current[1])
                    if user_value.isdigit():
                        var_stor[current[0]] = user_value
                        inval_input = False
                    else:
                        print("No valid number")
            return var_stor
        else:
            print("Invalid input")
            continue

    print(n)

set_startvalues(2, 4, 5, -10, 0)

###Noch kein nutzen, dienen zur orientierung

