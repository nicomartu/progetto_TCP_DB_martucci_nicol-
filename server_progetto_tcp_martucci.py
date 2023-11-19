import threading 
import socket
import mysql.connector
comunicazioni = ["",""]
PASSWORD = "einaudi2024"



def gestisci_comunicazione(conn):
    try:
        ciao="Benvenuto, inserisci password: "
        conn.send(ciao.encode())
        data = conn.recv(1024).decode()
        i=0
        while data != PASSWORD and i<2:
            i+=1
            conn.send(f"Password ERRATA, reinserisci password: tentativi rimasti {3-i} ".encode())
            data = conn.recv(1024).decode()      

        if(data != PASSWORD):
            conn.send(f"Password ERRATA troppe volte, arrivederci".encode())
            conn.close()
            return

        if(data == PASSWORD):
            flag=True

        
            while flag:

                print(i)
                conn.send("Benvenuto, cosa vuoi fare: i=insert, u=update,r=read,d=delete, e=exit".encode())
                data = conn.recv(1024).decode()
                print(data)
    ############################################################################################################ insert
                if(data=="i"):
                    conn.send("su che tabella vuoi cercare: C=clienti, Z=zone di lavoro".encode())
                    data = conn.recv(1024).decode()

                    if data.upper()=="C":
                        conn.send("inserisci nome".encode())
                        nome = conn.recv(1024).decode()

                        conn.send("inserisci cognome".encode())
                        cognome = conn.recv(1024).decode()

                        conn.send("inserisci posizione lavorativa".encode())
                        pos_lav = conn.recv(1024).decode()

                        conn.send("inserisci data assunzione".encode())
                        data_ass = conn.recv(1024).decode()

                        conn.send("inserisci data nascità".encode())
                        data_nasc = conn.recv(1024).decode()

                        conn.send("inserisci luogo nascità".encode())
                        luogo_nasc = conn.recv(1024).decode()

                        dati_query = db_insert_clienti(nome, cognome, pos_lav, data_ass, data_nasc, luogo_nasc)
                        

                    elif data.upper()=="Z":
                        conn.send("inserisci nome zona".encode())
                        nome_zona = conn.recv(1024).decode()

                        conn.send("inserisci numero clienti".encode())
                        numero_clienti = conn.recv(1024).decode()

                        conn.send("inserisci id_dipendente".encode())
                        id_dipendente = conn.recv(1024).decode()

                        conn.send("inserisci numero dipendenti".encode())
                        numero_dipendenti = conn.recv(1024).decode()
                        dati_query = db_insert_zona(nome_zona, numero_clienti, id_dipendente, numero_dipendenti)
                        

                    print(dati_query)
    ############################################################################################################ update
                elif(data=="u"):
                    conn.send("su che tabella vuoi modificare: C=clienti, Z=zone di lavoro".encode())
                    data = conn.recv(1024).decode()   
                    temp=""
                    if data.upper()=="C":      
                        conn.send("inserisci cella che vuoi modificare".encode())
                        cella = conn.recv(1024).decode()

                        conn.send("inserisci valore che vuoi che venga modificato".encode())
                        vecchio = conn.recv(1024).decode()

                        conn.send("inserisci valore nuovo".encode())
                        nuovo = conn.recv(1024).decode()

                        dati_query = db_update_clienti(cella,vecchio,nuovo)
                        conn.send(dati_query)

                    elif data.upper()=="Z":
                        conn.send("inserisci cella che vuoi modificare".encode())
                        cella = conn.recv(1024).decode()

                        conn.send("inserisci valore che vuoi che venga modificato".encode())
                        vecchio = conn.recv(1024).decode()

                        conn.send("inserisci valore nuovo".encode())
                        nuovo = conn.recv(1024).decode()

                        dati_query = db_update_zona(cella,vecchio,nuovo)
                        conn.send(dati_query)

                    print(dati_query)
    ############################################################################################################ delete
                elif(data=="d"):
                    conn.send("su che tabella vuoi eliminare: C=clienti, Z=zone di lavoro".encode())
                    data = conn.recv(1024).decode()
                    if data.upper()=="C":
                            conn.send(" inserisci un nome".encode())
                            data2 = (conn.recv(1024)).decode() 
                            dati_query = db_delete_clienti(data2)

                    elif data.upper()=="Z":
                            conn.send(" inserisci id_dipendente".encode())
                            data2 = (conn.recv(1024)).decode()

                    dati_query = db_delete_zona(data2)
                    print(dati_query)

    ############################################################################################################ read
                elif(data=="r"):
                    conn.send("su che tabella vuoi leggere: C=clienti, Z=zone di lavoro".encode())
                    data = conn.recv(1024).decode()           
                    dati_query = db_get(str(data))
                    conn.send(str(dati_query).encode())


                elif(data=="e"):
                    flag=False


    except Exception as e:  
        print(e)

################################################################################################ leggi

def db_get(lettera):
    conn = mysql.connector.connect(
    host="localhost",
    user="nicolo_martucci",
    password="martucci1234",
    database="5atepsit",
    port=3306, 
)

    if lettera.upper()=="C":
        mycursor=conn.cursor()

        query = f"SELECT * FROM clienti_martucci_nicolo"
        print(query)
        mycursor.execute(query)
        dati = mycursor.fetchall()
        print(dati)
        return dati
    elif lettera.upper()=="Z":

        mycursor=conn.cursor()

        query = f"SELECT * FROM zona_lavoro_martucci_nicolo"
        print(query)
        mycursor.execute(query)
        dati = mycursor.fetchall()
        print(dati)
        return dati
    
################################################################################################ fine
################################################################################################ insert clienti

def db_insert_clienti(nome, cognome, pos_lav, data_ass, data_nasc, luogo_nasc):
    conn = mysql.connector.connect(
        host="localhost",
        user="nicolo_martucci",
        password="martucci1234",
        database="5aTepsit",
        port=3306, 
    )
    mycursor=conn.cursor()

    query = f"INSERT INTO clienti_martucci_nicolo ( nome, cognome, pos_lav, data_ass, data_nasc, luogo_nasc) VALUES (%s, %s, %s, %s, %s, %s)"
    values=(nome, cognome, pos_lav, data_ass, data_nasc, luogo_nasc, )
    print(query)
    try:
        mycursor.execute(query, values)
        conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()

    
################################################################################################ fine clienti
################################################################################################ insert zona

def db_insert_zona(nome_zona, numero_clienti, id_dipendente, numero_dipendenti):
    conn = mysql.connector.connect(
        host="localhost",
        user="nicolo_martucci",
        password="martucci1234",
        database="5atepsit",
        port=3306, 
)
    
    mycursor=conn.cursor()

    query = f"INSERT INTO zona_lavoro_martucci_nicolo (nome_zona, numero_clienti, id_dipendente, numero_dipendenti) VALUES (%s, %s, %s, %s)"
    values=(nome_zona, numero_clienti, id_dipendente, numero_dipendenti, )

    print(query)
    try:

        mycursor.execute(query, values)
        conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


################################################################################################ fine zona
################################################################################################ update clienti
def db_update_clienti(cella,vecchio,nuovo):
    conn = mysql.connector.connect(
        host="localhost",
        user="nicolo_martucci",
        password="martucci1234",
        database="5atepsit",
        port=3306, 
)    
    
    query = f"UPDATE clienti_martucci_nicolo SET {cella}='{nuovo}' where {cella}='{vecchio}' "
    print(query)
   
    mycursor=conn.cursor()   

    try:

        mycursor.execute(query)
        conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()

################################################################################################ fine
################################################################################################ update zona
def db_update_zona(cella,vecchio,nuovo):
    conn = mysql.connector.connect(
        host="localhost",
        user="nicolo_martucci",
        password="martucci1234",
        database="5atepsit",
        port=3306, 
)    
    
    query = f"UPDATE zona_lavoro_martucci_nicolo SET {cella}='{nuovo}' where {cella}='{vecchio}'"
    print(query)

    mycursor=conn.cursor()   

    try:

        mycursor.execute(query)
        conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()
################################################################################################ fine
################################################################################################ elimina cliente
def db_delete_clienti(eliminato):
    conn = mysql.connector.connect(
        host="localhost",
        user="nicolo_martucci",
        password="martucci1234",
        database="5atepsit",
        port=3306, 
    )   
    mycursor=conn.cursor()
    query = "DELETE FROM clienti_martucci_nicolo WHERE nome = \'"+eliminato+"\'"
    print(query)
    try:
        mycursor.execute(query)        
        conn.commit()
        print("deleted")
    except Exception as e:
        print(e)
        conn.rollback

    print(mycursor.rowcount, "record(s) deleted")

################################################################################################ fine
################################################################################################ elimina zona

def db_delete_zona(eliminato):
    conn = mysql.connector.connect(
    host="localhost",
    user="nicolo_martucci",
    password="martucci1234",
    database="5atepsit",
    port=3306, 
    )   
    mycursor=conn.cursor()
    query = "DELETE FROM zona_lavoro_martucci_nicolo WHERE id_dipendente = \'"+eliminato+"\'"
    print(query)
    try:
        mycursor.execute(query)        
        conn.commit()
        print("deleted")
    except Exception as e:
        print(e)
        conn.rollback

    print(mycursor.rowcount, "record(s) deleted")

################################################################################################ fine



















print("server in ascolto: ")
lock = threading.Lock()
HOST = 'localhost'                 # Nome simbolico che rappresenta il nodo locale, ci va l'indirizzo IP
PORT = 50010            # Porta non privilegiata arbitraria
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)
thread = []
lista_connessioni = []
i=0

while True:
    lista_connessioni.append( s.accept() ) #connessione = s.accept() 
    print('Connected by', lista_connessioni[i][1]) # print(connessione[0])
    thread.append(threading.Thread(target=gestisci_comunicazione, args = (lista_connessioni[i][0],) )) 
    thread[i].start()
    i+=1
