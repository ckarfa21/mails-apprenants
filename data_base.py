import mysql.connector
from apprenants import apprenants

class data_base:
    #user = "root"
    #"password": "root",
    #"host": "localhost",
    #"port": "8081",
    #"database": "microsoftIA"}
    def __init__(self):
        self.cnx = mysql.connector.connect(user = "root", password= "root", host="localhost", port="8081", database="microsoftIA")
        self.cursor = self.cnx.cursor()

    def read_db(self):
        groupe =[]
        query = "SELECT id_apprenants, nom, prenom FROM apprenants"
        self.cursor.execute(query)
        for id, nom, prenom in self.cursor :
            nouveau = apprenants(id, nom, prenom, adresse_mail= None)
            groupe.append(nouveau)
        return groupe

    def create(self):
        self.cursor.execute("ALTER TABLE apprenants ADD mail VARCHAR(50) NOT NULL AFTER photo")
    
    def envoie(self, data, id):
        ref = (data, id)
        self.cursor.execute('''UPDATE apprenants SET mail=(%s) WHERE id_apprenants = (%s)''', ref)
        self.cnx.commit()

    def fermer(self):
        self.cursor.close()
        self.cnx.close()