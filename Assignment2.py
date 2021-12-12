#####################
# Name: Wai Ki Ip
#
# Student Id: 8689247
#
# Assignment 2
######################

import sqlite3 as lit
import os
import csv

def encryptPassword(pwd):
    pwd = pwd.replace('A', 'T')
    pwd = pwd.replace('B', 'I')
    pwd = pwd.replace('C', 'M')
    pwd = pwd.replace('D', 'E')
    pwd = pwd.replace('E', 'O')
    pwd = pwd.replace('F', 'D')
    pwd = pwd.replace('G', 'A')
    pwd = pwd.replace('H', 'N')
    pwd = pwd.replace('I', 'S')
    pwd = pwd.replace('J', 'F')
    pwd = pwd.replace('K', 'R')
    pwd = pwd.replace('L', 'B')
    pwd = pwd.replace('M', 'C')
    pwd = pwd.replace('N', 'G')
    pwd = pwd.replace('O', 'H')
    pwd = pwd.replace('P', 'J')
    pwd = pwd.replace('Q', 'K')
    pwd = pwd.replace('R', 'L')
    pwd = pwd.replace('S', 'P')
    pwd = pwd.replace('T', 'Q')
    pwd = pwd.replace('0', '9')
    pwd = pwd.replace('1', '8')
    pwd = pwd.replace('2', '7')
    pwd = pwd.replace('3', '6')
    pwd = pwd.replace('4', '5')
    pwd = pwd.replace('5', '4')
    pwd = pwd.replace('6', '3')
    pwd = pwd.replace('7', '2')
    pwd = pwd.replace('8', '1')
    pwd = pwd.replace('9', '0')

    return pwd

def DEcryptPassword(pwd):
    pwd = pwd.replace('T', 'A')
    pwd = pwd.replace('I', 'B')
    pwd = pwd.replace('M', 'C')
    pwd = pwd.replace('E', 'D')
    pwd = pwd.replace('O', 'E')
    pwd = pwd.replace('D', 'F')
    pwd = pwd.replace('A', 'G')
    pwd = pwd.replace('N', 'H')
    pwd = pwd.replace('S', 'I')
    pwd = pwd.replace('F', 'J')
    pwd = pwd.replace('R', 'K')
    pwd = pwd.replace('B', 'L')
    pwd = pwd.replace('C', 'M')
    pwd = pwd.replace('G', 'N')
    pwd = pwd.replace('H', 'O')
    pwd = pwd.replace('J', 'P')
    pwd = pwd.replace('K', 'Q')
    pwd = pwd.replace('L', 'R')
    pwd = pwd.replace('P', 'S')
    pwd = pwd.replace('Q', 'T')
    pwd = pwd.replace('9', '0')
    pwd = pwd.replace('8', '1')
    pwd = pwd.replace('7', '2')
    pwd = pwd.replace('6', '3')
    pwd = pwd.replace('5', '4')
    pwd = pwd.replace('4', '5')
    pwd = pwd.replace('3', '6')
    pwd = pwd.replace('2', '7')
    pwd = pwd.replace('1', '8')
    pwd = pwd.replace('0', '9')

    return pwd

createtablequery = "CREATE TABLE users (USER_ID INTEGER PRIMARY KEY AUTOINCREMENT, " \
                     "                      LOGIN TEXT, " \
                     "                      PASSWORD TEXT, " \
                     "                      ACCESS_COUNT INT)"


if os.path.exists('USER.db'):
    dbconn = lit.connect('USER.db')
    cur = dbconn.cursor()
else:
    dbconn = lit.connect('USER.db')
    cur = dbconn.cursor()

    cur.execute(createtablequery)

newUser = input("Enter y if you wanna create user, or n if you are not a new user: ")

if newUser == 'y':
    username = input("Enter your Login email:")
    password = input("Enter your password:")
    password = password.upper()
    password = encryptPassword(password)
    #print(password)

    cur.execute('INSERT INTO users (LOGIN,PASSWORD,ACCESS_COUNT) VALUES (?,?,?)', [username, password,0])
    dbconn.commit()
    dbconn.close()

    print("Account added")

elif newUser == 'n':
    username = input("Enter Login email: ")
    password = input("Enter password: ")
    password = password.upper()
    password = encryptPassword(password)

    cur.execute("SELECT * FROM users WHERE LOGIN = ? AND PASSWORD = ?",[username, password])

    if cur.fetchone() == None:
        print("Incorrect Credentials")
    else:
        cur.execute("UPDATE users SET ACCESS_COUNT= ACCESS_COUNT+1 WHERE LOGIN = ? AND PASSWORD = ?", (username, password))
        dbconn.commit()
        cur.execute("SELECT * FROM users WHERE LOGIN = ? AND PASSWORD = ?", [username, password])
        with open("userdb-backup.csv","w",newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            #csv_writer.writerow([i[0] for i in cur.description])
            csv_writer.writerow(cur)
        print("You are Loging in and export the csv. Please check.")


else:
    print("You have to enter 'y' or 'n'")