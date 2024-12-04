from flask import Flask, redirect, request, url_for
import sqlite3

app = Flask(__name__)

@app.route("/login", methods=['POST'])  
def login():
    """
    HINT: return "Welcome back username!" jika username dan password ada dalam database
    jika tidak maka, return "Login Failed! Please check your username & password!"
    """
    pass

def userLogin(username: str, password: str):
    # Open database connection
    connection = sqlite3.connect("user.db")
    cursor = connection.cursor()
    # Execute the query
    cursor.execute("SELECT username, password FROM user WHERE username = ? AND password = ?;", 
                   (username, password))
    count = cursor.fetchone()
    # Close the connection
    connection.close()
    return count


if __name__ == '__main__':
    print("This is flask Program!")
    app.run()


"""
ISI DARI TABLE USER SAAT INI
|real name|              |pob|          |username|              |password|
--------------------------------------------------------------------------------------
('dendyprtha',          'Indonesia',    'dendyprtha',           'qwe123'),
('Maria Don Banvard',   'Makasar',      'maria_don_banvard',    'mariaD0nB4nV4Rd'),
('John Guilemot',       'Aceh',         'john_guilemot',        'JohnGu!l3M0T'),
('Adid Kotelawala',     'Sragen',       '4DidN3Cis',            'Ad!N3C1sD4nK3R3n')
--------------------------------------------------------------------------------------
"""


def check_table(nama_table: str):
    """
    fungsi untuk mengecek table (nama_table) dari database user.db
    """
    connection = sqlite3.connect("user.db")
    cursor = connection.cursor()

    cursor.execute(f''' pragma table_info({nama_table}) ''')
    x = cursor.fetchall()

    for q in x: print(q)
    
    connection.commit()
    connection.close()

def select_all(nama_table: str):
    """
    fungsi untuk menampilkan semua data 
    dari tabel (nama_table) yang berada dalam database user.db
    """
    connection = sqlite3.connect("user.db")
    cursor = connection.cursor()
    cursor.execute(f''' select * from {nama_table} ''')
    x = cursor.fetchall()
    for q in x : print(q)
    connection.commit()
    connection.close()

def do_this(syntax: str):
    """
    fungsiku bukan fungsimu
    """
    connection = sqlite3.connect("user.db")
    cursor = connection.cursor()
    cursor.execute(syntax)
    connection.commit()
    connection.close()

"""
resources untuk belajar algoritma
persiapan semester 2
https://codingbat.com/python *
https://www.hackerrank.com/ *
https://codeforces.com/ *favorit
https://leetcode.com/ *
https://adventofcode.com/ *NATAL
--GOOD LUCK UAS (for me and for you)--
"""