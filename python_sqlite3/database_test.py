import sqlite3


def Main():

    try:
            con = sqlite3.connect('test.db')  # link to DB file (unique to DBMS)
            cursor = con.cursor()  # makes a selector for our cur connection
            # cursor.execute('CREATE TABLE Pets(Id INT, Name TEXT, Price INT)')
            # cursor.execute("INSERT INTO Pets VALUES(1, 'Cat', 400)")
            # cursor.execute("INSERT INTO Pets VALUES(2,'Dog', 600)")

            cursor.executescript("""DROP TABLE IF EXISTS Pets;
                                CREATE TABLE Pets(Id INT, Name TEXT, Price INT);
                                INSERT INTO Pets VALUES(1, 'Cat', 400);
                                INSERT INTO Pets VALUES(2,'Dog', 600);""")

            pets_tuple = ((3, 'Rabbit', 100),
                          (4, 'Bird', 60),
                          (5, 'Turtle', 150))

            cursor.executemany("INSERT INTO Pets VALUES(?,?,?)", pets_tuple)

            con.commit()  # commits our entries to the db file
            cursor.execute("SELECT * FROM Pets")  # takes SQL com to query data

            data = cursor.fetchall()  # data = all data returned from query above

            for row in data:
                print(row)

    except sqlite3.Error:
        if con:
            con.rollback()  # if there's an SQL error, rollback any changes to DB
            print("There was a problem with the SQL Query.")
    finally:
        if con:
            con.close()

if __name__ == '__main__':
    Main()
