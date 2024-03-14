#SET PostgreSQL database
import psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="xxx",
    user="postgres",
    password="xxx"
)
cursor = conn.cursor()
#SET SQLite3 database
import sqlite3
conn2 = sqlite3.connect('mabase.db')
cursor2 = conn2.cursor()
req = """CREATE TABLE IF NOT EXISTS utilisateurs(
id_utilisateur INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
nom TEXT,
login TEXT,
mdp TEXT)"""
cursor2.execute(req)
conn2.commit()
#SET DATE LAST UPDATE
datelast_update = '2024-02-23 08:37:00.705102+03'

###########################################################
def execute_new_requete_in_sqlite3(req):
    cursor2.execute(req)
    conn2.commit()

###########################################################
def sync_2bdd_postgre_sqlite3():
    req = "SELECT * FROM historiques WHERE datetimerequete>'"+datelast_update+"'";
    cursor.execute(req)
    print("............. New Requete ..........")
    for row in cursor.fetchall():
        print(row)
        req = row[2]
        execute_new_requete_in_sqlite3(req)

###########################################################
def list_utilisateurs_sqlite3():
    req = "SELECT * FROM utilisateurs"
    cursor2.execute(req)
    print("............. Utilisateurs in SQLite3 ..........")
    for row in cursor2.fetchall():
        print(row)

sync_2bdd_postgre_sqlite3()
list_utilisateurs_sqlite3()







