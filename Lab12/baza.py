import sqlite3

if __name__ == "__main__":

    conn = sqlite3.connect('database.db')
    print("BD otwarta")
    
    conn.execute('CREATE TABLE pracownicy (imienazwisko TEXT, nrpracownika TEXT, adres TEXT)')
    print("Tabela utworzona")
    
    conn.close()
    print("BD zamknieta")
    
    
    conn = sqlite3.connect('database.db')
    print("BD otwarta")
    cur = conn.cursor()
    
    cur.execute("INSERT INTO pracownicy (imienazwisko, nrpracownika, adres) VALUES (?,?,?)",('Andrzej Dudek', '1', 'ul. Zmysły 7/13, 24-680 Elblag') )
    cur.execute("INSERT INTO pracownicy (imienazwisko, nrpracownika, adres) VALUES (?,?,?)",('Marian Lewadnowski', '2', 'ul. Maja 2a/5, 11-111 Gdynia') )
    conn.commit()
    
    cur.execute('SELECT * FROM pracownicy ORDER BY nrpracownika')
    print(cur.fetchall())
    
    conn.close()
    print("BD zamknieta")