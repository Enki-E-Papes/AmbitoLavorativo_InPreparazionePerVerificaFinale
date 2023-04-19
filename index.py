#pip install xlsrd
from flask import Flask,render_template,request
import pandas as pd
import geopandas  as gpd
import contextily
import matplotlib.pyplot as plt



#per concludere l'es cerca su: https://towardsdatascience.com/web-visualization-with-plotly-and-flask-3660abf9c946
app = Flask(__name__)   #variabile che identifica il sito web
df = pd.read_excel('https://github.com/wtitze/3E/blob/main/BikeStores.xls?raw=true', sheet_name='customers')

@app.route('/', methods=['GET'])  #sono tutte le possibili richieste del utente
def home():
    
    return render_template("indexHome.html")

##########################################1#####################################################
@app.route('/es1', methods=['GET'])  #sono tutte le possibili richieste del utente
def es1():
    
    return render_template("index1.html")

@app.route('/solEs1', methods = ['POST', 'GET'])  #sono tutte le possibili richieste del utente
def solEs1():
    nome = request.args.get('nome')
    cognome = request.args.get('cognome')
    risultato = df[(df.first_name == nome) & (df.last_name == cognome)]
    return render_template("soluzione.html",risultato=risultato.to_html())

##########################################2#####################################################

@app.route('/es2', methods=['GET'])  #sono tutte le possibili richieste del utente
def es2():

    return render_template("index2.html")

@app.route('/solEs2', methods = ['POST', 'GET'])  #sono tutte le possibili richieste del utente
def solEs2():
    elenco = request.args.get('elenco')
    risultato = df[df.city == elenco]
    return render_template("soluzione2.html", risultato = risultato.to_html())

##########################################3#####################################################
@app.route('/es3', methods=['GET'])  #sono tutte le possibili richieste del utente
def es3():
    state = df.groupby(["state"]).count()[["last_name"]].reset_index()
    return render_template("index3.html", risultato = state.to_html())

##########################################4#####################################################
@app.route('/es4', methods=['GET'])  #da rivedere
def es4():
    state = df.groupby(["state"]).count()[["last_name"]].reset_index()
    maxVal = state[state["customer_id"] == state["customer_id"].max()][["last_name"]].reset_index()
    return render_template("index3.html", risultato = maxVal.to_html())

##########################################5#####################################################
@app.route('/es4', methods=['GET'])  #sono tutte le possibili richieste del utente
def es4():
    import numpy as np
    plt.style.use('fivethirtyeight')  #uno stile
    labels = ca['state']   #asse delle x == ascisse
    dati = ca['last_name']      #asse delle y== ordinate

    fig, ax = plt.subplots(figsize=(15,8))   #'figsize' la grandezza dell'immagine
    ax.bar(labels, dati, label='non sò che scrivere')  #'.bar' è il tipo di grafico
    ax.legend() #inserisce nel grafico ciò che c'è scritto in label
    plt=plt.show()  #fà partire il grafico senza far usire il calcolo del esecuzione

    return render_template("index4.html", risultato = plt.to_html())
"""
soluzione^index1.html
df = pd.read_excel('https://github.com/wtitze/3E/blob/main/BikeStores.xls?raw=true', sheet_name='customers')
@app.route('/es1', methods=['GET'])  #sono tutte le possibili richieste del utente
def es1():
    Se = df[(df.first_name == nome) & (df.last_name == cognome)]
    return render_template("index2.html", Se = Se.to_html())

@app.route('/es2', methods=['GET'])  #sono tutte le possibili richieste del utente
def es2():
    df = pd.read_excel('https://github.com/wtitze/3E/blob/main/BikeStores.xls?raw=true', sheet_name='customers')
    #input Html
    Se = df[(df.first_name == nome) & (df.last_name == cognome)]
    return render_template("index2.html", Se = Se.to_html())

"""





if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)    #fà partire il programma