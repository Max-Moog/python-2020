

# Update
#student.update({'street': 'feuerbach Strasse 12'})
#print(student)

#student.update({'name': 'Alex2'})
#print(student)

# delete an item
#del student['street']
#print(student)

# Lister von Dictionaries
backpack1 = ["handy", "wasser", "essen", "Kopfhöhrer"]
backpack2 = ["schal", "mütze","supercooles-superhelden-videospiel","notfallassistent-für-mögliche-zombie-angriffe"]

player1 = {"name" : "lennard","age": 15, "score" : 100, "backpack" : backpack1}
player2 = {"name" : "antoni","age": 4, "score" : -100, "backpack" : backpack2}

def initPlayers():
    antwort = input("Player 1 or 2? :")

    if antwort == "1":
        antwort2 = input("Wanna see his backpack? Type: see/ Wanna edit his backpack? type: edit.")

        if antwort2 == "see":
            print(backpack1)

        elif antwort2 == "edit":
            edit()

        else:
            print("falsche eingabe!")

    elif antwort == "2":
        antwort2 = input("Wanna see his backpack? Type: see/ Wanna edit his backpack? type: edit.")

        if antwort2 == "see":
            print(backpack2)

        elif antwort2 == "edit":
            edit()

        else:
            print("falsche eingabe!")

def edit():


initPlayers()
